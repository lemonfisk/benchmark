
from ansible.plugins.action import ActionBase

 
class ActionModule(ActionBase):
    def init(self, task, connection, play_context, loader, templar, shared_loader_obj):
        super(ActionModule, self).init(task, connection, play_context, loader, templar, shared_loader_obj)
 
    def run(self, task_vars=None):
         
 
        return {
            "projects processed": "catalog_base.count_projects"
        }