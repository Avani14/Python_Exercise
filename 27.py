# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:24:46 2020

@author: AVANI
"""

import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for n in installed_packages_list:
    print(n)