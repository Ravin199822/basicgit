#if loop
age=input("Enter your age:\n")
if int(age)>14:
    print("You are above 14") #space=indetation
    print("Okay...")



#pass statement    (pass statement is used when we don't want to write anything inside loop)
x=12
if x>12:
    pass


#if-else statement
age=input("Enter your age:\n")
if int(age)>14:
    print("You are above 14") #space=indetation
    print("Okay...")
else:
    print("Your age below 14")





# Exercise
import random
wining_number=random.randrange(0,100,13)
print(wining_number)
n1,n2=input("Enter number range n1,n2:\n").split(",")
if int(n1)<=wining_number<=int(n2):
    print("YOU WIN !!!!!")
else:
    if(int(n1)>wining_number):
        print("Number is too short...")
    if(int(n2)<wining_number):
        print("Number is too long....")




# and, or operator
name="Ravin"
age=22
if name=="Ravin" and age==22:
    print("Confition true(and)")
else:
    print("Condition False(and)")

if name=="Ravin" or age==21:
    print("Condition true(or)")
else:
    print("Condition False(or)")




#Exercise
u_name=input("Enter your name please\n")
u_age=input("Enter your age please\n")
if (u_name[0]=='a' or u_name[0]=='A') and int(u_age)>10:
    print("You can see 'coco' movie")
else:
    print("You can not see 'coco' movie")




#if-elif-else statement
age=input("Enter your age\n")
if int(age)==0 or int(age)<0:
    print("Enter valid age")
elif 1<int(age)<4:
    print("Ticket can be free")
elif 3<int(age)<11:
    print("Ticket price is: 150")
elif 10<int(age)<61:
    print("Ticket price is: 250")
else:
    print("Ticket price is: 200")



#in statement
name="Ravin"
if 'a' in name:
    print("a in Ravin") 
else:
    print("a is not in Ravin")


#check empty or not
name=""
if name.split():    #true id name is not empty
    print("Name is not empty")
else:
    print("Name is empty")


name=input("Enter your name:\n")
if name.split():
    print(f"your name is {name}")
else:
    print("you didn't enter your name")



# while loop
i=1
while i<=10:
    print("hello world")
    i+=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(f"Sum of 1-10 numbers is: {sum}")   


#Exercise
n=input("Enter number:\n")
i=1
sum=0
while i<=int(n):
    sum+=i
    i+=1
print(f"Sum of 1 to n number is: {sum}")


#Exercise
n=input("Enter number:\n")
n1=len(n)
i=0
sum=0
while i<n1:
    sum+=int(n[i])
    i+=1
print(sum)





# Exercise
n=input("Enter your full name:\n")
i=0
temp_var=""
while i<len(n):
    if n[i] not in temp_var:
        print(f"{n[i]} : {n.count(n[i])}")
        temp_var+=n[i]
    i+=1



#For loop
for i in range(10): print(i)
print("\n")
for i in range(1,10):print(i)
print("\n")
sum=0
for i in range(1,11):sum+=i
print(f"sum of 1-10 numbers: {sum}")
num=input("Enter number:\n")
l=len(num)
s=0
for i in range(l):s+=int(num[i])
print(f"sum of number: {s}")
name=input("Enter your name\n")
l=len(name)
temp_var=""
for i in range(l):
    if name[i] not in temp_var: 
        s=name.count(name[i])
        temp_var+=name[i]
        print(f"{name[i]} : {s}")




#break statement
for i in range(10):
    if i==5:break
    print(i)
print("\n")
#continue statement
for i in range(10):
    if i==5:continue
    print(i)



#Excercise
import random
winning_number=random.randint(1,100)
guess_number=input("Guess number between 1-100:\n")
i=0
game_over=False
while not game_over:
    if winning_number==int(guess_number):
        i+=1
        print(f"You win, and you guessed this number in {i} times")  
        game_over=True
    else:
        if int(guess_number)>winning_number:
            i+=1
            print("Number too high")
            guess_number=input("Guess again\n")
        else:
            i+=1
            print("Number too low")
            guess_number=input("Guess again\n")





#DRY principal--->Don't repet your self
import random
winning_number=random.randint(1,100)
guess_number=input("Guess number between 1-100:\n")
i=0
game_over=False
while not game_over:
    if winning_number==int(guess_number):
        i+=1
        print(f"You win, and you guessed this number in {i} times")  
        game_over=True
    else:
        if int(guess_number)>winning_number:
            print("Number too high")
        else:
            print("Number too low")
        i+=1
        guess_number=input("Guess again\n")





# Step argument
for i in range(1,11,1):     #(start,end,step)
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(11,0,-1):
    print(i)


# For loop in string
name="Ravin"
l=len(name)
for i in range(l):
    print(name[i])

name="Ravin"
for i in name:
    print(i)

num=input("Enter number\n")
sum=0
for i in num:
    sum+=int(i)
print(f"sum of given number: {sum}")
