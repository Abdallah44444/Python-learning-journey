#---------------------
#---variables [2]---
#---------------------
# Source Code : Original code you write it on computer 
# Translation : Convert source code to machine code (binary 0, 1)
# comapilation :translate code before run time 
# Run time : Period App take to Executing commands
# Interpreted : Code translated on the fly during Execution or Run time
# python is dynamically typed language => no need to declare variable type
#------------------------------------------

x = 5
x = "Hello World"
print(x)

help("keywords") # to see all python keywords (reserved words) 

a, b, c = 1, 2, 3 # multiple assignment in one line
print(a)
print(b)
print(c)
#or
print(a, b, c) # print multiple variables in one line separated by comma

x = 10
y = x
x = 20

print(y) # y will print 10 because it is assigned the value of x before x is changed to 20