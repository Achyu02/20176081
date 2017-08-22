import math
filename="text1.txt"
filename2="text2.txt"
st1= open(filename,"r")
st2=  open(filename2,"r")
t1=st1.read()
s1=t1.lower()
t2=st2.read()
s2=t2.lower()
l=[]
dic={}
dic2={}
l1=s1.split()
l2=s2.split()
for i in l1:                                        #converting l1 to dic and calculating the words
	if i not in dic.keys():
		dic[i]=1
	else:
		dic[i]=dic[i]+1
for i in l2:
	if i not in dic2.keys():                        #converting l1 to dic and calculating the words
		dic2[i]=1
	else:
		dic2[i]=dic2[i]+1
print(dic)
print(dic2)
for i in dic.keys():							#appending l1 and l2 and calculating simlar keys
	if i in dic2.keys():
		l.append(dic[i]*dic2[i])	
print(l)
p=0
for i in dic.values():
	p=p+(i**2)								#for calculating the values of l1
p=math.sqrt(p)
print(p)
q=0
for j in dic2.values():
	q=q+j**2								#for calculating the values of l2
print(q)
q=math.sqrt(q)
print(q)
print(dic2.values())
s=0
for i in range(len(l)):
	s=s+l[i]
result=(s/(p*q))*100
print(result)

