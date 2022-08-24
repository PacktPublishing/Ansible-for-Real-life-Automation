## ansible.cfg

```
[defaults] 
. 
. 
COLLECTIONS_PATHS = ./collections 
roles_path = roles 
```


## Installing an Ansible role using the ansible-galaxy command 

```
[ansible@ansible Chapter-08]$ ansible-galaxy install geerlingguy.postgresql -p roles/
Starting galaxy role install process
- downloading role 'postgresql', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-postgresql/archive/3.4.0.tar.gz
- extracting geerlingguy.postgresql to /home/ansible/ansible-book-packt/Chapter-08/roles/geerlingguy.postgresql
- geerlingguy.postgresql (3.4.0) was installed successfully
```

## deploy Postgres

```
[ansible@ansible Chapter-08]$ ansible-playbook postgres-deploy.yaml -e "NODES=node1" 
```

## Check PostgreSQL version

```
[devops@node-1 ~]$ sudo su - postgres
Last login: Tue Mar 15 09:59:35 UTC 2022 on pts/1

[postgres@node-1 ~]$ postgres -V
postgres (PostgreSQL) 10.17
```

## Figure 8.11 – Open psql client on database server 

```
[postgres@node-1 ~]$ psql
psql (10.17)
Type "help" for help.

postgres=#
```

## Figure 8.12 – Listing the existing databases in the psql command line 

```
postgres=# \l
                                    List of databases
     Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
---------------+----------+----------+-------------+-------------+-----------------------
 database_demo | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
(4 rows)
```

## Figure 8.13 – Verifying users in the psql command line 

```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 demouser  |                                                            | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 ```

## Figure 8.14 – Exiting the psql console 

```
postgres=# \q
[postgres@node-1 ~]$ 
```
## Figure 8.15 – Verifying the /var/lib/pgsql/data/pg_hba.conf file 

```
[postgres@node-1 ~]$ cat /var/lib/pgsql/data/pg_hba.conf 
#
# Ansible managed
#
# PostgreSQL Client Authentication Configuration File
# ===================================================
#
# See: https://www.postgresql.org/docs/current/static/auth-pg-hba-conf.html

local all all    peer 
host all all 0.0.0.0/0   md5 
```


## Figure 8.16 - Switch to postgres user and open psql cli

```
[devops@node-1 ~]$ sudo su - postgres 
Last login: Tue Mar 15 08:59:39 UTC 2022 on pts/1 
[postgres@node-1 ~]$

# Open psql command line
[postgres@node-1 ~]$ psql 
psql (10.17) 
Type "help" for help.
```

## Figure 8.17 - Change the password and exit from postgres account 

```
postgres=# ALTER USER postgres WITH ENCRYPTED PASSWORD 'PassWord'; 
ALTER ROLE 

## exit psql cli
postgres=# \q 

## exit postgres user
[postgres@node-1 ~]$ exit 
logout 
[devops@node-1 ~]$ 
```

## Figure 8.18 - Installing microsoft.sql collection
```
[ansible@ansible Chapter-08]$ ansible-galaxy collection install microsoft.sql 
```

## Figure 8.19 - Creating Microsoft SQL database

```
- name: Create a new database 
  community.general.mssql_db:  
    name: sales_db  
    state: present 
```

## Figure 8.24 - Execute playbook to create database, table and user 

```
[ansible@ansible Chapter-08]$ ansible-playbook postgres-manage-database.yaml -e "NODES=node1" 
```

## Figure 8.25 - Login to the database server and verify details

```
[devops@node-1 ~]$ sudo su - postgres
Last login: Sat Aug 20 13:59:54 UTC 2022 on pts/0
[postgres@node-1 ~]$ 
[postgres@node-1 ~]$ psql
psql (10.17)
Type "help" for help.

postgres=# \l
                                    List of databases
     Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
---------------+----------+----------+-------------+-------------+-----------------------
 database_demo | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 db_sales      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres         +
               |          |          |             |             | postgres=CTc/postgres+
               |          |          |             |             | devteam=c/postgres
 postgres      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
(5 rows)
```

## Figure 8.26 – Listing and verifying the newly created user 

```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 demouser  |                                                            | {}
 devteam   | Password valid until 2022-12-31 00:00:00+00                | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

## Figure 8.27 – Connecting to the newly created database and list tables 

```
postgres=# \c db_sales
You are now connected to database "db_sales" as user "postgres".
db_sales=# 
db_sales=# \dt
           List of relations
 Schema |    Name    | Type  |  Owner   
--------+------------+-------+----------
 public | demo_table | table | postgres
(1 row)
```

## Figure 8.15 – Database table details 

```
db_sales=# \d+ demo_table
                                                Table "public.demo_table"
 Column  |  Type  | Collation | Nullable |                Default                 | Storage  | Stat
s target | Description 
---------+--------+-----------+----------+----------------------------------------+----------+-----
---------+-------------
 id      | bigint |           | not null | nextval('demo_table_id_seq'::regclass) | plain    |     
         | 
 num     | bigint |           |          |                                        | plain    |     
         | 
 stories | text   |           |          |                                        | extended |     
         | 
Indexes:
    "demo_table_pkey" PRIMARY KEY, btree (id)
```

## Figure 8.29 – Verifying new user access and the list tables 

```
[postgres@node-1 ~]$ psql -U devteam -h localhost -d db_sales
Password for user devteam: 
psql (10.17)
Type "help" for help.

db_sales=> \dt
           List of relations
 Schema |    Name    | Type  |  Owner   
--------+------------+-------+----------
 public | demo_table | table | postgres
(1 row)
```

## Figure 8.30 - Grant user access to database 

```
- name: Grant users access to databases  
  community.postgresql.postgresql_pg_hba: 
    dest: /var/lib/postgres/data/pg_hba.conf 
    contype: host 
    users: johnt 
    source: 192.168.0.100/24 
    databases: db_sales 
    method: peer 
    create: true 
```

## Figure 8.31 - Database backup using Ansible 

```
    - name: Dump existing database to a file 
      community.postgresql.postgresql_db: 
        login_user: "{{ postgres_user }}" 
        login_password: "{{ postgres_password }}" 
        login_host: "{{ postgres_host }}" 
        name: "{{ postgres_database }}" 
        state: dump 
        target: /data/db_dumps/daily_prod_db_sales.sql 
```

## Figure 8.32 - Restore database from backup file 

```
    - name: Restore backup from file to database 
      community.postgresql.postgresql_db: 
        login_user: "{{ postgres_user }}" 
        login_password: "{{ postgres_password }}" 
        login_host: "{{ postgres_host }}" 
        name: "{{ postgres_database }}" 
        state: restore 
        target: /tmp/test.sql 
```        

