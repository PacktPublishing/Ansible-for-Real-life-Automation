
## docker connection plugin

```
[ansible@ansible Chapter-06]$ ansible-doc -s -t connection community.docker.docker
> COMMUNITY.DOCKER.DOCKER    (/home/ansible/ansible-book-packt/Chapter-06/collections/ansible_collectio>

        Run commands or put/fetch files to an existing docker container. Uses the
        Docker CLI to execute commands in the container. If you prefer to directly
        connect to the Docker daemon, use the community.docker.docker_api
        connection plugin.

OPTIONS (= is mandatory):

- container_timeout
        Controls how long we can wait to access reading output from the container
        once execution started.
        [Default: 10]
        set_via:
          env:
          - name: ANSIBLE_TIMEOUT
          - name: ANSIBLE_DOCKER_TIMEOUT
            version_added_collection: community.docker
          ini:
          - key: timeout
            section: defaults
          - key: timeout
:
```

## group variables

```
[ansible@ansible Chapter-06]$ cat group_vars/windows  
---
ansible_user: "ansible"
ansible_password: "MySecretWindowsPassword"
ansible_port: "5985"
ansible_connection: "winrm"
ansible_winrm_transport: "basic"
ansible_winrm_server_cert_validation: ignore
```