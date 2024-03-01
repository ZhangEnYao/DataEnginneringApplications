from dash import dcc as dash_core_componets, html as dash_html
import dash_ag_grid
import dash_bootstrap_components
import pandas
from application.sercives.database_accessor.application.configurations import configuration, Parameters
from ..models import Relation
from functools import reduce

relation = Relation(
    configuration=configuration
)

class IDs:
    @property
    def elements(self):
        class Elements:
            operating_relation = 'elements_operatingRelation'
            logs_creation = 'elements_logsCreation'
            logs_updation = 'elements_logsUpdation'
            logs_deletion = 'elements_logsDeletion'
        return Elements()
    @property
    def functionalities(self):
        class Functionalities:
            quick_filter = 'listener_quickFilter'
            upload_file = 'functionalities_uploadFile'
            container_upload_file = 'container_uploadFileFunctionalities'
        return Functionalities()
    @property
    def listeners(self):
        class Listeners:
            clear_sorting = 'listener_clearSorting'
            clear_filtering = 'listener_clearFiltering'
            instance_create = 'listener_createInstance'
            instance_delete = 'listener_deleteInstance'
            instance_update = 'listener_updateInstance'
            save = 'listener_save'
        return Listeners()
    
ids = IDs()

class AGGridConfigure:
    @property
    def column_definitions(self):
        class ColumnDefinitions:
            column = [{
                'field': column,
                'cellDataType': Parameters.type_data[index],
            } for index, column in enumerate(relation.table.columns.keys())]
            selections = [{
                "headerCheckboxSelection": index == 0,
            } for index, column in enumerate(relation.table.columns.keys())]
            row_dragging = [{
                'rowDrag': index == 0,
            } for index, column in enumerate(relation.table.columns.keys())]
            sorting = [{
                'sortable': (column not in Parameters.columns_unsortable),
            } for index, column in enumerate(relation.table.columns.keys())]
            filtering = [{
                'filter': (column not in Parameters.columns_nonfilter),
                "filterParams": {"buttons": ["cancel", "clear", "apply", "reset",], "closeOnApply": True,},
            } for index, column in enumerate(relation.table.columns.keys())]
            editing = [{
                "editable": (column not in Parameters.columns_uneditable),
            } for index, column in enumerate(relation.table.columns.keys())]
            tooltip = [{
                "headerTooltip": column,
            } for index, column in enumerate(relation.table.columns.keys())]
            styles = [{
                "type": "rightAligned",
            } for index, column in enumerate(relation.table.columns.keys())]
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
                'alwaysMultiSort': True,
            }
            filtering = None
            editing = {
                "undoRedoCellEditing": True,
                "undoRedoCellEditingLimit": 23,
            }
            navigation = {
                "enterNavigatesVertically": True,
                "enterNavigatesVerticallyAfterEdit": True,
            }
        return Options()
