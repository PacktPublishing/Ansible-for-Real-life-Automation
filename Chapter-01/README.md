# Ansible Installation

## Installing Ansible on RHEL OS

Read official documentation [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) for other platforms.

Create a user for Ansible (Optional) with sudo acccess

```shell
[root@ansible ~]# useradd ansible
[root@ansible ~]# passwd ansible
[root@ansible ~]# echo "ansible ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/ansible
[root@ansible ~]# su - ansible
[ansible@ansible ~]$ 
```

Check if Python installed

```shell
[ansible@ansible ~]$ sudo dnf list installed python3*
Updating Subscription Management repositories.
Installed Packages
python3-bind.noarch                          32:9.11.26-3.el8                         @rhel8-appstream-media
python3-chardet.noarch                       3.0.4-7.el8                              @anaconda             
.
.
.   
python36.x86_64                              3.6.8-2.module+el8.1.0+3334+5cb623d7     @rhel8-appstream-media
```

Check Python version

```shell
[ansible@ansible ~]$ python3 -V
Python 3.6.8
```

Install Ansible

```shell
[ansible@ansible ~]$ sudo  dnf install ansible
```

Check Ansible version

```shell
[ansible@ansible ~]$ ansible --version
ansible 2.9.27
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.6/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.6.8 (default, Mar 18 2021, 08:58:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)]
```

Remove old Ansibe

```shell
[ansible@ansible ~]$ sudo dnf remove ansible
```

Install Ansible using Python pip

```shell
[ansible@ansible ~]$ python3 -m pip install ansible --user
```

Check Ansible version again

```shell
ansible@ansible ~]$ ansible --version
[DEPRECATION WARNING]: Ansible will require Python 3.8 or newer on the controller starting with Ansible 
2.12. Current version: 3.6.8 (default, Mar 18 2021, 08:58:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)]. This 
feature will be removed from ansible-core in version 2.12. Deprecation warnings can be disabled by setting 
deprecation_warnings=False in ansible.cfg.
ansible [core 2.11.6] 
  config file = None
  configured module search path = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/ansible/.local/lib/python3.6/site-packages/ansible
  ansible collection location = /home/ansible/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/ansible/.local/bin/ansible
  python version = 3.6.8 (default, Mar 18 2021, 08:58:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)]
  jinja version = 3.0.3
  libyaml = True
```

## Deploying Ansible

Create a project directory and `ansible.cfg`

```shell
[ansible@ansible ~]$ mkdir ansible-demo
[ansible@ansible ~]$ cd ansible-demo/
[ansible@ansible ansible-demo]$ vim ansible.cfg

[ansible@ansible ansible-demo]$ cat ansible.cfg 
  [defaults]
  inventory = ./hosts 
  remote_user = devops
  ask_pass = false       
```

Check version and ansible.cfg

```shell
  ansible@ansible ansible-demo]$ ansible --version
  ansible [core 2.11.6] 
    config file = /home/ansible/ansible-demo/ansible.cfg
    .
    .
```

Sample `ansible.cfg` with privilege escaltion details.

```shell
[ansible@ansible ansible-demo]$ cat ansible.cfg 
[defaults]
inventory = ./hosts 
remote_user = devops
ask_pass = false       

[privilege_escalation]
become = false 
become_method = sudo
become_user = root 
become_ask_pass = true
```

## Creating Ansible Inventory

```shell
[ansible@ansible ansible-demo]$ cat hosts 
[local]
localhost ansible_connection=local

[dev]
dev-rhel8-55 ansible_host=192.168.100.4
```

Check hosts

```shell
[ansible@ansible ansible-demo]$ ansible all --list-hosts
  hosts (2):
    localhost
    dev-rhel8-55
```

Another inventory

```shell
[ansible@ansible ansible-demo]$ cat myinventory 
[myself]
localhost

[intranetweb]
servera.techbeatly.com
serverb.techbeatly.com

[database]
db101.techbeatly.com

[everyone:children]
myself
intranetweb
database
```

```shell
[ansible@ansible ansible-demo]$ ls -l
total 12
-rw-rw-r--. 1 ansible ansible 181 Nov 19 15:40 ansible.cfg
-rw-rw-r--. 1 ansible ansible  90 Nov 19 15:33 hosts
-rw-rw-r--. 1 ansible ansible 162 Nov 19 15:44 myinventory
```

List new inventory

```shell
[ansible@ansible ansible-demo]$ ansible all --list-hosts -i myinventory 
  hosts (4):
    localhost
    servera.techbeatly.com
    serverb.techbeatly.com
    db101.techbeatly.com
```

Ansible help

```shell
[ansible@ansible ansible-demo]$ ansible --help
.
.

  -h, --help            show this help message and exit
  -i INVENTORY, --inventory INVENTORY, --inventory-file INVENTORY
                        specify inventory host path or comma separated host
                        list. --inventory-file is deprecated
  -l SUBSET, --limit SUBSET
                        further limit selected hosts to an additional pattern
  -m MODULE_NAME, --module-name MODULE_NAME
                        Name of the action to execute (default=command)
  -o, --one-line        condense output
  -t TREE, --tree TREE  log output to this directory
  -v, --verbose         verbose mode (-vvv for more, -vvvv to enable
                        connection debugging)
.
.
.
```

Filtering nodes

```shell
[ansible@ansible ansible-demo]$ ansible --list-hosts -i myinventory *techbeatly.com
  hosts (3):
    servera.techbeatly.com
    serverb.techbeatly.com
    db101.techbeatly.com

[ansible@ansible ansible-demo]$ ansible --list-hosts -i myinventory db*
  hosts (1):
    db101.techbeatly.com
```

