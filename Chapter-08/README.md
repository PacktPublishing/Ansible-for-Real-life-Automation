

## Changing PostgreSQL default user password

```shell
## switch to postgres user
[devops@node-1 ~]$ sudo su - postgres
Last login: Mon Mar 14 11:24:09 UTC 2022 on pts/0

## login to postgres database as postgres user
[postgres@node-1 ~]$ psql postgres postgres
psql (10.17)
Type "help" for help.

postgres=# 

## change the password
postgres=# ALTER USER postgres PASSWORD 'PassWord';
ALTER ROLE
postgres=# \q
```