#!/usr/bin/python -tt

# Trick here is to use the tranlate mthd and maketrans fn it 
# can be done easily by gettin ascii and converting but this is a 'pythonic'
# way!!!

import sys
from string import maketrans

def main():
	secret = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
	amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q 
	ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
	lmu ynnjw ml rfc spj'''
	secret_url = "http://www.pythonchallenge.com/pc/def/map.html"
	

	intab = "abcdefghijklmnopqrstuvwxyz"
	outtab = "cdefghijklmnopqrstuvwxyzab"
	print secret.translate(maketrans(intab, outtab))
	print secret_url.translate(maketrans(intab, outtab))
	print "Now apply the characters between /...jvon from above line"

if __name__ == '__main__':
	main()
