#--variable data types: str
# name="sam"
# print(type(name))
# for commenting all the code ctrl+/

#integar
# age=21 .. integer data type is assigned to a variable with no quotation marks
# age += 1
# print (age)
# print ("your age is "+ str(age))  #.. this is typecasting >> changing int to str

#floating point values, boolean values
# Human= False
# print(Human)
# print(type(Human))

#str(var) is string concatination which adds other data types to a string for printing

#--multiple assignment
# x, y, z= "sam", 21, True
# print(x,y,z)
# spongebob= patrick = sandy =30
# print(spongebob,patrick,sandy)

#-- string method
# name = "Bro Code"
#print (len (name))
# print(name.find("o"))
#print (name.capitalize())
#print (name.upper())
#print (name.lower())
#print (name. isdigit())
#print (name.isalpha())
# print(name.count("o"))
#print (name.replace("o","a"))
# print (name*3)


#--type casting
# x=1
# y=2.1
# z="3"
#
# z=float(z) #this way variable is reassinged as a new data type
# print(int(y)) #but this way the change of data type is not permanent
# print(z+1)



#--some math functions
# import math
# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(math.sqrt(pi))
# print(abs(pi)) #how much is it away from zero
# print(pow(pi,2))
# print(type(pi))
# x,y,z=1,2,3
# print(max(x,y,z))
# print(min(x,y,z))


#string slicing - creating another string by extracting elements from another string >> indexing[] or slice() -- [start:stop:step]
# name="zee sam"
# first_name=name[0:3] #intention to write zs >>> now the first index is inclusive and last is exclusive if you want stoping index 2 you have to write 3
# print(first_name)
# last_name=name[:4]
# print(last_name)
# just_name=name[2:]
# print(just_name)
# messingaroundwith_step=name[0:7:2]
# messingaroundwith_step2=name[::3]
# print(messingaroundwith_step)
# print(messingaroundwith_step2)
# reversed_name=name[::-1]
# print(reversed_name)

#now slice()
# website="https://www.google.com"
# website2="https://www.netflix.com"
# slicing =slice(12,-4,)  #this is how you create an object
# print(website[slicing]) #thats how you apply object
# print((website2[slicing]))


#--If else statement
# age=int(input("whats your age? "))
# if age>=18:
#     print("you are eligible")
# elif age>0 and age<18:   #mistake: elif age<18 & age!=0: wrong as -20 is != 0 but its also not a good approach to use this
#     print(("you are not eligible"))
# else:
#     print("type right input")

#logical operators >> and, or, not, not operator reverse the results
# temp = int(input("What is the temperature outside?: "))
# if not (temp>=0 and temp<=39):
#     print("the temperature is good today!")
#     print("go outside!")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is bad today!")
#     print("stay inside!")
