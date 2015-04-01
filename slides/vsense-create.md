## vSense

```
./vsense create
Usage: vsense create [-f <fixture>] [-e <env_type>] [-b <build_env>] [-d <db>] [-o <os>] [-s <stage>] <environment name>
    -f, --fixtures FIXTURE           Install fixtures (gls)
    -e, --env ENVIRONMENT            Environment type (build|run|infrastructure) [default: run]
    -d, --database DATABASE          Database backend (mysql|postgres|mssql)
    -o, --os RUN_OS                  Runtime OS/distribution (ubuntu|debian|centos|opensuse) [default: ubuntu]
    -s, --stage STAGE                Stage (nightly|testing|stable) [default: stable]
    -b, --build BUILD                Use a local build environment [default: use official bigsense.io]
    -h, --help                       Show this message

```