from dash import dcc as dash_core_componets, html as dash_html
import dash_ag_grid
import dash_bootstrap_components
import pandas
from application.sercives.database_accessor.application.configurations import configuration, Parameters
from ..models import Relation

from dataclasses import dataclass

relation = Relation(
    configuration=configuration
)

@dataclass
class IDs:
    object_relation = 'object_relation'
    object_dropZone = 'object_dropZone'
    object_processingRelation = 'object_processingRelation'
    functionality_uploadFile = 'functionality_uploadFile'
    functionality_dropdown = 'functionality_dropdown'
    listener_createInstance = 'listener_addInstance'
    listener_deleteInstance = 'listener_deleteInstance'
    listener_updateInstance = 'listener_updateInstance'
    listener_saveOperatingInstances = 'listener_saveOperatingInstances'
    listener_resetOrdering = 'listener_clearSorting'
    listener_quickFilter = 'listener_quickFilter'
    container_uploadFileFunctionality = 'container_uploadFileFunctionality'

@dataclass
class Objects:

    object_relation = dash_ag_grid.AgGrid(
        id=IDs.object_relation,
        rowData=relation.instances.to_dict("records"),
        columnDefs=[
            {
                'field': column,
                'cellDataType': Parameters.type_data[index],
                "headerTooltip": column,
                "headerCheckboxSelection": index == 0,
                'sortable': (column not in Parameters.columns_unsortable),
                'filter': (column not in Parameters.columns_nonfilter),
                "filterParams": {"buttons": ["cancel","clear","apply","reset",], "closeOnApply": True,},
                "editable": (column not in Parameters.columns_uneditable),
                "type": "rightAligned",
            }
            for index, column in enumerate(relation.table.columns.keys())
        ],
        defaultColDef={
            "wrapHeaderText": True,
            "autoHeaderHeight": True,
        },
        dashGridOptions={
            'alwaysMultiSort': True,
            "rowSelection": "multiple",
            "rowDragManaged": True,
            "rowDragMultiRow": True,
            "rowDragEntireRow": True,
            "suppressMoveWhenRowDragging": True,
            "enterNavigatesVertically": True,
            "enterNavigatesVerticallyAfterEdit": True,
            "undoRedoCellEditing": True,
            "undoRedoCellEditingLimit": 23,
            "stopEditingWhenCellsLoseFocus": True,
        },
        getRowId="params.data.id",
        columnSize="sizeToFit",
        className="ag-theme-quartz-auto-dark",
    )

    object_processingRelation = dash_ag_grid.AgGrid(
        id=IDs.object_processingRelation,
        rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
        columnDefs=[
            {
                'field': column,
                'cellDataType': Parameters.type_data[index],
                "headerTooltip": column,
                "headerCheckboxSelection": index == 0,
                'sortable': (column not in Parameters.columns_unsortable),
                'filter': (column not in Parameters.columns_nonfilter),
                "filterParams": {"buttons": ["cancel","clear","apply","reset",], "closeOnApply": True,},
                "editable": (column not in Parameters.columns_uneditable),
                "type": "rightAligned",
            }
            for index, column in enumerate(relation.table.columns.keys())
        ],
        defaultColDef={
            "wrapHeaderText": True,
            "autoHeaderHeight": True,
        },
        dashGridOptions={
            'alwaysMultiSort': True,
            "rowSelection": "multiple",
            "rowDragManaged": True,
            "rowDragMultiRow": True,
            "rowDragEntireRow": True,
            "suppressMoveWhenRowDragging": True,
            "enterNavigatesVertically": True,
            "enterNavigatesVerticallyAfterEdit": True,
            "undoRedoCellEditing": True,
            "undoRedoCellEditingLimit": 23,
            "stopEditingWhenCellsLoseFocus": True,
        },
        getRowId="params.data.id",
        columnSize="sizeToFit",
        className="ag-theme-balham-auto-dark",
    )

    functionarity_resetOrdering=dash_bootstrap_components.Button(
        id=IDs.listener_resetOrdering,
        children="Reset Ordering",
        color="secondary",
    )

    functionality_quickFilter = dash_bootstrap_components.Col(
        dash_html.Div(
            dash_bootstrap_components.Input(
                id=IDs.listener_quickFilter,
                placeholder="Quick Filter",
            ),
        ),
    )

    functionarity_createInstance = dash_bootstrap_components.Button(
        id=IDs.listener_createInstance,
        children='Create',
        n_clicks=0,
        color="secondary",
    )

    functionarity_deleteInstance = dash_bootstrap_components.Button(
        id=IDs.listener_deleteInstance,
        children='Delete',
        n_clicks=0,
        color="secondary",
    )

    functionality_uploadFile = dash_core_componets.Upload(
        id=IDs.functionality_uploadFile,
        children=dash_html.Div(
            children='Drag and Drop or Click to Select Files',
        ),
        style={
            'padding': '23px',
            'borderStyle': 'dashed',
            'borderWidth': '1.3px',
            'borderRadius': '2.3px',
            'borderColor': 'rgb(255, 255, 255)',
            'backgroundColor': 'rgba(255, 255, 255, 0.618)',
            'textAlign': 'center',
        },
    )