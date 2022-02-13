# Chapter-05 Content


Sample Ansible project directory structure

```shell
[ansible@ansible Chapter-05]$ tree ./
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
├── roles                       # roles directory
│   ├── deploy-web-server       # web deployment role and content
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── templates
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   ├── security-baseline-rhel8
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
│   │   │   ├── banner
│   │   │   └── issue
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   ├── main.yml
│   │   │   ├── part-01.yml
│   │   │   └── part-02.yml
│   │   ├── templates
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   ├── send-email
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   └── system-report
│       ├── defaults
│       │   └── main.yml
│       ├── files
│       ├── handlers
│       │   └── main.yml
│       ├── meta
│       │   └── main.yml
│       ├── README.md
│       ├── tasks
│       │   └── main.yml
│       ├── templates
│       │   └── system-information.html.j2
│       ├── tests
│       │   ├── inventory
│       │   └── test.yml
│       └── vars
│           └── main.yml
├── security-compliance-rhel8.yml
├── site.yml
├── system-info.yml
├── system-reboot.yml
└── vars                         # other common variables directory
    ├── baseline_exclusions.yml
    ├── common.yml
    ├── secrets
    └── smtp_secrets.yml

38 directories, 56 files
```

Ansible inventory with meaningful names

```ini
10.1.10.100
192.168.1.25
10.1.10.25
10.2.100.40

dbserver-101.example.com
prod-app-101.example.com
```

Ansible inventory with meaningful names

```ini
web01 ansible_host=10.1.10.100
app02 ansible_host=192.168.1.25
lb101 ansible_host=10.1.10.25
db201 ansible_host=10.2.100.40

web102 ansible_host=sglxwp-101.example.com
app301 ansible_host=slixmkp-app-101.example.com
```