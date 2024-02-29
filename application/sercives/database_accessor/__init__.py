UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME = '/service_database_accessor/'

from flask import Blueprint
database_accessor = Blueprint(
    'database_accessor',
    __name__,
    url_prefix='/database_accessor'
)

from . import views, errors

from .application import register_dash_service