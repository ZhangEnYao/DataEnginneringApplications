import dash_bootstrap_components
from dash import (ClientsideFunction, Input, Output, Patch, State, callback,
                  clientside_callback)
from dash import ctx as context
from dash import dcc as dash_core_componets
from dash import html as dash_html
from dash import no_update
from dash_extensions.enrich import DashProxy as Dash
from dash_extensions.enrich import MultiplexerTransform

from application.sercives.database_accessor import \
    UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME


def register_dash_service(
    server,
):

    service_database_accessor = Dash(
        __name__,
        server=server,
        url_base_pathname=UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME,
        external_stylesheets=[
            dash_bootstrap_components.themes.MATERIA,
        ],
        transforms=[
            MultiplexerTransform()
        ],
        prevent_initial_callbacks=True,
    )
    with server.app_context() as context:
        from .source.layout import Layout
        layour = Layout()
        layour.register(service_database_accessor)

        from .source.callbacks import Callbacks
        Callbacks.register(service_database_accessor)

        service_database_accessor.title = 'Database Accessor'
