#!/usr/bin/env python
import os
import platform

opsys = list(platform.linux_distribution())[0]

if opsys == "Ubuntu":
 print("OS detected as Ubuntu")
 os.system('curl -s https://raw.githubusercontent.com/amitsdalal/getdocker/install_docker_ubuntu.sh | bash')
elif opsys == "CentOS Linux":
 print("OS Detected as CentOS7")
 os.system('curl -s https://raw.githubusercontent.com/amitsdalal/getdocker/install_docker_centos7.sh | bash')
else:
 print('Not detected as Ubuntu or CentOS')
 os.system('exit 1')