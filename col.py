# ssh col@pwnable.kr -p2222 (pw:guest)
"""
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}

int main(int argc, char* argv[]){
	if(argc<2){
		printf("usage : %s [passcode]\n", argv[0]);
		return 0;
	}
	if(strlen(argv[1]) != 20){
		printf("passcode length should be 20 bytes\n");
		return 0;
	}

	if(hashcode == check_password( argv[1] )){
		setregid(getegid(), getegid());
		system("/bin/cat flag");
		return 0;
	}
	else
		printf("wrong passcode.\n");
	return 0;
}
"""

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