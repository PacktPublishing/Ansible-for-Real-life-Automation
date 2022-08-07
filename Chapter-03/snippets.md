## setup output

```
[ansible@ansible Chapter-02]$ ansible-playbook install-package.yaml  
  
PLAY [Install Chrony Package] ******************************************************************************* 
  
TASK [Gathering Facts] ************************************************************************************** 
ok: [dev-rhel8-55] 
...output omitted... 
```

## Role structure

```
[ansible@ansible Chapter-03]$ tree ./
./
├── ansible.cfg
├── deploy-web.yml
├── hosts
├── node1-ansible-facts
├── README.md
├── roles
│   ├── deploy-web-server
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
...<output omitted>...
```

## Jinja2 template motd

```
Welcome to {{ ansible_facts.hostname }} 
(IP Address: {{ ansible_facts.default_ipv4.address }}) 

Access is restricted; if you are not authorized to use it  
please logout from this system 

If you have any issues, please contact {{ system_admin_email }}. 
Phone: {{ system_admin_phone | default('1800 1111 2222') }} 

------------------------------------- 
This message is configured by Ansible 
------------------------------------- 
```

## motd templated

```
Welcome to node1 
(IP Address: 10.1.10.25) 

Access is restricted; if you are not authorized to use it  
please logout from this system 
  
If you have any issues, please contact sysops@lab.local. 
Phone: 1800 1111 2222 
  
------------------------------------- 
This message is configured by Ansible 
------------------------------------- 
```

## role directory

```
[ansible@ansible roles]$ tree deploy-web-server/
deploy-web-server/
├── defaults
│   └── main.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

6 directories, 8 files
[ansible@ansible roles]$ 
```

## Directory content

```
[ansible@ansible Chapter-03]$ ls -l 
total 16 
-rw-rw-r--. 1 ansible ansible  209 Jan  8 14:16 ansible.cfg 
-rw-rw-r--. 1 ansible ansible  158 Jan  9 09:41 deploy-web.yml 
-rw-rw-r--. 1 ansible ansible  159 Jan  8 14:17 hosts 
-rw-rw-r--. 1 ansible ansible 1249 Jan  8 13:45 README.md 
drwxrwxr-x. 3 ansible ansible   31 Jan  9 09:24 roles 
```

## deploy webserver

```
[ansible@ansible Chapter-03]$ ansible-playbook deploy-web.yml 

PLAY [Deploy Webserver using apache] ******************************************************************

TASK [Gathering Facts] ********************************************************************************
ok: [webserver1]

TASK [Deploy Web service] *****************************************************************************

TASK [deploy-web-server : Create directory] ***********************************************************
changed: [webserver1]

TASK [deploy-web-server : Install httpd and firewalld] ************************************************
changed: [webserver1]

TASK [deploy-web-server : Enable and Run Firewalld] ***************************************************
changed: [webserver1]

TASK [deploy-web-server : Firewalld permit httpd service] *********************************************
ok: [webserver1]

TASK [deploy-web-server : httpd enabled and running] **************************************************
changed: [webserver1]

PLAY RECAP ********************************************************************************************
webserver1                 : ok=6    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## deploy web server again

```
[ansible@ansible Chapter-03]$ ansible-playbook deploy-web.yml  

PLAY [Deploy Webserver using apache] **************************************************************************** 

TASK [Gathering Facts] ******************************************************************************************* 
ok: [webserver1] 
  
...<output omitted>....

TASK [deploy-web-server : Firewalld permit httpd service] ******************************************************** 
ok: [webserver1] 

TASK [deploy-web-server : httpd enabled and running] ************************************************************* 
ok: [webserver1] 

PLAY RECAP ******************************************************************************************************* 
webserver1                 : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## ansible_facts

```
node1 | SUCCESS => { 
    "ansible_facts": { 
        "ansible_all_ipv4_addresses": [ 
            "192.168.100.101", 
            "192.168.56.25", 
            "10.0.2.15" 
        ], 
        ...output omitted...  

        "ansible_date_time": { 
            "date": "2022-01-10", 
            "day": "10", 
            ...output omitted... 
        }, 
        "module_setup": true 
    }, 
    "changed": false 
} 
```

