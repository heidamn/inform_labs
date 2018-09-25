import math
a=list(input('your string '))
a1=''
for i in range (len(a)):
   a[i]=int(ord(a[i]))
a.sort()
for m in range (len(a)):
      a1+=chr(a[m])
print(a1)
a1=''
for i in range(math.factorial(len(a))-1):
   for m in range (len(a)-1):
      if a[m]<a[m+1]:
         j=m
   l=j
   for m in range(j+1, len(a)):
      if a[m]>a[j]:
         l=m
   a[l],a[j]=a[j],a[l]
   b=a[j+1:]
   b.reverse()
   for m in range(j+1, len(a)):
      a[m]=b[m-j-1]
   for m in range (len(a)):
      a1+=chr(a[m])
   print(a1)
   a1=''