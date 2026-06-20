#------------------------------------------
#----Variables----
#------------------------------------------
# Syntax => [Variable Name] = [Value]
#
# Name conventions and rules:
# [1] can start with [a-z, A-Z] or Underscore [_]
# [2] you cannot start with [0-9] or special characters [!, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /, ~, `]
# [3] can contain [a-z, A-Z, 0-9] or Underscore [_]
# [4] case-sensitive [name, Name, NAME] are different variables
# [5] cannot use Python keywords (reserved words) [False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield]
# [6] cannot use spaces
# [7] you cannot use a variable before declaring it

name = "Abdallah"      # single word variable => normal
userName = "Abdallah"  # two words => camelCase variable
user_name = "Abdallah" # two words => snake_case variable

print(name)
print(userName)
print(user_name)