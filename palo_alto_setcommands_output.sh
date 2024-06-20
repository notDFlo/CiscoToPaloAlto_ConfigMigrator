[Running] python -u "c:\dev\github\Python\CiscoToPaloAlto_ConfigMigrator\app.py"

 # Generated Palo Alto __ObjectGroup__ Set Commands:

set address H-172.16.24.1 ip-netmask 172.16.24.1/32
set address H-172.16.24.2 ip-netmask 172.16.24.2/32
set address H-172.16.24.3 ip-netmask 172.16.24.3/32
set address H-172.16.24.4 ip-netmask 172.16.24.4/32
set address H-172.16.24.5 ip-netmask 172.16.24.5/32
set address H-172.16.24.6 ip-netmask 172.16.24.6/32
set address H-172.16.24.7 ip-netmask 172.16.24.7/32
set address H-172.16.24.8 ip-netmask 172.16.24.8/32
set address H-172.16.24.9 ip-netmask 172.16.24.9/32
set address H-172.16.24.10 ip-netmask 172.16.24.10/32
set address H-172.16.24.11 ip-netmask 172.16.24.11/32
set address H-172.16.24.12 ip-netmask 172.16.24.12/32
set address H-172.16.24.13 ip-netmask 172.16.24.13/32
set address H-172.16.24.14 ip-netmask 172.16.24.14/32
set address H-172.16.24.15 ip-netmask 172.16.24.15/32
set address H-172.16.24.16 ip-netmask 172.16.24.16/32
set address H-172.16.24.17 ip-netmask 172.16.24.17/32
set address H-172.16.24.18 ip-netmask 172.16.24.18/32
set address H-172.16.24.19 ip-netmask 172.16.24.19/32
set address H-172.16.24.20 ip-netmask 172.16.24.20/32
set address H-172.16.24.21 ip-netmask 172.16.24.21/32
set address H-172.16.24.22 ip-netmask 172.16.24.22/32
set address H-172.16.24.23 ip-netmask 172.16.24.23/32
set address H-172.16.24.24 ip-netmask 172.16.24.24/32
set address H-172.16.24.25 ip-netmask 172.16.24.25/32
set address H-172.16.24.26 ip-netmask 172.16.24.26/32
set address H-172.16.24.27 ip-netmask 172.16.24.27/32
set address H-172.16.24.28 ip-netmask 172.16.24.28/32
set address H-172.16.24.29 ip-netmask 172.16.24.29/32
set address H-172.16.24.30 ip-netmask 172.16.24.30/32
set address H-172.16.24.31 ip-netmask 172.16.24.31/32
set address H-172.16.24.32 ip-netmask 172.16.24.32/32
set address H-172.16.24.33 ip-netmask 172.16.24.33/32
set address H-172.16.24.34 ip-netmask 172.16.24.34/32
set address H-0.0.0.0-8 ip-netmask 0.0.0.0/8
set address-group WEB-TEST static [ H-172.16.24.1 H-172.16.24.2 H-172.16.24.3 H-172.16.24.4 H-172.16.24.5 H-172.16.24.6 H-172.16.24.7 H-172.16.24.8 H-172.16.24.9 H-172.16.24.10 H-172.16.24.11 H-172.16.24.12 H-172.16.24.13 H-172.16.24.14 H-172.16.24.15 H-172.16.24.16 H-172.16.24.17 ]
set address-group WEB-DEV static [ H-172.16.24.18 H-172.16.24.19 H-172.16.24.20 H-172.16.24.21 H-172.16.24.22 H-172.16.24.23 H-172.16.24.24 H-172.16.24.25 H-172.16.24.26 H-172.16.24.27 H-172.16.24.28 H-172.16.24.29 H-172.16.24.30 H-172.16.24.31 H-172.16.24.32 H-172.16.24.33 H-172.16.24.34 ]
set address-group VIPS static [ H-0.0.0.0-8 ]

 # Generated Palo Alto __ACL__ Set Commands:

set rulebase security rules Allow-IP-101 from any
set rulebase security rules Allow-IP-101 to any
set rulebase security rules Allow-IP-101 source [ 172.16.24.1/32 172.16.24.2/32 172.16.24.3/32 172.16.24.4/32 172.16.24.5/32 172.16.24.6/32 172.16.24.7/32 ]
set rulebase security rules Allow-IP-101 destination [ WEB-TEST ]
set rulebase security rules Allow-IP-101 application any
set rulebase security rules Allow-IP-101 service ip
set rulebase security rules Allow-IP-101 action allow
set rulebase security rules Deny-IP-102 from any
set rulebase security rules Deny-IP-102 to any
set rulebase security rules Deny-IP-102 source [ 172.16.24.11/32 172.16.24.12/32 172.16.24.13/32 172.16.24.14/32 172.16.24.15/32 ]
set rulebase security rules Deny-IP-102 destination [ WEB-DEV ]
set rulebase security rules Deny-IP-102 application any
set rulebase security rules Deny-IP-102 service ip
set rulebase security rules Deny-IP-102 action deny
set rulebase security rules Allow-IP-102 from any
set rulebase security rules Allow-IP-102 to any
set rulebase security rules Allow-IP-102 source [ 172.16.24.16/32 172.16.24.17/32 172.16.24.18/32 ]
set rulebase security rules Allow-IP-102 destination [ WEB-DEV ]
set rulebase security rules Allow-IP-102 application any
set rulebase security rules Allow-IP-102 service ip
set rulebase security rules Allow-IP-102 action allow
set rulebase security rules Allow-TCP-101 from any
set rulebase security rules Allow-TCP-101 to any
set rulebase security rules Allow-TCP-101 source [ any ]
set rulebase security rules Allow-TCP-101 destination [ WEB-SRVS VIPS ]
set rulebase security rules Allow-TCP-101 application tcp
set rulebase security rules Allow-TCP-101 service tcp
set rulebase security rules Allow-TCP-101 action allow

set service