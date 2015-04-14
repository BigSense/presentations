## vSense/virtual-env/vsense.yml 

```
---
environments:
- name: build
  type: build
- name: org
  type: infrastructure
- name: gls
  type: run
security:
  pgp_id: 7ACLOZ8Y
boxes:
  ubuntu: baremettle/ubuntu-14.04
  debian: zauberpony/wheezy
  centos: hansode/centos-7.0.1406-x86_64
  opensuse: alchemy/opensuse-13.2-64

```