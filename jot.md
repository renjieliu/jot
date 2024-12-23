Entrypoint -             

"Entrypoint": [
    "/opt/mssql/bin/permissions_check.sh"
],


"Cmd": [
                "/bin/sh",
                "-c",
                "/opt/mssql/bin/launchpadd -usens=false -enableOutboundAccess=true -usesameuser=true -sqlGroup root -- -reparentOrphanedDescendants=true -useDefaultLaunchers=false & /app/asdepackage/AsdePackage & /opt/mssql/bin/sqlservr"

"Env": [
    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "MSSQL_RPC_PORT=135",
    "CONFIG_EDGE_BUILD=1",
    "PAL_BOOT_WITH_MINIMAL_CONFIG=1",
    "PAL_ENABLE_PAGE_ALIGNED_PE_FILE_CREATION=1",
    "LD_LIBRARY_PATH=/opt/mssql/lib"
],


line below 
---

~~done~~




```sql
select * from table_xx
```

```python
print('OK')
```





