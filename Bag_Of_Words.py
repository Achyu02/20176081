import math
import re
import os
class BagofWords(object):
	"""docstring for BagofWords"""
	def __init__(self, arg):
		super(BagofWords, self).__init__()
		self.arg = arg
	def fileToList(filename,filename2):
		s1=filename.read().lower()
		l1=re.sub('[^a-z\ \']+',"",s1).split(" ")
		s2=filename2.read().lower()
		l2=re.sub('[^a-z\ \']+',"",s2).split(" ")
		return (l1,l2)
	def freqValues(l1,l2):
		dic,dic2={},{}
		for i in l1:                  #converting l1 to dic and calculating the words
			if i not in dic.keys():
				dic[i]=1
			else:dic[i]=dic[i]+1
		for i in l2:
			if i not in dic2.keys():  #converting l1 to dic and calculating the words
				dic2[i]=1
			else:dic2[i]=dic2[i]+1
		return (dic,dic2)
	def dotProduct(dic,dic2):
		l=[]
		for i in dic.keys():		#appending l1 and l2 and calculating simlar keys
			if i in dic2.keys():
				l.append(dic[i]*dic2[i])
		#print(l)
		return l	
	def Euclidean(l):
		p,q,s=0,0,0
		for i in dic.values():
			p=p+(i**2)				 #for calculating the values of squares ofl1
		p=math.sqrt(p)
		for j in dic2.values():
			q=q+(j**2)				#for calculating the values of squares of l2
		q=math.sqrt(q)
		for i in range(len(l)):
			s=s+l[i]
		result=(s/(p*q))*100
		return result
files_txt=[z for z in (os.listdir(os.getcwd())) if z.endswith('.txt')]
print(files_txt) 
global b
b=[]
temp=[]
for x in range(len(files_txt)):
        g=[]
        for y in range(len(files_txt)):
                if(x<y):
                        filename=files_txt[x]
                        filename2=files_txt[y]
                        st1= open(filename,"r")
                        st2=  open(filename2,"r")
                        (l1,l2)=BagofWords.fileToList(st1,st2)
                        (dic,dic2)=BagofWords.freqValues(l1,l2)
                        l=BagofWords.dotProduct(dic,dic2)
                        result=BagofWords.Euclidean(l)
                        print("Plagarism for the two files is ", filename , filename2,result)
                        b.append(result)
                        g.append(round(result,2))
                        #st1.close()
                        #st2.close()
                else:
                        g.append(0)
             
        temp.append(g)
print(b)
print('\n'.join([' '.join(['{:5}'.format(j) for j in row])  for row in temp]))


	
