# Sleuthkit Intro

Download the disk.img file from task. Ensure, that you have this tool http://www.sleuthkit.org/sleuthkit/man/mmls.html installed:

```bash
apt-get install sleuthkit
```

Then:

```bash
mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```

We see everything that we needed, so it is time to get the flag:

```bash
nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```

