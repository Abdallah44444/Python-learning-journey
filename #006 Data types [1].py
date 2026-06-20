# --------------------------------------------
# type() function
# All data types in Python are objects
# --------------------------------------------
print(type(10))  # int => integer
print(type(200)) # int => integer
print(type(-10)) # int => integer

print(type(10.5)) # float => floating point Number
print(type(3.14)) # float => floating point Number
print(type(-10.5))# float => floating point Number

print(type("Hello")) # str => string
print(type('A'))     # str => string     #in Python there is no char data type the character is a string 

print(type( [1, 2, 3, 4, 5] )) # list => list

print(type( (1, 2, 3, 4, 5) )) # tuple => tuple

print(type( { "name": "abdallah", "age": 20, "country": "Egypt", "one": 1 } )) # dict => dictionary

print(type( 2==2 )) # bool => boolean (True, False)
print(type( 2==4 ))  # bool => boolean (True, False)

print(type(False)) # bool => boolean (True, False)