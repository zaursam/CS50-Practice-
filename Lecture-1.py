#conditionals
# x=int(input("whats x? "))
# y=int(input("whats y? "))
# if x<y:
#     print("x is less than y")
# elif x>y:
#     print("x is greater than y")
# else:
#     print("x is equals to y")
#--------------------------------------------------------------------#

#WRONG AND NOT WORKING WHEN OTHER DATA TYPE LIKE STRINGS ARE ADDED
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")
# else:
#     print("Please enter correct input")
#--------------------------------------------------------------------#

#logical operators --- or , and
#or
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# if x>y or x<y:
#     print("x is not equals to y")
# else:
#     print("x==y")


#improved version
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# if x!=y:
#     print("x is not equals to y")
# else:
#     print("x==y")

#and
# score=int(input("enter your score here: "))
# if score >=90 and score<=100:
#     print("A+")
# elif score >=80 and score<90:
#     print("A")
# elif score >= 70 and score < 80:
#     print("B+")
# elif score >= 60 and score < 70:
#     print("B")
# elif score >= 50 and score < 60:
#     print("C")
# else:
#     print("Fail")

#improved approach - comparsion operators - cleaner not necessarily better - same no. of asked
# score=int(input("enter your score here: "))
# if 90<=score<=100:
#     print("A+")
# elif 80<=score<90:
#     print("A")
# elif 70<=score< 80:
#     print("B+")
# elif 60<=score< 70:
#     print("B")
# elif 50<=score< 60:
#     print("C")
# else:
#     print("Fail")

#to reduce no. of questions asked just remove the other parameter
#--------------------------------------------------------------------#
#--parity - telling whether no. is even or odd
# x = float(input("What's x? "))
# if x%2==0:
#      print("its even")
# else:
#     print("its odd")
#--------------------------------------------------------------------#
#making parity function

# def main():
#     x =int(input("whats x? "))
#     if is_even(x):
#         print("x is even")
#     else:
#         print("x is odd")
#
# def is_even(n):
#     if n % 2 == 0:
#       return True;
#     else:
#         return False;
# a pythonic expression for this function can be>  return True if n%==0 else return False
#another way can be>
# return n%2 == 0

# main()
#--------------------------------------------------------------------#
#keyword -- match (as same as switch in other programming languages like c++,
# you dont need break; statement _ works as catchall


name=input("Name: ")
match name:
        case "Harry" | "Hermione" | "Ron":
                print("Gyrffindor")
        case "Draco":
                print("Syltherin")
        case _:
                print("who?")




