import dash_bootstrap_components
from dash import html as dash_html
from dash_extensions import EventListener
from dash_extensions.enrich import Dash

from .logs import Logs
from .navigation import navigation_bar
from .operations import Operations


class Layout:
    def __init__(self):
        self.layout = dash_html.Div(
            [
                EventListener(),
                dash_bootstrap_components.Container(
                    [
                        dash_bootstrap_components.Row(
                            [
                                dash_bootstrap_components.Col(navigation_bar),
                            ],
                        ),
                        dash_html.Div(
                            [
                                dash_bootstrap_components.Row(
                                    [
                                        dash_bootstrap_components.Col(
                                            Operations.quick_filter
                                        ),
                                    ],
                                ),
                                dash_bootstrap_components.Row(
                                    [
                                        dash_bootstrap_components.Col(Operations.reset),
                                    ],
                                ),
                                dash_bootstrap_components.Row(
                                    [
                                        dash_bootstrap_components.Col(
                                            Operations.operating_relation
                                        ),
                                    ],
                                ),
                                dash_bootstrap_components.Row(
                                    [
                                        dash_bootstrap_components.Col(
                                            Operations.operators
                                        ),
                                    ],
                                ),
                                dash_bootstrap_components.Row(
                                    [
                                        dash_bootstrap_components.Col(
                                            Operations.upload_file
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        dash_bootstrap_components.Row(
                            [
                                dash_bootstrap_components.Col(Logs.relations),
                            ],
                        ),
                    ],
                ),
            ],
        )

    def register(self, server: Dash):
        server.layout = self.layout