## Configuring your Managed nodes

```shell
[root@dev-rhel8-55 ~]# useradd devops
[root@dev-rhel8-55 ~]# passwd devops
Changing password for user devops.
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: all authentication tokens updated successfully.

[root@dev-rhel8-55 ~]# echo "devops ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/devops

```

Create ssh key

```shell
[ansible@ansible ansible-demo]$ ssh-keygen -t rsa -b 4096 -C "ansible@ansible.lab.local"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ansible/.ssh/id_rsa): 
Created directory '/home/ansible/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ansible/.ssh/id_rsa.
Your public key has been saved in /home/ansible/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:nhkOzshIv27mrEpRTi+kHllitufdoyYJ96huGGpQqrE ansible@ansible.lab.local
The key's randomart image is:
+---[RSA 4096]----+
|                 |
|                 |
| + =             |
|o % .            |
| O.+ .. S        |
|*o==o+.+ +       |
|=*+.B.oo=        |
|Eo =o+. .        |
|=+o*B.           |
+----[SHA256]-----+

[ansible@ansible ansible-demo]$ ls -la ~/.ssh/
total 8
drwx------. 2 ansible ansible   38 Nov 19 16:14 .
drwx------. 7 ansible ansible  175 Nov 19 16:14 ..
-rw-------. 1 ansible ansible 3389 Nov 19 16:14 id_rsa
-rw-r--r--. 1 ansible ansible  751 Nov 19 16:14 id_rsa.pub
```

Copy public key to managed node

```shell
[ansible@ansible ansible-demo]$ ssh-copy-id -i ~/.ssh/id_rsa devops@dev-rhel8-55
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/ansible/.ssh/id_rsa.pub"
The authenticity of host 'dev-rhel8-55 (192.168.100.4)' can't be established.
RSA key fingerprint is SHA256:UEQ72EtSvn+0/tuEDbeclQuhHNTtp/uPf+VVvKkuB6k.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
devops@dev-rhel8-55's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'devops@dev-rhel8-55'"
and check to make sure that only the key(s) you wanted were added.
```

Test ssh access

```shell
[ansible@ansible ansible-demo]$ ssh devops@dev-rhel8-55
Last login: Fri Nov 19 16:23:25 2021
[devops@dev-rhel8-55 ~]$ 
[devops@dev-rhel8-55 ~]$ sudo -i
[root@dev-rhel8-55 ~]# hostname
dev-rhel8-55.lab.local
```

Configure ssh details in inventory

```shell
[dev]
dev-rhel8-55 ansible_host=192.168.100.4 ansible_ssh_private_key_file=/home/ansible/.ssh/id_rsa ansible_user=
devops

## or

[dev]
dev-rhel8-55 ansible_host=192.168.100.4 

[dev:vars]
ansible_ssh_private_key_file=/home/ansible/.ssh/id_rsa 
ansible_user=devops
```

Check connection

```shell
[ansible@ansible ansible-demo]$ ansible all -m ping
localhost | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "ping": "pong"
}
dev-rhel8-55 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "ping": "pong"
}
```

Ad hoc commands

```shell
[ansible@ansible ansible-demo]$ ansible all -m shell -a "whoami"
localhost | CHANGED | rc=0 >>
ansible
dev-rhel8-55 | CHANGED | rc=0 >>
devops

[ansible@ansible ansible-demo]$ ansible all -m shell -a "hostname;uptime;date;cat /etc/*release| grep ^NAME;uname -a"
localhost | CHANGED | rc=0 >>
ansible
 16:58:15 up  1:37,  1 user,  load average: 0.00, 0.00, 0.00
Fri Nov 19 16:58:15 UTC 2021
NAME="Red Hat Enterprise Linux"
Linux ansible 4.18.0-305.el8.x86_64 #1 SMP Thu Apr 29 08:54:30 EDT 2021 x86_64 x86_64 x86_64 GNU/Linux
dev-rhel8-55 | CHANGED | rc=0 >>
dev-rhel8-55.lab.local
 16:58:15 up  1:43,  2 users,  load average: 0.24, 0.05, 0.02
Fri Nov 19 16:58:15 UTC 2021
NAME="Red Hat Enterprise Linux"
Linux dev-rhel8-55.lab.local 4.18.0-305.el8.x86_64 #1 SMP Thu Apr 29 08:54:30 EDT 2021 x86_64 x86_64 x86_64 GNU/Linux
```

Install package using Ansible

```shell
[ansible@ansible ansible-demo]$ ansible dev-rhel8-55 -m dnf -a 'name=vim state=latest'
dev-rhel8-55 | FAILED! => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "msg": "This command has to be run under the root user.",
    "results": []
}

## install with become
[ansible@ansible ansible-demo]$ ansible dev-rhel8-55 -m dnf -a 'name=vim state=latest' -b
dev-rhel8-55 | CHANGED => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": true,
    "msg": "",
    "rc": 0,
    "results": [
        "Installed: vim-common-2:8.0.1763-16.el8.x86_64",
        "Installed: vim-enhanced-2:8.0.1763-16.el8.x86_64",
        "Installed: gpm-libs-1.20.7-17.el8.x86_64"
    ]
}

## remove a package

[ansible@ansible ansible-demo]$ ansible dev-rhel8-55 -m dnf -a 'name=vim state=absent' -b
dev-rhel8-55 | CHANGED => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": true,
    "msg": "",
    "rc": 0,
    "results": [
        "Removed: vim-enhanced-2:8.0.1763-16.el8.x86_64"
    ]
}
```
