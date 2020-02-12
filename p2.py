s1="Ravin"
print(s1[2]) #o/p: v
print(s1[-2]) #o/p: -i
print("\n")

#String slicing
# [start:stop:step]
print(s1[2:3]) #o/p:v
print(s1[-4:5]) #o/p:avin
print(s1[1:2])
print(s1[:]) #o/p:Ravin
print(s1[1:]) #o/p:avin
print(s1[:3]) #o/p:Rav
print("Rupen"[2:5]) #o/p:pen
print(s1[0:5:2]) #o/p:Rvn
print(s1[0::2]) #o/p:Rvn
print(s1[::2]) #o/p:Rvn
print(s1[-1::-1]) #o/p:nivaR
print(s1[-1::-2]) #o/p:nvR
print(s1[::-1]) #o/p:nivaR0

 
#exercise 2
s2=input("Enter your name:\n")
print("Reverse name is"+" "+s2[::-1])
 #OR
print(f"Reverse name is {s2[::-1]}")
    #o/p:
        # Enter your name:
        #                 Rebel
        #                 Reverse name is lebeR
        #                 Reverse name is lebeR


#String Methods s2="RaViN raKhOlIya"
print("lenth of the string is:"+str(len(s2)))  #o/p: lenth of the string is:15
print("lowe data is:"+str(s2.lower())) #lowe data is:ravin rakholiya
print("upper data is:"+str(s2.upper())) #upper data is:RAVIN RAKHOLIYA
print("Title case is:"+str(s2.title())) #Title case is:Ravin Rakholiya
print("number of 'a' is:"+str(s2.count("a"))) #number of 'a' is:3



#exercise
a1,a2=input("Enter your name, any character:").split(",")
print(f"length of the user's name is: {len(a1)}")
print(f"number of inputed charcter in a1 is: {a1.lower().count(a2)}")
# o/p:
#     Enter your name, any character:RaViN raKhOlIya,r
#     length of the user's name is: 15
#     number of inputed charcter in a1 is: 2

#     And also
# o/p:
#     Enter your name, any character:afafaf, f
#     length of the user's name is: 6
#     number of inputed charcter in a1 is: 0







#strip() function
d1="  Ravin  "
d2="......."
print(d1+d2) #o/p:  Ravin  .......
print(d1.lstrip()+d2) #o/p:Ravin  .......
print(d1.rstrip()+d2) #o/p:  Ravin.......
print(d1.strip()+d2.strip()) #o/p:Ravin.......


#exercise
a4,a6=input("Enter your name, any character:").split(",")
print(f"length of the user's name is: {len(a4)}")
print(f"number of inputed charcter in a1 is: {a4.strip().lower().count(a6.strip().lower())}")
# o/p:
#     Enter your name, any character:afafaf,   F
#     length of the user's name is: 6
#     number of inputed charcter in a1 is: 3


#Remove space
a5="   Ravin Rakholiya   "
print(a5)  #o/p:   Ravin Rakholiya   
print(a5.strip()) #o/p:Ravin Rakholiya
print(a5.replace(" ","")) #o/p:RavinRakholiya


#replace() and find() function
a7="he is handsome and he is good stunter"
print(a7.replace(" ","_"))  #o/p:he_is_handsome_and_he_is_good_stunter
print(a7.replace("is","was")) #o/p:he was handsome and he was good stunter
print(a7.replace("is","was",1)) #o/p:he was handsome and he is good stunter
print(a7.replace("is","was",2)) #o/p:he was handsome and he was good stunter
print(a7.replace("is","was",3)) #o/p:he was handsome and he was good stunter

print(a7.rfind("is")) #o/p:22
print(a7.find("is")) #o/p:3
n1=a7.find("is") #n1 is number
print(a7.find("is",n1)) #o/p:3
print(a7.find("is",n1+1)) #o/p:22


#center() function
name="Ravin"
print(name.center(6,"*")) #o/p:Ravin*
print(name.center(7,"*")) #o/p:*Ravin*
print(name.center(len(name)+3,"*")) #o/p:*Ravin**
print(name.center(len(name)+4,"*")) #o/p:**Ravin**
na1=input("Enter your name please\n")
print(na1.center(len(na1)+8,"@")) #o/p:@@@@Ravin@@@@


#Strings are immutable in python
na2="Ravin"
# na2[2]="A"  ---> we can not wriye this it will give typeerror
print(na2.replace("a","A"))  #o/p:RAvin
print(na2) #o/p:Ravin
#   here we can see that in line 119 we replaced a to A but when we print na2 in next line(120) the na2 is not updated,
#     the fact is that python create new var when we use replace method, and don't make any changes in previous one which called immutable.
na3=na2.replace("a","A")
print(na3) #o/p:RAvin
