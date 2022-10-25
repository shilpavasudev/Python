#TASK 1 NUMBERS AND VARIABLES

#1

#a ,b ,c = 12, 15.20 , 'Lene'
#print( a,b,c)

#2

#x,y = 5+2j, 5
#print(x,y)
#x,y = y,x
#print(x,y)

#3
#x,y= 4,5
#print("before swap", x,y)
#temp = x
#x=y
#y=temp
#print("after swap" , x,y)

#a = 4
#b = 5
#print("before swap",a,b)
#a, b = b, a
#print("after swap",a,b)

#5
#x,y = input('Enter the numbers between 1-10 :  ').split()
#z= int(x) + int(y)
#a= 30+ z
#print('the final sum is ' , a)

#6
#a = int(input('enter a value : ' ))
#print( 'the type of entered value is : ',type(a))
#b = input('enter a value : ' )
#print( 'the type of entered value is : ',type(b))

#7
#from re import sub
#a= input('enter a name : ')
#print(a.upper())
#a = sub(r"(_|-)+", " ", a).title().replace(" ", "")
#print(''.join([a[0].upper(), a[1:]]))
#a = sub(r"(_|-)+", " ", a).title().replace(" ", "")
#print(''.join([a[0].lower(), a[1:]]))

#8
#a=10
#a=23
#print(a) - the value is overwritten by the new value

#task from the class day 2
#l1=[1,2,2,4,3,5,2,4,1,6,4,9,5]
#even =[]
#odd =[]
#for i in l1:
#    if(i%2) == 0:
#        even.append(i)
#    else:
#         odd.append(i)

#print('its a even list', even)
#print('its a odd list ', odd)


#Assignement on Operations and decision making#

#1
#inp = int(input("enter a number to check : "))
#if inp%3 == 0  and inp%5 == 0:
#        print ("Consultadd-Python training")
#elif inp%3 == 0:
#        print("Consultadd")
#elif inp%5 == 0:
#        print("Python Training")

#2

#from audioop import avg
#a = int(input("Choose an operation from below : \n 1 = Addition \n 2 = Subtraction \n 3 = Division \n 4 = Multiplication \n 5 = Average \n : "))

#if (a == 1 or a== 2 or a == 3 or a == 4 or a == 5):

#     num1,num2 = ([int(i) for i in input("Enter two values : ").split()])

#if a == 5: 
#    num3,num4 = ([int(i) for i in input("Enter two more values : ").split()])


#if a == 1:
#    c = num1 + num2
#elif a == 2:
#    c = num1 - num2
#elif a == 3:
#    c = float(num1/num2)
#elif a == 4:
#    c = num1 * num2
#if a == 5 :
#   sum = num1 + num2 + num3 +num4
#   c = (sum/4)

#if int(c) >= 0:
#   print (" the output is : " ,c)
#else:
#   print ("Nagative" , c)


#3

#a = 10
#b = 20
#c = 30
#avg = (a+b+c)/3
#print("avg = ",avg)
#if avg > a and avg > b and avg > c:
#   print("avg is highrt than a,b,c ")
#elif avg > a and avg > b:
#   print( " avg is higher than a,b ")
#elif avg > a and avg > c:
#   print( " avg is higher than a,c ")
#elif avg > b and avg > c:
#   print( " avg is higher than b,c ")
#elif avg > a:
#   print( " avg is just higher than a ")
#elif avg > b:
#   print( " avg is just higher than b ")
#elif avg > c:
#   print( " avg is just higher than c ")




#4

#a= float(input(" Enter the number : "))
#for i in range (5):
#   if (a < 0):
#      print("Its over")
#      break
#   else :
#      print("Good Going")
#      a= float(input(" Enter new number : "))
#      continue

#5
#for i in range(2000,3200,1):
#   if i % 7 == 0 and i % 5 != 0 :
#      print (i)
#      continue

#6 

#x= 123
#for i in x:
#   print(i)
#Result = TypeError: 'int' object is not iterable



#i = 0
#while i < 5:
#   print(i)
#   i+= 1
#   if i == 3:
#      break
#   else:
#      print("error")
#Result: 0
#error
#1
#error
#2




# for the next statment: Program will go into loop and run indefinitely

#7
#for i in range(6):
#   if i == 3 or i == 6:
#      continue
#   print(i)


#8
#from curses.ascii import isdigit


#value = input(" enter a string : ")
#letters = 0
#digits = 0
#for i in value:
#   if i.isalpha():
#      letters = letters +1
#   elif i.isdigit():
#      digits = digits +1
#print("Letters = :", letters)
#print("digits = : ",digits)

#9 first half

#luckynumber = 2
#answer= int(input("Guess the lucky number :  "))
#while answer  != luckynumber:
#   #answer= int(input("Guess the lucky number again :  "))
#   continue
#else:
#   print("Correct Guess")
   
   

#Second half of 9

#n = 2
#answer= int(input("Guess the lucky number :  "))
#while answer  != n:
#   number,answer= (input("Guess the a number again and tell if you want to continue (Yes/No):  ")).split(maxsplit=1)
#   if answer == 'No' :
#      print("Ok! You dont want to guess more!")
#      break
#   elif int(number) == n:
#      print("You guessed it right") 
#      break
#   elif answer !='No' and int(number) != n:
#      continue
#else:
#   print("guessed right")

#10


#from itertools import count
#count= 1
#lc = 4
#while (count <=5):
#   num = int(input("Guess the lucky number : "))
#   if num != lc :
#       print("try again")
#   else:
#      print("good guess")
#   count = count+1
#else:
#   print("game over")

#11
#from itertools import count
#count= 1
#lc = 4
#while (count <=5):
#   num = int(input("Guess the lucky number : "))
#   if num != lc :
#       print("try again")
#   else:
#      print("good guess")
#      break
#   count = count+1
#else:
#   print("Sorry but that was not very successful")
