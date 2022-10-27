#TASK FIVE FILE HANDLING AND EXCEPTION HANDLING

#1
#try:
#    eval("sum = a+b")
#except SyntaxError:
#    print("syntax error is accepted")
#finally:
#    print("this line is printed anyway")

#2
#import sys

#print("given arguments are ",sys.argv)
#print("lenght of the command line arguments are ",len(sys.argv))
#try:
#    with open(sys.argv[1], 'r') as f:
#        print(f.read())
#except FileNotFoundError:
#    print("enter the file name again in arguments")
#finally:
#    print("this line is printed anyway")

# my command line arguments given for test are 
# test1
# input is: python3 task5andtask6.py doc.txt 
#and output is :given arguments are  ['task5andtask6.py', 'doc.txt']
#lenght of the command line arguments are  2
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#this line is printed anyway

#and test2:
#input is=python3 task5andtask6.py dffc.txt
#output is :given arguments are  ['task5andtask6.py', 'dffc.txt']
#lenght of the command line arguments are  2
#enter the file name again in arguments
#this line is printed anyway


#3

#try: 
#    number = int(input("Type in a number with four digits: "))
#except ValueError:
#    print("wrong value ")
#if number > 9999 or number < 1000:
#    print("The length is too short/long !!! Please provide only four digits")
#    number = int(input("Type in a number with four digits again: "))
#else:
#    print(number)

#import sys
#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , str(sys.argv))


#4
#print("Enter the username and password")
#count=0
#while count < 3:
#    username = input("Enter username: ")
#    password = input("Enter password: ")
#    if password=="WORKSan12" and username=="testpython":
#        print("logged in proceed")
#        break
#    else:
#        print("wrong id or password,please try again")
#        count += 1


#6
#with open("doc.txt", "w") as f:
#    line1 = "Hello I am a file\n"
#    line2 = "Where you need to return the data string\n"
#    line3 = "Which is of even length"
#    f.writelines([line1 +line2 +line3])

#with open("doc.txt", "r") as f:
#    data = f.read()
#     print(data)
#    newdata = data.split()
#    print(newdata)
#    for i in newdata:
#        if len(i) % 2 == 0:
#            print(i)


#TASK SIX GENERATORS, LIST COMPREHENSION AND DECORATORS

#1
#str1 ="PythonAssignmentTaskS"
#print("the original line is : ", str1)
#extract = [i for i in str1 if i.isupper()]
#print("The uppercase chars in the string is : " , extract)


#2 using zip
#studentlist = ["Eleven","max","will","Mike"]
#sublist = ["english","maths","science","physics"]

#dict1 = dict(zip(studentlist, sublist))
#print("dictionary values are : ", dict1)


#for method:
#studentlist = ["Eleven","max","will","Mike"]
#sublist = ["english","maths","science","physics"]
#dict1 = { }
#for i in studentlist:
#    for j in sublist:
#        dict1[i]= j
#        sublist.remove(j)
#        break
#print("dictionary values are : ", dict1)

#4
#def function4(str1):
#    length =len(str1)
#    for i in range(length-1,-1,-1):
#        yield str1[i]
#for i in function4("ConsultAdd Training"):
#    print(i)

#5 example of decorator
#def function1():
#    print("hello world")

#def decorator_fun(func):
#    def inner():
#        print("displaying before execution", func.__name__)
#        func()
#        print("displaying after execution")
#    return inner
#function3 = decorator_fun(function1)
#function3()

#with @ 
#def decorator_fun(func):
#    def inner():
#        print("displaying before execution", func.__name__)
#        func()
#        print("displaying after execution")
#    return inner
#@decorator_fun # using @
#def function1():
#    print("hello world")









