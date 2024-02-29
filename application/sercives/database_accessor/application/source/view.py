from dash import html as dash_html, dcc as dash_core_componets
import dash_bootstrap_components
from .objects import IDs

from .objects import Objects

class Layout:
    def __init__(self):
        self.layout = dash_html.Div([
            dash_bootstrap_components.Container([
                dash_bootstrap_components.Row([
                    dash_bootstrap_components.Col(
                        dash_html.Div([
                            Objects.functionality_quickFilter,
                        ],),
                    ),
                ],),
                dash_html.Div([
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div([
                                dash_html.Div(
                                    dash_bootstrap_components.ButtonGroup([
                                        Objects.functionarity_createInstance,
                                        Objects.functionarity_deleteInstance,
                                    ],),
                                    style={'float': 'left'},
                                ),
                                dash_html.Div(
                                    dash_bootstrap_components.ButtonGroup([
                                        Objects.functionarity_resetOrdering,
                                    ],),
                                    style={'float': 'right'},
                                ),
                            ])
                        ),
                    ],),
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div([
                                Objects.functionality_uploadFile,
                            ], id=IDs.container_uploadFileFunctionality),
                        )
                    ],),
                    dash_bootstrap_components.Row([
                        dash_bootstrap_components.Col(
                            dash_html.Div([
                                Objects.object_relation,
                                Objects.object_processingRelation,
                            ],),
                        )
                    ],),
                ],),
            ]),
        ],)
    
    def register(self, server):
        server.layout = self.layout