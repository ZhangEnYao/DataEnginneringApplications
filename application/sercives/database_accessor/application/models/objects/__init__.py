from dataclasses import dataclass


@dataclass
class configurationRole:
    user: str = None
    password: str = None


@dataclass
class configurationManageSystem:
    system: str = None
    connector: str = None


@dataclass
class configurationRelation:
    host: str = None
    port: str = None
    database: str = None
    schema: str = None
    table: str = None
    columns: str = None
    rows: str = None


@dataclass
class Configuration:
    role: configurationRole
    manage_system: configurationManageSystem
    relation: configurationRelation


from .connection import Connection
from .relation import Relation
