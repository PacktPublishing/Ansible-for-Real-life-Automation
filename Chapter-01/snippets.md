## Figure 1.4 - Ansible ping module and yum module 

```
- name: Ping to managed node 
  ping: 
- name: Install httpd package 
  yum: 
    name: httpd 
    state: latest 
```

## Figure 1.7 - Checking installed Python packages and version 

```
[ansible@ansible ~]$ sudo dnf list installed python3* 
Updating Subscription Management repositories. 
Installed Packages 
python3-bind.noarch                          32:9.11.26-3.el8                         @rhel8-appstream-media 
python3-chardet.noarch                       3.0.4-7.el8                              @anaconda             
. 
. 
..<output omitted for brevity>..
python36.x86_64                              3.6.8-2.module+el8.1.0+3334+5cb623d7     @rhel8-appstream-media 

## Also verify the version of Python
[ansible@ansible ~]$ python3 -V 
Python 3.6.8 
```

## Figure 1.8 - Installing Ansible package 

```
## on RHEL/Fedora/CentOS systems
[ansible@ansible ~]$ sudo dnf install ansible  

## For an Ubuntu system, you can use the apt command as follows: 
$ sudo apt install ansible 
```

## Figure 1.9 - Verify Ansible installation 

```
[ansible@ansible ~]$ ansible --version  
ansible 2.9.27  
config file = /etc/ansible/ansible.cfg  
configured module search path = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']  
ansible python module location = /usr/lib/python3.6/site-packages/ansible  
executable location = /usr/bin/ansible  
python version = 3.6.8 (default, Mar 18 2021, 08:58:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] 
```

## Figure 1.10 - Installing Ansible using Python pip 

```
## download and install Python pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
$ python get-pip.py --user  

## If pip is already installed, then make sure it is upgraded to the latest supported version.  
$ python -m pip install --upgrade pip  

## Then, install Ansible using pip: 
$ python -m pip install --user ansible 
```

## Figure 1.11 - Installing specific version of Ansible using pip 

```
## Installing old ansible version (ansible + modules)  
$ python -m pip install ansible==2.9.25 --user  

## Installing Ansible package (ansible-core + Ansible collections)  
$ python -m pip install ansible==4 --user  

## Installing ansible-base (ansible-base only; you need to install required collections separately)  
$ python -m pip install ansible-base==2.10.13 --user  

## Installing ansible-core (ansible-core only; you need to install required collections separately)  
$ python -m pip install ansible-core==2.11.4 --user  
```

## Figure 1.12 - Check Ansible version 

```
[ansible@ansible ~]$ ansible --version  
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

## Figure 1.13 - Creating ansible.cfg file 

```
[ansible@ansible ~]$ mkdir ansible-demo  
[ansible@ansible ~]$ cd ansible-demo/  
[ansible@ansible ansible-demo]$ vim ansible.cfg  
```

## Figure 1.14 - Content of ansible.cfg 

```
[defaults]  
inventory = ./hosts  
remote_user = devops  
ask_pass = false
```

## Figure 1.15 - Checking which ansible.cfg is taken by Ansible 

```
ansible@ansible ansible-demo]$ ansible --version  
ansible [core 2.11.6]  
config file = /home/ansible/ansible-demo/ansible.cfg  
.  
..<output omitted for brevity>..
```


## Figure 1.16 -  Another ansible.cfg sample with privilege escalation parameters 

```
[ansible@ansible ansible-demo]$ cat ansible.cfg  
[defaults]  
inventory = ./hosts  
remote_user = devops  
ask_pass = false        
  
[privilege_escalation]  
become = true  
become_method = sudo  
become_user = root  
become_ask_pass = true 
```

## Figure 1.17 - Creating inventory file inside project directory 

```
## switch to project directory
[ansible@ansible ~]$ cd ansible-demo/  

## Open the file in text editor
[ansible@ansible ansible-demo]$ vim hosts  
```

## Figure 1.8 - Sample inventory file content

```
[local]  
localhost  
  
[dev]  
192.168.100.4  
```

## Figure 1.19 - Ansible inventory with human-readable names and ansible_host 
```
[ansible@ansible ansible-demo]$ cat hosts  
[local]  
localhost ansible_connection=local  

