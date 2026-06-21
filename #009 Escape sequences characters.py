#----------------------------------
#---Escape sequences characters---
#----------------------------------
# \b => Backspace
# \newline => Escape the newline + \
# \\ => Escape backslash
# \' => Escape single quote
# \" => Escape double quote
# \n => New line
# \r => carriage return
# \t => Horizontal tab
# \xhh => character Hex Value
#----------------------------------



# Backspace
print("Hello\bWorld")  # Output: HellWorld

# Escape the newline
print("i \
love  python")  # Output: i love python

# Escape backslash
print("\\Users\\Name")  # Output: \Users\Name

# Escape single quote
print('i love python \'programming\'')  # Output: i love python 'programming'

# Escape double quote
print("i love python \"programming\"")  # Output: i love python "programming"

# New line
print("Hello\nWorld")  # Output: Hello
                       #         World

# carriage return 
print("12345678\rABCD")  # Output: ABCD5678

# Horizontal tab
print("Hello\tWorld")  # Output: Hello   World

# character Hex Value
print("\x41\x23")  # Output: A#