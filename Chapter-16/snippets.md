# Ansible Automation Best Practices for Production

- [Ansible Automation Best Practices for Production](#ansible-automation-best-practices-for-production)
  - [Figure 16.1. Typical Ansible project directory](#figure-161-typical-ansible-project-directory)
  - [Figure 16.2. Ansible roles directory](#figure-162-ansible-roles-directory)
  - [Figure 16.3. Sample static inventory file.](#figure-163-sample-static-inventory-file)
  - [Figure 16.4. Ansible inventory with user-friendly names](#figure-164-ansible-inventory-with-user-friendly-names)
  - [Figure 16.5. Ansible inventory organized based on environment](#figure-165-ansible-inventory-organized-based-on-environment)
  - [Figure 16.6. Ansible inventory organized based on environment](#figure-166-ansible-inventory-organized-based-on-environment)
  - [Figure 16.7. Host groups and group variables for managed nodes](#figure-167-host-groups-and-group-variables-for-managed-nodes)
  - [Figure 16.8. Hosts and host groups listing using ansible-inventory command](#figure-168-hosts-and-host-groups-listing-using-ansible-inventory-command)
  - [Figure 16.10. Ansible inventory with web group](#figure-1610-ansible-inventory-with-web-group)
  - [Figure 16.11. Create directories for group variables and host variables](#figure-1611-create-directories-for-group-variables-and-host-variables)
  - [Figure 16.12. Create group variable file](#figure-1612-create-group-variable-file)
  - [Figure 16.13. Create host variable file](#figure-1613-create-host-variable-file)
  - [Figure 16.14. Create host variable file for node2](#figure-1614-create-host-variable-file-for-node2)
  - [Figure 16.15. Project directory structure with group variable and host variables](#figure-1615-project-directory-structure-with-group-variable-and-host-variables)
  - [Figure 16.16. Verify inventory and variables using ansible-inventory command](#figure-1616-verify-inventory-and-variables-using-ansible-inventory-command)
  - [Figure 16.17. Different use account for remote nodes.](#figure-1617-different-use-account-for-remote-nodes)
  - [Figure 16.18. Encrypt sensitive files using Ansible vault](#figure-1618-encrypt-sensitive-files-using-ansible-vault)
  - [Figure 16.19. Ansible vault password prompting](#figure-1619-ansible-vault-password-prompting)

## Figure 16.1. Typical Ansible project directory 

```shell
[ansible@ansible Chapter-16]$ tree ./ 
./ 
├── ansible.cfg                 # ansible configuration 
├── deploy-web.yml              # a playbook 
├── group_vars                  # directory for group level variables 
│   ├── dbnodes.yaml            # variables for inventoy group dbnodes 
│   └── web.yaml                # variables for inventoy group web 
├── hosts                       # another inventory file 
├── host_vars                   # directory for host level variables 
│   ├── node1.yaml              # variables for node1 
│   └── node2.yaml              # variables for node2 
├── nodes_development           # inventory for development nodes 
├── nodes_production            # inventory for production nodes 
├── nodes_staging               # inventory for staging nodes 
├── README.md 
```

## Figure 16.2. Ansible roles directory

```shell
├── roles                        # roles directory 
│   ├── deploy-web-server        # web deployment role 
│   │   ├── defaults 
│   │   │   └── main.yml 
│   │   ├── tasks 
│   │   │   └── main.yml 
│   │   ├── templates 
│   │   ├── tests 
│   │   │   ├── inventory 
│   │   │   └── test.yml 
│   │   └── vars 
│   │       └── main.yml 
│   ├── security-baseline-rhel8  # security hardening role
     ... output omitted... 
├── site.yml 
├── system-info.yml 
├── system-reboot.yml 
  
38 directories, 56 files 
```

## Figure 16.3. Sample static inventory file. 

```shell
10.1.10.100 
192.168.1.25 
10.1.10.25 
10.2.100.40 
dbserver-101.example.com 
prod-app-101.example.com
```

## Figure 16.4. Ansible inventory with user-friendly names

```ini
web01 ansible_host=10.1.10.100 
app02 ansible_host=192.168.1.25 
lb101 ansible_host=10.1.10.25 
db201 ansible_host=10.2.100.40 
web102 ansible_host=sglxwp-101.example.com 
app301 ansible_host=slixmkp-app-101.example.com 
```

## Figure 16.5. Ansible inventory organized based on environment

```shell
[ansible@ansible inventories]$ tree ./ 
./ 
├── dev 
│   ├── group_vars 
│   │   ├── dbnodes.yaml 
│   │   └── web.yaml 
│   └── hosts 
├── prod 
│   ├── group_vars 
│   │   ├── dbnodes.yaml 
│   │   └── web.yaml 
│   ├── hosts 
│   └── host_vars 
│       ├── node1.yaml 
│       └── node2.yaml 
└── stg 
    └── hosts 
```

## Figure 16.6. Ansible inventory organized based on environment 

```shell
[ansible@ansible inventories]$ tree ./
./ 
├── dev 
│   ├── group_vars 
│   │   ├── dbnodes.yaml 
│   │   └── web.yaml 
│   └── hosts 
├── prod 
│   ├── group_vars 
│   │   ├── dbnodes.yaml 
│   │   └── web.yaml 
│   ├── hosts 
│   └── host_vars 
│       ├── node1.yaml 
│       └── node2.yaml 
└── stg 
    └── hosts 
```

## Figure 16.7. Host groups and group variables for managed nodes 

```shell
# file: dev/hosts 
# singapore web servers 
# group variables in dev/group_vars/web.yaml 
[web] 
web101.example.com 
web102.example.com 
web103.example.com 
  
# singapore db servers 
# group variable in dev/group_vars/dbnodes.yaml 
[dbnodes] 
db201.example.com 
db202.example.com 
db203.example.com 
  
# backup nodes in Malaysia 
[backupnodes] 
bkp101.example.com 
bkp102.example.com 
  
# Singapore servers in a parent group 
[sgnodes:children] 
web 
dbnodes
```

## Figure 16.8. Hosts and host groups listing using ansible-inventory command 

```shell
[ansible@ansible inventories]$ ansible-inventory -i dev/hosts --list 
{ 
    "_meta": { 
        "hostvars": {} 
    }, 
    "all": { 
        "children": [ 
            "backupnodes", 
            "sgnodes", 
            "ungrouped" 
        ] 
    }, 
    ... output omitted... 
    "sgnodes": { 
        "children": [ 
            "dbnodes", 
            "web" 
        ] 
    }, 
    "web": { 
        "hosts": [ 
            "web101.example.com", 
            "web102.example.com", 
            "web103.example.com" 
        ] 
    } 
}
```

## Figure 16.10. Ansible inventory with web group

```shell
# file: stg/hosts 
[web] 
node1 ansible_host=192.168.56.25 
node2 ansible_host=192.168.56.24 
node3 ansible_host=192.168.56.60 
  
[all:vars] 
ansible_ssh_private_key_file=/home/ansible/.ssh/id_rsa
```

## Figure 16.11. Create directories for group variables and host variables

```shell
[ansible@ansible Chapter-16]$ mkdir inventories/stg/group_vars 
[ansible@ansible Chapter-16]$ mkdir inventories/stg/host_vars 
```

## Figure 16.12. Create group variable file 

```shell
# file: stg/group_vars/web.yaml 
web_server_port: 80 
```

## Figure 16.13. Create host variable file 

```shell
# file: stg/host_vars/node1.yaml 
web_server_port: 8080
```

## Figure 16.14. Create host variable file for node2

```shell
# file: stg/host_vars/node2.yaml 
web_server_port: 8081 
default_web_page_content: "Welcome to node2"
```

## Figure 16.15. Project directory structure with group variable and host variables 

```shell
[ansible@ansible Chapter-16]$ tree inventories/stg/ 
inventories/stg/ 
├── group_vars 
│   ├── dbnodes.yaml 
│   └── web.yaml 
├── hosts 
└── host_vars 
    ├── node1.yaml 
    └── node2.yaml 
  
2 directories, 5 files 
```

## Figure 16.16. Verify inventory and variables using ansible-inventory command 

```shell
[ansible@ansible Chapter-16]$ ansible-inventory --list -i inventories/stg/ 
{ 
    "_meta": { 
        "hostvars": { 
            "node1": { 
                "ansible_host": "192.168.56.25", 
                "ansible_ssh_private_key_file": "/home/ansible/.ssh/id_rsa", 
                "web_server_port": 8080 
            }, 
            "node2": { 
                "ansible_host": "192.168.56.24", 
                "ansible_ssh_private_key_file": "/home/ansible/.ssh/id_rsa", 
                "default_web_page_content": "Welcome to node2", 
                "web_server_port": 8081 
            }, 
            "node3": { 
                "ansible_host": "192.168.56.60", 
                "ansible_ssh_private_key_file": "/home/ansible/.ssh/id_rsa", 
                "web_server_port": 80 
            } 
        } 
    }, 
    ...output omitted... 
} 
```

## Figure 16.17. Different use account for remote nodes. 

```shell
[ansible@ansible Chapter-06]$ ansible-inventory web --list 
{ 
    "_meta": { 
        "hostvars": { 
            "node1": { 
                "ansible_host": "192.168.56.25", 
                "ansible_ssh_private_key_file": "/home/ansible/.ssh/id_rsa", 
                "ansible_user": "ansibleadmin" 
            }, 
            "node2": { 
                "ansible_host": "192.168.56.24", 
                "ansible_user": "user1" 
            }, 
            "node3": { 
                "ansible_host": "192.168.56.60", 
                "ansible_user": "devops" 
            }, 
            "win2019": { 
...output omitted... 
                "ansible_user": "ansible", 
                "ansible_winrm_server_cert_validation": "ignore", 
                "ansible_winrm_transport": "basic" 
            } 
        } 
    }, 
...output omitted... 
```

## Figure 16.18. Encrypt sensitive files using Ansible vault

```shell
[ansible@ansible Chapter-03]$ ansible-vault create vars/secrets  
New Vault password: 
Confirm New Vault password: 
[ansible@ansible Chapter-03]$ cat vars/secrets  
$ANSIBLE_VAULT;1.1;AES256 
38393063373031356638353866353937306462663565366266323166363130356435326564343735 
3061663831326237356430353361646235396661663538310a373337376339383561353762356265 
39363830316465346166303666373064353061343563613734343336653630656533393739643238 
3136306130633761610a646138326130333435373836303832343335373737303535353665616430 
32323537303765356366383930623631666561393661626535663135316362326134623066623234 
31373138616137346132626230626464343034306637316636633539663530303338396163666131 
383237626162626334376133663039366331 
```

## Figure 16.19. Ansible vault password prompting

```shell
[ansible@ansible Chapter-06]$ ansible-playbook password-promt.yaml --ask-pass 
SSH password:  
```

```shell
# variable names with shortnames
myvar: something
webport: 8080
dbpath: /opt/mysql
fwpackage: firewalld
fg_api: 10.1.10.10

# variables with meaningful names
user_location: /home/devops/
httpd_web_port: 8080
mysql_database_home: /opt/mysql
firewall_package: firewalld
fortigate_api_ip: 10.1.10.10

```