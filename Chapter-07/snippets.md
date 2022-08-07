
## install vmware collection

```
[ansible@ansible Chapter-07]$ ansible-galaxy collection install community.vmware 
Starting galaxy collection install process 
Process install dependency map 
Starting collection install process 
Downloading https://galaxy.ansible.com/download/community-vmware-2.1.0.tar.gz to /home/ansible/.ansible/tmp/ansible-local-2922ya8yiroz/tmpgwmpkp4a/community-vmware-2.1.0-hk7iqmqh 
Installing 'community.vmware:2.1.0' to '/home/ansible/ansible-book-packt/Chapter-07/collections/ansible_collections/community/vmware' 
community.vmware:2.1.0 was installed successfully 
```

## verify collections

```
[ansible@ansible Chapter-07]$ ansible-galaxy collection list community.vmware 
  
# /home/ansible/ansible-book-packt/Chapter-07/collections/ansible_collections 
Collection       Version 
---------------- ------- 
community.vmware 2.1.0   
  
# /usr/local/lib/python3.6/site-packages/ansible_collections 
Collection       Version 
---------------- ------- 
community.vmware 1.17.0 
```

## python requirements

```
[ansible@ansible Chapter-07]$ cat collections/ansible_collections/community/vmware/requirements.txt  
pyVmomi>=6.7 
git+https://github.com/vmware/vsphere-automation-sdk-python.git ; python_version >= '2.7'  # Python 2.6 is not supported
```

## create vault

```
[ansible@ansible Chapter-07]$ mkdir vars 
[ansible@ansible Chapter-07]$ cd vars/ 
[ansible@ansible vars]$ ansible-vault create vmware-credential.yaml 
New Vault password:  
Confirm New Vault password: 
```

## create role vmware-provision-vm-from-template

```
[ansible@ansible Chapter-07]$ mkdir roles 

[ansible@ansible Chapter-07]$ cd roles 
[ansible@ansible roles]$ ansible-galaxy role init vmware-provision-vm-from-template 
- Role vmware-provision-vm-from-template was created successfully 
```

## Figure 7.24. Execute the playbook to create VMWare VM 

```
[ansible@ansible Chapter-07]$ ansible-playbook vmware-provision-vm-from-template.yml  --ask-vault-password 
Vault password:
```

## Figure 7.27 - Install collections using requirements.yaml

```
[ansible@ansible Chapter-07]$ [ansible@ansible Chapter-07]$ ansible-galaxy install -r requirements.yaml 
```

## Figure 7.28. Ansible collection list 

```
[ansible@ansible Chapter-07]$ ansible-galaxy collection list
.
.
# /home/ansible/ansible-book-packt/Chapter-07/collections/ansible_collections
Collection        Version
----------------- -------
amazon.aws        3.0.0  
ansible.posix     1.3.0  
community.aws     3.1.0  
community.general 4.0.1  
community.vmware  2.1.0  
google.cloud      1.0.2  
```

## AWS infra ELB details

```
[ansible@ansible Chapter-07]$ ansible-playbook aws-infra-provisioning.yaml 
...<output omitted>...TASK [debug] ****************************************************************************** 
ok: [localhost] => { 
    "msg": "Website is accessible on Appication ELB: ansible-iac-demo-elb-app-lb-893112002.ap-southeast-1.elb.amazonaws.com (It may take some time to get the backend instance to come InService)" 
} 
```