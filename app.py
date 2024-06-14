# from pa_objectgroup_setcommands import convert_cisco_object_groups_to_palo_set_commands as obj_groups
# from pa_objectgroup_setcommands_2 import convert_cisco_object_groups_to_palo_set_commands_2 as obj_groups
from pa_objectgroup_setcommands_3 import convert_cisco_object_groups_to_palo_set_commands_3 as obj_groups
from pa_acl_setcommands_3 import convert_cisco_to_palo_acl_set_commands_3 as acls

def main():
  Generate_PaloAlto_ObjectGroup_SetCommands()
  Generate_PaloAlto_ACL_SetCommands()
  

def Generate_PaloAlto_ObjectGroup_SetCommands():
  with open('cisco_object_groups.txt', 'r') as objectgroup_input_file:
      cisco_object_groups = objectgroup_input_file.read()
  obj_groups(cisco_object_groups)

def Generate_PaloAlto_ACL_SetCommands():
  with open('cisco_acl_list.txt', 'r') as acl_input_file:
    cisco_acl_list = acl_input_file.read()
  acls(cisco_acl_list)

