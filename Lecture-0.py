"""
Topics covered in the lecture 0 - Integrated Development Environments (IDEs), command-line interface (cli), interpreter, return values, variables, bugs and debugging,
parameters and named parameters, arguments and passing multiple arguments in a function, escape sequences, side effect, functions, comments and pseudocode, string (str)
and fstring, methods, int for integers and operators, interactive mode, concatination, nesting functions, data types float, def for defining a function, scope
"""

#writing first program
print ("hello world")
name = input("what is your name? ")
print ("hello, " + name)

""" 
this is a multi-line comment, print("hello")
"""
print ("hello, ", name)

#now to remove the space is we have to change sep=" " to sep="" and to move the cursor to the next line end="\n" to end=""
#print(*objects, sep=' ', end='\n', file=None, flush=False) -- from original documentation of python

print ("hello, ", end="")
print (name)


print ('hey, "friend"')
print ("hey, \"friend\"")
print (f"hey, {name}") #fstring means format string it formats the string so that its considered speical

#title() just makes every first letter of a word captial. capitalize() can also be used if there is one word in the name
pname=input("what is your preferred name? ").title()
#you can also do this pname=input("what is your preferred name? ").title().strip()

#strip() strips out the blank spaces from left and right of the word
pname=pname.strip()
print(pname)
#all the above string built in functions in this contexts are referred as methods

#now spliting users name into first and last name
first, last=name.split(" ")
print ("hello, " + first)


#calculator
x=1
y=2
z=x+y
print (z)

#lets take inputs
a=input("value here ")
b=input("value here ")
c=int(a)+int(b)

print (c)

#another way and nesting functions 
s=float(input("value1 "))
t=float(input("value2 "))
print(round(s+t))
#round(number, ndigits=None) - round function can also do z=round(x+y)

#not preferred but another way - too much nesting of functions
print(int(input("s="))+int(input("t=")))

# separating values with ,
i=float(input("value "))
j=int(input("value "))
k=i+j
print(f"{k:,}") #fstring


#rounding off in division, can also be done as just >> print(f"{k:.2f}")
k=round(i/j, 2)

print(k)


#defining a function >> def function_name

def hello(to="world"):
    print("Hello,", to)
hello()
yourname=input("whats your name ")
hello(yourname)


#define a function in later line
def main():
    myname=input("name")
    hey(myname)
    x = int(input("whats value of x? "))
    print("square of x is ", square(x))

def hey(to):
    print("hey,", to)

 # returning values
def square(n):
    return n*n
    #return pow(n, 2) raising the power of 2 to the number n given

main() #calling the function > main function has hey() function nested

#scope is a variable only defined with in a certain context > not a general variable