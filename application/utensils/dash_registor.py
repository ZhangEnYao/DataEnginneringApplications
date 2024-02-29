from dash_extensions.enrich import MultiplexerTransform, DashProxy as Dash
import dash_bootstrap_components

def register_dash_service(
    server,
    title,
    layout,
    base_pathname,
):

    service_dash = Dash(
        __name__,
        server=server,
        url_base_pathname=base_pathname,
        external_stylesheets=[dash_bootstrap_components.themes.DARKLY],
        prevent_initial_callbacks=True,
    )

    with server.app_context() as context:
        service_dash.title = title
        service_dash.layout = layout
