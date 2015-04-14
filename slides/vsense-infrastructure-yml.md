## core/environment.yml

```
---
name: core
type: infrastructure
domain: internal
ext_gq: 10.42.7.1
servers:
  haproxy:
    hostname: haproxy
    ip: 10.11.2.10
    ext_iface: eth1
    ext_ip: 10.22.2.10
  wiki:
    hostname: wiki
    ip: 10.22.2.12
confluence:
  version: 5.6.6
  db_name: confluence
  db_user: confluence
  db_pass: wikipass
haproxy:
  vhosts:
    - { subdomain: repo , ip: 10.11.1.10 , port: 80 }
    - { ip: 10.22.2.12 , port: 8090 }
```