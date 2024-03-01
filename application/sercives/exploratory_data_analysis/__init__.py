from flask import Blueprint

UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME = '/service_exploratory_data_analysis/'

exploratory_data_analysis = Blueprint(
    'exploratory_data_analysis',
    __name__,
    url_prefix='/exploratory_data_analysis'
)

from . import errors, views
from .application import register_dash_service
