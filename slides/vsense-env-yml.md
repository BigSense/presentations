## demo1/environment.yml

```
---
name: demo1
type: run
domain: internal
repository:
  custom: false
  protocol: https
  host: repo.bigsense.io
  stage: nightly
servers:
  bigsense:
    hostname: bigsense-demo1
    os: ubuntu
    ip: 10.11.1.20
  ltsense:
    hostname: ltsense-demo1
    os: ubuntu
    ip: 10.11.1.21
  database:
    hostname: db-demo1
    ip: 10.11.1.22
database:
  type: mysql
  name: bigsense
  username: bigsense
  password: bigsense
  ddl_username: bigsense_ddl
  ddl_password: bigsense_ddl
bigsense:
  security_manager: DisabledSecurityManager
  http_port: 8080
  server: tomcat
```