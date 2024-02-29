UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME = '/service_exploratory_data_analysis/'

from flask import Blueprint
exploratory_data_analysis = Blueprint(
    'exploratory_data_analysis',
    __name__,
    url_prefix='/exploratory_data_analysis'
)

from application.templates.services.explorary_data_analysis import layout
from dash_extensions.enrich import MultiplexerTransform, DashProxy as Dash
import dash_bootstrap_components

from . import views, errors

def register_dash_service(
    server,
):

    service_dash = Dash(
        __name__,
        server=server,
        url_base_pathname=UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME,
        external_stylesheets=[dash_bootstrap_components.themes.DARKLY],
        prevent_initial_callbacks=True,
    )

    with server.app_context() as context:
        service_dash.title = 'Exploratory Data Analysis'
        service_dash.layout = layout