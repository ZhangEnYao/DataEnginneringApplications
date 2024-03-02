import dash_bootstrap_components
from dash import html as dash_html

from ..components import ids, objects


class Operations:
    quick_filter = (
        dash_html.Div(
            [
                objects.functionalities.quick_filter,
            ],
        ),
    )

    reset = (
        dash_html.Div(
            dash_bootstrap_components.ButtonGroup(
                [
                    objects.functionalities.clear_sorting,
                    objects.functionalities.clear_filtering,
                    objects.functionalities.refresh,
                ],
            ),
            style={"float": "right"},
        ),
    )

    operating_relation = (dash_html.Div(objects.relations.operating_relation),)

    operators = (
        dash_html.Div(
            [
                dash_html.Div(
                    dash_bootstrap_components.ButtonGroup(
                        [
                            objects.functionalities.create_instance,
                            objects.functionalities.delete_instance,
                        ],
                    ),
                    style={"float": "left"},
                ),
                dash_html.Div(
                    objects.functionalities.save,
                    style={"float": "right"},
                ),
            ],
        ),
    )

    upload_file = (
        dash_html.Div(
            [
                objects.functionalities.upload_file,
            ],
            id=ids.functionalities.container_upload_file,
        ),
    )
