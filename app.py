import os
import argparse

from pa_objectgroup_setcommands import convert_cisco_object_groups_to_palo_set_commands as obj_groups
from pa_acl_setcommands import convert_cisco_to_palo_acl_set_commands as acls

def Main(output_file_arg, append_arg=False):
  palo_alto_commands = Generate_PaloAlto_ObjectGroup_SetCommands()
  palo_alto_commands += Generate_PaloAlto_ACL_SetCommands()
  Write_To_Output_File(output_file_arg, palo_alto_commands, append_arg)

def Generate_PaloAlto_ObjectGroup_SetCommands():
  with open('source_cisco_objectgroups.txt', 'r') as objectgroup_input_file:
    cisco_object_groups = objectgroup_input_file.read()
  return obj_groups(cisco_object_groups)

def Generate_PaloAlto_ACL_SetCommands():
  with open('source_cisco_acls.txt', 'r') as acl_input_file:
    cisco_acl_list = acl_input_file.read()
  return acls(cisco_acl_list)

def Set_Output_Filepath(filepath:str=None):
  try:
    if filepath is None:
      return os.path.join(os.getcwd(), 'palo_alto_setcommands.sh')
    else:
      filepath = Validate_Filepath_Per_OS(filepath)

    print(f"Output file path: {filepath}")
    
    if os.path.isabs(filepath):
      return os.path.join(os.getcwd(), filepath)
    else:
      return filepath
  except Exception as e:
    print(f"[Set_Output_Filepath] An error occurred: {e}")
    exit()

def Validate_Filepath_Per_OS(filepath:str):
  try:
      
    if filepath is not None and os.name == 'nt':
      filepath = filepath.replace('/', '\\')
    else:
      filepath = filepath.replace('\\', '/')
    return filepath
  except Exception as e:
    print(f"[Validate_Filepath_Per_OS] An error occurred: {e}")
    exit()

def Write_To_Output_File(filepath, commands:list, append=False):
  try:
    file_mode = 'a' if append else 'w'
    with open(filepath, file_mode) as file:
      for command in commands:
        file.write(command)
        file.write('\n')
    print(f"Palo Alto commands successfully written to: {filepath}.")
  except Exception as e:
    print(f"An error occurred: {e}")
    exit()

def Show_Help():
  print('This script converts Cisco ASA configuration to Palo Alto configuration.')
  print('The script reads the source files: source_cisco_objectgroups.txt and source_cisco_acls.txt.')
  print('The script generates Palo Alto set commands for object groups and ACLs.')
  print('The output is written to the (specified) file (or default: ./palo_alto_setcommands.sh).')
  print('Options:')
  print('  --h: Show Help Menu (this)')
  print('  --a: Append or overwrite current output shell script file (Default: Overwrite)')
  print('  --f: The file path to append content to (Default: \'palo_alto_setcommands.sh\' in current directory)')
  print('Example Usage:')
  print('  python app.py --h')
  print('     shows this help menu.')
  print('  python app.py --a true')
  print('     appends to output file, and uses default file path for output.')
  print('  python app.py --f /path/to/output-file.sh')
  print('     overwrites specified output file.')
  print('  python app.py --a true --f /path/to/output-file.sh')
  print('     appends to output file, and uses specified file path for output.')
  exit()

def Show_Exit_Output(filepath:str):
  print('Conversion process complete.')
  print()
  print(f'Palo Alto commands successfully written to: {filepath}.')
  print()
  print('Please review/validate output in the shell file before executing the commands.')
  print()
  print('Connect to, then execute the shell script to configure the Palo Alto device.')
  print()
  print('Exiting script...')
  print()

if __name__ == '__main__':
  # default Arg values
  append = False
  filepath = Set_Output_Filepath()

  # Create and configure parser
  parser = argparse.ArgumentParser()
  parser.add_argument('--h', action='store_true', help='Shows Help')
  parser.add_argument('--a', action='store_true', help='Append or overwrite current output shell script file.')
  parser.add_argument('--f', type=str, default='palo_alto_setcommands.sh', help='The file path to append content to.')
  supplied_args = parser.parse_args()

  if (supplied_args.h):
    Show_Help() # exits script
  if (supplied_args.a):
    append = True # default behavior is to overwrite the output file
  if (supplied_args.f is not None):
    filepath = Set_Output_Filepath(supplied_args.f) # sets the full output file path
  print()
  print('Starting conversion process...')
  print()

  Main(filepath, append)

  Show_Exit_Output(filepath) # exits script
