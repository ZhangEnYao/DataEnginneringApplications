import pandas
from sqlalchemy import Engine


class DataAccessor:

    @staticmethod
    def read(
        engine: Engine,
        statement: str,
    ):
        return pandas.read_sql(sql=statement, con=engine)
