import dash_bootstrap_components
from dash_extensions.enrich import DashProxy as Dash
from dash_extensions.enrich import MultiplexerTransform

from application.sercives.exploratory_data_analysis import (
    UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME,
)

from .source import layout


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
        service_dash.title = "Exploratory Data Analysis"
        service_dash.layout = layout
