## Environment (ansible)


```
---
- name: BigSense Server
  hosts: bigsense
  sudo: true
  vars_files:
    - ../environment.yml
  roles:
   - security
   - { role: build-host, when: repository.custom == true }
   - bigsense
```