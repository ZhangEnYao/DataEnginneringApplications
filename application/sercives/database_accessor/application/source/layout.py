from dash import html as dash_html, dcc as dash_core_componets
from dash_extensions.enrich import Dash
import dash_bootstrap_components
from .objects import ids
from .objects import objects
from dash_extensions import EventListener

class Layout:
    def __init__(self):
        self.layout = dash_html.Div([
            EventListener(),
            dash_bootstrap_components.Container([
                dash_bootstrap_components.Row([
                    dash_bootstrap_components.Col(
                        dash_html.Div([
                            objects.navigation_bar,
                        ],),
                    ),
                ],),
                dash_bootstrap_components.Row([
                    dash_bootstrap_components.Col(
                        dash_html.Div([
                            objects.functionalities.quick_filter,
                        ],),
                    ),
                ],),
                dash_html.Div([
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div(
                                dash_bootstrap_components.ButtonGroup([
                                    objects.functionalities.clear_sorting,
                                    objects.functionalities.clear_filtering,
                                ],),
                                style={'float': 'right'},
                            ),
                        ),
                    ],),
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div(
                                objects.elements.operating_relation
                            ),
                        ),
                    ]),
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div([
                                dash_html.Div(
                                    dash_bootstrap_components.ButtonGroup([
                                        objects.functionalities.create_instance,
                                        objects.functionalities.delete_instance,
                                    ],),
                                    style={'float': 'left'},
                                ),
                                dash_html.Div(
                                    objects.functionalities.save,
                                    style={'float': 'right'},
                                ),
                            ])
                        ),
                    ]),
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div([
                                objects.functionalities.upload_file,
                            ], id=ids.functionalities.container_upload_file
                        ),),
                    ],),
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_bootstrap_components.Tabs([
                                dash_bootstrap_components.Tab(
                                    dash_html.Div(
                                        objects.elements.logs_deletion
                                    ), label='Deleted Instances',
                                ),
                                dash_bootstrap_components.Tab(
                                    dash_html.Div(
                                        objects.elements.logs_updation
                                    ), label='Updated Instances',
                                ),
                                dash_bootstrap_components.Tab(
                                    dash_html.Div(
                                        objects.elements.logs_creation
                                    ), label='Created Instances',
                                ),
                            ]),
                        ),
                    ],),
                ],),
            ]),
        ],)
    
    def register(self, server: Dash):
        server.layout = self.layout