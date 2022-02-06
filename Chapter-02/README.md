
Output of playbook execution

```shell
[ansible@ansible Chapter-02]$ ansible-playbook install-package.yaml 

PLAY [Install Chrony Package] ***************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [dev-rhel8-55]

TASK [Ensure chrony package is installed] ***************************************************************
ok: [dev-rhel8-55]

TASK [Copy chrony configuration to node] ****************************************************************
changed: [dev-rhel8-55]

TASK [Enable and start chrony Service] ******************************************************************
ok: [dev-rhel8-55]

PLAY RECAP **********************************************************************************************
dev-rhel8-55               : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Segregated Inventory

```shell
inventories/
   production/
      hosts               # production servers inventory file 
   staging/
      hosts               # staging environment inventory file 
   development/
      hosts               # development environment inventory file 
```         