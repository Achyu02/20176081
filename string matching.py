
#p1="what is your name"
#p2="my name is xyz"
p1="To be or not to be"
p2="Doubt truth to be a liar"
x=len(p1)
y=len(p2)
p1=p1.lower()
p2=p2.lower()
s1=p1.split()
s2=p2.split()
print(s1)
print(s2)
lcs=1
for i in range(len(s1)):
	for j in range(len(s2)):
		c=0
		if(len(s1[i]))==len(s2[j]):
			for p in s1[i]:
				for q in s2[j]:
					if(p==q):
						c=c+1
			if(c==len(s1[i])):lcs=lcs*c
print(lcs)
den=x+y
matching=(lcs/den)*100
print(matching)
