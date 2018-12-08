import sys
import re

def decode(str):
	ret=str.decode('hex')
	return ret

def decrypt(x):
	str = (list(x))
	decrypt_str = ''.join(chr(ord(str[i])^3)for i in range(len(str)))
	final_str = decrypt_str.decode('base64')

	return final_str

def deflipper(a):
	y=a[::-1]
	s=list(y)
	dec=''
	for i in range(len(s)):
		if(s[i]=='!' or s[i]=='$' or s[i]=='#' or s[i]=='@' or s[i]=='%' or s[i]=='^' or s[i]=='&' or s[i]=='*' or s[i]=='(' or s[i]==')'):
			continue
		else:
			dec=dec+s[i]
	return dec

if __name__=="__main__":

	file=open(sys.argv[1],'rb')
	inp=file.read()
	new=decode(deflipper(decrypt(inp)))
	print new
	file.close()

