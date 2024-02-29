import pandas
from psycopg2 import extras
from psycopg2.errors import UndefinedColumn
from logging import error
import sqlalchemy
from sqlalchemy import Engine, Table, MetaData, inspect
from sqlalchemy.exc import NoSuchTableError
import sqlalchemy.dialects.postgresql as postgresql
import numpy
from psycopg2.extensions import register_adapter, AsIs
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
                schema = schema,
                autoload_with = engine
            )
            
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
            error(error_message)
    
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
                schema = schema,
                autoload_with = engine
            )

            primary_key_columns = [key.name for key in object_table.primary_key]
            constraint_primary_key = (", ").join([f'{object_table}."{column}"' for column in primary_key_columns])

            instances = tuple(tuple(instance) for instance in data[primary_key_columns].to_numpy())

            connection = engine.raw_connection()
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                statement = f'DELETE FROM {object_table} WHERE ({constraint_primary_key}) in (%s);'
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
            error(error_message)