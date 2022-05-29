# Code snippet

- [Code snippet](#code-snippet)
  - [6.1](#61)
  - [6.2](#62)
  - [6.3](#63)
  - [6.4](#64)
  - [6.8](#68)
  - [6.9](#69)
  - [6.10](#610)
  - [6.11](#611)
  - [6.12](#612)
  - [6.15 - ansible network inventory](#615---ansible-network-inventory)
  - [6.16 - vyos playbook output](#616---vyos-playbook-output)
  - [6.17. Cisco ASA inventory variables](#617-cisco-asa-inventory-variables)
  - [6.19 Cisco ASA Playbok 01](#619-cisco-asa-playbok-01)
  - [6.20  cisco asa Playbok 02](#620--cisco-asa-playbok-02)
  - [6.24 - Cisco ASA device verification](#624---cisco-asa-device-verification)
  - [6.25 - tftp backup](#625---tftp-backup)


## 6.1

```shell
$ ansible-doc -l -t connection 
ansible.netcommon.httpapi      Use httpapi to run command on network applia... 
ansible.netcommon.libssh       (Tech preview) Run tasks using libssh for ss... 
ansible.netcommon.napalm       Provides persistent connection using NAPALM  
ansible.netcommon.netconf      Provides a persistent connection using the n... 
ansible.netcommon.network_cli  Use network_cli to run command on network ap... 
ansible.netcommon.persistent   Use a persistent unix socket for connection  
community.aws.aws_ssm          execute via AWS Systems Manager              
community.docker.docker        Run tasks in docker containers               
...
<output omitted>
... 
containers.podman.podman       Interact with an existing podman container   
kubernetes.core.kubectl        Execute tasks in pods running on Kubernetes  
local                          execute on controller                        
paramiko_ssh                   Run tasks via python ssh (paramiko)          
psrp                           Run tasks over Microsoft PowerShell Remoting... 
ssh                            connect via ssh client binary                
winrm                          Run tasks over Microsoft's WinRM          
```


## 6.2

```shell
$ ansible-doc -t connection community.docker.docker 
> COMMUNITY.DOCKER.DOCKER    (/usr/local/lib/python3.6/site-packages/ansible_col> 

        Run commands or put/fetch files to an existing docker 
        container. Uses the Docker CLI to execute commands in the 
        container. If you prefer to directly connect to the Docker 
        daemon, use the community.docker.docker_api connection plugin. 

OPTIONS (= is mandatory): 
  
- docker_extra_args 
        Extra arguments to pass to the docker command line 
        [Default: ] 
...output omitted... 
```

## 6.3

```yaml
--- 
# inventory variables 
ansible_connection: "winrm"  
ansible_user: "ansible" 
ansible_password: "MySecretWindowsPassword" 
ansible_port: "5985" 
ansible_winrm_transport: "basic" 
ansible_winrm_server_cert_validation: ignore 
```

## 6.4

```shell
ansible_ssh_private_key_file=/home/ansible/.ssh/id_rsa 
ansible_ssh_common_args='-o StrictHostKeyChecking=no"' 
```


## 6.8

```powershell
PS C:\Users\Administrator> (Get-Host).Version 
  
Major  Minor  Build  Revision 
-----  -----  -----  -------- 
5      1      14393  693 
```

## 6.9

```powershell
PS C:\Users\Administrator> $url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1" 
PS C:\Users\Administrator> $file = "$env:temp\ConfigureRemotingForAnsible.ps1" 
PS C:\Users\Administrator> (New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file) 
PS C:\Users\Administrator> powershell.exe -ExecutionPolicy ByPass -File $file 
Self-signed SSL certificate generated; thumbprint: DD2BFCC45E7503BC9C05BA9174326B593614C733 
  
wxf                 : http://schemas.xmlsoap.org/ws/2004/09/transfer 
a                   : http://schemas.xmlsoap.org/ws/2004/08/addressing 
w                   : http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd 
lang                : en-US 
Address             : http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous 
ReferenceParameters : ReferenceParameters 
  
Ok. 
```

## 6.10

```powershell
C:\Users\Administrator>winrm e winrm/config/listener 
Listener 
    Address = * 
    Transport = HTTP 
    Port = 5985 
    Hostname 
    Enabled = true 
    URLPrefix = wsman 
    CertificateThumbprint 
    ListeningOn = 10.0.2.15, 127.0.0.1, 192.168.99.103, ::1, fe80::5efe:10.0.2.15%3, fe80::5efe:192.168.99.103%13, fe80::785d:9659:c4d4:9b0f%16 
  
Listener 
    Address = * 
    Transport = HTTPS 
    Port = 5986 
    Hostname = WIN-CCUQI8Q4RMH 
    Enabled = true 
    URLPrefix = wsman 
    CertificateThumbprint = 64E69568BD75F3068BDCBF7ED819E4EA9ED1FDA3 
    ListeningOn = 10.0.2.15, 127.0.0.1, 192.168.99.103, ::1, fe80::5efe:10.0.2.15%3, fe80::5efe:192.168.99.103%13, fe80::785d:9659:c4d4:9b0f%16 
```    

## 6.11

```shell
[ansible@ansible Chapter-06]$ nc -vz 192.168.56.22 5985 
Connection to 192.168.56.22 5985 port [tcp/wsman] succeeded! 

[ansible@ansible Chapter-06]$ nc -vz 192.168.56.22 5986 
Connection to 192.168.56.22 5986 port [tcp/wsmans] succeeded!
```

## 6.12

```shell
[ansible@ansible Chapter-06]$ ansible windows -m win_ping 
win2019 | SUCCESS => { 
    "changed": false,
    "ping": "pong" 
} 
```

## 6.15 - ansible network inventory

```shell
[coreswtiches] 
c7000-sw01 ansible_host=192.168.0.242 
  
[coreswtiches:vars] 
ansible_connection=ansible.netcommon.network_clinetwork_cli 
ansible_network_os=cisco.ios.iosios 
ansible_password='Cisco@123' 
ansible_user=admin 
ansible_become_method=enable 
ansible_become_password='Cisco@123' 
  
[distributionswtiches] 
hp5130ds01 ansible_host=192.168.0.253 
  
[distributionswtiches:vars] 
ansible_password=hpadmin 
ansible_user=hppassword 
```

## 6.16 - vyos playbook output

```shell
[ansible@ansible Chapter-06]$ ansible-playbook -i inventories/ vyos-facts.yaml  
  
PLAY [Collecting VyOS facts] ************************************************************* 
  
TASK [Fetching VyOS details] ************************************************************* 
ok: [vyos-01] 
  
TASK [Display fact output] *************************************************************** 
ok: [vyos-01] => { 
    "msg": "VyOS version: VyOS 1.4-rolling-202202130317" 
} 
  
PLAY RECAP ******************************************************************************* 
vyos-01                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## 6.17. Cisco ASA inventory variables 

```shell
[asa] 
ciscoasa ansible_host=192.168.57.121 

[asa:vars] 
ansible_user=adminasa 
ansible_ssh_pass=password 
ansible_become=true 
ansible_become_method=ansible.netcommon.enable 
ansible_become_pass=password 
ansible_connection=ansible.netcommon.network_cli 
ansible_network_os=cisco.asa.asa
```

## 6.19 Cisco ASA Playbok 01

```yaml
---
- name: Cisco ASA Create ACL Entry
  hosts: "{{ nw_devices }}"
  gather_facts: no

  vars:
    take_backup: "Yes"
    tftp_server: 192.168.57.106
    tftp_server_port: 69
  
    acl_identifier: Demo-ACL
    acl_type: extended
    acl_action: permit #or deny
    acl_entry_source_ip: 10.1.20.11
    acl_entry_source_mask: 255.255.255.255

    asa_object_group_name: DEMO-NETWORK-TEAM-NEW
    asa_object_group_type: network # service, security etc.
    asa_object_group_host: 192.0.50.4
```    

## 6.20  cisco asa Playbok 02

```yaml
  tasks:
    - name: Set backup filename
      ansible.builtin.set_fact:
        backup_filename: "{{ inventory_hostname }}_{{ lookup('pipe', 'date +%Y%m%d-%H%M%S') }}_backup.cfg"
        
    - block:
      - name: Save configuration and take device Backup to tftp
        cisco.asa.asa_command:
          commands:
          - write memory
          - copy /noconfirm running-config tftp://{{ tftp_server }}/{{ backup_filename }}
        when: take_backup == "Yes"

      - name: Merge module attributes of given object-group
        cisco.asa.asa_ogs:
          config:
          - object_type: network
            object_groups:
              - name: "{{ asa_object_group_name }}"
                network_object:
                  host:
                    - "{{ asa_object_group_host }}"
          state: merged       

      - name: Add new ACL Entry and Merge configuration with device configuration
        cisco.asa.asa_acls:
          config:
            acls:
              - name: "{{ acl_identifier }}"
                acl_type: "{{ acl_type }}"
                aces:
                - grant: "{{ acl_action }}"
                  protocol_options:
                    tcp: true
                  source:
                    address: "{{ acl_entry_source_ip }}"
                    netmask: "{{ acl_entry_source_mask }}"
                  destination:
                    object_group: "{{ asa_object_group_name }}"
          state: merged
      when:
        - ansible_network_os == 'cisco.asa.asa'
```

## 6.24 - Cisco ASA device verification

```shell
$ ssh adminasa@192.168.57.121
adminasa@192.168.57.121's password: 
User adminasa logged in to ciscoasa
Logins over the last 1 days: 2.  Last login: 03:49:07 UTC May 29 2022 from 192.168.57.1
Failed logins since the last login: 0.  
Type help or '?' for a list of available commands.
ciscoasa> en
Password: ********
ciscoasa# 
ciscoasa#
ciscoasa# show running-config object-group | include DEMO-NETWORK-TEAM-NEW
object-group network DEMO-NETWORK-TEAM-NEW
ciscoasa#
ciscoasa# show running-config access-list | include Demo-ACL
access-list Demo-ACL extended permit tcp host 10.1.20.11 object-group DEMO-NETWORK-TEAM-NEW 
```

## 6.25 - tftp backup

```shell
[operator@tftp-prod tftpboot]$ ls -lrt
total 48
-rw-r--r--. 1 nobody nobody 8368 May 29 03:54 ciscoasa_20220529-115451_backup.cfg
-rw-r--r--. 1 nobody nobody 8368 May 29 03:55 ciscoasa_20220529-115531_backup.cfg
-rw-r--r--. 1 nobody nobody 8400 May 29 03:55 ciscoasa_20220529-115553_backup.cfg
-rw-r--r--. 1 nobody nobody 8432 May 29 03:56 ciscoasa_20220529-115610_backup.cfg
```