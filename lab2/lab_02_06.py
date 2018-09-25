a=int(input(), base=16)
b=[]
aout=''
if a<0:
	a=int("FFFFFFFF",base=16)+a+1
while a>0:
	b.append(int(a%16))
	a=a//16

while (len(b))<8:
	b.append(0)
b.reverse()
for i in range(8):
	if b[i]>9:
		print(chr(55+b[i]),end='')
	else:
		print(b[i], end='')
print('')