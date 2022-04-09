Install image as loops and mount the third one:

```console
[user@host Operation Oni]$ sudo kpartx -a -v disk.img 
add map loop19p1 (253:22): 0 204800 linear 7:19 2048
add map loop19p2 (253:23): 0 264192 linear 7:19 206848
[user@host Operation Oni]$ sudo mount /dev/mapper/loop19p2 mnt/
```

Enumerate the root directory. There is a *.ssh* directory with key, that we need: 

```console
[user@host Operation Oni]$ cd mnt/root
[user@host Operation Oni]$ ls -la
razem 4
drwx------  3 root root 1024 paź  6  2021 .
drwxr-xr-x 21 root root 1024 paź  6  2021 ..
-rw-------  1 root root   36 paź  6  2021 .ash_history
drwx------  2 root root 1024 paź  6  2021 .ssh
[user@host root]$  cd .ssh 
[user@host .ssh]$  ls
id_ed25519  id_ed25519.pub
```

Use it to get the flag:

```console
[user@host .ssh]$  ssh -i ./id_ed25519 -p 53334 ctf-player@saturn.picoctf.net  
The authenticity of host '[saturn.picoctf.net]:53334 ([18.217.86.78]:53334)' can't be established.
ECDSA key fingerprint is SHA256:0L/+wJ14/Sk4s6Ue+TxXnAW7qNBuaMeIxA9dXp2zzaU.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:53334,[18.217.86.78]:53334' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1021-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat 
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_b5066e83}ctf-player@challenge:~$ logout
Connection to saturn.picoctf.net closed.
```

Cleanup:

```console
[user@host .ssh]$ cd ../../../
[user@host Operation Oni]$ umount mnt 
[user@host Operation Oni]$ sudo kpartx -d disk.img 
loop deleted : /dev/loop19
```
