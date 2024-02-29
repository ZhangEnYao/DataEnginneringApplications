from dash import dcc as dash_core_componets, html as dash_html
import dash_ag_grid
import dash_bootstrap_components
import pandas
from application.sercives.database_accessor.application.configurations import configuration, Parameters
from ..models import Relation

relation = Relation(
    configuration=configuration
)

class IDs:
    @property
    def elements(self):
        class Elements:
            relation = 'object_relation'
            logs_creation = 'object_logsCreation'
            logs_updation = 'object_logsUpdation'
            logs_deletion = 'object_logsDeletion'
        return Elements()
    @property
    def functionalities(self):
        class Functionalities:
            upload_file = 'functionality_uploadFile'
            container_upload_file = 'container_uploadFileFunctionality'
        return Functionalities()
    @property
    def listeners(self):
        class Listeners:
            reset_ordering = 'listener_clearSorting'
            quick_filter = 'listener_quickFilter'
            instance_create = 'listener_createInstance'
            instance_delete = 'listener_deleteInstance'
            instance_update = 'listener_updateInstance'
            save = 'listener_save'

        return Listeners()

class Objects:
    @property
    def navigation_bar(self):
        navigation_bar = dash_bootstrap_components.NavbarSimple(
            children=[
                dash_bootstrap_components.NavItem(
                    dash_bootstrap_components.NavLink("Logout", href="/authority/logout", external_link=True)
                ),
            ],
            brand="Application Center",
            brand_href='/',
            brand_external_link=True,
            fluid = True,
            color="dark",
        )
        return navigation_bar
    @property
    def elements(self):
        class Elements:
            operating_relation = dash_ag_grid.AgGrid(
                id=ids.elements.relation,
                rowData=relation.instances.to_dict("records"),
                columnDefs=[
                    {
                        'field': column,
                        'cellDataType': Parameters.type_data[index],
                        "headerTooltip": column,
                        "headerCheckboxSelection": index == 0,
                        'rowDrag': index == 0,
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
                },
                getRowId="params.data.id",
                columnSize="sizeToFit",
                className="ag-theme-quartz-auto-dark",
            )

            logs_creation = dash_ag_grid.AgGrid(
                id=ids.elements.logs_creation,
                rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
                columnDefs=[
                    {
                        'field': column,
                        'sortable': (column not in Parameters.columns_unsortable),
                        'rowDrag': index == 0,
                        'filter': (column not in Parameters.columns_nonfilter),
                        "filterParams": {"buttons": ["cancel","clear","apply","reset",], "closeOnApply": True,},
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
                },
                getRowId="params.data.id",
                columnSize="sizeToFit",
                className="ag-theme-balham-auto-dark",
            )

            logs_updation = dash_ag_grid.AgGrid(
                id=ids.elements.logs_updation,
                rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
                columnDefs=[
                    {
                        'field': column,
                        'sortable': (column not in Parameters.columns_unsortable),
                        'rowDrag': index == 0,
                        'filter': (column not in Parameters.columns_nonfilter),
                        "filterParams": {"buttons": ["cancel","clear","apply","reset",], "closeOnApply": True,},
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
                },
                getRowId="params.data.id",
                columnSize="sizeToFit",
                className="ag-theme-balham-auto-dark",
            )

            logs_deletion = dash_ag_grid.AgGrid(
                id=ids.elements.logs_deletion,
                rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
                columnDefs=[
                    {
                        'field': column,
                        'sortable': (column not in Parameters.columns_unsortable),
                        'rowDrag': index == 0,
                        'filter': (column not in Parameters.columns_nonfilter),
                        "filterParams": {"buttons": ["cancel","clear","apply","reset",], "closeOnApply": True,},
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
                },
                getRowId="params.data.id",
                columnSize="sizeToFit",
                className="ag-theme-balham-auto-dark",
            )
        return Elements()

    @property
    def functionalities(self):
        class Functionalities:
            reset_ordering=dash_bootstrap_components.Button(
                id=ids.listeners.reset_ordering,
                children="Reset Ordering",
                color="secondary",
            )

            quick_filter = dash_bootstrap_components.Col(
                dash_html.Div(
                    dash_bootstrap_components.Input(
                        id=ids.listeners.quick_filter,
                        placeholder="Quick Filter",
                    ),
                ),
            )

            upload_file = dash_core_componets.Upload(
                id=ids.functionalities.upload_file,
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

            create_instance = dash_bootstrap_components.Button(
                id=ids.listeners.instance_create,
                children='Create',
                n_clicks=0,
                color="secondary",
            )

            delete_instance = dash_bootstrap_components.Button(
                id=ids.listeners.instance_delete,
                children='Delete',
                n_clicks=0,
                color="secondary",
            )

            save = dash_bootstrap_components.Button(
                id=ids.listeners.save,
                children='Save',
                n_clicks=0,
                color="secondary",
            )

        return Functionalities()

ids = IDs()
objects = Objects()