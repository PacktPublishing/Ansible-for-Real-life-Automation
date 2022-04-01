#! /bin/bash
sudo amazon-linux-extras install -y epel
sudo useradd devops
echo -e 'devops\ndevops' | sudo passwd devops
echo 'devops ALL=(ALL) NOPASSWD: ALL' | sudo tee /etc/sudoers.d/devops
sudo sed -i "s/PasswordAuthentication no/PasswordAuthentication yes/g" /etc/ssh/sshd_config
sudo systemctl restart sshd.service
sudo yum install -y python3
sudo yum install -y vim
sudo yum install -y ansible
sudo yum install -y git
# sudo yum update -y