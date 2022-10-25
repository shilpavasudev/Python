#TASK THREE DATA STRUCTURES

#1
#list1=[1,3,'elena',1+2j, 4,2,'damon','stefen',22.2,3.4]
#print(list1)

#2
#list2 = [2,3,4,2,4]
#print(list2[1:4:2])

#3
#from operator import mul


#list3 = [1,4,2,3,2,4]
#print(sum(list3))
#print(mul(list3))

#4

#list4 = [5,4,2,3,2,4]
#print(min(list4))
#print(max(list4))

#5

#list5 = [5,4,2,3,2,4,2,7,1,4,2,8,9]
#for num in list5:
#        if num % 2 != 0:
#            print(num,  end =' ')

#6
#list6= list()
#for i in range(1,30):
#		list6.append(i**2)
#print(list6[:5])
#print(list6[-5:])

#7
#list7 = [1,3,5,9,10]
#list8=[2,4,6,8]
#list7[-1:] = list8 ; #or it can be list7[4:] = list8 
#print (list7)

#8
#from operator import concat

#a = {1:10,2:20}
#b = {3:30,4:40}
#c= a.copy()
#c.update(b)
#print(c)

#9
#n=int(input("enter a number "))
#a = dict()
#for x in range(1,n+1):
#    a[x]=x*x
#print(a) 

#10
#a = input('enter some comma seperated numbers')
#list1 = a.split(",")
#tuple1 = tuple(list)
#print('lists are : ',list1)
#print('tuples are : ',tuple1)



#TASK FOUR TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS & HIGHER ORDER FUNCTIONS

#1
#str1 = "1234abcd"
#str2 = str1[::-1]
#print(str2)

#2
#from curses.ascii import isupper

#def function1(str1): 
#    up1 =0
#    low1= 0
#    for i in str1:
#        if i.isupper() :
#            up1 = up1+1
#        elif i.islower():
#            low1 = low1 +1
#    print("upper letters = : ",up1)
#    print("lower letters = :",low1)
#str1 = input("enter a string:  ")
#s1= function1(str1)

#3
#def function2(list1):
#    newlist = []
#    for i in list1:
#        if i not in newlist:
#            newlist.append(i)
#    print(newlist)

#s1= function2([1,2,2,2,3,4,5,5,6,6])

#from functools import reduce
#import operator

#lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
#joinedlist = reduce(operator.add,lists)
 
#print(joinedlist)  

#4

#print("enter some hyphen seperated words:- ")
#result1=[word for word in input().split('-')]
#result1.sort()
#print('-'.join(result1))


#5

#from string import *
#Lines = [] #blanch list
#print("Enter few lines and when done just press enter for blank line")
#while True:
#    Line = input('-')
#    if not Line:
#        break
#    Lines.append(Line.upper())
#print(Lines)


#6
#def function6(num1,num2):
#    sum1 = int(num1) + int(num2)
#    return sum1

#n1,n2 = input("enter two numbers:  ").split()
#s1 = function6(n1,n2)
#print(s1)

#7
#def function7(str1,str2):
#    if len(str1)> len(str2):
#        print("printing string with max lenght: ", str1)
#    elif len(str1)<len(str2):
#        print("printing string with max lenght: ", str2)
#    else:
#        print("both strings have same lenght: ",str1,str2,sep='\n')

#string1,string2=input("enter two strings: ").split()
#function7(string1,string2)



#8

#def function8():
#	l=list()
#	for i in range(1,21):
#		l.append(i**2)
#	print(l) #prints list
#	print(tuple(l))  #prints tuple
        
#function8()


#9

#def Function9(limit):
#	for i in range(0,limit+1):
#		if i % 2 == 0:
#			print(i,"EVEN")
#		else:
#			print(i,"ODD")

#Function9(5)

#10
#def even(num):
#   return num % 2 == 0
#newlist = list(filter(even,range(1,21)))
#print(newlist)

#11
#def evenlist(num):
#	return num % 2 == 0

#newlist = list(filter(evenlist,range(1,21)))
#squarelist = map(lambda x: x**2, newlist)
#print(list(squarelist))

#12
#def division1():
#	try:
#		result = 5/0
#	except ZeroDivisionError:
#		print("number 5 is not divisible by 0")
#	finally:
#		print("anyways this is executed")

#division1()

#13
#from functools import reduce 
#l=reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7,8], 0)
#print(l)


#14

#def function14():
#	result = list (filter (lambda x: (x % 7 == 0 and x % 3 !=0),range(1,100)))
#	return(result)	  
#s1=function14()
#print(s1)


#15

#def function15(n):
#    return n * n

#list1= [1,2,3,4,5]

#result = map(function15,list1)
#print(list(result))


#16 - output of functions:
#1)

#def foo():
#	try:
#		return 1
#	finally: 
#		return 2
#k = foo() 
#print(k)

#result is 2

#2)
#def a(): 
#	try:
#		f(x, 4) 
#	finally:
#		print('after f')
#		print('after f?') 

#a()

#result= NameError: name 'f' is not defined

	    