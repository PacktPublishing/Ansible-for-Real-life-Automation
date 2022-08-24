# Code snippets for reference

- [Code snippets for reference](#code-snippets-for-reference)
  - [4.1](#41)
  - [4.2](#42)
  - [4.3](#43)
  - [4.11](#411)
  - [4.18](#418)
  - [4.19](#419)
  - [4.20](#420)
  - [4.21](#421)
  - [4.22](#422)
  - [4.23](#423)
  - [4.24](#424)
  - [4.31](#431)
  - [4.32](#432)
  - [4.33](#433)
  - [4.34](#434)
  - [4.35](#435)

## 4.1

```shell
[ansible@ansible ansible-roles]$ ls -l 
total 0 
drwxr-xr-x  14 gini  staff  448 21 Jan 12:46 ansible-role-pgsql-replication 
drwxr-xr-x  12 gini  staff  384 21 Jan 12:45 ansible-role-repo-epel 
drwxr-xr-x  11 gini  staff  352 21 Jan 12:42 ansible-role-setup-user 
drwxr-xr-x  14 gini  staff  448 21 Jan 12:45 ansible-role-system-facts-report 
drwxr-xr-x  15 gini  staff  480 21 Jan 12:41 ansible-role-tower-setup 
```

## 4.2

```shell
[ansible@ansible ansible-collections]$ ls -l 
total 0 
drwxr-xr-x  14 gini  staff  448 21 Jan 13:22 ansible-collection-custom-modules 
drwxr-xr-x   5 gini  staff  160 21 Jan 13:21 ansible-collection-kubernetes_home_lab 
```

## 4.3

```shell
├── ansible-inventory-development 
│   ├── group_vars 
│   │   └── mysqlservers 
│   ├── host_vars 
│   └── inventory 
├── ansible-inventory-production 
│   ├── group_vars 
│   │   ├── mysqlservers 
│   │   └── webservers 
│   ├── host_vars 
│   └── inventory 
└── ansible-inventory-staging 
    ├── group_vars 
    │   ├── mysqlservers 
    │   └── webservers 
    ├── host_vars 
    └── inventory 
```

## 4.11

```shell
[ansible@ansible ~]$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDgzrPJQ4Vp6FGO4XVGUpQNzpTOyO1+pS/9whfBqjvY8OOgfJM2eg/rpcubMsMAamCPzeFmy0RKXIHixAno5Snm9VcENfobknHb4IQmRq0ATOiG1niyWDJB9fUIm/3YOPt+ZxPiiUa/iQvc8B4FqLGvBGSWB9GZE4OPPFk+sfCrmDrlI+2kgBeRJ3xKqMxoj70aReHDdO/jVN9VcUiHQ+WrTqBSHyHObb1SCxWFScj7VKR2BnayyKrS1EDOluPKLwfcEM5scms6tL8cwnyCvko4W2afIQqSbEdhOesoGh/fQl4c7ycFnkIxaicnReEEDEXnBso9Ndp3PCTojoT86RyqDUgpazjMsZkmL52YPcq2aX6RGOrE8eWIeATHNNM4nH5tTMf/35j3+3WXA/9NSdvsikGet5FKL21tIy2qo5hKHgMnL9Dipdoai3cnlCD/t4A/Z0bNsAMWDgzSPsmVjdDCBealRJYiLJimj8sTjleruah5DlZqfZoTymuMloInxsM= ansible@ansible-controlnode
```

## 4.18


```shell
[ansible@ansible ~]$ git clone git@github.com:demouser-2022/ansible-package-installation.git 
Cloning into 'ansible-package-installation'... 
remote: Enumerating objects: 3, done. 
remote: Counting objects: 100% (3/3), done. 
remote: Compressing objects: 100% (2/2), done. 
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 
Receiving objects: 100% (3/3), done.
```

## 4.19

```shell
[ansible@ansible ~]$ cd ansible-package-installation/ 
[ansible@ansible ansible-package-installation]$ ls -la 
total 4 
drwxrwxr-x. 3 ansible ansible  35 Jan 21 14:25 . 
drwxrwxrwt. 9 root    root    208 Jan 21 14:25 .. 
drwxrwxr-x. 8 ansible ansible 163 Jan 21 14:25 .git 
-rw-rw-r--. 1 ansible ansible  69 Jan 21 14:25 README.md 
```

## 4.20

```shell
[ansible@ansible ansible-package-installation]$ ls -la
total 24
drwxrwxr-x.  3 ansible ansible  121 Jan 21 14:24 .
drwx------. 13 ansible ansible 4096 May 28 03:26 ..
-rw-rw-r--.  1 ansible ansible  209 Jan 21 14:24 ansible.cfg
-rw-rw-r--.  1 ansible ansible  222 Jan 21 14:24 chrony.conf.sample
drwxrwxr-x.  8 ansible ansible  185 Jan 21 14:32 .git
-rw-rw-r--.  1 ansible ansible  135 Jan 21 14:24 hosts
-rw-rw-r--.  1 ansible ansible  558 Jan 21 14:24 install-package.yaml
-rw-rw-r--.  1 ansible ansible   69 Jan 21 14:21 README.md
```

## 4.21

```shell
[ansible@ansible ansible-package-installation]$ git status 
On branch main 
Your branch is up to date with 'origin/main'. 

Untracked files: 
  (use "git add <file>..." to include in what will be committed) 
        ansible.cfg 
        chrony.conf.sample 
        hosts 
        install-package.yaml 
        
nothing added to commit but untracked files present (use "git add" to track)
```

## 4.22

```shell
[ansible@ansible ansible-package-installation]$ git status 
On branch main 
Your branch is up to date with 'origin/main'. 

Changes to be committed: 
  (use "git restore --staged <file>..." to unstage) 
        new file:   ansible.cfg 
        new file:   chrony.conf.sample 
        new file:   hosts 
        new file:   install-package.yaml 
```        

## 4.23

```shell
[ansible@ansible ansible-package-installation]$ git commit -m "First commit with Ansible files" 
[main 302dfcc] First commit with Ansible files 
4 files changed, 51 insertions(+) 
create mode 100644 ansible.cfg 
create mode 100644 chrony.conf.sample 
create mode 100644 hosts 
create mode 100644 install-package.yaml
```

## 4.24

```shell
[ansible@ansible ansible-package-installation]$ git push 
Enumerating objects: 7, done. 
Counting objects: 100% (7/7), done. 
Compressing objects: 100% (6/6), done. 
Writing objects: 100% (6/6), 1.04 KiB | 1.04 MiB/s, done. 
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 
To github.com:demouser-2022/ansible-package-installation.git 
   e02e43b..302dfcc  main -> main
```   

## 4.31

```shell
$ git clone git@github.com:ginigangadharan/ansible-package-installation.git 
Cloning into 'ansible-package-installation'... 
remote: Enumerating objects: 9, done. 
remote: Counting objects: 100% (9/9), done. 
remote: Compressing objects: 100% (8/8), done. 
Receiving objects: 100% (9/9), done. 
remote: Total 9 (delta 0), reused 6 (delta 0), pack-reused 0 
 
$ cd ansible-package-installation  
$ ls -l 
total 40 
-rw-r--r--  1 gini  staff   69 22 Jan 12:33 README.md 
-rw-r--r--  1 gini  staff  209 22 Jan 12:33 ansible.cfg 
-rw-r--r--  1 gini  staff  222 22 Jan 12:33 chrony.conf.sample 
-rw-r--r--  1 gini  staff  135 22 Jan 12:33 hosts 
-rw-r--r--  1 gini  staff  558 22 Jan 12:33 install-package.yaml 
```

## 4.32

```shell
$ git status 
On branch feature-1 
Changes not staged for commit: 
  (use "git add <file>..." to update what will be committed) 
  (use "git restore <file>..." to discard changes in working directory) 
        modified:   install-package.yaml 
  
no changes added to commit (use "git add" and/or "git commit -a") 
```

## 4.33

```shell
$ git add * 
$ git commit -m "updated install-package.yaml" 
[feature-1 6e7004b] updated install-package.yaml 
1 file changed, 2 insertions(+), 2 deletions(-) 
```

## 4.34

```shell
$ git log    
commit 898e5dfde4d90805feb579d245efdce5a18738c7 (HEAD -> feature-1) 
Author: ginigangadharan <net.gini@gmail.com> 
Date:   Sat Jan 22 13:04:26 2022 +0800 
  
    updated install-package.yaml

commit 302dfccd4cc5b018e17619d8fb1a107b9f230350 (origin/main, origin/HEAD, main) 
Author: demouser-2022 <M demo1@techbeatly.com> 
Date:   Fri Jan 21 14:32:14 2022 +0000 
  
    First commit with Ansible files 
  
commit e02e43be5e66504e6c129443b38c228245a6444a 
Author: demouser-2022 <98160880+demouser-2022@users.noreply.github.com> 
Date:   Fri Jan 21 21:23:13 2022 +0800 
  
    Initial commit 
```

## 4.35

```shell
$ git push -u origin feature-1 
Enumerating objects: 5, done. 
Counting objects: 100% (5/5), done. 
...<output omitted>... 
* [new branch]      feature-1 -> feature-1 
Branch 'feature-1' set up to track remote branch 'feature-1' from 'origin'.
```