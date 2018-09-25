cif=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
a=list(input("ваше число "))
aout=''
if a[0]=="-":  
#проверка на знак числа и получение первого бита
#если n <0, то первая цифра F, минус убирается 
	a.insert(a.index('-'),'0')
	a.remove('-')
	while len(a)<7:
		a.insert(0,'0')
	a.insert(0,"F") 
else:
	while len(a)<8:
		a.insert(0,'0')
#обработка отрицательных чисел
if a[0]=='F':				
	for i in range(1,8):
		for j in range(16):
			if a[i]==cif[j]:
				a[i]=cif[15-j]
				break
#добавление 1
	m=7
	while a[m]=="F" and m>=0:
		a[m]='0'
		m-=1
	for j in range(16):
			if a[m]==cif[j]:
				a[m]=cif[j+1]
				break		
for i in range(8):
	aout+=a[i]
print (aout)