## create role

```
[ansible@ansible Chapter-03]$ cd roles/ 
[ansible@ansible roles]$ ansible-galaxy role init system-report 
- Role system-report was created successfully 
```

## create security role

```
[ansible@ansible Chapter-03]$ cd roles/ 
[ansible@ansible roles]$ ansible-galaxy role init security-baseline-rhel8 
- Role security-baseline-rhel8 was created successfully 
```

## motd and issue files

```
[ansible@ansible Chapter-03]$ cat roles/security-baseline-rhel8/files/banner  
Authorized uses only. All activities will be monitored and reported. 

[ansible@ansible Chapter-03]$ cat roles/security-baseline-rhel8/files/issue  
Authorized uses only. All activities will be monitored and reported. 
```

## Role cntent

```
[ansible@ansible Chapter-03]$ tree roles/security-baseline-rhel8/
roles/security-baseline-rhel8/
├── defaults
│   └── main.yml
├── files
│   ├── banner
│   └── issue
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   ├── main.yml
│   ├── part-01.yml
│   └── part-02.yml
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

7 directories, 12 files
```

## execute secuity baseline playbook

```
[ansible@ansible Chapter-03]$ ansible-playbook security-compliance-rhel8.yml -e "NODES=nodes" 

PLAY [Performing Security Scanning and Configuration - RHEL8] ****************************** 
  
...<output omitted>... 
  
TASK [security-baseline-rhel8 : Running Part 01 checks] ************************************ 
included: /home/ansible/ansible-book-packt/Chapter-03/roles/security-baseline-rhel8/tasks/part-01.yml for node1 
  
TASK [security-baseline-rhel8 : Ensure sudo is installed] ********************************** 
ok: [node1] 
  
TASK [security-baseline-rhel8 : Ensure sudo log file exists] ******************************* 

...<output omitted>... 
  
PLAY RECAP ********************************************************************************* 
node1                      : ok=6    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```

## verify on node1

```
[ansible@ansible Chapter-03]$ ssh devops@node1 
Authorized uses only. All activities will be monitored and reported. 
Last login: Mon Jan 10 08:09:50 2022 from 192.168.56.23 
[devops@node-1 ~]$ 
```

## extra vars

```
$ ansible-playbook site.yml --extra-vars "version=1.23.45 other_variable=foo" 

$ ansible-playbook site.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}' 

$ ansible-playbook site.yml --extra-vars "@vars_file.json" 
```

## reboot status

```
[devops@node-1 ~]$ uptime 
 14:53:59 up 0 min,  1 user,  load average: 0.23, 0.08, 0.03 
```


## create vault file

```
[ansible@ansible Chapter-03]$ ansible-vault create vars/secrets 
New Vault password:  
Confirm New Vault password:  
```

## variable file after encryption

```
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

## Vault file for email secret


```
[ansible@ansible Chapter-03]$ ansible-vault create vars/smtp_secrets.yml  
New Vault password:  
Confirm New Vault password: 
```

## add content to vault file

```
email_smtp_username: 'ansible-automation@lab.local' 
email_smtp_password: 'secretpassword' 
~        
~        
~            
~                  
~                         
~
~           
:wq
```

## playbook without vault password

```
[ansible@ansible Chapter-03]$ ansible-playbook system-reboot-with-email.yml -e "NODES=nodes" 
ERROR! Attempting to decrypt but no vault secrets found 
```

## playbook with vault password

```
[ansible@ansible Chapter-03]$ ansible-playbook system-reboot-with-email.yml -e "NODES=nodes" --ask-vault-password 
Vault password:  
  
PLAY [System Reboot - Linux with email notification] ************************************************************************************************************* 
  
TASK [Email notification before reboot] ************************************************************************************************************************** 
  
TASK [send-email : Sending notification email] ******************************************************************************************************************* 
...<output omitted>... 
```