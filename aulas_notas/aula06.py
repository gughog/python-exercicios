# Conversion of types
# In an input we generally get and string, 
# but we can format this value to anoter primitive
# type.

# with this user input, we'll et a string
""" n1 = input('Digite o primeiro número:') """ 

# to confirm, execute this:
""" print(type(n1)) """

# Apllying the int() function will format the input.
""" 
n1 = int(input('Digite o primeiro número:'))
print(type(n1))
 """

# Mixing variables with strings; (desafio extra)
""" 
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
s = n1 + n2

print('A soma entre', n1, 'e', n2, 'é:', s)
 """

# Improving the code above:
""" 
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
s = n1 + n2
 """
#Here's the trick: with the double curly braces we define that'll be and variable here, and with '.format()' we pass these variables in the same order we need them to appear.
""" 
print('A soma entre {} e {} é: {}'.format(n1, n2, s))
 """

# We can check if a input is a number or not.
# If the input is a number it returns True, if It's not,
#returns False.
""" 
n = input('Digite algo:')
print(n.isnumeric())
 """

#We can check too if the input is string :
""" 
n = input('Digite algo:')
print(n.isalpha())
 """

# And we can ckeck too too if an input is aphanumeric (number or string). If it is a space or $, returns false.
""" 
n = input('Digite algo:')
print(n.isalnum()) 

"""

# Others methods:

"""

.isupper() -> Check if the string is written in capslock.
.islower() -> Makes the inverse of above.


"""