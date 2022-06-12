# Code snippets and references
- [Code snippets and references](#code-snippets-and-references)
  - [15.2. Output of Python Installation playbook](#152-output-of-python-installation-playbook)
  - [Figure 15.4. Inventory variables for FortiOS connection.](#figure-154-inventory-variables-for-fortios-connection)
  - [Figure 15.5. FortiOS backup using fortios_monitor_fact module.](#figure-155-fortios-backup-using-fortios_monitor_fact-module)
  - [Figure 15.6.  FortiOS backup using raw commands](#figure-156--fortios-backup-using-raw-commands)
  - [Figure 15.7. Inventory variables for FortiOS for using raw commands.](#figure-157-inventory-variables-for-fortios-for-using-raw-commands)
  - [Figure 15.8. Running FortiOS software upgrade using raw module](#figure-158-running-fortios-software-upgrade-using-raw-module)
  - [Figure 15.9. Cisco ASA backup using raw commands](#figure-159-cisco-asa-backup-using-raw-commands)
  - [Figure 15.10. Gathering AWS EC2 information using module](#figure-1510-gathering-aws-ec2-information-using-module)
  - [Figure 15.11. Test ToDo API access](#figure-1511-test-todo-api-access)
  - [Figure 15.14. API healthcheck sample output](#figure-1514-api-healthcheck-sample-output)
  - [Figure 15.15. API call returned content](#figure-1515-api-call-returned-content)
  - [Figure 15.17. ToDo items fetched using API call](#figure-1517-todo-items-fetched-using-api-call)
  - [Figure 15.19. Output of new items add tasks](#figure-1519-output-of-new-items-add-tasks)
  - [Figure 15.23. Ansible module path](#figure-1523-ansible-module-path)
  - [Figure 15.24. Library path in ansible.cfg](#figure-1524-library-path-in-ansiblecfg)
  - [Figure 15.27. Ansible playbook output for custom module](#figure-1527-ansible-playbook-output-for-custom-module)
  - [Figure 15.32. Custom module details using ansible-doc command](#figure-1532-custom-module-details-using-ansible-doc-command)
  - [Figure 15.33. Ansible custom module documentation details using ansible-doc command.png](#figure-1533-ansible-custom-module-documentation-details-using-ansible-doc-commandpng)
  - [Figure 15.35. Verify playbook execution and hello_message module](#figure-1535-verify-playbook-execution-and-hello_message-module)
  - [Figure 15.37. Build Ansible collection archive](#figure-1537-build-ansible-collection-archive)
  - [Figure 15.38. Publish collection to Ansible Galaxy](#figure-1538-publish-collection-to-ansible-galaxy)

## 15.2. Output of Python Installation playbook

```shell
[ansible@ansible Chapter-15]$ ansible-playbook install-python.yaml -e "NODES=node1"

PLAY [Installing Python on target machine] **************************************************

TASK [Install Latest Python package] ********************************************************
changed: [node1]

TASK [Verify Python version] ****************************************************************
changed: [node1]

TASK [Display installed Python version.] ****************************************************
ok: [node1] => {
    "msg": "Installed Python version: ['Python 3.6.8']"
}

PLAY RECAP **********************************************************************************
node1                      : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Figure 15.4. Inventory variables for FortiOS connection.  

```ini
[fortios]
fg01 ansible_host=192.168.57.125

[fortios:vars]
ansible_user=admin
ansible_ssh_pass='Admin#123'
ansible_host_key_checking=false
ansible_network_os=fortinet.fortios.fortios
ansible_connection=ansible.netcommon.httpapi
ansible_httpapi_use_ssl=True
ansible_httpapi_validate_certs=False
```

## Figure 15.5. FortiOS backup using fortios_monitor_fact module.

```yaml
- name: Backup global settings on FortiOS device
  fortinet.fortios.fortios_monitor_fact:
     selector: 'system_config_backup'
     vdom: 'root'
     params:
         scope: 'global'
```


## Figure 15.6.  FortiOS backup using raw commands 

```yaml
- name: FortiGate Configuration Backup
  raw: |
        execute cfg save
        execute backup config tftp {{ backup_filename }} {{  tftp_server }}       
  register: tftp_copy_status
```

## Figure 15.7. Inventory variables for FortiOS for using raw commands.  

```ini
[fortios]
fg01 ansible_host=192.168.57.125

[fortios:vars]
ansible_user=admin
ansible_ssh_pass='Admin#123'
ansible_host_key_checking=false
#ansible_network_os=fortinet.fortios.fortios
#ansible_connection=ansible.netcommon.httpapi
#ansible_httpapi_use_ssl=True
#ansible_httpapi_validate_certs=False
```

## Figure 15.8. Running FortiOS software upgrade using raw module

```yaml
- name: FortiGate Update Software
  raw: |
        execute restore image tftp {{ fortios_image_filename }} {{ tftp_server }}  
        Y
  register: image_update_status
```

## Figure 15.9. Cisco ASA backup using raw commands 

```yaml
- name: Take Cisco ASA Backup
  cisco.asa.asa_command:
    commands:
    - write memory
    - copy /noconfirm running-config tftp://{{ tftp_server }}/{{ backup_filename }}
  register: tftp_copy_status
```

## Figure 15.10. Gathering AWS EC2 information using module 

```yaml
- name: Gather EC2 insance details
  amazon.aws.ec2_instance_info:

- name: Gather information about instances in Singapore
  amazon.aws.ec2_instance_info:
    filters:
      availability-zone: ap-southeast-1
```      

## Figure 15.11. Test ToDo API access 

```shell
$ curl http://todo-app.example.com:8081/api/todos
[{"id":1,"title":"Send weekly report to team","description":"Weekly health check report","completed":false},{"id":2,"title":"Arrange team dinner","description":"Check for places","completed":false},{"id":3,"title":"Schedule meeting with John for security audit","description":"Pending long time","completed":false}]
```

## Figure 15.14. API healthcheck sample output 


```shell
TASK [Display health check status] ************************************************************************************
ok: [localhost] => {
    "msg": {
        "changed": false,
        "connection": "close",
        "content": "{\"uptime\":2438.676111528,\"message\":\"OK\",\"timestamp\":1655004678873}",
        "content_length": "66",
        "cookies": {},
        "cookies_string": "",
        "date": "Sun, 12 Jun 2022 03:31:18 GMT",
        "elapsed": 0,
        "failed": false,
        "msg": "OK (66 bytes)",
        "redirected": false,
        "status": 200,
        "url": "http://todo-app.example.com:8081/health"
    }
}
```

## Figure 15.15. API call returned content 

```shell
TASK [Display health check status] ************************************************************************************
ok: [localhost] => {
    "msg": {
        "message": "OK",
        "timestamp": 1655004693105,
        "uptime": 2452.908586769
    }
}
```

## Figure 15.17. ToDo items fetched using API call

```bash
<omitted>...
TASK [Display items] ************************************************************************************************************************
ok: [localhost] => {
    "msg": [
        {
            "completed": false,
            "description": "Weekly health check report",
            "id": 1,
            "title": "Send weekly report to team"
        },
        {
            "completed": false,
            "description": "Check for places",
            "id": 2,
            "title": "Arrange team dinner"
        },
        {
            "completed": false,
            "description": "Pending long time",
            "id": 3,
            "title": "Schedule meeting with John for security audit"
        }
    ]
}
<omitted>...
```
## Figure 15.19. Output of new items add tasks 

```shell
<omitted>...
TASK [Add a new item in ToDo list] **********************************************************************************************************
ok: [localhost]

TASK [Display items] ************************************************************************************************************************
ok: [localhost] => {
    "msg": {
        "changed": false,
        "connection": "close",
        "content": "{\"id\":12,\"title\":\"Learn API call using Ansible\",\"description\":\"A new task added by Ansible\",\"completed\":false}",
        "content_type": "application/json",
        "cookies": {},
        "cookies_string": "",
        "date": "Sun, 12 Jun 2022 04:21:50 GMT",
        "elapsed": 0,
        "failed": false,
        "json": {
            "completed": false,
            "description": "A new task added by Ansible",
            "id": 12,
            "title": "Learn API call using Ansible"
        },
        "msg": "OK (unknown bytes)",
        "redirected": false,
        "status": 201,
        "transfer_encoding": "chunked",
        "url": "http://todo-app.example.com:8081/api/todos"
    }
}
<omitted>...
```

## Figure 15.23. Ansible module path

```yaml
[ansible@ansible Chapter-15]$ ansible-config dump |grep DEFAULT_MODULE_PATH
DEFAULT_MODULE_PATH(default) = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
```

## Figure 15.24. Library path in ansible.cfg

```ini
[defaults]

library = ./library
```

## Figure 15.27. Ansible playbook output for custom module

```bash
<omitted>...
TASK [debug] *************************************************************************************************************
ok: [node1] => {
    "msg": {
        "changed": true,
        "failed": false,
        "hostname": "node-1",
        "msg": "Application Name: bash (version: 1.0) - This is a bash App",
        "operating_system": "Linux"
    }
}
<omitted>...
```

## Figure 15.32. Custom module details using ansible-doc command

```shell
[ansible@ansible Chapter-15]$ ansible-doc hello_message
> HELLO_MESSAGE    (/home/ansible/ansible-book-packt/Chapter-15/library/hello_message.py)

        A Hello Message Module

OPTIONS (= is mandatory):

= message
        The message to be printed.

        type: string

- name
        The name of the person.
        [Default: (null)]
        type: string


AUTHOR: Gineesh Madapparambath (@ginigangadharan)

EXAMPLES:
```

## Figure 15.33. Ansible custom module documentation details using ansible-doc command.png

```shell
<omitted>...
EXAMPLES:

# Simple Custom Hello App
- name: Calling hello_message module
  hello_message:
    message: "Hello"
    name: "John"


RETURN VALUES:
- greeting
        Hello Response

        returned: success
        sample: Hello World
        type: str

- os_version
        Operating System Information
<omitted>...
```

## Figure 15.35. Verify playbook execution and hello_message module 

```shell
<omitted>...
TASK [debug] *************************************************************************************************************
ok: [localhost] => {
    "msg": {
        "changed": false,
        "failed": false,
        "greeting": "Hello John",
        "os_version": "Linux 4.18.0-305.el8.x86_64 #1 SMP Thu Apr 29 08:54:30 EDT 2021"
    }
}
<omitted>...
```

##


```shell
collection/
├── docs/
├── galaxy.yml
├── meta/
│   └── runtime.yml
├── plugins/
│   ├── modules/
│   │   └── module1.py
│   ├── inventory/
│   └── .../
├── README.md
├── roles/
│   ├── role1/
│   ├── role2/
│   └── .../
├── playbooks/
│   ├── files/
│   ├── vars/
│   ├── templates/
│   └── tasks/
└── tests/
...<omitted>...
```

## Figure 15.37. Build Ansible collection archive

```shell
[ansible@ansible Chapter-15]$ cd collection
[ansible@ansible collection]$ ansible-galaxy collection build
Created collection for ginigangadharan.custom_modules_demo at /home/ansible/ansible-book-packt/Chapter-15/collection/ginigangadharan-custom_modules_demo-1.0.0.tar.gz
[ansible@ansible Chapter-15]$
```

## Figure 15.38. Publish collection to Ansible Galaxy 

```shell
[ansible@ansible collection]$ ansible-galaxy collection publish \
> --token $ANSIBLE_GALAXY_TOKEN \
> ./ginigangadharan-custom_modules_demo-1.0.0.tar.gz 
Publishing collection artifact '/home/ansible/ansible-book-packt/Chapter-15/collection/ginigangadharan-custom_modules_demo-1.0.0.tar.gz' to default https://galaxy.ansible.com/api/
Collection has been published to the Galaxy server default https://galaxy.ansible.com/api/
Waiting until Galaxy import task https://galaxy.ansible.com/api/v2/collection-imports/20104/ has completed
Collection has been successfully published and imported to the Galaxy server default https://galaxy.ansible.com/api/
```