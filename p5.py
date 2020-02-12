# # # List------->Ordered collection of items

# # # it is data structure
# # # we can store anything inside list such as int, float, string, double


# # numbers=[1,2,3,4,5]
# # print(numbers)
# # print(numbers[2])




# # str1=["Ravin","Rupen",'Sunny']
# # print(str1)
# # print(str1[1])


# # mixed=[1,2,3,4,5,"Ravin","Rebel"]
# # print(mixed)                     # o/p: [1, 2, 3, 4, 5, 'Ravin', 'Rebel']
# # print(mixed[2])                  # o/p: 3
# # print(mixed[-1])                 # o/p: Rebel
# # print(mixed[:2])                 # o/p: [1, 2]
# # print(mixed[2:])                 # o/p: [3, 4, 5, 'Ravin', 'Rebel']
# # mixed[1]="hello"
# # print(mixed)                     # o/p: [1, 'hello', 3, 4, 5, 'Ravin', 'Rebel']
# # mixed[1:]="hello"
# # print(mixed)                     # o/p: [1, 'h', 'e', 'l', 'l', 'o']
# # mixed[1:]=["hey","Hi"]
# # print(mixed)                     # o/p: [1, 'hey', 'Hi']



# #add data in list using append method

# fruits=["mango",'graps']
# print(fruits)                    #o/p: ['mango', 'graps']
# fruits.append("apple")
# print(fruits)     #append method always add data in last position in list.
# #o/p: ['mango', 'graps', 'apple']

# #using insert method
# fruits.insert(1,"banana")   #if we write position which is not in list, item will post on last position, for e.g,----> if i write 20 insted of 1, banana will post on last position
# print(fruits)                   #o/p: ['mango', 'banana', 'graps', 'apple']
# fruits.insert(20,"ABC")
# print(fruits)                   #o/p: ['mango', 'banana', 'graps', 'apple', 'ABC']


# #concatenate two list
# num=[1,2,3]
# al=['a','b','c','d']
# s=num+al
# print(s)                        #o/p: [1, 2, 3, 'a', 'b', 'c', 'd']



# # difference between append and extend

# num=[1,2,3]
# al=['a','b','c','d']
# num.extend(al)
# print(num)                     #o/p: [1, 2, 3, 'a', 'b', 'c', 'd']
# print(al)                      #o/p: ['a', 'b', 'c', 'd']

# num.append(al)
# print(num)                       #o/p: [1, 2, 3, ['a', 'b', 'c', 'd']]
# print(al)                        #o/p: ['a', 'b', 'c', 'd']
# print(num[3])                    #o/p: ['a', 'b', 'c', 'd']




# #  Delete data from list

# #BY usin pop method
# fruits=["Apple","Banana",'graps','kiwi','strowbarry']
# fruits.pop()       #delet item from last
# print(fruits)      #o/p:['Apple', 'Banana', 'graps', 'kiwi']
# fruits.pop(2)
# print(fruits)      #o/p:['Apple', 'Banana', 'kiwi']



# #BY using del operator
# fruits=["Apple","Banana",'graps','kiwi','strowbarry']
# del fruits[2]
# print(fruits)        #o/p:['Apple', 'Banana', 'kiwi', 'strowbarry']



# #BY using remove method
# fruits=["Apple","Banana",'graps','kiwi','strowbarry',"kiwi"]
# fruits.remove('Banana')
# print(fruits)          #o/p:['Apple', 'graps', 'kiwi', 'strowbarry','kiwi']
# fruits.remove("kiwi")  #it removes only first kiwi in list
# print(fruits)          #o/p:['Apple', 'graps', 'strowbarry', 'kiwi']



# # List
# # add data in list--------->append,extend,insert
# # delete data from list---->pop,del,remove


# # in_list
# fruits=["apple","Banana","Graps","KiWi"]
# n=input("Enter fruit\n")
# if n in fruits:
#     print("True")
# else:
#     print("False")



# #other methods in list