ag_grid_configure = AGGridConfigure()
class Objects:
    @property
    def navigation_bar(self):
        navigation_bar = dash_bootstrap_components.NavbarSimple(
            children=[
                dash_bootstrap_components.NavItem(
                    dash_bootstrap_components.NavLink("Logout", href="/authority/logout", external_link=True)
            ),],
            brand="Application Center",
            brand_href='/',
            brand_external_link=True,
            fluid = True,
            color="light",
        )
        return navigation_bar
    @property
    def elements(self):
        class Elements:
            operating_relation = dash_ag_grid.AgGrid(
                id=ids.elements.operating_relation,
                rowData=relation.instances.to_dict("records"),
                columnDefs=[
                    reduce(
                        lambda one, another: {**one, **another},
                        configurations
                    )
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
                defaultColDef={
                    **ag_grid_configure.column_definitions.defaults.styles
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
                columnSize="responsiveSizeToFit",
                className="ag-theme-material",
                persistence=True,
            )
            logs_creation = dash_ag_grid.AgGrid(
                id=ids.elements.logs_creation,
                rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
                columnDefs=[
                    reduce(
                        lambda one, another: {**one, **another},
                        configurations
                    )
                    for configurations in zip(
                        ag_grid_configure.column_definitions.column,
                        ag_grid_configure.column_definitions.row_dragging,
                        ag_grid_configure.column_definitions.sorting,
                        ag_grid_configure.column_definitions.filtering,
                        ag_grid_configure.column_definitions.styles,
                    )
                ],
                defaultColDef={
                    **ag_grid_configure.column_definitions.defaults.styles
                },
                dashGridOptions={
                    **ag_grid_configure.options.sorting,
                    **ag_grid_configure.options.selection,
                    **ag_grid_configure.options.row_dragging,
                    **ag_grid_configure.options.navigation,
                },
                getRowId="params.data.id",
                columnSize="responsiveSizeToFit",
                className="ag-theme-material",
            )
            logs_updation = dash_ag_grid.AgGrid(
                id=ids.elements.logs_updation,
                rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
                columnDefs=[
                    reduce(
                        lambda one, another: {**one, **another},
                        configurations
                    )
                    for configurations in zip(
                        ag_grid_configure.column_definitions.column,
                        ag_grid_configure.column_definitions.row_dragging,
                        ag_grid_configure.column_definitions.sorting,
                        ag_grid_configure.column_definitions.filtering,
                        ag_grid_configure.column_definitions.styles,
                    )
                ],
                defaultColDef={
                    **ag_grid_configure.column_definitions.defaults.styles
                },
                dashGridOptions={
                    **ag_grid_configure.options.sorting,
                    **ag_grid_configure.options.selection,
                    **ag_grid_configure.options.row_dragging,
                    **ag_grid_configure.options.navigation,
                },
                getRowId="params.data.id",
                columnSize="responsiveSizeToFit",
                className="ag-theme-material",
            )
            logs_deletion = dash_ag_grid.AgGrid(
                id=ids.elements.logs_deletion,
                rowData=pandas.DataFrame(columns=relation.instances.keys()).to_dict('records'),
                columnDefs=[
                    reduce(
                        lambda one, another: {**one, **another},
                        configurations
                    )
                    for configurations in zip(
                        ag_grid_configure.column_definitions.column,
                        ag_grid_configure.column_definitions.row_dragging,
                        ag_grid_configure.column_definitions.sorting,
                        ag_grid_configure.column_definitions.filtering,
                        ag_grid_configure.column_definitions.styles,
                    )
                ],
                defaultColDef={
                    **ag_grid_configure.column_definitions.defaults.styles
                },
                dashGridOptions={
                    **ag_grid_configure.options.sorting,
                    **ag_grid_configure.options.selection,
                    **ag_grid_configure.options.row_dragging,
                    **ag_grid_configure.options.navigation,
                },
                getRowId="params.data.id",
                columnSize="responsiveSizeToFit",
                className="ag-theme-material",
            )
        return Elements()

    @property
    def functionalities(self):
        class Functionalities:
            clear_sorting=dash_bootstrap_components.Button(
                id=ids.listeners.clear_sorting,
                children="Clear Ordering",
                color="secondary",
                size="sm",
            )
            clear_filtering=dash_bootstrap_components.Button(
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
                    children='Drag and Drop or Click to Select Files',
                ),
                style={
                    'padding': '23px',
                    'borderStyle': 'dashed',
                    'borderWidth': '1.3px',
                    'borderRadius': '2.3px',
                    'borderColor': 'rgb(127, 127, 127)',
                    'backgroundColor': 'rgba(127, 127, 127, 0.23)',
                    'textAlign': 'center',
                },
            )
            create_instance = dash_bootstrap_components.Button(
                id=ids.listeners.instance_create,
                children='Create',
                n_clicks=0,
                color="secondary",
                size="sm",
            )
            delete_instance = dash_bootstrap_components.Button(
                id=ids.listeners.instance_delete,
                children='Delete',
                n_clicks=0,
                color="secondary",
                size="sm",
            )
            save = dash_bootstrap_components.Button(
                id=ids.listeners.save,
                children='Save',
                n_clicks=0,
                color="secondary",
                size="sm",
            )
        return Functionalities()
objects = Objects()