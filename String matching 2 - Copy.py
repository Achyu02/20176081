import os
class stringM(object):
	'''
	class stringM consists of multiple methods used to calculate plagiarism 

	for multiple files

	'''
	def __init__(self,arg):
		'''Initializer automatically calls when you create a new instance of class'''
		self.arg=arg
	def pieces(p1):
		'''
	Input : files 

	functionality : appends the multiple string permutations to list

	output : returns the list

		'''
		s=""
		l=[]
		for i in range(len(p1)):
			s=''
			for j in range(i,len(p1)):
					s=s+p1[j]
					l.append(s)
		return l
	def combine(l,l1):
		'''
	Input : two lists

	Functionality : Appends the similar values to the list and removes

					spaces front and end of the values

	Output : List

		'''
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
obj=stringM(object)
path=input("Enter the path")
fils=os.chdir(path)
files=[z for z in (os.listdir()) if z.endswith(".txt")]
print(files)
li=[]
temp=[]
li.append('filenames')
for i in files:
	li.append(i)
temp.append(li)
for k in range(len(files)):
	g=[]
	g.append(files[k])
	for j in range(len(files)):
		if(k==j):
			g.append(0)
		else:
			file1=files[k]
			file2=files[j]
			p1=open(file1,'r').read().lower()
			p2=open(file2,'r').read().lower()
			x=len(p1)
			y=len(p2)
			l=stringM.pieces(p1)
			l1=stringM.pieces(p2)
			if(len(l)==0 and len(l1)==0):
				g.append(100)
			else:
				z=stringM.combine(l,l1)
				l2=[]
				for p in z:
					l2.append(len(p))
				if len(l2)==0:
					g.append(0)
				else:
					m=max(l2)
					#print(m)
					calculation=((m*2)/(x+y))*100
					g.append(round(calculation,2))
			#file1.close()
			#file2.close()
	temp.append(g)
print('\n'.join(['  '.join(['{:8}'.format(y1) for y1 in row])  for row in temp]))
