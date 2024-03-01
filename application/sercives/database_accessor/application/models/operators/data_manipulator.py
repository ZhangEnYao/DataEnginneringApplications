from logging import error

import numpy
import pandas
import sqlalchemy.dialects.postgresql as postgresql
import sqlalchemy.engine as Engine
from psycopg2 import extras
from psycopg2.extensions import AsIs, register_adapter
from sqlalchemy import MetaData, Table, inspect

register_adapter(numpy.int64, AsIs)


class DataManipulator:

    @staticmethod
    def create(
        engine: Engine,
        data: pandas.DataFrame,
        schema: str,
        relation: str,
    ):
        try:
            object_table = Table(
                relation,
                MetaData(),
                schema=schema,
                autoload_with=engine
            )

            columns = list(data.columns)
            instances = [tuple(instance) for instance in data.to_numpy()]

            primary_key = [key.name for key in object_table.primary_key]

            conflict_condition = ' AND '.join(
                [f'"{key}" = temporary_table."{key}"' for key in primary_key])

            insert_attributes = ', '.join(
                [f'"{column}"' for column in columns])
            update_attributes = ', '.join(
                [f'"{column}" = temporary_table."{column}"' for column in columns])

            update_condition = ' AND '.join(
                [f'{object_table}."{key}" = temporary_table."{key}"' for key in primary_key])

            connection = engine.raw_connection()

            with connection.cursor() as cursor:

                statement = f'''CREATE LOCAL TEMPORARY TABLE temporary_table AS (SELECT {
                    insert_attributes} FROM {object_table}) WITH NO DATA;'''
                cursor.execute(statement)

                statement = f'''INSERT INTO temporary_table ({
                    insert_attributes}) VALUES %s;'''
                extras.execute_values(cursor, statement, instances)

                statement = f'''
                        INSERT INTO
                            {object_table} (
                            {insert_attributes}
                        ) (
                            SELECT
                                {insert_attributes}
                            FROM
                                temporary_table
                            WHERE
                                NOT EXISTS (
                                SELECT
                                    1
                                FROM
                                    {object_table}
                                WHERE
                                    {conflict_condition}
                            )
                        );

                        UPDATE
                            {object_table}
                        SET
                            {update_attributes}
                        FROM
                            temporary_table
                        WHERE
                            {update_condition};

                        DROP TABLE IF EXISTS
                            temporary_table;
                    '''
                cursor.execute(statement)

            connection.commit()

        except Exception as error_message:
            error(error_message)

    @staticmethod
    def upsert(
        engine: Engine,
        data: pandas.DataFrame,
        schema: str,
        relation: str,
    ):
        try:

            object_table = Table(
                relation,
                MetaData(),
                schema = schema,
                autoload_with = engine
            )

            del data[object_table._autoincrement_column.name]
            data = data.to_dict(orient='records')

            constraint = inspect(engine).get_pk_constraint(relation, schema=schema)

            with engine.connect() as connection:
                statement_insert = postgresql.insert(object_table).values(data)
                statement_upsert = statement_insert.on_conflict_do_update(
                    constraint=constraint.get('name'),
                    set_={exclusion.key: exclusion for exclusion in statement_insert.excluded if exclusion.key not in constraint.get('constrained_columns')},
                )
                connection.execute(statement_upsert)
                connection.commit()

        except Exception as error_message:
            raise(error_message)

    @staticmethod
    def delete(
        engine: Engine,
        data: pandas.DataFrame,
        schema: str,
        relation: str,
    ):
        try:
            object_table = Table(
                relation,
                MetaData(),
                schema=schema,
                autoload_with=engine
            )

            primary_key_columns = [
                key.name for key in object_table.primary_key]
            constraint_primary_key = (", ").join(
                [f'{object_table}."{column}"' for column in primary_key_columns])

            instances = tuple(tuple(instance)
                              for instance in data[primary_key_columns].to_numpy())

            connection = engine.raw_connection()
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                statement = f'DELETE FROM {
                    object_table} WHERE ({constraint_primary_key}) in (%s);'
                extras.execute_values(cursor, statement, instances)
            connection.commit()

        except Exception as error_message:
            error(error_message)

    @staticmethod
    def execute(
        engine: Engine,
        statement: str
    ):
        try:
            with engine.connect() as connection:
                connection.execute(statement)
                connection.commit()

        except Exception as error_message:
            raise (error_message)
