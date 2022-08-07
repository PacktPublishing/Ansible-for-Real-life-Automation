## playbook to install chrony

```shell
[ansible@ansible Chapter-02]$ ansible-playbook install-package.yaml  
  
PLAY [Install Chrony Package] ******************************************************************************* 

TASK [Gathering Facts] ************************************************************************************** 
ok: [node1] 

TASK [Ensure Chronry package is installed] ****************************************************************** 
changed: [node1] 

PLAY RECAP ************************************************************************************************** 
dev-rhel8-55node1               : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
```

## check on node1

```shell
[devops@node1 ~]$ sudo yum list installed chrony 
Updating Subscription Management repositories. 
Installed Packages 
chrony.x86_64                          4.1-1.el8                           @rhel-8-for-x86_64-baseos-rpms 
```

## chrony full play

```shell
[ansible@ansible Chapter-02]$ ansible-playbook install-package.yaml  

PLAY [Install Chrony Package] *************************************************************************** 

TASK [Gathering Facts] ********************************************************************************** 
ok: [dev-rhel8-55] 

TASK [Ensure chrony package is installed] *************************************************************** 
ok: [dev-rhel8-55] 

TASK [Copy chrony configuration to node] **************************************************************** 
changed: [node1] 

TASK [Enable and start chrony Service] ****************************************************************** 
ok: [node1] 

PLAY RECAP ********************************************************************************************** 
node1               : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## chrony status

```shell
[devops@node-1 ~]$ cat /etc/chrony.conf
server 0.sg.pool.ntp.org
server 1.sg.pool.ntp.org
server 2.sg.pool.ntp.org
server 3.sg.pool.ntp.org
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
keyfile /etc/chrony.keys
leapsectz right/UTC
logdir /var/log/chrony[devops@node-1 ~]$ 
[devops@node-1 ~]$ 
[devops@node-1 ~]$ sudo systemctl status chronyd
● chronyd.service - NTP client/server
   Loaded: loaded (/usr/lib/systemd/system/chronyd.service; enabled; vendor preset: enabl>
   Active: active (running) since Sun 2022-07-24 07:58:06 UTC; 1h 8min ago
     Docs: man:chronyd(8)
           man:chrony.conf(5)
  Process: 834 ExecStartPost=/usr/libexec/chrony-helper update-daemon (code=exited, statu>
  Process: 816 ExecStart=/usr/sbin/chronyd $OPTIONS (code=exited, status=0/SUCCESS)
 Main PID: 828 (chronyd)
    Tasks: 1 (limit: 2741)
   Memory: 1.1M
   CGroup: /system.slice/chronyd.service
           └─828 /usr/sbin/chronyd

Jul 24 07:58:06 node-1 chronyd[828]: Frequency -8.096 +/- 0.195 ppm read from /var/lib/ch>
Jul 24 07:58:06 node-1 chronyd[828]: Using right/UTC timezone to obtain leap second data
Jul 24 07:58:06 node-1 systemd[1]: Started NTP client/server.
Jul 24 08:00:40 node-1 chronyd[828]: Selected source 218.186.3.36 (1.sg.pool.ntp.org)
Jul 24 08:00:40 node-1 chronyd[828]: System clock wrong by 1.641355 seconds
lines 1-18
```

## ansible module list

```shell
[ansible@ansible Chapter-02]$ ansible-doc -l 
add_host                                                                                 Add a host ... 
amazon.aws.aws_az_facts                                                                  Gather info... 
amazon.aws.aws_az_info                                                                   Gather info... 
amazon.aws.aws_caller_facts                                                              Get informa... 
amazon.aws.aws_caller_info                                                               Get informa... 
amazon.aws.aws_s3                                                                        manage obje... 
amazon.aws.cloudformation                                                                Create or d... 
amazon.aws.cloudformation_facts                                                          Obtain info... 
amazon.aws.cloudformation_info                                                           Obtain info... 
...output omitted...
```

## dnf snippet

```
[ansible@ansible Chapter-02]$ ansible-doc -s dnf  
- name: Manages packages with the `dnf' package manager 
  dnf: 
      allow_downgrade:       # Specify if the named package and version is allowed to downgrade 
                               a maybe already installed higher 
                               version of that package. Note 
                               that setting allow_downgrade=True 
                               can make this module behave in a 
                               non-idempotent way. The task 
                               could end up with a set of 
                               packages that does not match the 
...output omitted... 
```

## dnf module

```
[ansible@ansible Chapter-02]$ ansible-doc dnf  
> ANSIBLE.BUILTIN.DNF    (/home/ansible/.local/lib/python3.6/site-packages/ansible/modules/dnf.> 
  
        Installs, upgrade, removes, and lists packages and groups with the 
        `dnf' package manager. 
  
OPTIONS (= is mandatory): 
  
- allow_downgrade 
        Specify if the named package and version is allowed to downgrade a 
        maybe already installed higher version of that package. Note that 
        setting allow_downgrade=True can make this module behave in a non- 
        idempotent way. The task could end up with a set of packages that 
...output omitted... 
VERSION_ADDED_COLLECTION: ansible.builtin 
  
EXAMPLES: 
  
- name: Install the latest version of Apache 
  dnf: 
    name: httpd 
    state: latest 
  
- name: Install Apache >= 2.4 
  dnf: 
    name: httpd>=2.4 
    state: present 
...output omitted... 
```

## search module

```shell
dnf                                                                                      Manages packa...
dpkg_selections                                                                          Dpkg package ...
expect                                                                                   Executes a co...
f5networks.f5_modules.bigip_apm_acl                                                      Manage user-d...
f5networks.f5_modules.bigip_apm_network_access                                           Manage APM Ne...
f5networks.f5_modules.bigip_apm_policy_fetch                                             Exports the A...
f5networks.f5_modules.bigip_apm_policy_import                                            Manage BIG-IP...
f5networks.f5_modules.bigip_asm_advanced_settings                                        Manage BIG-IP...
f5networks.f5_modules.bigip_asm_dos_application                                          Manage applic...
f5networks.f5_modules.bigip_asm_policy_fetch                                             Exports the A...
f5networks.f5_modules.bigip_asm_policy_import                                            Manage BIG-IP...
f5networks.f5_modules.bigip_asm_policy_manage                                            Manage BIG-IP...
f5networks.f5_modules.bigip_asm_policy_server_technology                                 Manages Serve...
f5networks.f5_modules.bigip_asm_policy_signature_set                                     Manages Signa...
f5networks.f5_modules.bigip_cgnat_lsn_pool                                               Manage CGNAT ...
f5networks.f5_modules.bigip_cli_alias                                                    Manage CLI al...
f5networks.f5_modules.bigip_cli_script                                                   Manage CLI sc...
f5networks.f5_modules.bigip_command                                                      Run TMSH and ...
/dnf
```

## become plugins

```
[ansible@ansible Chapter-02]$ ansible-doc -t become -l 
ansible.netcommon.enable     Switch to elevated permissions on a network device             
community.general.doas       Do As user                                                     
...output omitted...                    
runas                        Run As user                                                    
su                           Substitute User                                                
sudo                         Substitute User DO    
```

## vim editor

```
  1 ---
  2 - name: Install Chrony Package
  3   hosts: node1
  4   become: true
  5   tasks:
  6     - name: Ensure chrony package is installed
  7       ansible.builtin.dnf:
  8         name: chrony
  9         state: latest
 10 
 11     - name: Copy chrony configuration to node
 12       ansible.builtin.copy:
 13         src: chrony.conf.sample
 14         dest: /etc/chrony.conf
 15         mode: 644
 16         owner: root
 17         group: root
 18 
 19     - name: Enable and start chrony Service
 20       ansible.builtin.systemd:
 21         name: chronyd
 22         state: started
 23         enabled: yes
:set nu
```

## vimrc

```
[ansible@ansible Chapter-02]$ cat ~/.vimrc  
autocmd FileType yaml setlocal et ts=2 ai sw=2 nu sts=0 
colorscheme desert 
```

## inventory

```
[ansible@ansible Chapter-02]$ tree inventories/
inventories/
├── development
│   └── hosts
├── production
│   └── hosts
└── staging
    └── hosts

3 directories, 3 files
```

## winrm plugin

```
[ansible@ansible Chapter-02]$ ansible-doc -t connection -l |grep winrm 
winrm                          Run tasks over Microsoft's WinRM 
```

## winrm in inventory

```
[ansible@ansible Chapter-02]$ cat inventories/production/hosts 
[win2019] 
prod-db-101 ansible_host=192.168.110.10 

[win2019:vars] 
ansible_connection=winrm 
```

## winrm in playbook

```
--- 
- name: Install Package 
  hosts: win2019 
  become: true 
  connection: local 
```

## winrm in playbook execution

```
[ansible@ansible Chapter-02]$ ansible-playbook playbook.yml --connection=local
```

