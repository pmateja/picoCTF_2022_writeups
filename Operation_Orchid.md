Lets start with mounting the img file:

```console
[user@host Operation Orchid]$ sudo kpartx -a -v disk.flag.img
[sudo] hasło użytkownika user: 
add map loop18p1 (253:19): 0 204800 linear 7:18 2048
add map loop18p2 (253:20): 0 204800 linear 7:18 206848
add map loop18p3 (253:21): 0 407552 linear 7:18 411648
[user@host Operation Orchid]$ sudo mount /dev/mapper/loop18p3 mnt
```

Now we want to do quick enumeration. All we need is _.hidden_ in root dir:

```console
[user@host Operation Orchid]$ sudo -s
root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid# cd mnt/root/
root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid/mnt/root# ls -la
razem 4
drwx------  2 root root 1024 paź  6  2021 .
drwxr-xr-x 22 root root 1024 paź  6  2021 ..
-rw-------  1 root root  202 paź  6  2021 .ash_history
-rw-r--r--  1 root root   64 paź  6  2021 flag.txt.enc
root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid/mnt/root# cat .ash_history 
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid/mnt/root# cat flag.txt.enc 
Salted__A��)o�B�Aq��ncb���#�>=D� /� >4Z�������Ȥ7� ���؎$�'%root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid/mnt/root# 
```
In history file we see the whole operation used to encrypt flag. All we need now to do is reverse it:

```console
root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid/mnt/root# openssl aes256 -d --in flag.txt.enc -k unbreakablepassword1234567
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
140289917540160:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:../crypto/evp/evp_enc.c:610:
picoCTF{h4un71ng_p457_0a710765}root@host:/home/user/Hacking/ctf/PicoCTF2022/Operation Orchid/mnt/root# 
```

Final cleanup:

```console
[user@host Operation Orchid]$ sudo umount mnt/
[user@host Operation Orchid]$ sudo kpartx -d disk.flag.img

```
