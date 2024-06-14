import re


def convert_cisco_object_groups_to_palo_set_commands_3(cisco_object_groups):
    set_commands = []
    address_commands = []
    address_group_members = {}

    current_group = None
    for line in cisco_object_groups.splitlines():
        line = line.strip()
        if not line:
            continue

        # Match network object groups
        match_network = re.match(r"object-group network (\S+)", line)
        if match_network:
            current_group = match_network.group(1)
            address_group_members[current_group] = []
            continue

        # Match network-object
        match_network_object = re.match(
            r"network-object (host )?([\d.]+)( ([\d.]+))?", line
        )
        if match_network_object and current_group:
            host, ip, _, subnet = match_network_object.groups()
            if host:
                address_name = f"H-{ip}"
                address_commands.append(
                    f"set address {address_name} ip-netmask {ip}/32"
                )
                address_group_members[current_group].append(address_name)
            else:
                cidr = convert_to_cidr(ip, subnet)
                address_name = f'H-{cidr.replace("/", "-")}'
                address_commands.append(f"set address {address_name} ip-netmask {cidr}")
                address_group_members[current_group].append(address_name)
            continue

    # Generate set commands for address groups
    for group, members in address_group_members.items():
        members_list = " ".join(members)
        set_commands.append(f"set address-group {group} static [ {members_list} ]")

    return address_commands + set_commands


def convert_to_cidr(ip, subnet):
    ip_parts = list(map(int, ip.split(".")))
    subnet_parts = list(map(int, subnet.split(".")))
    netmask_parts = [255 - s for s in subnet_parts]
    network_parts = [ip & netmask for ip, netmask in zip(ip_parts, netmask_parts)]
    subnet = ".".join(map(str, network_parts))
    netmask = sum(bin(n).count("1") for n in netmask_parts)
    return f"{subnet}/{netmask}"


# Read Cisco Object Groups from file
with open("cisco_object_groups.txt", "r") as file:
    cisco_object_groups = file.read()

palo_alto_set_commands = convert_cisco_object_groups_to_palo_set_commands_3(
    cisco_object_groups
)

print("\n # Generated Palo Alto __ObjectGroup__ Set Commands:\n")
for command in palo_alto_set_commands:
    print(command)