# #count method
# fruits=["Apple","Banana",'graps','kiwi','strowbarry',"kiwi"]
# print(fruits.count("kiwi"))   #o/p:2
# fruits.sort()
# print(fruits)                 #o/p:['Apple', 'Banana', 'graps', 'kiwi', 'kiwi', 'strowbarry']
# #or
# print(sorted(fruits))         #o/p:['Apple', 'Banana', 'graps', 'kiwi', 'kiwi', 'strowbarry']
# print(fruits)                 #o/p:["Apple","Banana",'graps','kiwi','strowbarry',"kiwi"]
# numbers=[10,3,2,7,4,3,8]
# # numbers.sort()
# print(numbers)                #o/p:[2, 3, 3, 4, 7, 8, 10]
# #or
# print(sorted(numbers))        #o/p:[2, 3, 3, 4, 7, 8, 10]
# print(numbers)                #o/p:[10, 3, 2, 7, 4, 3, 8]


# numbers_copy=numbers.copy()
# print(numbers_copy)           #o/p:[10, 3, 2, 7, 4, 3, 8]

# numbers.clear()
# print(numbers)                #o/p:[]



# #is and ==
# fruits1=["apple","banana","graps"]
# fruits2=["apple","banana","graps"]
# fruits3=["pear","kiwi","apple","banana"]
# print(fruits1==fruits3)      #o/p:False
# print(fruits1==fruits2)      #o/p:True
# print(fruits1 is fruits2)    #o/p:False
# #here is check fruits1 and fruits2 are on same location in memory



# #Split method
# #convert String to List
# user_info="Ravin 24".split()
# print(user_info)           #o/p:['Ravin', '24']

# user_info1="Ravin,24".split(",")
# print(user_info1)          #o/p:['Ravin', '24']

# name,age=("Ravin,22").split(",")
# print(name)                #o/p:Ravin
# print(age)                 #o/p:22


# #Join method
# #convert List to String
# user_info2=["Ravin",24]
# #print(",".join(user_info2))    #o/p:Error
# user_info3=["Ravin","24"]
# print(",".join(user_info3))     #o/p:Ravin,24
# print("".join(user_info3))      #o/p:Ravin24
# print(" ".join(user_info3))     #o/p:Ravin 24




# list----->ordered collection of items of anytype and flexible
# array---->ordered collection of items of same type
#array module in python---->we can store fix data type
# javascript array = python list / flexible






# #String vs List

# #String is immutable
# s="ravin"
# s.title()
# print(s)    #o/p:ravin    #s shold be change but it can't becoz string is immutable

# #list is mutable
# s1=["rav","rupen","yash","nandan"]
# s1.append("chirag")
# print(s1)  #o/p:['rav', 'rupen', 'yash', 'nandan', 'chirag']     #s1 can be updated becoz s1 is list and list is mutable



# #Looping in list

# #For loop
# fruits1=["apple","banana","graps"]
# for i in (fruits1):
#     print(i,end=",")
# print()


# #while loop
# j=0
# while j<len(fruits1):
#     print(fruits1[j],end=" ")
#     j+=1



# #List in List---------------->2-d list(matrix)
# l1=[[1,2,3],[4,5,6],[7,8,9]]             #o/P:
# for sublist in l1:                      #      1 2 3
#     for i in sublist:                   #      4 5 6
#         print(i,end=" ")                #      7 8 9
#     print()


# print(l1[2][2])    #o/p:9

# #type function
# s="Ravin"
# print(type(s))   #o/p:<class 'str'>
# print(type(l1))  #o/p:<class 'list'>






# #Generate list using range function
# numbers=list(range(1,21))
# print(numbers)                   #o/p:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# numbers.pop()
# print(numbers)                   #o/p:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#    #pop method can give us pop value
# s1=numbers.pop()
# print(s1)                        #o/p:19
# print(numbers)                   #o/p:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# print(numbers.index(2))          #o/p:1
# print(numbers.index(5))          #o/p:4
# #index method can give us the position of data
# n1=[1,3,2,1,4,6,2]
# print(n1.index(2))                                    #o/p:2
# print(n1.index(2,3))   #(check,start point)           #o/p:6
# print(n1.index(3,2,6)) #(check,startpoint,endpoint)   #o/p:error 3 is not in list

