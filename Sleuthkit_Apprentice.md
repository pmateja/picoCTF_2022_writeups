# Sleuthkit Apprentice

Download the disk.img file from task, you can also create a temporaty directory for mounting it. We will use **kpartx** for this taks:

```bash
$ mkdir mnt
$ sudo kpartx -v -a disk.flag.img
add map loop2p1 (253:4): 0 204800 linear 7:2 2048
add map loop2p2 (253:5): 0 153600 linear 7:2 206848
add map loop2p3 (253:6): 0 253952 linear 7:2 360448
$ sudo mount /dev/mapper/loop2p3 mnt #  Mount the third partition
$ sudo -s #  may require root privileges for next steps
$ cd mnt/root/my_folder
$ cat flag.uni.txt 
picoCTF{by73_5urf3r_3497ae6b}
$ sudo umount mnt #  cleanup: umount the partition
$ sudo kpartx -d disk.flag.img #  cleanup: delete the partition mappings
```