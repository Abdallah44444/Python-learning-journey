#--------------------------------
#-----concatenation-----
#--------------------------------



message = "Hello"
name = "abdallah" 

print (message + name)  # Output: Helloabdallah

print (message + " " + name)  # Output: Hello abdallah

print (message , name)  # Output: Hello abdallah but "," not concatenated it just print the two variables with a space in between

full = message + " " + name
print (full)  # Output: Hello abdallah 

a = "Hello \
world \
iam \
abdallah"

b = "1 \
2 \
3 \
4"
print(a + "\n" + b)

# print("Hello" + 123)  # Error: TypeError: can only concatenate str (not "int") to str 