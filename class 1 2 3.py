##### # class 1  # #####

'''
print("Hey Jibon.","How are you?","123")
print(4+5)
print("Jibon" - "Jubayer")
'''
# variable in python
var_1 = "Jibon"
var_2 = "Jubayer"
x = 7
y = 2
print(var_1+" " +var_2)
print(id(x))
print(x-y)
print(x**y)
print(x/y)
print(x//y)

##### # class 2  # #####

# assigenment operators
#  =, +=, -=
'''
var_1 = "Jibon"
var_2 = 10
print(var_2)
var_2 += 5 # var_2 = var_2 + 5
print(var_2)
var_2 -= 7 # var_2 = var_2 - 7
print(var_2)
'''
# comparison operators
# ==, !=, >, <, >=, <=
'''
var_1 = 25
var_2 = 33
print(var_1 == var_2) # false
print(var_1 == 25) # true
print(var_2 != var_1) # true
print(var_1 > var_2) # false
print(var_1 < var_2) # true
print(var_1 >= var_2) # false
print(var_1 <= var_2) # true
'''

# logical oprators
# and, or, not
'''
var_1 = 13
var_2 = "Male"
print(var_1 >= 14 and var_2 == "Male") # false
print(var_2 == "Male" or var_2 == "Female") # true
print(not(var_1 >= 14 and var_2 == "Male")) # true
print(not(var_1 != 10)) # false
'''

# string is a boject.
# membership opreators
# in, not in
'''
var_1 = "Jibon"
var_2 = "i"
var_3 = "j"
var_4 = "e"
print(var_2 in var_1) # true
print(var_3 in var_1) # false
print(var_4 in var_1) # false
print(var_4 not in var_1) # true
'''
# is, is not
# is --> ==
# is not --> !=
var_1 = 10
var_2 = 10
print(var_1 is var_2) # false



##### # class 3  # #####

# true = 1
# false = 0

# bit waise opreators
# &, |, ^
# & -> and
# | -> or
# ^ -> xor
# convert in to binary:
var_1 = bin(10)
# 1010
# 1010
#and
# 1010
print(var_1)

print( 10 & 10) 
print(10 | 7)
print(10 ^ 7)
