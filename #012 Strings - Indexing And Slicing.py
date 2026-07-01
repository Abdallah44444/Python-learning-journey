#-------------------------------------
# Strings - Indexing and Slicing
# [1] All Data in Python is object
# [2] Object contain Elements 
# [3] Every ELement has Its own Index
# [4] Python used Zero-based Indexing (Index start from 0)
# [5] use square brackets to access elements of an object
# [6] Enable accessing parts of an object using slicing

# Indexing (Access sigle item)
myString = "I love python"

print(myString[0]) # Index 0 --> I
print(myString[9]) # Index 9 --> t

print(myString[-1]) # Index -1 --> n    First character from the end
print(myString[-3]) # Index -3 --> h    Third character from the end

# Slicing (Access multiple items)
# [Start:End] End not included
# [Start:End:Step] Step is optional
print(myString[8:11]) # Index 8 to 10 --> yth

print(myString[:10]) # if Start is not specified, it will start from the beginning
print(myString[5:]) # if End is not specified, it will go to the end 

print(myString[:]) # Full data

print(myString[0::1]) # Full data with step 1

print(myString[0::2]) # Full data with step 2 (every second character)

print(myString[::-1]) # Full data in reverse order

# print(myString[100]) # IndexError: string index out of range
print(myString[100:]) # returns empty string if index is out of range 
