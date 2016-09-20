#
# Copyright 2018 Cloudbase Solutions SRL
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys

import cotyledon
from oslo_service import service as os_service


if sys.platform != 'win32':
    ServiceBase = cotyledon.Service
else:
    class ServiceBase(os_service.Service):
        def __init__(self, worker_id=0):
            self.started = False
            super(ServiceBase, self).__init__()

        def start(self):
            self.started = True
            super(ServiceBase, self).start()
