from dash import dcc as dash_core_componets, html as dash_html, Input, Output, State, Patch, ctx as context, no_update, clientside_callback
import pandas
from .utensils import FileParser
from .objects import IDs, Objects
from copy import deepcopy

class Callbacks:

    @staticmethod
    def register(server):

        @server.callback(
            Output(IDs.object_relation, "columnState"),
            Output(IDs.object_relation, "resetColumnState"),
            Output(IDs.object_relation, "columnSize"),
            Output(IDs.object_relation, "columnSizeOptions"),
            State(IDs.object_relation, "columnState"),
            Input(IDs.listener_resetOrdering, "n_clicks"),
            prevent_initial_call=True,
        )
        def reset_ordering(column_states, *_):
            if context.triggered_id == IDs.listener_resetOrdering:
                for state in column_states:
                    state['sort'] = None
            return (
                column_states,
                True,
                "autoSize",
                {"skipHeader": False},
            )

        @server.callback(
            Output(IDs.object_relation, "dashGridOptions"),
            Output(IDs.object_processingRelation, "dashGridOptions"),
            Input(IDs.listener_quickFilter, "value"),
            prevent_initial_call=True,
        )
        def quick_filter(filter_text):
            updated_filter_text = Patch()
            updated_filter_text['quickFilterText'] = filter_text
            return (
                updated_filter_text,
                updated_filter_text,
            )

        @server.callback(
            Output(IDs.object_relation, "rowTransaction"),
            Output(IDs.object_relation, "selectedRows"),
            Output(IDs.container_uploadFileFunctionality, "children"),
            Input(IDs.listener_createInstance, "n_clicks"),
            State(IDs.object_relation, "selectedRows"),
            State(IDs.object_relation, "columnDefs"),
            State(IDs.object_relation, "rowData"),
            State(IDs.functionality_uploadFile, "contents"),
            State(IDs.functionality_uploadFile, "filename"),
            prevent_initial_call=True,
        )
        def create_instance(
            n_clicks,
            selected_instances,
            column_definations,
            instances_relation,
            contents,
            filename,
        ):
            
            ids = [instance['id'] for instance in instances_relation]
            maximum_id = max(ids) if ids else 0

            if selected_instances:

                instances = deepcopy(selected_instances)
                
                for index, instance in enumerate(instances):
                    instance['id'] = (maximum_id + 1) + index
                
            else:

                instances = [
                    {
                        defination['field']: (maximum_id + 1 if defination['field'] == 'id' else None)
                        for defination in column_definations
                    }
                ]
            
            if contents:

                parser = FileParser(
                    contents=contents,
                    filename=filename,
                )
                instances = parser.execute()

                instances = instances.to_dict('records')

                for index, instance in enumerate(instances):
                    instance['id'] = (maximum_id + 1) + index
                
            transaction = {
                "addIndex": 0,
                "add": instances,
            }
            selected_rows = []
            upload_container_children = Objects.functionality_uploadFile

            return (
                transaction,
                selected_rows,
                upload_container_children,
            )

        @server.callback(
            Output(IDs.object_relation, "rowTransaction"),
            Output(IDs.object_processingRelation, "rowTransaction"),
            Output(IDs.object_relation, "selectedRows"),
            Input(IDs.listener_deleteInstance, "n_clicks"),
            State(IDs.object_relation, "selectedRows"),
            prevent_initial_call=True,
        )
        def delete_instance(
            n_clicks,
            selected_instances,
        ):

            transaction_deleteRelationInstance = {
                "remove": selected_instances,
            }

            transaction_addProcessingRelationDeletedInstances = {
                "addIndex": 0,
                "add": selected_instances,
            }
            
            return (
                transaction_deleteRelationInstance,
                transaction_addProcessingRelationDeletedInstances,
                [],
            )
        
        @server.callback(
            Output(IDs.object_relation, "rowTransaction"),
            Output(IDs.object_relation, "selectedRows"),
            Input(IDs.object_relation, "cellValueChanged"),
            State(IDs.object_relation, "selectedRows"),
        )
        def update_instance(
            changed_cell,
            selected_instances,
        ):
            changed_cell = changed_cell.pop()
            changed_column = changed_cell['colId']
            
            value = changed_cell['value']

            for instance in selected_instances:
                instance[changed_column] = value

            transaction = {
                'update': selected_instances
            }

            return transaction, []
        
        @server.callback(
            Output(IDs.functionality_uploadFile, 'children'),
            Input(IDs.functionality_uploadFile, 'contents'),
            State(IDs.functionality_uploadFile, 'filename')
        )
        def log_uploaded_files(list_of_contents, filename):
            return dash_html.Div(filename)