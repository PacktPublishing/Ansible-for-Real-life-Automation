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

## Figure 15.20. Jinja2 template to prepare Akamai API call body 

```yaml

```
