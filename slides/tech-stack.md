## Technology Stack

- BigSense Web service written in Scala
  - embedded Tomcat/Jetty
- LtSense Client written in Python
  - Queue system for unreliable networks
  - Multi-format support (XML, JSON)
  - Support for 1-Wire sensors via One Wire File System (OWFS)
  - Support for Phidgets (vendor supplied python wrappers)
- vSense Virtual Environment written in Ruby
  - Vagrant, Ansible
- Originally packaged for OpenWRT
- Currently packaged for Ubuntu 14, Debian 7/8, CentOS 7 and openSUSE 13
