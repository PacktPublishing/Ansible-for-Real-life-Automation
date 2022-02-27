#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_dns_config
short_description: Manage VMware ESXi DNS Configuration
description:
    - Manage VMware ESXi DNS Configuration
author:
- Joseph Callen (@jcpowermac)
notes:
    - Tested on vSphere 5.5
requirements:
    - "python >= 2.6"
    - PyVmomi
deprecated:
    removed_at_date: '2022-06-01'
    why: Will be replaced with new module M(community.vmware.vmware_host_dns).
    alternative: Use M(community.vmware.vmware_host_dns) instead.
options:
    change_hostname_to:
        description:
            - The hostname that an ESXi host should be changed to.
        required: True
        type: str
    domainname:
        description:
            - The domain the ESXi host should be apart of.
        required: True
        type: str
    dns_servers:
        description:
            - The DNS servers that the host should be configured to use.
        required: True
        type: list
        elements: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Configure ESXi hostname and DNS servers
  community.vmware.vmware_dns_config:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    change_hostname_to: esx01
    domainname: foo.org
    dns_servers:
        - 8.8.8.8
        - 8.8.4.4
  delegate_to: localhost
'''

try:
    from pyVmomi import vim, vmodl
    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import HAS_PYVMOMI, connect_to_api, get_all_objs, vmware_argument_spec


def configure_dns(host_system, hostname, domainname, dns_servers):

    changed = False
    host_config_manager = host_system.configManager
    host_network_system = host_config_manager.networkSystem
    config = host_network_system.dnsConfig

    config.dhcp = False

    if config.address != dns_servers:
        config.address = dns_servers
        changed = True
    if config.domainName != domainname:
        config.domainName = domainname
        changed = True
    if config.hostName != hostname:
        config.hostName = hostname
        changed = True
    if changed:
        host_network_system.UpdateDnsConfig(config)

    return changed


def main():

    argument_spec = vmware_argument_spec()
    argument_spec.update(dict(change_hostname_to=dict(required=True, type='str'),
                              domainname=dict(required=True, type='str'),
                              dns_servers=dict(required=True, type='list', elements='str')))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    if not HAS_PYVMOMI:
        module.fail_json(msg='pyvmomi is required for this module')

    change_hostname_to = module.params['change_hostname_to']
    domainname = module.params['domainname']
    dns_servers = module.params['dns_servers']
    try:
        content = connect_to_api(module)
        host = get_all_objs(content, [vim.HostSystem])
        if not host:
            module.fail_json(msg="Unable to locate Physical Host.")
        host_system = list(host)[0]
        changed = configure_dns(host_system, change_hostname_to, domainname, dns_servers)
        module.exit_json(changed=changed)
    except vmodl.RuntimeFault as runtime_fault:
        module.fail_json(msg=runtime_fault.msg)
    except vmodl.MethodFault as method_fault:
        module.fail_json(msg=method_fault.msg)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
