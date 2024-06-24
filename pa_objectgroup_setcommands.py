import re

def convert_cisco_object_groups_to_palo_set_commands(cisco_object_groups):
    set_commands = []
    address_commands = []
    service_commands = []
    address_group_members = {}
    service_group_members = {}
    
    current_group = None
    group_type = None
    
    for line in cisco_object_groups.splitlines():
        line = line.strip()
        if not line:
            continue
        
        # Match network object groups
        match_network = re.match(r'object-group network (\S+)', line)
        if match_network:
            current_group = match_network.group(1)
            group_type = 'network'
            address_group_members[current_group] = []
            continue
        
        # Match service object groups
        match_service = re.match(r'object-group service (\S+)', line)
        if match_service:
            current_group = match_service.group(1)
            group_type = 'service'
            service_group_members[current_group] = []
            continue
        
        # Match network-object
        if group_type == 'network':
            match_network_object = re.match(r'network-object (host )?([\d.]+)( ([\d.]+))?', line)
            if match_network_object and current_group:
                host, ip, _, subnet = match_network_object.groups()
                if host:
                    address_name = f'H-{ip}'
                    address_commands.append(f'set address {address_name} ip-netmask {ip}/32')
                    address_group_members[current_group].append(address_name)
                else:
                    cidr = convert_to_cidr(ip, subnet)
                    address_name = f'H-{cidr.replace("/", "-")}'
                    address_commands.append(f'set address {address_name} ip-netmask {cidr}')
                    address_group_members[current_group].append(address_name)
            continue
        
        # Match service-object
        if group_type == 'service':
            match_service_object = re.match(r'service-object (\S+) (\d+)', line)
            if match_service_object and current_group:
                protocol, port = match_service_object.groups()
                service_name = f'{protocol}-{port}'
                service_commands.append(f'set service {service_name} protocol {protocol} port {port}')
                service_group_members[current_group].append(service_name)
            continue
    
    # Generate set commands for address groups
    for group, members in address_group_members.items():
        members_list = " ".join(members)
        set_commands.append(f'set address-group {group} static [ {members_list} ]')
    
    # Generate set commands for service groups
    for group, members in service_group_members.items():
        members_list = " ".join(members)
        set_commands.append(f'set service-group {group} members [ {members_list} ]')
    
    return address_commands + service_commands + set_commands

def convert_to_cidr(ip, subnet):
    ip_parts = list(map(int, ip.split('.')))
    subnet_parts = list(map(int, subnet.split('.')))
    netmask_parts = [255 - s for s in subnet_parts]
    network_parts = [ip & netmask for ip, netmask in zip(ip_parts, netmask_parts)]
    subnet = '.'.join(map(str, network_parts))
    netmask = sum(bin(n).count('1') for n in netmask_parts)
    return f"{subnet}/{netmask}"

# Read Cisco Object Groups from file
with open('source_cisco_objectgroups.txt', 'r') as file:
    cisco_object_groups = file.read()