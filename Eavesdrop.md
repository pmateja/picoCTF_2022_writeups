It is pretty easy to find the flag with *Wireshark* by reading tcp streams in **Analyze->Streams**, but we can do the same with *tshark*, the cli version:

```console
[user@host Eavesdrop]$ tshark -r capture.flag.pcap -q -z conv,tcp
================================================================================
TCP Conversations
Filter:<No Filter>
                                                           |       <-      | |       ->      | |     Total     |    Relative    |   Duration   |
                                                           | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
10.0.2.15:57876            <-> 10.0.2.4:9001                   17 1 330bytes      18 1 411bytes      35 2 741bytes    15,175413000       224,2402
10.0.2.15:43928            <-> 35.224.170.84:80                 5 442bytes        5 377bytes       10 819bytes    165,383043000         0,5623
10.0.2.15:56370            <-> 10.0.2.4:9002                    4 272bytes        4 320bytes        8 592bytes    205,301478000        11,8833
================================================================================
```

There are three conversations to read, so lets read them:

```console
user@host Eavesdrop]$ tshark -r capture.flag.pcap -q -z follow,tcp,ascii,0

===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 0
Node 0: 10.0.2.15:57876
Node 1: 10.0.2.4:9001
        41
Hey, how do you decrypt this file again?

16
You're serious?

        18
Yeah, I'm serious

83
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123

        19
Ok, great, thanks.

47
Let's use Discord next time, it's more secure.

        51
C'mon, no one knows we use this program like this!

10
Whatever.

        5
Hey.

6
Yeah?

        41
Could you transfer the file to me again?

25
Oh great. Ok, over 9002?

        17
Yeah, listening.

8
Sent it

        8
Got it.

20
You're unbelievable

===================================================================
```

```console
[user@host Eavesdrop]$ tshark -r capture.flag.pcap -q -z follow,tcp,ascii,1

===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 1
Node 0: 10.0.2.15:43928
Node 1: 35.224.170.84:80
87
GET / HTTP/1.1
Host: connectivity-check.ubuntu.com
Accept: */*
Connection: close


        148
HTTP/1.1 204 No Content
Date: Mon, 04 Oct 2021 18:08:52 GMT
Server: Apache/2.4.18 (Ubuntu)
X-NetworkManager-Status: online
Connection: close


===================================================================
```

```console
[user@host Eavesdrop]$ tshark -r capture.flag.pcap -q -z follow,tcp,ascii,2

===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 2
Node 0: 10.0.2.15:56370
Node 1: 10.0.2.4:9002
48
Salted__............=a.....Z..........F8..v.<8EY
===================================================================
```

We can skip the second one, because it does not contain anything interesting. The first one shows us a literal conversation with a cool command and credentials included. The third is a secret to decrypt.

So we have to save the secret properly, because the **ascii** output of thark is replacing non-printable characters with dots. We will use the **raw** option with some pipes to remove obsolete text and transform the message to real raw data:

```console
[user@host Eavesdrop]$ tshark -r capture.flag.pcap -q -z follow,tcp,raw,2 | tail -n +7 | head -n 1 | xxd -r -p > secret 
```

Last step, decryption:

```console
[user@host Eavesdrop]$ openssl des3 -d -salt -in secret  -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
picoCTF{nc_73115_411_5786acc3}[user@host Eavesdrop]$ 
```
