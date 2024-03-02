from functools import reduce

import dash_ag_grid
import pandas

from application.sercives.database_accessor.application.configurations import (
    Parameters,
    configuration,
)

from ...models import Relation
from ..configurations import ids

relation = Relation(configuration=configuration)


class AGGridConfigure:
    @property
    def column_definitions(self):
        class ColumnDefinitions:
            column = [
                {
                    "field": column,
                    "cellDataType": Parameters.type_data[index],
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            selections = [
                {
                    "headerCheckboxSelection": index == 0,
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            row_dragging = [
                {
                    "rowDrag": index == 0,
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            sorting = [
                {
                    "sortable": (column not in Parameters.columns_unsortable),
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            filtering = [
                {
                    "filter": (column not in Parameters.columns_nonfilter),
                    "filterParams": {
                        "buttons": [
                            "cancel",
                            "clear",
                            "apply",
                            "reset",
                        ],
                        "closeOnApply": True,
                    },
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            editing = [
                {
                    "editable": (column not in Parameters.columns_uneditable),
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            tooltip = [
                {
                    "headerTooltip": column,
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]
            styles = [
                {
                    "type": "rightAligned",
                }
                for index, column in enumerate(relation.table.columns.keys())
            ]

            @property
            def defaults(self):
                class Defaults:
                    styles = {
                        "wrapHeaderText": True,
                        "autoHeaderHeight": True,
                    }

                return Defaults()

        return ColumnDefinitions()

    @property
    def options(self):
        class Options:
            selection = {
                "rowSelection": "multiple",
            }
            row_dragging = {
                "rowDragManaged": True,
                "rowDragMultiRow": True,
                "rowDragEntireRow": True,
                "suppressMoveWhenRowDragging": True,
            }
            sorting = {
                "alwaysMultiSort": True,
            }
            filtering = None
            editing = {
                "undoRedoCellEditing": True,
                "undoRedoCellEditingLimit": 23,
            }
            paginatoin = {
                "pagination": True,
                "paginationAutoPageSize": True,
            }
            navigation = {
                "enterNavigatesVertically": True,
                "enterNavigatesVerticallyAfterEdit": True,
            }

        return Options()


ag_grid_configure = AGGridConfigure()


class Relations:
    operating_relation = dash_ag_grid.AgGrid(
        id=ids.elements.operating_relation,
        rowData=relation.instances.to_dict("records"),
        columnDefs=[
            reduce(lambda one, another: {**one, **another}, configurations)
            for configurations in zip(
                ag_grid_configure.column_definitions.column,
                ag_grid_configure.column_definitions.selections,
                ag_grid_configure.column_definitions.row_dragging,
                ag_grid_configure.column_definitions.sorting,
                ag_grid_configure.column_definitions.filtering,
                ag_grid_configure.column_definitions.editing,
                ag_grid_configure.column_definitions.tooltip,
                ag_grid_configure.column_definitions.styles,
            )
        ],
        defaultColDef=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.column_definitions.defaults.styles,
                ],
            )
        ),
        dashGridOptions=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.options.selection,
                    ag_grid_configure.options.sorting,
                    ag_grid_configure.options.row_dragging,
                    ag_grid_configure.options.paginatoin,
                    ag_grid_configure.options.navigation,
                    ag_grid_configure.options.editing,
                ],
            )
        ),
        getRowId="params.data.id",
        columnSize="responsiveSizeToFit",
        className="ag-theme-material",
        persistence=True,
    )
    logs_creation = dash_ag_grid.AgGrid(
        id=ids.elements.logs_creation,
        rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict("records"),
        columnDefs=[
            reduce(lambda one, another: {**one, **another}, configurations)
            for configurations in zip(
                ag_grid_configure.column_definitions.column,
                ag_grid_configure.column_definitions.row_dragging,
                ag_grid_configure.column_definitions.sorting,
                ag_grid_configure.column_definitions.filtering,
                ag_grid_configure.column_definitions.styles,
            )
        ],
        defaultColDef=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.column_definitions.defaults.styles,
                ],
            )
        ),
        dashGridOptions=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.options.selection,
                    ag_grid_configure.options.sorting,
                    ag_grid_configure.options.row_dragging,
                    ag_grid_configure.options.paginatoin,
                    ag_grid_configure.options.navigation,
                ],
            )
        ),
        getRowId="params.data.id",
        columnSize="responsiveSizeToFit",
        className="ag-theme-material",
    )
    logs_updation = dash_ag_grid.AgGrid(
        id=ids.elements.logs_updation,
        rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict("records"),
        columnDefs=[
            reduce(lambda one, another: {**one, **another}, configurations)
            for configurations in zip(
                ag_grid_configure.column_definitions.column,
                ag_grid_configure.column_definitions.row_dragging,
                ag_grid_configure.column_definitions.sorting,
                ag_grid_configure.column_definitions.filtering,
                ag_grid_configure.column_definitions.styles,
            )
        ],
        defaultColDef=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.column_definitions.defaults.styles,
                ],
            )
        ),
        dashGridOptions=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.options.selection,
                    ag_grid_configure.options.sorting,
                    ag_grid_configure.options.row_dragging,
                    ag_grid_configure.options.paginatoin,
                    ag_grid_configure.options.navigation,
                ],
            )
        ),
        getRowId="params.data.id",
        columnSize="responsiveSizeToFit",
        className="ag-theme-material",
    )
    logs_deletion = dash_ag_grid.AgGrid(
        id=ids.elements.logs_deletion,
        rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict("records"),
        columnDefs=[
            reduce(lambda one, another: {**one, **another}, configurations)
            for configurations in zip(
                ag_grid_configure.column_definitions.column,
                ag_grid_configure.column_definitions.row_dragging,
                ag_grid_configure.column_definitions.sorting,
                ag_grid_configure.column_definitions.filtering,
                ag_grid_configure.column_definitions.styles,
            )
        ],
        defaultColDef=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.column_definitions.defaults.styles,
                ],
            )
        ),
        dashGridOptions=(
            reduce(
                lambda one, another: {**one, **another},
                [
                    ag_grid_configure.options.selection,
                    ag_grid_configure.options.sorting,
                    ag_grid_configure.options.row_dragging,
                    ag_grid_configure.options.paginatoin,
                    ag_grid_configure.options.navigation,
                ],
            )
        ),
        getRowId="params.data.id",
        columnSize="responsiveSizeToFit",
        className="ag-theme-material",
    )
