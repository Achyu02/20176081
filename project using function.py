import math
l=[]
dic={}
dic2={}
class BagofWords(object):
	"""docstring for BagofWords"""
	def __init__(self, arg):
		super(BagofWords, self).__init__()
		self.arg = arg
	def fileToList(filename,filename2):
		t1=filename.read()
		s1=t1.lower()
		t2=filename2.read()
		s2=t2.lower()
		l1=s1.split()
		l2=s2.split()
		return (l1,l2)
	def freqValues(l1,l2):
		for i in l1:                         #converting l1 to dic and calculating the words
			if i not in dic.keys():
				dic[i]=1
			else:
				dic[i]=dic[i]+1
		for i in l2:
			if i not in dic2.keys():         #converting l1 to dic and calculating the words
				dic2[i]=1
			else:
				dic2[i]=dic2[i]+1
		print("Multiple words count in " +str(filename)+ " is ",dic)
		print("Multiple words count in " +str(filename2)+ " is ",dic2)
		return (dic,dic2)

	def dotProduct(dic,dic2):
		for i in dic.keys():				#appending l1 and l2 and calculating simlar keys
			if i in dic2.keys():
				l.append(dic[i]*dic2[i])
		print(l)
		return l	

	def Euclidean(l):
		p=0
		q=0
		s=0
		for i in dic.values():
			p=p+(i**2)										#for calculating the values of squares ofl1
		p=math.sqrt(p)
		for j in dic2.values():
			q=q+(j**2)								#for calculating the values of squares of l2
		q=math.sqrt(q)
		for i in range(len(l)):
			s=s+l[i]
		result=(s/(p*q))*100
		return result
filename="text1.txt"
filename2="text2.txt"
st1= open(filename,"r")
st2=  open(filename2,"r")
(l1,l2)=BagofWords.fileToList(st1,st2)
(dic,dic2)=BagofWords.freqValues(l1,l2)
l=BagofWords.dotProduct(dic,dic2)
result=BagofWords.Euclidean(l)
print("Plagarism for the two files is ",result)

