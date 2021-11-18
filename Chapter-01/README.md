# Intalling Ansible on RHEL OS

Check if Python installed

```shell
[root@ansible ~]# dnf list installed python3*
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
[root@ansible ~]# python3 -V
Python 3.6.8
```

Install Ansible

```shell
[root@ansible ~]# dnf install ansible
```

Check Ansible version

```shell
[root@ansible ~]# ansible --version
ansible 2.9.27
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.6/site-packages/ansible
  executable location = /bin/ansible
  python version = 3.6.8 (default, Mar 18 2021, 08:58:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)]
```
