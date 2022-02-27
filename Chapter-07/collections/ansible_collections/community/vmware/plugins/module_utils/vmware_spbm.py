# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Ansible Project
# Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    from pyVmomi import pbm
    from pyVim.connect import SoapStubAdapter
except ImportError:
    pass

from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi


class SPBM(PyVmomi):
    def __init__(self, module):
        super(SPBM, self).__init__(module)
        self.spbm_content = None
        self.spbm_si = None
        self.version = "pbm.version.version2"

    def get_spbm_connection(self):
        """
        Creates a Service instance for VMware SPBM
        """
        client_stub = self.si._GetStub()
        try:
            session_cookie = client_stub.cookie.split('"')[1]
        except IndexError:
            self.module.fail_json(msg="Failed to get session cookie")
        ssl_context = client_stub.schemeArgs.get('context')
        additional_headers = {'vcSessionCookie': session_cookie}
        hostname = self.module.params['hostname']
        if not hostname:
            self.module.fail_json(msg="Please specify required parameter - hostname")
        stub = SoapStubAdapter(host=hostname, path="/pbm/sdk", version=self.version,
                               sslContext=ssl_context, requestContext=additional_headers)

        self.spbm_si = pbm.ServiceInstance("ServiceInstance", stub)
        self.spbm_content = self.spbm_si.PbmRetrieveServiceContent()

    def find_storage_profile_by_name(self, profile_name):
        storage_profile = None
        self.get_spbm_connection()
        pm = self.spbm_content.profileManager
        profile_ids = pm.PbmQueryProfile(resourceType=pbm.profile.ResourceType(resourceType="STORAGE"),
                                         profileCategory="REQUIREMENT")
        if len(profile_ids) > 0:
            storage_profiles = pm.PbmRetrieveContent(profileIds=profile_ids)
            for profile in storage_profiles:
                if profile.name == profile_name:
                    storage_profile = profile
        else:
            self.module.warn("Unable to get storage profile IDs with STORAGE resource type and REQUIREMENT profile category.")

        return storage_profile
