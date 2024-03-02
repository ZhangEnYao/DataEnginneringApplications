import dash_bootstrap_components
from dash import html as dash_html

from ..components import objects


class Logs:
    relations = (
        dash_bootstrap_components.Tabs(
            [
                dash_bootstrap_components.Tab(
                    dash_html.Div(objects.relations.logs_deletion),
                    label="Deleted Instances",
                ),
                dash_bootstrap_components.Tab(
                    dash_html.Div(objects.relations.logs_updation),
                    label="Updated Instances",
                ),
                dash_bootstrap_components.Tab(
                    dash_html.Div(objects.relations.logs_creation),
                    label="Created Instances",
                ),
            ],
        ),
    )
