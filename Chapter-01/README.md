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
  [Defaults]
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
[Defaults]
inventory = ./hosts 
remote_user = devops
ask_pass = false       

[privilege_escalation]
become = true 
become_method = sudo
become_user = root 
become_ask_pass = true
```