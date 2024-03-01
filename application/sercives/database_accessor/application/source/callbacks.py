from dash import dcc as dash_core_componets, html as dash_html, Input, Output, State, Patch, ctx as context, no_update, clientside_callback
import pandas
from .utensils import FileParser
from .objects import ids, objects, relation
from copy import deepcopy
from ..models import DataManipulator
from dash_extensions import Keyboard

class Callbacks:

    @staticmethod
    def register(server):

        @server.callback(
            Output(ids.elements.operating_relation, "resetColumnState"),
            # Output(ids.elements.operating_relation, "columnSize"),
            # Output(ids.elements.operating_relation, "columnSizeOptions"),
            Input(ids.listeners.clear_sorting, "n_clicks"),
            State(ids.elements.operating_relation, "columnState"),
            prevent_initial_call=True,
        )
        def clear_sorting(
            n_clicks,
            column_states,
        ):
            return (
                True
                # "autoSize",
                # {"skipHeader": False},
            )

        @server.callback(
            Output(ids.elements.operating_relation, "dashGridOptions"),
            Output(ids.elements.operating_relation, "filterModel"),
            Output(ids.functionalities.quick_filter, "value"),
            Input(ids.listeners.clear_filtering, "n_clicks"),
            State(ids.elements.operating_relation, "filterModel"),
        )
        def clear_filtering(
            n_clicks,
            model,
        ):
            patch = Patch()
            patch['quickFilterText'] = ''
            value = ''
            model = {}
            return (
                patch,
                model,
                value,
            )

        @server.callback(
            Output(ids.elements.operating_relation, "dashGridOptions"),
            Input(ids.functionalities.quick_filter, "value"),
            prevent_initial_call=True,
        )
        def quick_filter(
            filter_value,
        ):
            patch = Patch()
            patch['quickFilterText'] = filter_value
            return (
                patch
            )

        @server.callback(
            Output(ids.elements.operating_relation, "rowTransaction"), # Synchronize.
            Output(ids.elements.logs_creation, "rowTransaction"),
            Output(ids.elements.operating_relation, "selectedRows"), # Refresh.
            Output(ids.functionalities.container_upload_file, "children"),
            Input(ids.listeners.instance_create, "n_clicks"),
            State(ids.elements.operating_relation, "selectedRows"), # For create or duplicate.
            State(ids.elements.operating_relation, "columnDefs"),
            State(ids.elements.operating_relation, "rowData"),
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
                
                for offset, instance in enumerate(instances, start=1):
                    instance['id'] = maximum_id + offset
            else:

                if contents:

                    parser = FileParser(
                        contents=contents,
                        filename=filename,
                    )
                    instances = parser.execute()

                    instances = instances.to_dict('records')

                    for offset, instance in enumerate(instances, start=1):
                        instance['id'] = maximum_id + offset
                else:

                    instances = [{
                        defination['field']: (maximum_id + 1 if defination['field'] == 'id' else None)
                        for defination in column_definations
                    }]
                
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
            Output(ids.elements.operating_relation, "rowTransaction"),
            Output(ids.elements.logs_creation, "rowTransaction"),
            Output(ids.elements.logs_updation, "rowTransaction"),
            Output(ids.elements.operating_relation, "selectedRows"),
            Input(ids.elements.operating_relation, "cellValueChanged"),
            State(ids.elements.operating_relation, "selectedRows"),
            State(ids.elements.logs_updation, "rowData"),
            State(ids.elements.logs_creation, "rowData"),
        )
        def update_instance(
            changed_cell,
            instances_selected,
            logs_updated_instances,
            logs_created_instances,
        ):
            changed_cell = changed_cell.pop()

            changed_cell_id = int(changed_cell['rowId'])
            changed_cell_column = changed_cell['colId']
            changed_cell_value = changed_cell['value']
            # If changed cell is not selected, revised the selected informations.
            ids_selected_instances = [instance['id'] for instance in instances_selected]
            if changed_cell_id not in ids_selected_instances:
                ids_selected_instances = [changed_cell_id]
                instances_selected = [changed_cell['data']]

            instances_updated = pandas.DataFrame(instances_selected)
            instances_updated[changed_cell_column] = changed_cell_value
            
            ids_logs_creation = set(int(instance['id']) for instance in logs_created_instances)
            ids_logs_updation = set(int(instance['id']) for instance in logs_updated_instances)

            updated_instances_from_logs_creation = instances_updated.query("id in @ids_logs_creation")
            updated_instances_from_logs_updation = instances_updated.query("id not in @ids_logs_creation & id in @ids_logs_updation")
            updated_instances_not_created_in_logs_updation = instances_updated.query("id not in @ids_logs_creation & id not in @ids_logs_updation")
            
            transaction_update_relation = {
                'update': instances_updated.to_dict('records')
            }
            
            transaction_update_logs_creation = {
                'update': updated_instances_from_logs_creation.to_dict('records')
            }

            transaction_upsert_logs_updation = {
                "addIndex": 0,
                "add": updated_instances_not_created_in_logs_updation.to_dict('records'),
                'update': updated_instances_from_logs_updation.to_dict('records')
            }

            return (
                transaction_update_relation,
                transaction_update_logs_creation,
                transaction_upsert_logs_updation,
                [],
            )
        
        @server.callback(
            Output(ids.elements.operating_relation, "rowTransaction"),
            Output(ids.elements.logs_deletion, "rowTransaction"),
            Output(ids.elements.operating_relation, "selectedRows"),
            Input(ids.listeners.instance_delete, "n_clicks"),
            State(ids.elements.operating_relation, "selectedRows"),
            prevent_initial_call=True,
        )
        def delete_instance(
            n_clicks,
            selected_instances,
        ):

            transaction_deleteRelationInstance = {
                "remove": selected_instances,
            }

            transaction_addLogsDeletionInstances = {
                "addIndex": 0,
                "add": selected_instances,
            }
            
            return (
                transaction_deleteRelationInstance,
                transaction_addLogsDeletionInstances,
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
            State(ids.elements.operating_relation, "rowData"),
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
                DataManipulator.write(
                    engine=relation.connection.engine,
                    data=pandas.DataFrame(instance_created),
                    schema=relation.configuration.relation.schema,
                    relation=relation.configuration.relation.table,
                )
            if instance_updated:
                DataManipulator.write(
                    engine=relation.connection.engine,
                    data=pandas.DataFrame(instance_updated),
                    schema=relation.configuration.relation.schema,
                    relation=relation.configuration.relation.table,
                )
            if instance_deleted:
                DataManipulator.write(
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
