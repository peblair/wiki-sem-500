#!/usr/bin/env python
#
# Copyright 2016 Basis Technology Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pip
import sys

dependencies = [
    # Word embeddings
    "polyglot==16.7.4",
    # Polyglot peer dependency
    "six==1.10.0"
]

version = sys.version_info

if version[0] < 3 or version[1] < 5:
    dependencies += ["scandir==1.3"]


def install_dependencies():
    for dep in dependencies:
        pip.main(['install', dep])

if __name__ == "__main__":
    install_dependencies()
