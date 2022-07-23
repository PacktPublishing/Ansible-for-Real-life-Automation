

## Figure 5.19 AWS inventory plugin

```shell
[ansible@ansible Chapter-05]$ ansible-doc -t inventory -l |grep aws  
amazon.aws.aws_ec2                                      EC2 inventory sourc... 
amazon.aws.aws_rds                                      rds instance source
```

## Figure 5.14. AWS profile config file 

```shell
[ansible@ansible Chapter-05]$ cat ~/.aws/credentials  
[default] 
aws_access_key_id=EXAMPLEKEY 
aws_secret_access_key=EXAMPLEACCESSKEY 
[ansible] 
aws_access_key_id=EXAMPLEKEY 
aws_secret_access_key=EXAMPLEACCESSKEY
```

## Figure 5.15. Inventory file for AWS ec2 instances 

```shell
[ansible@ansible Chapter-05]$ mkdir inventories/aws 

[ansible@ansible Chapter-05]$ cd inventories/aws/ 
[ansible@ansible aws]$ cat lab.aws_ec2.yml  
# lab.aws_ec2.yml 
plugin: amazon.aws.aws_ec2 
boto_profile: ansible 
regions: 
  - ap-southeast-1
```

## Figure 5.16. Verify AWS dynamic inventory 

```shell
[ansible@ansible Chapter-05]$ ansible-inventory -i inventories/aws/ --graph 
@all: 
  |--@aws_ec2: 
  |  |--ec2-13-250-108-199.ap-southeast-1.compute.amazonaws.com 
  |  |--ec2-13-250-48-91.ap-southeast-1.compute.amazonaws.com 
  |  |--ec2-54-179-175-153.ap-southeast-1.compute.amazonaws.com 
  |--@ungrouped:
```

## Figure 5.17. AWS dynamic inventory with additional filters 

```shell
[ansible@ansible Chapter-05]$ ansible-inventory -i inventories/aws/ --graph 
@all: 
  |--@aws_ec2: 
  |  |--ec2-54-179-175-153.ap-southeast-1.compute.amazonaws.com 
  |--@ungrouped:
```

## Figure 5.18. Ansible ping test using the AWS dynamic inventory 

```shell
[ansible@ansible Chapter-05]$ ansible all -m ping -i inventories/aws/  
ec2-13-250-108-199.ap-southeast-1.compute.amazonaws.com | SUCCESS => { 
    "ansible_facts": { 
        "discovered_interpreter_python": "/usr/bin/python" 
    }, 
    "changed": false, 
    "ping": "pong" 
}
```