# #pass list to a function
# def negative_list(l):
#     negative=[]
#     for i in l:
#         negative.append(i*-1)
#     return negative

# print(negative_list(numbers))     #o/p:[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]





# #Excercise
# def square_list(s1):
#     s3=[]
#     for i in s1:
#         s3.append(i*i)
#     return s3

# l=int(input("Enter length of list\n"))
# s=[]
# for i in range(l):
#     l1=int(input(f"Enter number {i}\n"))
#     s.append(l1)
# print(f"list is: {s}")
# print(square_list(s))    #o/p:[1, 4, 9, 16, 25, 36, 49, 64, 81, 0]





# #Excercise
# def reverse_list(s4):
#     s2=[]
#     for i in range (len(s4)):
#         s7=s4.pop()
#         s2.append(s7)
#     return s2

# l=int(input("Enter length of list\n"))
# s=[]
# for i in range(l):
#     l1=int(input(f"Enter number {i}\n"))
#     s.append(l1)
# print(f"list is: {s}")
# print(reverse_list(s))      #o/p:[5, 4, 3, 2, 1]





# #Excercise
# def rev_listel(s1):
#     s2=[]
#     for i in s1:
#         s2.append(i[::-1])
#     return s2
    
# l=int(input("Enter length of list:\n"))
# list1=[]
# for i in range(l):
#     s=input(f"Enter element {i}\n")
#     list1.append(s)
# print(list1)                         #o/p:['Ravin', 'Rupen', 'Yas', 'dhara', 'ajay']
# print(rev_listel(list1))             #o/p:['nivaR', 'nepuR', 'saY', 'arahd', 'yaja']










# #Excercise
# def filter_odd_even(list2):
#     l_odd=[]
#     l_even=[]
#     l_main=[]
#     for i in (list2):
#         if int(i)%2==0:
#             l_even.append(i)
#         else:
#             l_odd.append(i)
#     l_main.append(l_even)
#     l_main.append(l_odd)
#     #or
#     # l_main=[l_even,l_odd]
#     return l_main

# l=int(input("Enter length of list\n"))
# list1=[]
# for i in range(l):
#     d1=input(f"Enter data {i+1}\n")
#     list1.append(d1)
# print(list1)                                #o/p:['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# print(filter_odd_even(list1))               #o/p:[['2', '4', '6', '8', '0'], ['1', '3', '5', '7', '9']]







# #Excercise
# def finder_fun(list1,list2):
#     same_ele=[]
#     for i in list1:
#         if i in list2:
#             same_ele.append(i)
#     return same_ele

# l1=int(input("Enter length of list 1\n"))
# list_1=[]
# for i in range(l1):
#     d1=input(f"Enter value of list {i}\n")
#     list_1.append(d1)
# l2=int(input("Enter length of list 2\n"))
# list_2=[]
# for i in range(l2):
#     d1=input(f"Enter value of list {i}\n")
#     list_2.append(d1)
# print(list_1,list_2)                              #o/p:['1', '2', '3', '4'] ['2', '1', '7', '8', '9']
# print(f"Same elements in both list are: {finder_fun(list_1,list_2)}")     #o/p:Same elements in both list are: ['1', '2']






# #Max and Min function
# list1=[2,60,34]
# print(min(list1))                     #o/p:2
# print(max(list1))                     #o/p:60

# def ma_min_dif(l):
#     return max(l)-min(l)

# l=int(input("Enter length of list\n"))
# l1=[]
# for i in range(l):
#     s=int(input(f"Enter data {i+1}\n"))
#     l1.append(s)
# print(l1)                                #o/p:[134, 4, 54, 131, 56]
# print(ma_min_dif(l1))                    #o/p:130



#Excercise
def check_inside_list(li1):
    n=0
    for i in li1:
        if type(i)==list:
            n+=1
    return n

li_1=[1,2,3,[1,2],[4,5],[6,7,8]]
print(li_1)                          #o/P:[1, 2, 3, [1, 2], [4, 5], [6, 7, 8]]
print(check_inside_list(li_1))       #o/p:3


#mixed
