# -*- coding: utf-8 -*-

# Copyright: (c) 2016, Charles Paul <cpaul@ansible.com>
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2019, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):
    # Parameters for VMware modules
    DOCUMENTATION = r'''
notes:
  - All modules requires API write access and hence is not supported on a free ESXi license.
options:
    hostname:
      description:
      - The hostname or IP address of the vSphere vCenter or ESXi server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.
      - Environment variable support added in Ansible 2.6.
      type: str
    username:
      description:
      - The username of the vSphere vCenter or ESXi server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.
      - Environment variable support added in Ansible 2.6.
      type: str
      aliases: [ admin, user ]
    password:
      description:
      - The password of the vSphere vCenter or ESXi server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.
      - Environment variable support added in Ansible 2.6.
      type: str
      aliases: [ pass, pwd ]
    validate_certs:
      description:
      - Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.
      - Environment variable support added in Ansible 2.6.
      - If set to C(true), please make sure Python >= 2.7.9 is installed on the given machine.
      type: bool
      default: true
    port:
      description:
      - The port number of the vSphere vCenter or ESXi server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.
      - Environment variable support added in Ansible 2.6.
      type: int
      default: 443
    proxy_host:
      description:
      - Address of a proxy that will receive all HTTPS requests and relay them.
      - The format is a hostname or a IP.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PROXY_HOST) will be used instead.
      - This feature depends on a version of pyvmomi greater than v6.7.1.2018.12
      type: str
      required: False
    proxy_port:
      description:
      - Port of the HTTP proxy that will receive all HTTPS requests and relay them.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PROXY_PORT) will be used instead.
      type: int
      required: False
'''

    # This doc fragment is specific to vcenter modules like vcenter_license
    VCENTER_DOCUMENTATION = r'''
notes:
  - All modules requires API write access and hence is not supported on a free ESXi license.
options:
    hostname:
      description:
      - The hostname or IP address of the vSphere vCenter server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.
      - Environment variable supported added in Ansible 2.6.
      type: str
    username:
      description:
      - The username of the vSphere vCenter server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.
      - Environment variable supported added in Ansible 2.6.
      type: str
      aliases: [ admin, user ]
    password:
      description:
      - The password of the vSphere vCenter server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.
      - Environment variable supported added in Ansible 2.6.
      type: str
      aliases: [ pass, pwd ]
    validate_certs:
      description:
      - Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.
      - Environment variable supported added in Ansible 2.6.
      - If set to C(true), please make sure Python >= 2.7.9 is installed on the given machine.
      type: bool
      default: true
    port:
      description:
      - The port number of the vSphere vCenter server.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.
      - Environment variable supported added in Ansible 2.6.
      type: int
      default: 443
    proxy_host:
      description:
      - Address of a proxy that will receive all HTTPS requests and relay them.
      - The format is a hostname or a IP.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PROXY_HOST) will be used instead.
      type: str
      required: False
    proxy_port:
      description:
      - Port of the HTTP proxy that will receive all HTTPS requests and relay them.
      - If the value is not specified in the task, the value of environment variable C(VMWARE_PROXY_PORT) will be used instead.
      type: int
      required: False
    '''
