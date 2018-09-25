a=int(input(), base=12)
b=[]
mi=False
if a<0:
	a*=-1
	mi=True
while a>0:
	b.append(int(a%14))
	a=a//14
b.reverse()
if mi==True:
	print('-', end='')
for i in range(len(b)):
	if b[i]>9:
		print(chr(55+b[i]),end='')
	else:
		print(b[i], end='')
print('')