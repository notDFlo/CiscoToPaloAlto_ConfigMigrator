from pa_objectgroup_setcommands_3 import convert_cisco_object_groups_to_palo_set_commands_3 as obj_groups
from pa_acl_setcommands_3 import convert_cisco_to_palo_acl_set_commands_3 as acls

def main():
  Generate_PaloAlto_ObjectGroup_SetCommands()
  Generate_PaloAlto_ACL_SetCommands()
  
def Generate_PaloAlto_ObjectGroup_SetCommands():
  with open('source_cisco_objectgroups.txt', 'r') as objectgroup_input_file:
      cisco_object_groups = objectgroup_input_file.read()
  pa_objgroup_setcommands_content = obj_groups(cisco_object_groups)
  pa_objgroup_setcommands_filepath = 'palo_alto_setcommands_output.sh'

def Generate_PaloAlto_ACL_SetCommands():
  with open('source_cisco_acls.txt', 'r') as acl_input_file:
    cisco_acl_list = acl_input_file.read()
  pa_acl_setcommands_content = acls(cisco_acl_list)
  pa_acl_setcommands_filepath = 'palo_alto_setcommands_output.sh'
