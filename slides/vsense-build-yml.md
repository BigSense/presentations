## builder/environment.yml

```
---
name: builder
type: build
domain: internal
servers:
  repository:
    hostname: repo
    ip: 10.11.1.10
  build:
    hostname: build
    ip: 10.11.1.11
    bigsense_src: http://github.com/BigSense/BigSense
    bigsense_tester_src: http://github.com/BigSense/BigSenseTester
    ltsense_src : http://github.com/BigSense/LtSense
pgp:
  key_type: DSA
  key_length: 1024
  subkey_type: ELG-E
  subkey_length: 1024
  name: http://example.org
  comment: BigSensePGPKey
  expire: 0
  passphrase: changeme
scm:
  polling: true
  polling_interval: H/15 * * * *

```