# Ansible Lab - Using Terraform and AWS

*Warning: this is still in-progress and do not use*

Also check **[Terraform IaC Examples ](https://github.com/ginigangadharan/terraform-iac-usecases)**.

Read Full Article here : [Use Terraform to Create a FREE Ansible Lab in AWS](https://www.techbeatly.com/2021/06/use-terraform-to-create-a-free-ansible-lab-in-aws.html)

## Introduction

Terraform will provision below resources and take note on details.

- 1x ec2 instance for Ansible Engine.
- 2x ec2 instances fro Ansible managed nodes.
- We are using `Amazon Linux 2 AMI (HVM), SSD Volume Type` (`ami-02f26adf094f51167`); you can create with other AMI's as well by changing the AMI details in `variables.tf` (Consider adjusting the installation commands if you are changing the AMI or OS)
- Default `region = "ap-southeast-1"` (**Singapore**), change this in `main.tf` if needed.
- A new Security Group will be created as `ansible-lab-security-group` (which will be destroyed when you do `terraform destroy` together with all other resources)
- All Nodes will be configured with ssh access.
- All Nodes will be installed with ansible, git, vim and other necessary packages.
- Uncomment `# sudo yum update -y` in `user-data-*.sh` if you need to update the nodes with latest updates.

# How to use this repository
## Step 1. Install Terraform

If you haven't yet, [Download](https://www.terraform.io/downloads.html) and [Install](https://learn.hashicorp.com/tutorials/terraform/install-cli) Terraform.

## Step 2. Configure AWS Credential

Refer [AWS CLI Configuration Guide](https://github.com/ginigangadharan/vagrant-iac-usecases#aws-setup) for details.

## Step 3. Create SSH Keys to Access the ec2 instances

If you have existing keys, you can use that; otherwise create new ssh keys.

- ***Warning**: Please remember to not to overwrite the existing ssh key pair files; use a new file name if you want to keep the old keys.*
- If you are using any key files other than `~/.ssh/id_rsa`, then remember to update the same in `variables.tf` as well.

```shell
$ ssh-keygen
```

## Step 4. Clone the Repository and create your Ansible Lab

```shell
$ git clone https://github.com/ginigangadharan/terraform-iac-usecases
$ cd terraform-aws-ansible-lab

## init terraform
$ terraform init

## verify the resource details before apply
$ terraform plan

## Apply configuration - This step will spin up all necessary resources in your AWS Account
$ terraform apply
.
.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_key_pair.ec2loginkey: Creating...
aws_security_group.ansible_access: Creating...
.
.
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

ansible-engine = <Public IP ADDRESS>
ansible-node-1 = <Public IP ADDRESS>
ansible-node-2 = <Public IP ADDRESS>
```

### How to Access the Lab ?

Terraform will show you the `Public IP` of `ansible-engine` instance and you can access the ansible-engine using that IP. 

- Host: Public IP of `ansible-engine`. SSH Keys are already copied inside **all ec2 instances** under `devops` user but still you can access it using below credentials if accessing from different machines.
  - Username: `devops`
  - Password: `devops` 

```shell
$ ssh devops@IP_ADDRESS
[devops@ansible-engine ~]$
```

- A default `ansible.cfg` and `inventory` files are already available to use under home directory (`/home/devops/`)
  
```shell
## Check Files copied automatically
[devops@ansible-engine ~]$ ls -l
total 8
-rwxr-xr-x 1 devops devops  82 Jun 10 09:04 ansible.cfg
-rwxr-xr-x 1 devops devops 524 Jun 10 09:04 inventory
```

- `ansible-engine` to `ansible-nodes` ssh connection is already setup using password in `inventory` file.

```shell
## Verify Instance Access
[devops@ansible-engine ~]$ ansible all -m ping
ansible-engine | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
node2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
node1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
```


## Step 5. Destroy Lab Once you are Done 

As we know, we are dealing with FREE tier, remember to destroy the resources once you finish the lab or practicing for that day. 

```shell
$ terraform destroy
```

DO not need to worry, you will get the same lab setup whenever you needed by simply doing a `terraform apply` command again. 

## Appendix

### Use `local-exec` if you have Ansible installed locally

If you are using Linux/Mac machine and ansible is available locally, then you an use below method for executing Terraform provisioner. (Current configuration is to execute ansible playbook  from `ansible-engine` node itself.)

```json
  provisioner "local-exec" {
    command = "ansible-playbook engine-config.yaml"
  }
```  