# Snippets

```shell
[dockerhost] 
node1 ansible_host=192.168.56.25 
```

## Installing docker roles

```shell
[ansible@ansible Chapter-10]$ ansible-galaxy install geerlingguy.docker -p roles/ 
[ansibe@ansible Chapter-10]$ ansible-galaxy install geerlingguy.pip -p roles/ 
You can verify the roles installation as follows. 
[ansible@ansible Chapter-10]$ ansible-galaxy role list 
# /home/ansible/ansible-book-packt/Chapter-10/roles 
- geerlingguy.docker, 4.1.3 
- geerlingguy.pip, 2.1.0 
```

## Verify Docker installation

```shell
[root@node-1 ~]# docker version 
Client: Docker Engine - Community 
Version:           20.10.14 
API version:       1.41 
Go version:        go1.16.15 
..<output omitted>.. 
Server: Docker Engine - Community 
Engine: 
  Version:          20.10.14 
  API version:      1.41 (minimum version 1.12) 
  Go version:       go1.16.15 
..<output omitted>.. 
containerd: 
  Version:          1.5.11 
  GitCommit:        3df54a852345ae127d1fa3092b95168e4a88e2f8 
..<output omitted>.. 
```

## ansibl.cfg with collection and role paths

```ini
[defaults]
inventory = ./hosts  
remote_user = devops 
ask_pass = false

COLLECTIONS_PATHS = ./collections 
roles_path = roles 
```

## Docker collection 

```shell
./collections). 
[ansible@ansible Chapter-10]$ ansible-galaxy collection list |grep -i docker 
community.docker              1.10.2  
community.docker 2.3.0   
```

## nginx container running

```shell
[root@node-1 ~]# docker ps 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES 
e36fb7419165   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   0.0.0.0:8080->80/tcp   web 
```

##  nginx website using curl

```shell
[ansible@ansible Chapter-10]$ curl http://node1:8080 
<!DOCTYPE html>
<html> 
<head> 
<title>Welcome to nginx!</title> 
..<output omitted>.. 
<a href="http://nginx.com/">nginx.com</a>.</p> 
  
<p><em>Thank you for using nginx.</em></p> 
</body> 
</html> 
```

## nginx container stopped and removed

```shell
[root@node-1 ~]# docker ps -a 
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES 
[root@node-1 ~]#
```

## TODO app deployed using Ansible

```shell
[root@node-1 ~]# docker ps |grep todo 
0e158f5710bf   ginigangadharan/todo-app   "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   0.0.0.0:8081->3000/tcp   todo-app
```

## Wordpress containers

```shell
[devops@node-1 ~]$ sudo docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                  NAMES
d5253f49d1c9   wordpress   "docker-entrypoint.s…"   15 minutes ago   Up 15 minutes   0.0.0.0:8082->80/tcp   wordpress
74eb2db91a52   mariadb     "docker-entrypoint.s…"   15 minutes ago   Up 15 minutes   3306/tcp               mariadb
[devops@node-1 ~]$ 
[devops@node-1 ~]$ sudo docker volume ls
DRIVER    VOLUME NAME
local     mariadb
local     wordpress
```