[dev]  
node01 ansible_host=192.168.100.4 
```

## Figure 1.20 - List inventory hosts 

```
[ansible@ansible ansible-demo]$ ansible all --list-hosts  
hosts (2):  
  localhost  
  node01  
```  

## Figure 1.21 - Another Ansible inventory with more hosts and groups 

```
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

## Figure 1.22 - Multiple inventory files in project directory 

```
[ansible@ansible ansible-demo]$ ls -l  
total 12  
-rw-rw-r--. 1 ansible ansible 181 Nov 19 15:40 ansible.cfg  
-rw-rw-r--. 1 ansible ansible  90 Nov 19 15:33 hosts  
-rw-rw-r--. 1 ansible ansible 162 Nov 19 15:44 myinventory  
```

## Figure 1.23 - List inventory hosts with different inventory file 

```
[ansible@ansible ansible-demo]$ ansible all --list-hosts -i myinventory  
hosts (4):  
  localhost  
  servera.techbeatly.com  
  serverb.techbeatly.com  
  db101.techbeatly.com 
```  

## Figure 1.24 - Checking Ansible help and arguments 

```
[ansible@ansible ansible-demo]$ ansible --help  
.  
.  
  
-h, --help            show this help message and exit  
-i INVENTORY, --inventory INVENTORY, --inventory-file INVENTORY  
                      speciy inventory host path or comma separated host  
                      list. --inventory-file is deprecated  
-l SUBSET, --limit SUBSET  
                      further imit selected hosts to an additional pattern  
-m MODULE_NAME, --module-name MODULE_NAME  
                      Name of the actionto execute (default=command)  
-o, --one-line        condense output  
-t TREE, --tree TREE  log output to this directory  
-v, --verbose         verbose mode (-vvv for more, -vvvv to enable  
                      connection debugging)  
.  
...<output omitted for brevity>...
```

## Figure 1.25 - Host selection using patterns 

```
[ansible@ansible ansible-demo]$ ansible --list-hosts -i myinventory *techbeatly.com  
hosts (3):  
  servera.techbeatly.com  
  serverb.techbeatly.com  
  db101.techbeatly.com  

## Print only db servers: 
[ansible@ansible ansible-demo]$ ansible --list-hosts -i myinventory db*  
hosts (1):  
  Db101.techbeatly.com  
```

## Figure 1.26 - Create new user and set password 

```
## create a new user - devops
[root@node01 ~]# useradd devops  

## set password for the new user
[root@node01 ~]# passwd devops  
Changing password for user devops.  
New password:  
Retype new password:  
passwd: all authentication tokens updated successfully.  
```

## Figure 1.27 - Enabled privileged access for the new user 

```
[root@node01 ~]# echo "devops ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/devops  
```

## Figure 1.28 - Generating SSH key pair on Ansible control node 

```
[ansible@ansible ansible-demo]$ ssh-keygen -t rsa -b 4096 -C "ansible@ansible.lab.local"  
Generating public/private rsa key pair.  
Enter file in which to save the key (/home/ansible/.ssh/id_rsa):  
Created directory '/home/ansible/.ssh'.  
Enter passphrase (empty for no passphrase):  
Enter same passphrase again:  
Your idetification has been saved in /home/ansible/.ssh/id_rsa.  
Your ublic key has been saved in /home/ansible/.ssh/id_rsa.pub.  
..<output omitted>.. 
+----[SHA256]-----+  
```

## Figure 1.30 - Verify SSH key permission

```
[ansible@ansible ansible-demo]$ ls -la ~/.ssh/  
total 8  
drwx------. 2 ansible ansible   38 Nov 19 16:14 .  
drwx------. 7 ansible ansible  175 Nov 19 16:14 ..  
-rw-------. 1 ansible ansible 3389 Nov 19 16:14 id_rsa  
-rw-r--r--. 1 ansible ansible  751 Nov 19 16:14 id_rsa.pub  
```

## Figure 1.31 - Copy SSH public key to managed node 

