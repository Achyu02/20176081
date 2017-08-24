import os
class stringM(object):
	def __init__(self,arg):
		self.arg=arg
	def pieces(p1):
		s=""
		l=[]
		for i in range(len(p1)):
			for j in range(i,len(p1)):
					s=s+p1[j]
					l.append(s)
			s=""
		return l
	def combine(l,l1):
		z=[]
		for i in l:
			if i in l1:
				z.append(i)
		#print(z)
		for i in range(len(z)):
			d=z[i]
			c=z[i]
			for j in range(len(z[i])):
				if(c[0]==" "):
					d=d[1:]
				elif(c[len(c)-1]==" "):
					d=d[:len(c)-1]
				elif(c[0]==" "or c[len(c)-1]==" "):
					d=d[:(len(z[i])-1)]+d[1:]
			z[i]=d
		#print("string matching for ",file1,file2,z)
		return z
	def match(z):
		lcs=len(z[0])
		for j in z:
			if(lcs<len(j)):
				#print(j)
				lcs=len(j)
		print(lcs)
		calculation=((lcs*2)/(x+y))*100
		print("String matching for "+str(file1)+ " " +str(file2)+" is "+str(calculation))
		return calculation
obj=stringM(object)
files=[z for z in os.listdir(os.getcwd()) if z.endswith(".txt")]
print(files)
temp=[]
for i in range(len(files)):
        g=[]
        for j in range(len(files)):
                if(i<j):
                        file1=files[i]
                        file2=files[j]
                        p1=open(file1,'r').read().lower()
                        p2=open(file2,'r').read().lower()
                        x=len(p1)
                        y=len(p2)
                        l=stringM.pieces(p1)
                        l1=stringM.pieces(p2)
                        z=stringM.combine(l,l1)
                        m=stringM.match(z)
                        g.append(round(m,2))
                else:
                        g.append(0)
        temp.append(g)
print('\n'.join([' '.join(['{:5}'.format(item) for item in row])  for row in temp]))




			
