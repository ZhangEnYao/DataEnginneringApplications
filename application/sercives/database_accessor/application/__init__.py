from dash import dcc as dash_core_componets, html as dash_html, Input, Output, State, Patch, ctx as context, no_update, ClientsideFunction, clientside_callback, callback
from dash_extensions.enrich import MultiplexerTransform, DashProxy as Dash
import dash_bootstrap_components
from .models import Relation
from .configurations import configuration
from application.sercives.database_accessor import UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME


def register_dash_service(
    server,
):

    service_database_accessor = Dash(
        __name__,
        server=server,
        url_base_pathname=UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME,
        external_stylesheets=[
            dash_bootstrap_components.themes.DARKLY,
        ],
        transforms=[
            MultiplexerTransform()
        ],
        prevent_initial_callbacks=True,
    )
    with server.app_context() as context:
        from .source.view import Layout
        layour = Layout()
        layour.register(service_database_accessor)

        from .source.callbacks import Callbacks
        Callbacks.register(service_database_accessor)

        service_database_accessor.title = 'Database Accessor'