```
[ansible@ansible ansible-demo]$ ssh-copy-id -i ~/.ssh/id_rsa devops@node01  
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/ansible/.ssh/id_rsa.pub"  
The authenticity of host 'node01 (192.168.100.4)' can't be established.  
RSA key fingerprint is SHA256:UEQ72EtSvn+0/tuEDbeclQuhHNTtp/uPf+VVvKkuB6k.  
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes  
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed  
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys  
devops@node01's password:  
  
Number of key(s) added: 1  
  
Now try logging into the machine, with:   "ssh 'devops@node01'"  
and check to make sure that only the key(s) you wanted were added.  
```

## Figure 1.32 - Login to managed node without password 

```
[ansible@ansible ansible-demo]$ ssh devops@node01node-1  
Last login: Fri Nov 19 16:23:25 2021  
[devops@node01node-1 ~]$

## check sudo access
[devops@node01node-1 ~]$ sudo -i  
[root@node01node-1 ~]# hostname  
Node01Node-1.lab.local 
```

## Figure 1.33 - Configuring SSH key information for managed nodes 

```
[dev]  
node01 ansible_host=192.168.100.4 ansible_ssh_private_key_file=/home/ansible/.ssh/id_rsa ansible_user=devops  

## Or, you can configure the variable details
## separately in the inventory file: 
[dev]  
node01 ansible_host=192.168.100.4  
  
[dev:vars]  
ansible_ssh_private_key_file=/home/ansible/.ssh/id_rsa  
ansible_user=devops  
```

## Figure 1.34 - Ansible ad hoc command using ping module 

```
[ansible@ansible ansible-demo]$ ansible all -m ping  
localhost | SUCCESS => {  
  "ansible_facts": {  
      "discovered_interpreter_python": "/usr/libexec/platform-python"  
  },  
  "changed": false,  
  "ping": "pong"  
}  
node01 | SUCCESS => {  
  "ansible_facts": {  
      "discovered_interpreter_python": "/usr/libexec/platform-python"  
  },  
  "changed": false,  
  "ping": "pong"  
}  
```

## Figure 1.35 - Ansible ad hoc command using shell module

```
[ansible@ansible ansible-demo]$ ansible all -m shell -a "whoami"  
localhost | CHANGED | rc=0 >>  
ansible  
node01 | CHANGED | rc=0 >>  
devops 
```

## Figure 1.36 - Multiple commands in shell module

```
[ansible@ansible ansible-demo]$ ansible all -m shell -a "hostname;uptime;date;cat /etc/*release| grep ^NAME;uname -a"  
localhost | CHANGED | rc=0 >>  
ansible  
16:58:15 up  1:37,  1 user,  load average: 0.00, 0.00, 0.00  
Fri Nov 19 16:58:15 UTC 2021  
NAME="Red Hat Enterprise Linux"  
Linux ansible 4.18.0-305.el8.x86_64 #1 SMP Thu Apr 29 08:54:30 EDT 2021 x86_64 x86_64 x86_64 GNU/Linux  
node01 | CHANGED | rc=0 >>  
node01.lab.local  
16:58:15 up  1:43,  2 users,  load average: 0.24, 0.05, 0.02  
Fri Nov 19 16:58:15 UTC 2021  
NAME="Red Hat Enterprise Linux"  
Linux node01.lab.local 4.18.0-305.el8.x86_64 #1 SMP Thu Apr 29 08:54:30 EDT 2021 x86_64 x86_64 x86_64 GNU/Linux 
```

## Figure 1.37 - Ansible ad hoc command using setup module

```
[ansible@ansible ansible-demo]$ ansible all –m setup -a "filter=ansible_distribution*" 
```

## Figure 1.38 - Ansible ad hoc command using dnf module 

```
[ansible@ansible ansible-demo]$ ansible node01 -m dnf -a 'name=vim state=latest'  
node01 | FAILED! => {  
  "ansible_facts": {  
      "discovered_interpreter_python": "/usr/libexec/platform-python"  
  },  
  "changed": false,  
  "msg": "This command has to be run under the root user.",  
  "results": []  
}  
```

## Figure 1.39 - Installing package using dnf module and privileged mode 

```
[ansible@ansible ansible-demo]$ ansible node01 -m dnf -a 'name=vim state=latest' -b  
node01 | CHANGED => {  
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
```

## Figure 1.41 - Removing package using Ansible ad hoc command 

```
[ansible@ansible ansible-demo]$ ansible node01 -m dnf -a 'name=vim state=absent' -b  
node01 | CHANGED => {  
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
