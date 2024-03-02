class IDs:
    @property
    def elements(self):
        class Elements:
            operating_relation = "elements_operatingRelation"
            logs_creation = "elements_logsCreation"
            logs_updation = "elements_logsUpdation"
            logs_deletion = "elements_logsDeletion"

        return Elements()

    @property
    def functionalities(self):
        class Functionalities:
            quick_filter = "listener_quickFilter"
            upload_file = "functionalities_uploadFile"
            container_upload_file = "container_uploadFileFunctionalities"

        return Functionalities()

    @property
    def listeners(self):
        class Listeners:
            refresh = "listener_refresh"
            clear_sorting = "listener_clearSorting"
            clear_filtering = "listener_clearFiltering"
            instance_create = "listener_createInstance"
            instance_delete = "listener_deleteInstance"
            instance_update = "listener_updateInstance"
            save = "listener_save"

        return Listeners()


ids = IDs()
