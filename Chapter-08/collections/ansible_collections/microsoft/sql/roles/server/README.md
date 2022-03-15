# Microsoft SQL Server

![CI Testing](https://github.com/linux-system-roles/template/workflows/tox/badge.svg)

This role installs, configures, and starts Microsoft SQL Server.

The role also optimizes the operating system to improve performance and
throughput for SQL Server by applying the `mssql` Tuned profile.

The role currently works with SQL Server 2017 and 2019.

## Requirements

* SQL Server requires a machine with at least 2000 megabytes of memory.
* You must configure the firewall to enable connections on the SQL Server TCP port that
  you set with the `mssql_tcp_port` variable. The default port is 1443.
* Optional: If you want to input T-SQL statements and stored procedures to SQL Server,
  you must create a file with the `.sql` extension containing these SQL
  statements and procedures.

## Role Variables

### `mssql_accept_microsoft_odbc_driver_17_for_sql_server_eula`

Set this variable to `true` to indicate that you accept EULA for installing the
`msodbcsql17` package.

The license terms for this product can be downloaded
from <https://aka.ms/odbc17eula> and found in `/usr/share/doc/msodbcsql17/LICENSE.txt`.

Default: `false`

Type: `bool`

### `mssql_accept_microsoft_cli_utilities_for_sql_server_eula`

Set this variable to `true` to indicate that you accept EULA for installing the
`mssql-tools` package.

The license terms for this product can be downloaded
from <http://go.microsoft.com/fwlink/?LinkId=746949> and found in
`/usr/share/doc/mssql-tools/LICENSE.txt`.

Default: `false`

Type: `bool`

### `mssql_accept_microsoft_sql_server_standard_eula`

Set this variable to `true` to indicate that you accept EULA for using
Microsoft SQL Server.

The license terms for this product can be found in `/usr/share/doc/mssql-server`
or downloaded from <https://go.microsoft.com/fwlink/?LinkId=2104078&clcid=0x409>.
The privacy statement can be viewed at
<https://go.microsoft.com/fwlink/?LinkId=853010&clcid=0x409>.

Default: `false`

Type: `bool`

### `mssql_version`

The version of the SQL Server to configure. The role currently supports versions
2017 and 2019.

Default: `2019`

Type: `int`

### `mssql_upgrade`

If you want to upgrade your SQL Server 2017 to 2019, set the `mssql_version`
variable to `2019` and this variable to `true`.

Note that the role does not support downgrading SQL Server.

Default: `false`

Type: `bool`

### `mssql_password`

The password for the database sa user. The password must have a minimum length
of 8 characters, include uppercase and lowercase letters, base 10 digits or
non-alphanumeric symbols. Do not use single quotes ('), double quotes ("), and
spaces in the password because `sqlcmd` cannot authorize when the password
includes those symbols.

This variable is required when you run the role to install SQL Server.

When running this role on a host that has SQL Server installed, the `mssql_password`
variable overwrites the existing sa user password to the one that you specified.

Default: `null`

Type: `str`

### `mssql_edition`

The edition of SQL Server to install.

This variable is required when you run the role to install SQL Server.

Use one of the following values:

* `Enterprise`
* `Standard`
* `Web`
* `Developer`
* `Express`
* `Evaluation`
* A product key in the form `#####-#####-#####-#####-#####`, where `#` is a
  number or a letter.
  For more information, see
  <https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-ver15>.

Default: `null`

Type: `str`

### `mssql_tcp_port`

The port that SQL Server listens on.

If you define this variable, the role configures SQL Server with the defined TCP
port.

If you do not define this variable when installing SQL Server, the role configures
SQL Server to listen on the SQL Server default TCP port `1443`.

If you do not define this variable when configuring running SQL Server, the role does
not change the TCP port setting on SQL Server.

Default: `null`

Type: `str`

### `mssql_ip_address`

The IP address that SQL Server listens on.

If you define this variable, the role configures SQL Server with the defined IP
address.

If you do not define this variable when installing SQL Server, the role configures
SQL Server to listen on the SQL Server default IP address `0.0.0.0`, that is, to listen on
every available network interface.

If you do not define this variable when configuring running SQL Server, the role does
not change the IP address setting on SQL Server.

Default: `null`

Type: `str`

### `mssql_input_sql_file`

You can use the role to input a file containing SQL statements or procedures into
SQL Server. With this variable, enter the path to the SQL file containing the
database configuration.

When specifying this variable, you must also specify the `mssql_password`
variable because authentication is required to input an SQL file to SQL Server.

If you do not pass this variable, the role only configures the SQL Server
and does not input any SQL file.

Note that this task is not idempotent, the role always inputs an SQL file if
this variable is defined.

You can find an example of the SQL file at `tests/sql_script.sql`.

Default: `null`

Type: `str`

### `mssql_enable_sql_agent`

Set this variable to `true` or `false` to enable or disable the SQL agent.

Default: `null`

Type: `bool`

### `mssql_install_fts`

Set this variable to `true` or `false` to install or remove the
`mssql-server-fts` package that provides full-text search.

Default: `null`

Type: `bool`

### `mssql_install_powershell`

Set this variable to `true` or `false` to install or remove the `powershell` package that provides PowerShell.

Default: `null`

Type: `bool`

### `mssql_enable_ha`

Set this variable to `true` or `false` to install or remove the
`mssql-server-ha` package and enable or disable the `hadrenabled` setting.

Default: `null`

Type: `bool`

### `mssql_tune_for_fua_storage`

Set this variable to `true` or `false` to enable or disable settings that
improve performance on hosts that support Forced Unit Access (FUA) capability.

Only set this variable to `true` if your hosts are configured for FUA
capability.

When set to `true`, the role applies the following settings:

* Set the `traceflag 3979 on` setting to enable trace flag 3979 as a startup
parameter
* Set the `control.alternatewritethrough` setting to `0`
* Set the `control.writethrough` setting to `1`

When set to `false`, the role applies the following settings:

* Set the `traceflag 3982 off` parameter to disable trace flag 3979 as a
startup parameter
* Set the `control.alternatewritethrough` setting to its default value `0`
* Set the `control.writethrough` setting to its default value `0`

For more details, see SQL Server and Forced Unit Access (FUA) I/O subsystem
capability at <https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-performance-best-practices?view=sql-server-ver15>.

Default: `null`

Type: `bool`

### `mssql_tls_enable`

Use the variables starting with `mssql_tls` to configure SQL Server to encrypt
connections using TLS certificates.

You are responsible for creating and securing TLS certificate and private
key files. It is assumed you have a CA that can issue these files. If not, you
can use the `openssl` command to create these files.

You must have TLS certificate and private key files on the Ansible control node.

When you use this variable, the role copies TLS cert and private key files to
SQL Server and configures SQL Server to use these files to encrypt connections.

Set to `true` or `false` to enable or disable TLS encryption.

When set to `true`, the role performs the following tasks:

1. Copies TLS certificate and private key files to SQL Server to the
`/etc/pki/tls/certs/` and `/etc/pki/tls/private/` directories respectively
2. Configures SQL Server to encrypt connections using the copied TLS certificate and
private key

When set to `false`, the role configures SQL Server to not use TLS encryption.
The role does not remove the existing certificate and private key files if this
variable is set to `false`.

Default: `null`

Type: `bool`

### `mssql_tls_cert`

Path to the certificate file to copy to SQL Server.

Default: `null`

Type: `str`

### `mssql_tls_private_key`

Path to the private key file to copy to SQL Server.

Default: `null`
Type: `str`

### `mssql_tls_version`

TLS version to use.

Default: `1.2`

Type: `str`

### `mssql_tls_force`

Set to `true` to replace the existing certificate and private key files on host
if they exist at `/etc/pki/tls/certs/` and `/etc/pki/tls/private/` respectively.

Default: `false`

Type: `bool`

## Example Playbooks

This section outlines example playbooks that you can use as a reference.

### Setting up SQL Server

This example shows how to use the role to set up SQL Server with the minimum
required variables.

```yaml
- hosts: all
  vars:
    mssql_accept_microsoft_odbc_driver_17_for_sql_server_eula: true
    mssql_accept_microsoft_cli_utilities_for_sql_server_eula: true
    mssql_accept_microsoft_sql_server_standard_eula: true
    mssql_password: "p@55w0rD"
    mssql_edition: Evaluation
  roles:
    - microsoft.sql.server
```

### Setting up SQL Server with Custom Network Parameters

This example shows how to use the role to set up SQL Server and configure it to
use custom IP address and TCP port.

```yaml
- hosts: all
  vars:
    mssql_accept_microsoft_odbc_driver_17_for_sql_server_eula: true
    mssql_accept_microsoft_cli_utilities_for_sql_server_eula: true
    mssql_accept_microsoft_sql_server_standard_eula: true
    mssql_password: "p@55w0rD"
    mssql_edition: Evaluation
    mssql_tcp_port: 1433
    mssql_ip_address: 0.0.0.0
  roles:
    - microsoft.sql.server
```

### Setting Up SQL Server and Enabling Additional Functionality

This example shows how to use the role to set up SQL Server and enable the
following additional functionality:

* Enable the SQL Agent
* Install FTS
* Install PowerShell
* Configure SQL Server for FUA capability
* After SQL Server is set up, input an SQL file to SQL Server

```yaml
- hosts: all
  vars:
    mssql_accept_microsoft_odbc_driver_17_for_sql_server_eula: true
    mssql_accept_microsoft_cli_utilities_for_sql_server_eula: true
    mssql_accept_microsoft_sql_server_standard_eula: true
    mssql_password: "p@55w0rD"
    mssql_edition: Evaluation
    mssql_enable_sql_agent: true
    mssql_install_fts: true
    mssql_install_powershell: true
    mssql_tune_for_fua_storage: true
    mssql_input_sql_file: mydatabase.sql
  roles:
    - microsoft.sql.server
```

### Setting Up SQL Server with TLS Encryption

This example shows how to use the role to set up SQL Server and configure it to
use TLS encryption.

```yaml
- hosts: all
  vars:
    mssql_accept_microsoft_odbc_driver_17_for_sql_server_eula: true
    mssql_accept_microsoft_cli_utilities_for_sql_server_eula: true
    mssql_accept_microsoft_sql_server_standard_eula: true
    mssql_password: "p@55w0rD"
    mssql_edition: Evaluation
    mssql_tls_enable: true
    mssql_tls_cert: mycert.pem
    mssql_tls_private_key: mykey.key
    mssql_tls_version: 1.2
    mssql_tls_force: false
  roles:
    - microsoft.sql.server
```

## License

MIT
