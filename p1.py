print('hello world') # we can use single quotes as well as double quotes for print String
print("Hello World")
print("I'm Rain") # we can use single quotes inside double quotes but we can not use single quotes inside double quotes (it's also similar for double quotes)
print("Hello \"world\" world") # this problem can be retrived by using back slash
print('I\'m Ravin')
print("Line A\nLine B\n Line C") #\n can be used for new line
print("Name\tRavin") #\t can be used for tab
print("This is \ blackslash")
print("This is blackslash\\") # we can not write \ at end of the line, we may get Syntax error, this can be retrived by using doublequotes
print("This is double blackslash\\\\") #4\ are used when we want 2\ at end of line
print("Hell\blo") #\b can be used for deleting character into string

#prac
print("Line A \\n Line B")
print(r"Line A \n Line B") #Raw String
print("\\\"\\'")

print("\n")
#Exercise 1
print("This is \\\\ double blackslash") #o/p: This is \\ double blackslash
print("These are /\\/\\/\\/\\/\\/\\ mountain") #o/p: This is /\/\/\/\/\/\ mountain
print("He is\tawesome") #o/p: He is   awesome
print("\\\" \\n \\t \\\'")


#emoji
print("\U0001F600") #�😀
print("\U0001F601") #�😀

#calculator
print(2+3) #Addition
print(2-3) #Substaraction
print(2+3*4)
print(2//4) #Integer division
print(2/4) #Float division
print(2**3) #Exponent(power)
print(3%2) #modulp
print(2**0.5)
print(round(2**0.5,4))
print("\n")

#String Concatenation

f_name="Ravinkumar"
l_name='Rakholiya'
full_name=f_name+" "+l_name
print(full_name)
#you can not conacate string and number
#print(full_name+3) here, you will get type error
print(full_name+"3") #O/p: Ravinkumar Rakholiya3
#OR
print(full_name+str(3)) #O/P: Ravinkumar Rakholiya3
print(f_name*3) #O/P: RavinkumarRavinkumarRavinkumar


#USER INPUT FROM KEYBOARD
name=input("Enter your name:\n")
print("hello"+" "+name)
#   O/P:
#       Enter your name:
#       Ravin
#       hello Ravin

#input function always takes input from user in string.
age=input("What's your age?\n")
print("Yo're age is:"+" "+age)

n1=input("Enter 1st number:\n") #4
n2=input("Enter 2nd number:\n") #3
total=n1+n2
print("total is:"+" "+total) #O/P: total is: 43

n1=(input("Enter 1st number:\n")) #4
n2=input("Enter 2nd number:\n") #3
total=int(n1)+int(n2)
print("Total is:"+" "+str(total)) # O/P:Total is: 7
total=float(n1)+float(n2)
print("Total is:"+" "+str(total)) #O/p:Total is: 7.0

n3=float("44")
n4=int("11")
print(n3+n4) #O/P:55.0   output in float

#multiple variable can be declared in single line
n5,n6="Rebel",22
print("Hello"+" "+n5+" "+"yo're age is"+" "+str(n6)) #O/P: Hello Rebel yo're age is 22

x=y=z=1
print(x+y+z) #o/p:3

#Take user data in single line
n7,n8=input("Enyer your name and age:\n").split() #Enyer your name and age:Ravin 22
print(n7) #O/p:Ravin
print(n8) #O/P:24
  #OR
#we can use split function with comma and space and input which takes from keyboard will be affected by it.
n17,n18=input("Enyer your name and age:\n").split(",") #Enyer your name and age:Ravin,24
print(n17) #O/P:Ravin
print(n18) #O/P:24


#String Formatting
print("Hello {} yo're age is {}".format(n5,n6)) #here we don't need to think about n6's data type. python 3
 #O/P:Hello Rebel yo're age is 22
   #or
print(f"Hello {n5} yo're age is {n6}") #python 3.6
 #O/P:Hello Rebel yo're age is 22
 #here we can (n6+3)


 #Exercise ch1
num1,num3,num4=input("Enter nummber 1, number 2, number 3\n").split(",") #Enter nummber 1, number 2, number 3  1,3,5
print(f"number 1 is:{num1}\nnumber 2 is:{num3}\nnumber 3 is:{num4}\naverage is:{(int(num1)+int(num3)+int(num4))/3}")
# o/p: 
#     number 1 is:1
#     number 2 is:3
#     number 3 is:5
#     average is:3.0



