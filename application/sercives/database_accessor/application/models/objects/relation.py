from pandas import read_sql
from sqlalchemy import MetaData, Table

from . import Configuration
from .connection import Connection


class Relation:
    def __init__(
        self,
        configuration: Configuration,
    ):
        self.configuration = configuration
        self.connection = Connection(
            self.configuration
        )

        self._table = Table(
            self.configuration.relation.table,
            MetaData(),
            schema=self.configuration.relation.schema,
            autoload_with=self.connection.engine
        )
        self._instance = self.load()

    @property
    def table(self):
        return self._table

    @property
    def instances(self):
        return self._instance

    def load(self):
        data = read_sql(
            sql='select * from {schema}.{table}'.format(
                schema=self.configuration.relation.schema,
                table=self.configuration.relation.table
            ),
            con=self.connection.engine
        )
        return data

    def reload(self):
        self._instance = self.load()
        return self._instance
