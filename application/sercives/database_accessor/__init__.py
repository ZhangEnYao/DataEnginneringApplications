from flask import Blueprint

UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME = '/service_database_accessor/'

database_accessor = Blueprint(
    'database_accessor',
    __name__,
    url_prefix='/database_accessor'
)

from . import errors, views
from .application import register_dash_service
