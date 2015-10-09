#This is a comment
'''
This is a multiline
comment :)
'''

#Primitive Data Types
a=21 #int
b=12 #int
c=3.3 #float
speedygonzalez = True #boolean
none = None #none

#to check a variable's type, use the type function
type(a) #===> int


#Arithmetic
print 1+21
print 3**2
print 16/4
print 10%3
print 1-4
print 5/2 #2
print 5.0/2 #2.5

#boolean operators

print 1<5 #true
print 1==1 or  5==7
print 1 == 1 and 5==7
print 5!=5 #false
print not(5!=6) #false
print 3==2+1



#Strings!!!
x, y, z = "a", "b", "c"
first, last, age= "Bryan", "Gonzalez", 18
print "robotics" + "club"
print "My first name is %s and my last name is %s and I'm %d years old" %(first, last, age)
print "My first name is {}, my last name is {} and I'm {} years old".format(first, last, age)



#Task 1
#Assign variable ccny the string purple, then print out variable ccny 10 times

ccny= "purple" 
print ccny*10







#Task 2
#Format a string "I am a <> int, And I am a <> float, And I am a <> string, and I am a <> boolean", with the appropriate values

a, b, c, d = 10, 2.1, "Harry", True
print "My first name is %d, and I am a %f, and I am a %s, and I am a %s" %(a, b, c, d)
print "My first name is {}, and I am a {}, and I am a {}, and I am a {}".format(a, b, c, d)








#Task 3 
#Print a boolean to the screen, that compares the len() <--- *hint* of string "Apple" to that of string "Banana" 


print len("Apple") > len("Banana")


print "My name is \" dfgnhm  \" " 

#Editing this file on github, will git pull so I can have this locally
