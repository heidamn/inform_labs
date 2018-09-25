
n=input()
s=[]
raz=0
s1=[]
m=0
for i in range(len(n)):
	s.append(n[i])
for i in range(10**(len(n)-1),10**len(n)):
	i1=i
	while (i1>0):
		cifra=i1%10
		s1.append(cifra)
		i1=i1//10
	for j in range (len(s1)):
		if s1[j]<len(s1):
			m+=1
	if m==len(s1):
		for j in range (len(s1)):	
			print(s[s1[j]], end="")	
		print("")

	
	s1=[]
	m=0