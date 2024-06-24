import re

def convert_cisco_to_palo_acl_set_commands(cisco_acl):
    set_commands = []
    
    acl_regex = re.compile(
        r'access-list (\d+) extended (permit|deny) (\w+) (any|host [\d.]+|object-group \S+) (any|host [\d.]+|object-group \S+)( eq (\d+))?'
    )
    
    rule_definitions = {}

    for line in cisco_acl.splitlines():
        line = line.strip()
        if not line:
            continue
        
        match = acl_regex.match(line)
        if match:
            acl_num, action, protocol, src, dst, _, port = match.groups()
            action = 'allow' if action == 'permit' else action
            src_network = parse_network_or_object(src)
            dst_network = parse_network_or_object(dst)
            service = protocol if not port else f'{protocol}/{port}'
            application = 'any' if protocol == 'ip' else protocol
            rule_name = f"{action.capitalize()}-{protocol.upper()}-{acl_num}"
            
            if rule_name not in rule_definitions:
                rule_definitions[rule_name] = {
                    "from": "any",
                    "to": "any",
                    "source": [],
                    "destination": [],
                    "application": application,
                    "service": service,
                    "action": action
                }
            
            if src_network not in rule_definitions[rule_name]["source"]:
                rule_definitions[rule_name]["source"].append(src_network)
            if dst_network not in rule_definitions[rule_name]["destination"]:
                rule_definitions[rule_name]["destination"].append(dst_network)
    
    for rule_name, details in rule_definitions.items():
        set_commands.append(f'set rulebase security rules {rule_name} from {details["from"]}')
        set_commands.append(f'set rulebase security rules {rule_name} to {details["to"]}')
        set_commands.append(f'set rulebase security rules {rule_name} source [ {" ".join(details["source"])} ]')
        set_commands.append(f'set rulebase security rules {rule_name} destination [ {" ".join(details["destination"])} ]')
        set_commands.append(f'set rulebase security rules {rule_name} application {details["application"]}')
        set_commands.append(f'set rulebase security rules {rule_name} service {details["service"]}')
        set_commands.append(f'set rulebase security rules {rule_name} action {details["action"]}')
    
    return set_commands

def parse_network_or_object(network):
    if network == "any":
        return "any"
    elif network.startswith("host"):
        ip = network.split()[1]
        return f"{ip}/32"
    elif network.startswith("object-group"):
        return network.split()[1]
    else:
        ip, wildcard = network.split()
        return convert_to_cidr(ip, wildcard)

def convert_to_cidr(ip, wildcard):
    ip_parts = list(map(int, ip.split('.')))
    wildcard_parts = list(map(int, wildcard.split('.')))
    netmask_parts = [255 - s for s in wildcard_parts]
    network_parts = [ip & netmask for ip, netmask in zip(ip_parts, netmask_parts)]
    subnet = '.'.join(map(str, network_parts))
    netmask = sum(bin(n).count('1') for n in netmask_parts)
    return f"{subnet}/{netmask}"

# Read Cisco ACL from file
with open('source_cisco_acls.txt', 'r') as file:
    cisco_acl = file.read()