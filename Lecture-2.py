#While loop
# i=3
# while i!=0:
#     print("meow")
#     i=i-1
import time

# i =0
# while i<3:
#     print("woof")
#     i+=1

#for loop - First syntax is a guess
# for i in [1,...,3]:
#     print("meow")

# for i in range(3):
#     print("meow")
#
# Pythonic way
# for _ in range(3):
#     print("meow")

# print("meow\n"*3, end="")

# while True:
#     n=int(input("Whats n?" ))
#     if n>0:
#         break
# for _ in range(n):
#     print("meow")


#creating a meow function

# def main():
#     while True:
#         n=int(input("Whats n?" ))
#         if n>0:
#             break
#     meow(n)
#
# def meow(n):
#         for _ in range(n):
#             print("meow")
#
#
# main()


# def main():
#     number=getnumber()
#     meow(number)
# def getnumber():
#     while True:
#         n=int(input("Whats n?" ))
#         if n>0:
#             break
#             return n
# def meow(n):
#         for _ in range(n):
#             print("meow")
#
#
# main()
#creating a happy new year counter
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
#
# print("Happy New Year")

#nested loops
# rows=int(input("Number of rows? "))
# columns=int(input("Number of columns? "))
# symbols=input("Symbol? ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbols, end="")
#     print()
#  #loop control statements are break continue and pass


#lists and indexing
# students = ["Hermione", "Harry", "Ron"]
# print(students[1])
# #for loop for lists
# for _ in students:
#     print(_)
#using _ is making the code more cryptic, use a variable
# for student in students:
#     print(student)

#len function
# for i in range(len(students)):
#     print(i+1, students[i])

"""when code gets more complicated and its hard to keep track of things we use another data type called dictionaries or
dict"""

# students = {
#     "Hermione":"Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco":"Syltherin",
#
# }
# #dictionaries doesnt have numeric index it uses words
# print(students["Hermione"])
#
# print(type(students))
#
# # for student in students:
# #     print(student)
# #this is to print keys which in this case of dict is not numbers but words/names
# for student in students:
#     print(student,students[student],sep=",")
# #now this is printing keys



#list of dictionaries - in this each student is a dictionary(set of values) on its own.
# students =[
#     {"Name":"Harry","House":"Gryffindor","Patronus":"Stag"},
#     {"Name":"Hermione","House":"Gryffindor","Patronus":"Otter"},
#     {"Name":"Ron","House":"Gryffindor","Patronus":"Jack Russell Terrier"},
#     {"Name":"Draco","House":"Syltherin","Patronus":None}, #none is a keyword in python when there is no value for a certain thing
# ]
# print(type(students)) #its a list as the [] indicates
# for student in students:
#     print(student["Name"], student["House"], student["Patronus"], sep=",")


# Making a block of #
# for _ in range(3):
#     print("#")

# def main():
    # print_column(3)
    # print_rows(4)

# def print_column(height):
#     for _ in range(height):
#         print("#")
#another way of doing it

# def print_column(height):
#     print("#\n"*height, end="")
# def print_rows(width):
#      print("?"*width)
# main()
#Building a square block
def main():
    print_square(int(input("whats the number? ")))
# def print_square(size):
# #for each row in square
#     for i in range(size):
# #for each brick in row
#         for j in range(size):
# #printing brick
#          print("#", end="")
#         print() #this print prints only a new line at the end of the row (not end of brick)

#another way to do it
def print_square(size):
    for i in range(size):
        print("#"*size)

main()