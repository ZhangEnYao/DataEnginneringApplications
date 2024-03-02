from functools import reduce

import dash_bootstrap_components
from dash import dcc as dash_core_componets
from dash import html as dash_html

from application.sercives.database_accessor import (
    UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME,
)
from application.sercives.database_accessor.application.configurations import (
    configuration,
)

from ...models import Relation
from ..configurations import ids

relation = Relation(configuration=configuration)


class Functionalities:
    refresh = dash_bootstrap_components.Button(
        id=ids.listeners.refresh,
        children="Refresh",
        href=UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME,
        external_link=True,
        color="secondary",
        size="sm",
    )
    clear_sorting = dash_bootstrap_components.Button(
        id=ids.listeners.clear_sorting,
        children="Clear Ordering",
        color="secondary",
        size="sm",
    )
    clear_filtering = dash_bootstrap_components.Button(
        id=ids.listeners.clear_filtering,
        children="Clear Filtering",
        color="secondary",
        size="sm",
    )
    quick_filter = dash_bootstrap_components.Col(
        dash_html.Div(
            dash_bootstrap_components.Input(
                id=ids.functionalities.quick_filter,
                placeholder="Quick Filter",
            ),
        ),
    )
    upload_file = dash_core_componets.Upload(
        id=ids.functionalities.upload_file,
        children=dash_html.Div(
            children="Drag and Drop or Click to Select Files",
        ),
        style={
            "padding": "23px",
            "borderStyle": "dashed",
            "borderWidth": "1.3px",
            "borderRadius": "2.3px",
            "borderColor": "rgb(127, 127, 127)",
            "backgroundColor": "rgba(127, 127, 127, 0.23)",
            "textAlign": "center",
        },
    )
    create_instance = dash_bootstrap_components.Button(
        id=ids.listeners.instance_create,
        children="Create",
        n_clicks=0,
        color="secondary",
        size="sm",
    )
    delete_instance = dash_bootstrap_components.Button(
        id=ids.listeners.instance_delete,
        children="Delete",
        n_clicks=0,
        color="secondary",
        size="sm",
    )
    save = dash_bootstrap_components.Button(
        id=ids.listeners.save,
        children="Save",
        n_clicks=0,
        color="secondary",
        size="sm",
    )
