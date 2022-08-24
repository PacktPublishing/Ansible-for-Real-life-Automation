## Jenkins pipeline

```groovy
pipeline {
    agent any
    stages {
        stage ("Fetch Ansible content") {
            steps {
                git "https://github.com/ginigangadharan/website-demo-one-page.git"   
            }
        }
        stage("Deploy application using Ansible") {
           steps {
                ansiblePlaybook credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'Ansible', inventory: 'produ.inventory', playbook: 'deploy-web.yaml'
            }    
        }    
    }
}
```

## Execute ansible web deploy

```
[ansible@ansible Chapter-09]$ ansible-playbook deploy-web.yaml -e "NODES=web" 
. 
<output omitted> 
. 
.  
TASK [Verify application health] ********************************************************** 
ok: [localhost] 
. 
. 

```

## install haproxy role

```
[ansible@ansible Chapter-09]$ cd roles 

[ansible@ansible roles]$ ansible-galaxy role install geerlingguy.haproxy 
```
## Execute haproxy playbook

```
[ansible@ansible Chapter-09]$ ansible-playbook deploy-haproxy.yaml 
. 
.  
TASK [Verify load balancer health]************************************************************ 
ok: [node3 -> localhost] 
. 
. 
```

## Using serial in playbook

```
. 
  hosts: web 
  become: yes 
  serial: 25% 
  tasks: 
. 
. 
```

## Using serial 
```
  serial: 
    - 1 
    - 20% 
    - 100% 
```

## Updating source code in Git

```shell
## Update the website’s content with some changes by creating a new branch in the repository. (Use the https://github.com/ginigangadharan/website-demo-one-page repository and make a copy for testing purposes.) 

## Clone the repository to your local machine: 
[ansible@ansible ~]$ git clone git@github.com:ginigangadharan/website-demo-one-page 

## Switch to the repository’s directory: 
[ansible@ansible ~]$ cd website-demo-one-page 


## Switch to the production branch: 
[ansible@ansible website-demo-one-page]$ git checkout production 
Switched to branch 'production' 
Your branch is up to date with 'origin/production'. 

[ansible@ansible website-demo-one-page]$ git checkout -b v2            
Switched to a new branch 'v2' 

```

## [ansible@ansible website-demo-one-page]$ git add .;git commit -m "v2" 

[ansible@ansible website-demo-one-page]$ git push -u origin v2 

```
[ansible@ansible website-demo-one-page]$ git add .;git commit -m "v2" 

[ansible@ansible website-demo-one-page]$ git push -u origin v2 
```

## playbook rolling update

```shell
[ansible@ansible Chapter-09]$ ansible-playbook rolling-update.yaml -e "NODES=web application_branch=v2" 
. 
.
PLAY [Rolling Update] ********************************************************** 
 
TASK [Gathering Facts] ********************************************************* 
ok: [node1] 
  
TASK [Disable server in haproxy backend] *************************************** 
changed: [node1 -> node3] => (item=node3) 
. 
. 




.
.
PLAY [Rolling Update] ********************************************************** 


TASK [Gathering Facts] ********************************************************* 
ok: [node2] 
  
TASK [Disable server in haproxy backend] *************************************** 
changed: [node2 -> node3] => (item=node3) 
. 
.
Finally, the Verify load balancer traffic task is successful as follows. 
PLAY [Verify load balancer traffic] ***************************************** 

TASK [Gathering Facts] ********************************************************* 
ok: [node3] 

TASK [Verify load balancer traffic] ********************************************* 
ok: [node3 -> localhost] 
. 
. 
```

## terraform code

```shell
resource "aws_instance" "dbnodes" { 
  ami             = var.aws_ami_id 
  instance_type   = "t2.large" 
  key_name        = aws_key_pair.ec2loginkey.key_name 
  count           = var.dbnodes_count 
  security_groups = ["dbnodes-sg"] 
  user_data       = file("user-data-dbnodes.sh") 
  tags = { 
    Name = "dbnode-${count.index + 1}" 
  } 
} 
```

## terrform with Ansible

```shell
resource "aws_instance" "dbnodes" { 
  ami             = var.aws_ami_id 
  instance_type   = "t2.large" 
  key_name        = aws_key_pair.ec2loginkey.key_name 
  count           = var.dbnodes_count 
  security_groups = ["dbnodes-sg"] 
  user_data       = file("user-data-dbnodes.sh") 
  tags = { 
    Name = "dbnode-${count.index + 1}" 
  } 
 
  provisioner "local-exec" { 
    command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ec2-user -i '${self.public_ip},' --private-key ${var.ssh_key_pair} post-configuration.yaml" 

  } 
} 
```

## with user data

```shell
resource "aws_instance" "dbnodes" { 
  ami           = var.aws_ami_id #"ami-0cd31be676780afa7" 
  instance_type   = "t2.large" 
  key_name        = aws_key_pair.ec2loginkey.key_name 
  count           = var.dbnodes_count 
  security_groups = ["dbnodes-sg"] 
  user_data       = file("user-data-dbnodes.sh") 
  tags = { 
    Name = "dbnode-${count.index + 1}" 
  } 
```