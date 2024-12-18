This is the end to end process to make the Azure SQL Edge run on the Android phone, without docker.

### Prerequisite

1. Root the phone, for me, I am following below instruction 

[---->> Unlock Motorola G Power (2024) <<----](https://www.reddit.com/r/androidroot/comments/1eoqlk1/comment/lhr9iw0/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

2. Install Termux


### 1. To prepare the docker image - 


``` 
docker pull mcr.microsoft.com/azure-sql-edge
``` 

```
pip install docker-squash
```

```
docker-squash -t squashed_image:tag mcr.microsoft.com/azure-sql-edge:latest
```

To get the ENTRYPOINT and CMD, notedown the `COMMAND`, this will be the one to execute in the chroot
Also note down all the environement setups. `ENV`

```
docker inspect squashed_image:tag
```

```
docker save -o squashed.tar squashed_image:tag
```

```
tar xvf squashed.tar
```

Find the largest file, and rename it

```
mv the_largest_file_name main_layer_file.tar
```

### 2. Copy the tar file onto the phone

**Inside Termux**

```
termux-setup-storage
```

If copied onto the internal storage, it should be visible in below location

```
ls -al /storage/emulated/0/
```

If copied onto the MicroSD card, it should be visible in below location 

```
ls -al ~/storage/external-xx
```

```
cd ~
```

```
mkdir my_chroot
```

```
tar xf main_layer_file.tar -C 'my_chroot' >output.txt 2>&1
```

### 3. Install Termux on the Phone, and prepare the chroot environment
**Inside Termux**

```
pkg update
```

```
pkg install tsu
```

```
su
```

```
unset LD_PRELOAD
```

```
mount -t proc /proc my_chroot/proc
```

```
mount --rbind /dev my_chroot/dev
```

```
chroot ./my_chroot /bin/bash
```
Once inside the chroot environment, first is to export the `ENV` as noted in the step 1. 

For me, it's something like below

```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin 
export MSSQL_RPC_PORT=135 
export CONFIG_EDGE_BUILD=1 
export PAL_BOOT_WITH_MINIMAL_CONFIG=1 
export PAL_ENABLE_PAGE_ALIGNED_PE_FILE_CREATION=1 
and so on ...

```

Finally, is to execute the `COMMAND`, from ENTRYPOINT and CMD, as mentioned in step 1 


