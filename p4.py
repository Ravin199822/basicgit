#Function

name="Ravin"
print(len(name))   #Pre-defined function

def add_two(n1,n2):
    return n1+n2

a=input("Enter number 1:\n")
b=input("Enter number 2:\n")
s=add_two(int(a),int(b))
print(f"Addition of two number: {s}")

a1=input("Enter your first name:\n")
a2=input("Enter your Family name:\n")
full_name=add_two(a1,a2)
print("Your Full name is: "+full_name)
#or
print("Your Full name is: "+add_two(a1,a2))


def last_cahra(n):
    return n[-1]

a1=input("Enter name:\n")
s1=last_cahra(a1)
print(f"last char of entered name is: {s1}")
#o/p:
#    Enter name:
#    Ravin
#    last char of entered name is: n

#print(last_cahra(8))  #Error



def check_oddeven(n):
    if int(n)%2==0:
        return "Even"
    else:
        return "Odd"


n=input("Enter number:")
s=check_oddeven(n)
print(f"Number is {s}")



def check_even(n):
    if int(n)%2==0:
        return True
    else:
        return False
#or
def check_even1(n):
    if int(n)%2==0:
        return True
    return False
#or
def check_even2(n):
    return int(n)%2==0
a=input("Enter number\n")
s=check_even2(a)
print(s)




# exercise
def big_number(a,b):
    if a>b:
        return a
    else:
        return b

x=int(input("Enter number 1\n"))
y=int(input("Enter number 2\n"))
s=big_number(x,y)
print(f"{s} is greater")



def greatest_number(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

x=int(input("Enter number 1\n"))
y=int(input("Enter number 2\n"))
z=int(input("Enter number 3\n"))
s=greatest_number(x,y,z)
print(f"{s} is greatest")


def greater(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(x,y,z):
    bigger=greater(x,y)
    return greater(bigger,z)

n1=int(input("Enter number 1\n"))
n2=int(input("Enter number 2\n"))
n3=int(input("Enter number 3\n"))
print(f"greatest number is : {greatest(n1,n2,n3)}")




#Exercise
def is_palindrome(n):
    reverse_name=n[::-1]
    if reverse_name==n: #or n==n[::-1]:
        return "String is palindrome"
    return "String is not palindrome"

print(is_palindrome(input("Enter name\n")))



# Print in a line
def number_1():
    for i in range(10):
        print(i,end=",")
number_1()



#Exercise
def fibonacci_series(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(a,b,end=",")
    else:
        print(a,b,end=",")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=",")

fibonacci_series(int(input("Enter number\n")))






#Default parameter
def deault_param(f_name,l_name,age):
    print(f"First name:{f_name}")
    print(f"Last name:{l_name}")
    print(f"age is:{age}")

f_n=input("Enter first_name:\n")
l_n=input("Enter last_name:\n") 
age=input("Enter your age:\n")
deault_param(f_n,l_n,age)   




def deault_param1(f_name,l_name,age=22):   #here, if we don't initilize age,we may get error
    print(f"First name:{f_name}")
    print(f"Last name:{l_name}")
    print(f"age is:{age}")

f_n=input("Enter first_name:\n")
l_n=input("Enter last_name:\n") 
age=input("Enter your age:\n") #here, if we enter age, we may get updated age but we have to pass during calling def oterwise we can't update. i mean if i will enter age=24, i will get age=24 in output.
deault_param1(f_n,l_n)   # here, we don't pass the value of age and not initilize in def functiom, we will get error. in adiition, 


def deault_param2(f_name,l_name="none",age=22):   # here, we can not directly initilize l_name, first we have to initilize age other wise we will get error.Similarly for f_name, we have to initilize l_name and age for f_name.
    print(f"First name:{f_name}")
    print(f"Last name:{l_name}")
    print(f"age is:{age}")

f_n=input("Enter first_name:\n")
l_n=input("Enter last_name:\n") 
age=input("Enter your age:\n")
deault_param2(f_n)   #if here we don't pass the l_name and age while calling, we will not get updated data, that means we will get l_name = none and age=22.




#Scop

x=7   #global variable

def fun():
    x=5      #local variable
    return x


print(fun())
print(x)

#  o/p: 5
#       7



x=7   
def fun1():
    global x         #we are using global variable x, and x's value will be updated
    x=5      
    return x

print(x)
print(fun1())
print(x)

#    o/p: 7
#         5
#         5





