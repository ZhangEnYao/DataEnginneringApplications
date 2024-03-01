from sqlalchemy import create_engine

from . import Configuration


class Connection:
    def __init__(
        self,
        configuration: Configuration
    ):
        self.configuration = configuration
        self._engine = create_engine(
            '{system}+{connector}://{user}:{password}@{host}:{port}/{database}'.format(
                system=self.configuration.manage_system.system,
                connector=self.configuration.manage_system.connector,
                user=self.configuration.role.user,
                password=self.configuration.role.password,
                host=self.configuration.relation.host,
                port=self.configuration.relation.port,
                database=self.configuration.relation.database,
            )
        )

    @property
    def engine(self):
        return self._engine
