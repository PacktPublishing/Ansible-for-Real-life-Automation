#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright, (c) 2018, Ansible Project
# Copyright, (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_custom_attributes
short_description: Manage custom attributes from VMware for the given virtual machine
description:
    - This module can be used to add, remove and update custom attributes for the given virtual machine.
author:
    - Jimmy Conner (@cigamit)
    - Abhijeet Kasurde (@Akasurde)
notes:
    - Tested on vSphere 6.5
requirements:
    - "python >= 2.6"
    - PyVmomi
options:
   name:
     description:
     - Name of the virtual machine to work with.
     - This is required parameter, if C(uuid) or C(moid) is not supplied.
     type: str
   state:
     description:
     - The action to take.
     - If set to C(present), then custom attribute is added or updated.
     - If set to C(absent), then custom attribute is removed.
     default: 'present'
     choices: ['present', 'absent']
     type: str
   uuid:
     description:
     - UUID of the virtual machine to manage if known. This is VMware's unique identifier.
     - This is required parameter, if C(name) or C(moid) is not supplied.
     type: str
   moid:
     description:
     - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
     - This is required if C(name) or C(uuid) is not supplied.
     type: str
   use_instance_uuid:
     description:
     - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
   folder:
     description:
     - Absolute path to find an existing guest.
     - This is required parameter, if C(name) is supplied and multiple virtual machines with same name are found.
     type: str
   datacenter:
     description:
     - Datacenter name where the virtual machine is located in.
     type: str
   attributes:
     description:
     - A list of name and value of custom attributes that needs to be manage.
     - Value of custom attribute is not required and will be ignored, if C(state) is set to C(absent).
     suboptions:
        name:
          description:
          - Name of the attribute.
          type: str
          required: True
        value:
          description:
          - Value of the attribute.
          type: str
          default: ''
     default: []
     type: list
     elements: dict
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
  delegate_to: localhost
  register: attributes

- name: Add multiple virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
      - name: MyAttribute2
        value: MyValue2
  delegate_to: localhost
  register: attributes

- name: Remove virtual machine Attribute
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes

- name: Remove virtual machine Attribute using Virtual Machine MoID
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    moid: vm-42
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes
'''

RETURN = r'''
custom_attributes:
    description: metadata about the virtual machine attributes
    returned: always
    type: dict
    sample: {
        "mycustom": "my_custom_value",
        "mycustom_2": "my_custom_value_2",
        "sample_1": "sample_1_value",
        "sample_2": "sample_2_value",
        "sample_3": "sample_3_value"
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec


class VmAttributeManager(PyVmomi):
    def __init__(self, module):
        super(VmAttributeManager, self).__init__(module)

    def set_custom_field(self, vm, user_fields):
        result_fields = dict()
        change_list = list()
        changed = False

        for field in user_fields:
            field_key = self.check_exists(field['name'])
            found = False
            field_value = field.get('value', '')

            for k, v in [(x.name, v.value) for x in self.custom_field_mgr for v in vm.customValue if x.key == v.key]:
                if k == field['name']:
                    found = True
                    if v != field_value:
                        if not self.module.check_mode:
                            self.content.customFieldsManager.SetField(entity=vm, key=field_key.key, value=field_value)
                            result_fields[k] = field_value
                        change_list.append(True)
            if not found and field_value != "":
                if not field_key and not self.module.check_mode:
                    field_key = self.content.customFieldsManager.AddFieldDefinition(name=field['name'], moType=vim.VirtualMachine)
                change_list.append(True)
                if not self.module.check_mode:
                    self.content.customFieldsManager.SetField(entity=vm, key=field_key.key, value=field_value)
                result_fields[field['name']] = field_value

        if any(change_list):
            changed = True

        return {'changed': changed, 'failed': False, 'custom_attributes': result_fields}

    def check_exists(self, field):
        for x in self.custom_field_mgr:
            # The custom attribute should be either global (managedObjectType == None) or VM specific
            if x.managedObjectType in (None, vim.VirtualMachine) and x.name == field:
                return x
        return False


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str'),
        name=dict(type='str'),
        folder=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        state=dict(type='str', default='present',
                   choices=['absent', 'present']),
        attributes=dict(
            type='list',
            default=[],
            elements='dict',
            options=dict(
                name=dict(type='str', required=True),
                value=dict(type='str', default=''),
            )
        ),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['name', 'uuid', 'moid']
        ],
    )

    if module.params.get('folder'):
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    pyv = VmAttributeManager(module)
    results = {'changed': False, 'failed': False, 'instance': dict()}

    # Check if the virtual machine exists before continuing
    vm = pyv.get_vm()

    if vm:
        # virtual machine already exists
        if module.params['state'] == "present":
            results = pyv.set_custom_field(vm, module.params['attributes'])
        elif module.params['state'] == "absent":
            results = pyv.set_custom_field(vm, module.params['attributes'])
        module.exit_json(**results)
    else:
        # virtual machine does not exists
        vm_id = (module.params.get('name') or module.params.get('uuid') or module.params.get('moid'))
        module.fail_json(msg="Unable to manage custom attributes for non-existing"
                             " virtual machine %s" % vm_id)


if __name__ == '__main__':
    main()
