from dataclasses import dataclass

from .models import (
    Configuration,
    configurationManageSystem,
    configurationRelation,
    configurationRole,
)

"""
schema:
    id, attribute, value
"""
configuration = Configuration(
    role=configurationRole("postgres", "postgres"),
    manage_system=configurationManageSystem("postgresql", "psycopg2"),
    relation=configurationRelation(
        "127.0.0.1", "5432", "postgres", "public", "database_accessor_develop"
    ),
)


@dataclass
class Parameters:
    type_data = ["text" for index in range(3)]
    type_filtered_data = ["agTextColumnFilter" for index in range(3)]
    columns_uneditable = ["id"]
    columns_unsortable = []
    columns_nonfilter = []
    dropdown_columns = ["Attribute"]
