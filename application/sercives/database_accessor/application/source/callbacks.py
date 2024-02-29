from dash import dcc as dash_core_componets, html as dash_html, Input, Output, State, Patch, ctx as context, no_update, clientside_callback
import pandas
from .utensils import FileParser
from .objects import ids, objects, relation
from copy import deepcopy
from ..models import DataManipulator

class Callbacks:

    @staticmethod
    def register(server):

        @server.callback(
            Output(ids.elements.relation, "columnState"),
            Output(ids.elements.relation, "resetColumnState"),
            Output(ids.elements.relation, "columnSize"),
            Output(ids.elements.relation, "columnSizeOptions"),
            State(ids.elements.relation, "columnState"),
            Input(ids.listeners.reset_ordering, "n_clicks"),
            prevent_initial_call=True,
        )
        def reset_ordering(column_states, *_):
            if context.triggered_id == ids.listeners.reset_ordering:
                for state in column_states:
                    state['sort'] = None
            return (
                column_states,
                True,
                "autoSize",
                {"skipHeader": False},
            )

        @server.callback(
            Output(ids.elements.relation, "dashGridOptions"),
            Output(ids.elements.logs_deletion, "dashGridOptions"),
            Input(ids.listeners.quick_filter, "value"),
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
            Output(ids.elements.relation, "rowTransaction"), # Synchronize.
            Output(ids.elements.logs_creation, "rowTransaction"),
            Output(ids.elements.relation, "selectedRows"), # Refresh.
            Output(ids.functionalities.container_upload_file, "children"),
            Input(ids.listeners.instance_create, "n_clicks"),
            State(ids.elements.relation, "selectedRows"), # For create or duplicate.
            State(ids.elements.relation, "columnDefs"),
            State(ids.elements.relation, "rowData"),
            State(ids.elements.logs_deletion, "rowData"),
            State(ids.functionalities.upload_file, "contents"), # For upload.
            State(ids.functionalities.upload_file, "filename"),
            prevent_initial_call=True,
        )
        def create_instance(
            n_clicks,
            selected_instances,
            column_definations,
            instances_relation,
            instances_deleted,
            contents,
            filename,
        ):
            
            ids = [instance['id'] for instance in (instances_relation + instances_deleted)]
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
            upload_container_children = objects.functionalities.upload_file

            return (
                transaction,
                transaction,
                selected_rows,
                upload_container_children,
            )

        @server.callback(
            Output(ids.elements.relation, "rowTransaction"),
            Output(ids.elements.logs_creation, "rowTransaction"),
            Output(ids.elements.logs_updation, "rowTransaction"),
            Output(ids.elements.relation, "selectedRows"),
            Input(ids.elements.relation, "cellValueChanged"),
            State(ids.elements.relation, "selectedRows"),
            State(ids.elements.logs_updation, "rowData"),
        )
        def update_instance(
            changed_cell,
            instances_selected,
            logs_updated_instances,
        ):
            changed_cell = changed_cell.pop()

            # Coordinate of changed cell and changed value.
            changed_column = changed_cell['colId']
            id_changed_instance = changed_cell['rowId']
            value = changed_cell['value']

            # Updated instances
            instances_updated = deepcopy(instances_selected)
            for instance in instances_updated:
                instance[changed_column] = value
            
            
            ids_updated_instances = [instance['id'] for instance in logs_updated_instances]
            newest_updated_instances = [instance for instance in instances_updated if instance['id'] not in ids_updated_instances]

            print(instances_updated)
            print(ids_updated_instances)
            
            transaction_updation = {
                'update': instances_updated
            }

            transaction_upserion = {
                "addIndex": 0, 
                "add": newest_updated_instances,
                'update': instances_updated
            }

            return (
                transaction_updation,
                transaction_updation,
                transaction_upserion,
                [],
            )
        
        @server.callback(
            Output(ids.elements.relation, "rowTransaction"),
            Output(ids.elements.logs_deletion, "rowTransaction"),
            Output(ids.elements.relation, "selectedRows"),
            Input(ids.listeners.instance_delete, "n_clicks"),
            State(ids.elements.relation, "selectedRows"),
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
            Output(ids.functionalities.upload_file, 'children'),
            Input(ids.functionalities.upload_file, 'contents'),
            State(ids.functionalities.upload_file, 'filename')
        )
        def log_uploaded_files(list_of_contents, filename):
            return dash_html.Div(filename)
        
        @server.callback(
            Output(ids.elements.logs_creation, "rowData"),
            Output(ids.elements.logs_updation, "rowData"),
            Output(ids.elements.logs_deletion, "rowData"),
            Input(ids.listeners.save, "n_clicks"),
            State(ids.elements.relation, "rowData"),
            State(ids.elements.logs_creation, "rowData"),
            State(ids.elements.logs_deletion, "rowData"),
        )
        def save(
            n_clicks,
            instance_updated,
            instance_created,
            instance_deleted,
        ):
            if instance_created:
                DataManipulator.create(
                    engine=relation.connection.engine,
                    data=pandas.DataFrame(instance_created),
                    schema=relation.configuration.relation.schema,
                    relation=relation.configuration.relation.table,
                )
            if instance_updated:
                DataManipulator.create(
                    engine=relation.connection.engine,
                    data=pandas.DataFrame(instance_updated),
                    schema=relation.configuration.relation.schema,
                    relation=relation.configuration.relation.table,
                )
            if instance_deleted:
                DataManipulator.delete(
                    engine=relation.connection.engine,
                    data=pandas.DataFrame(instance_deleted),
                    schema=relation.configuration.relation.schema,
                    relation=relation.configuration.relation.table,
                )
            relation.reload()
            empty = pandas.DataFrame(columns=relation.instances.keys()).to_dict('records')
            return (
                empty,
                empty,
                empty,
            )