# If statement

numVar = 20

if numVar > 10: # runs when true
    print("numVar is greater than 10")

print()
print()

# Equal to
if numVar == 20:
    print("Equal to 20")
    
# Not Equal to 
if numVar != 30:
    print("Not equal to 30")

# Greater than
if numVar > 5:
    print("Greater than 5")

# Less than
if numVar < 70:
    print("Less than 70")

# Greater than or equal to
if numVar >= 20:
    print('numVar is either greater than or/and equal to 30')
    
# Less than or equal to

if numVar <= 30:
    print('numVar is less than or equal to 30')

#
print()
print()


# Else

password = 'password'

if password == 'password':
    print('Access granted')
else:
    print('Incorrect password')
    
print()
print()


# Elif

password = 'adsasdasdasdasdas'

if password == 'password':
    print('Access granted')
elif password == 'secretpassword':
    print('Secret admin access')
elif password == 'bad':
    print('you will be terminated')
else:
    print('incorrect password')

print()
print()

#

# Combining conditions

num = 200

if num >= 200 or num < 200 or num == 300:
    print('Favorite number is 200')
else:
    print('Error')
    
# and condition

ASK = False

if ASK == False and num == 200:
    print('Granted. ASK: %s. num: %s.' % (ASK, num))
    
#
print()
print()
print()
# None value

NOVAL = None

print(NOVAL)

#print(NOVAL == None)

if NOVAL == None:
    print(NOVAL != None)
    
#
print()
print()
print()
#

## Variable type conversion

# String
NUMBER = str(20)
if NUMBER == '20':
    print('NUMBER val has been converted into a string.')
print()
print()
print()

# int
STRING = '20'
STRINGNUM = int(STRING)

print(STRINGNUM == 20)

if STRINGNUM == 20:
    print('STRINGNUM has been converted into 20')
    
FLOATNUM = '10.5'
CONVERTED_FLOATNUM = float(FLOATNUM)

if CONVERTED_FLOATNUM == 10.5:
    print("FLOATNUM has been converted into a float variable type.")
    
#
space = ' ' * 99
print(space)
#

# CHALLENGE 1:
#money = 2000
#if money > 1000:
#    print("I'm rich!")
#else:
#    print("I'm not rich!")
#     print("But I might be later...")
# Correctly predicted output


# CHALLENGE 2: (Twinkies check)
twinkies = 501

if twinkies < 100 or twinkies > 500:
    print('Too few or too many')
else:
    print("Just perfect")
    
# CHALLENGE 3: (Money check)
money = 5001

if money > 100 and money < 500 or money > 1000 and money < 5000:
    print("Money check successful")
else:
    print("Unsuccessful money check")
print(space)
print(space)

# CHALLENGE 4: (Ninja check)

ninjas = 11

ninjas = 9

if ninjas < 10:
    print("I can fight those ninjas!")
elif ninjas < 30:
    print("It'll be a struggle, but I can take 'em")
elif ninjas < 50:
    print("That's too many")


