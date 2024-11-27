# Azure SQL Edge on Android through QEMU

Recently, I am working on a pet project, the goal is to have an Azure SQL Edge docker running on an Android device.

Below are the steps I have taken

### On the Host - Android, Termux

* Install termux on android
  * Within termux, install qemu packages
 
* Download alpine linux x86-64 image, start VM with qemu
  * Create a folder `myfolder_On_Termux_MicroSD`, for the guest OS to use
  * Create a sparse file with `qemu-img create -f qcow2 alpine.qcow2 20G`, this will serve as the disk for the guest OS to use.
  * Starting the QEMU VM with below command - 
  ```
    qemu-system-x86_64 -m 2048 \
				   -smp 4 \
				   -netdev user,id=n1,hostfwd=tcp::2222-:22,hostfwd=tcp::1434-:1434 \
				   -device virtio-net,netdev=n1 \
				   -nographic \
				   -drive file=alpine_x86_64.qcow2,format=qcow2,if=virtio \
				   -virtfs local,path=my_folder_for_alpine,mount_tag=myfolder_On_Termux_MicroSD,security_model=passthrough
  ```

  *  The keypart of the command is below - 
     *  `-m 2048 `--> this assigns 2048M to the guest OS
     *  `-smp 4` --> Symmetric Multi-Processing, allocates 4 CPUs for the guest OS
     *  `hostfwd=tcp::2222-:22` --> forward 2222 on the host to guest for SSH
     *  `hostfwd=tcp::1434-:1434` --> forward 1434 from the host to guest, for Azure SQL
     *  `-virtfs local,path=my_folder_for_alpine,mount_tag=myfolder_On_Termux_MicroSD,security_model=passthrough` --> this will ask QEMU to start a 9p server, which will allow the guest OS to mount the folder specified as the mount_tag.

<br>

### On the Guest OS

* Within VM, install docker on alpine Linux
  * apk add nano 
  * Add a startup script, and added into crontab with @reboot, so the I will have my customized startup script. 
    * Since this is a VM without KVM support, I am adding sleep 100 to the script, to make sure all the dependencies are ready. <br> `@reboot sleep 100 && sh /root/Share/start.sh`
  * Mount the folder with the mount_tag, as specified during the qemu starting
  <br>
  `mount -t 9p -o trans=virtio,version=9p2000.L myfolder_On_Termux_MicroSD /mnt`
  
* Get the Azure SQL Edge image from microsoft on docker hub
  * Start with below command <br> 
  `docker run --user $(id -u):$(id -g) -e 'ACCEPT_EULA=Y' -e 'ACCEPT_EULA_ML=Y' -e 'MSSQL_SA_PASSWORD=xxxxxxx' -p 1434:1433 -v /mnt/azsql/data:/var/opt/mssql/data -v /mnt/azsql/log:/var/opt/mssql/log -v /mnt/azsql/secrets:/var/opt/mssql/secrets -d mcr.microsoft.com/azure-sql-edge `

  * Explanation - 
    * `--user $(id -u):$(id -g)` to run the docker container as current user, to make sure it can access (read and write) the mounted folder
    * `-p 1434:1433` port mapping

### Takeaways from this practice

1. Since Android does not have KVM enabled, QEMU cannot directly use CPU virtualization. It will emulate all the hardware when the VM is running. Even if the Guest OS is in aarch64 format as well.

2. QEMU is truly amazing, just thinking about the amount of work it's doing, is already mindblowing. Hats off to the engineers behind it.

3. I have been trying to get an Azure SQL Edge server to run on an Android device for quite a while. But always trying to have docker container running directly on Android/Termux, but no avail, as cgroups/KVMs are not enabled. This time, I am changing the approach, by just make it work, regardless of the performance.

4. Now I understand the important thing is to make the thing work first, during this journey, I can learn a lot of Linux things, even it's just a virtual machine, which I don't have to compile and do some heavy lifting myself.







 

