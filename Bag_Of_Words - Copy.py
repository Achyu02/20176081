import math
import re
import os
class BagofWords(object):
        '''
        BagofWords class contains multiple methods used to calculate plagiarism of

        multiple files

        '''

        def __init__(self, arg):
                '''
        It is an initializer and is automatically called when you create a 
        new instance of class
                '''
                super(BagofWords, self).__init__()
                self.arg = arg

        def fileToList(filename,filename2):
                '''
        Input : It takes two files as input

        funtionality : It reads the string in files and removes the delimiters from strings

        Output : Returns two lists and files containing strings

                '''
                s1=filename.read().lower()
                l1=re.sub('[^a-z\ \']+',"",s1).split(" ")
                s2=filename2.read().lower()
                l2=re.sub('[^a-z\ \']+',"",s2).split(" ")
                return (l1,l2,s1,s2)
        def freqValues(l1,l2):
                '''
        Input : two files converting to lists l1 and l2 are taken as input for 

                freqValues method

        Functionality : Converts list to dictionary and calculate the multiple words in list

        Output : converted values stored in dictionary for two files d1 ad d2 are returned

                '''

                dic,dic2={},{}
                for i in l1:                  
                        if i not in dic.keys():
                                dic[i]=1
                        else:dic[i]=dic[i]+1
                for i in l2:
                        if i not in dic2.keys():  
                                dic2[i]=1
                        else:dic2[i]=dic2[i]+1
                return (dic,dic2)
        def dotProduct(dic,dic2):
                ''' 
        Input : Dictionary values of multiple values are given as input

        functionality : frequencies of two dictionaries vector product are calculated

        output : Returns list containing frequencies

                '''
                l=[]
                for i in dic.keys():            
                        if i in dic2.keys():
                                l.append(dic[i]*dic2[i])
                #print(l)
                return l        
        def Euclidean(l,dic,dic2):
                '''
        Input : list and dic values are taken as input

        Functionality : Calculation of vector product and matching percentage is

                         calcualted 
                
        Output : Returns calculated result value     
                '''
                p,q,s=0,0,0
                for i in dic.values():
                        p=p+(i**2)                              
                p=math.sqrt(p)
                for j in dic2.values():
                        q=q+(j**2)                              
                q=math.sqrt(q)
                for i in range(len(l)):
                        s=s+l[i]
                result=(s/(p*q))*100
                return result

path=input("Enter the path")
files=os.chdir(path)
files_txt=[z for z in (os.listdir()) if z.endswith('.txt')]
print(files_txt) 
temp=[]
li=[]
li.append('filename')
for i in files_txt:
        li.append(i)
temp.append(li)
for x in range(len(files_txt)):
        g=[]
        g.append(files_txt[x])
        for y in range(len(files_txt)):
                if x==y:
                        g.append(0)
                else:
                        filename=files_txt[x]
                        filename2=files_txt[y]
                        st1= open(filename,"r")
                        st2=  open(filename2,"r")
                        (l1,l2,s1,s2)=BagofWords.fileToList(st1,st2)
                        (dic,dic2)=BagofWords.freqValues(l1,l2)
                        len1=len(s1)
                        len2=len(s2)
                        if len1=="" and len2=="":
                                g.append(100)
                        else:
                                l=BagofWords.dotProduct(dic,dic2)
                                result=BagofWords.Euclidean(l,dic,dic2)
                                #print("Plagarism for the two files is ", filename , filename2,result)
                                g.append(round(result,2))
                        st1.close()
                        st2.close()
             
        temp.append(g)
print('\n'.join(['  '.join(['{:8}'.format(j) for j in row])  for row in temp]))


        
