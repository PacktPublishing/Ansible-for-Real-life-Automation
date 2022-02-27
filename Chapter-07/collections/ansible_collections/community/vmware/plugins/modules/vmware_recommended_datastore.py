#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: vmware_recommended_datastore
short_description: Returns the recommended datastore from a SDRS-enabled datastore cluster
description:
- This module provides the recommended datastore name from a datastore cluster only if the SDRS is enabled for the specified datastore cluster
author:
- Unknown (@MalfuncEddie)
- Alina Buzachis (@alinabuzachis)
- Abhijeet Kasurde (@Akasurde)
notes:
- Tested on vSphere 6.7 and 7.0.2
- Supports Check mode.
requirements:
- python >= 3
- PyVmomi
options:
  datacenter:
    description:
    - Name of the datacenter.
    type: str
    required: True
  datastore_cluster:
    description:
    - Name of the datastore cluster.
    type: str
    required: True
extends_documentation_fragment:
- community.vmware.vmware.documentation
version_added: '1.11.0'
"""


EXAMPLES = r"""
- name: Get recommended datastore from a Storage DRS-enabled datastore cluster
  community.vmware.vmware_recommended_datastore:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    datastore_cluster: '{{ datastore_cluster_name }}'
    datacenter: '{{ datacenter }}'
  register: recommended_ds
"""


RETURN = r"""
recommended_datastore:
  description: metadata about the recommended datastore
  returned: always
  type: str
  sample: {
    'recommended_datastore': 'datastore-01'
  }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    vmware_argument_spec,
)


class VmwareDatastoreClusterInfo(PyVmomi):
    def __init__(self, module):
        super(VmwareDatastoreClusterInfo, self).__init__(module)
        self.module = module
        self.params = module.params
        datacenter_name = self.params.get("datacenter")
        datacenter_obj = self.find_datacenter_by_name(datacenter_name)
        if datacenter_obj is None:
            self.module.fail_json(
                msg="Unable to find datacenter with name %s" % datacenter_name
            )
        datastore_cluster_name = self.params.get("datastore_cluster")
        datastore_cluster_obj = self.find_datastore_cluster_by_name(
            datastore_cluster_name, datacenter=datacenter_obj
        )

        datastore_name = self.get_recommended_datastore(
            datastore_cluster_obj=datastore_cluster_obj
        )
        if not datastore_name:
            datastore_name = ""
        result = dict(changed=False, recommended_datastore=datastore_name)
        self.module.exit_json(**result)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datacenter=dict(type="str", required=True),
        datastore_cluster=dict(type="str", required=True),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    VmwareDatastoreClusterInfo(module)


if __name__ == "__main__":
    main()
