
#1
#import math
#values = input("Enter values for D with Comma seperation : ")
#values = values.split(',')

#finallist=[]
#for d in values:
#    sq = round(math.sqrt(2 * 50 * int(d) / 30))
#    finallist.append(sq)

#print(finallist)

#2

#class shape():
#    def __init__(self):
#        pass
#    def area(self):
#        return 0
    
#class square(shape):
#    def __init__(self,length=0):
#        shape.__init__(self)
#        self.length=length
#    def area(self):
#        return self.length * self.length
#areasquare =square(int(input("please enter the length of the square: ")))
#print(areasquare.area())

#3
#class Listselect():
#	def Sumofthree(self,lists):
#		for i in range(0,len(lists)):
#			firstnum = lists[i]
#			for j in range(i+1,len(lists)):
#				 secondnum =lists[j]
#				for k in range(j+1,len(lists)):
#					thirdnum = lists[k]
#					if int(firstnum + secondnum + thirdnum) == 0:
#						print(lists[i],lists[j],lists[k])
#list = [-25,-10,-7,-3,2,4,8,10]
#s1 = Listselect()
#s1.Sumofthree(list)



#4
#class Time():

#	def __init__(self, hour, minutes):
#		self.hours = hour
#		self.minutes = minutes

#	def addTime(t1, t2):
#		t3 = Time(0,0)
#		if t1.minutes+t2.minutes > 60:
#			t3.hours = (t1.minutes+t2.minutes)//60
#		t3.hours = t3.hours+t1.hours+t2.hours
#		t3.minutes = (t1.minutes+t2.minutes) % 60
#		return t3

#	def displayTime(self):
#		print ("Total time is",self.hours,"hours and",self.minutes,"minutes")

#	def displayMinute(self):
#		print ("total minutes are " , self.hours*60+self.minutes)

#x = Time(2,50)
#y = Time(1,20)
#z = Time.addTime(x,y)
#z.displayTime()
#z.displayMinute()




#5
#class Person:
#    def __init__(self,inputage):
        
#        if inputage < 0:
#            print("Age is not valid, setting age to 0")
#            self.age=0
#        else:
#            self.age = inputage
#    def amIold(self):
#        if self.age > 0 and self.age < 13:
#            print("you are young",self.age)
#        elif self.age >= 13 and self.age <= 19:
#            print("you are a teenager",self.age)
#        else:
#            print("you are old",self.age)
#    def yearPasses(self):
#        self.age += 1
    

#loopnum = int(input())
#for i in range (0,loopnum):
#    age = int(input())
#    a= Person(age)
#    a.amIold()
#    for j in range(0,4):
#        a.yearPasses()
#    a.amIold()
    


