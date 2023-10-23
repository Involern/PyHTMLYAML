## Strings. Variable type that uses text only.

doublequote_String = "This is a string with double quotes."
singlequote_String = 'This is a string with single quotes.'
triplequote_String = '''This is a string
with triple quotes.'''

print(doublequote_String)
print(singlequote_String)
print(triplequote_String)
print()
print()

## Strings with apostrophes inside

apos_String = '''"Aren't, can't, shouldn't, wouldn't'''
print(apos_String)
single_quote_str = '"Aren\'t, can\'t, shouldn\'t, wouldn\'t"'
double_quote_str = "\"Aren't, can't, shouldn't, wouldn't.\""
print()
print(single_quote_str)
print(double_quote_str)
print()
print()

## Embedded values in strings.

score = 1000
name = "PLAYER"
text = "Your score: %s. Player Name: %s"
print(text % (score, name))
print()
print()

## Multiplying strings

print(10 * 'a') # Output is "aaaaaaaaaa"
print()
print()

## Lists

animal_List = ['Lion', 'Tiger', 'Dog', 'Turtle', 'Lizard', 'Eagle', 'Snail']
print(animal_List)
print()
print()

print(animal_List[2]) # Prints third item in the animal_List, which is 'Dog'
animal_List[2] = 'Cat'
print(animal_List[2]) # Prints 'cat', which is now the new value in the 2nd index of the list.


print(animal_List[2:5]) # Prints the 3rd item of the list up to the 5th (Dog, Turtle, Lizard)
print()
print()

# New Lists

some_numbers = [1, 2, 3, 4, 5] # Exclusively numbers
some_strings = ['I', 'am', 'awesome'] # Exclusively strings
nums_and_strings = ['I', 2, 3, 4, 'awesome'] # Numbers and strings
print(some_numbers)
print(some_strings)
print(nums_and_strings)
print()

NS_1 = [some_strings, some_numbers] # A list that stores other lists

print(NS_1)
print()
print()

# Adding items to a list using .append() function

animal_List.append("Wolf")
print(animal_List)

# Removing items using the del command

del animal_List[2] # Removes 'dog' or 'cat' from the list
print(animal_List)

# Joining lists using arithemtic

list1 = [1, 2, 3, 4]
list2 = ['words', 'in', 'a', 'list']
list3 = list1 + list2 # Adds both lists together
# Storing these items inside of a list itself while adding is unnecessary
print(list3)
print()
print()
print(list1 * 3) # Multiplies the list 3 times
print()
print()

# Note, division and subtraction does not work in lists.
# Adding anything to a list that is not a list also does not work.

## Tuple; like a list with parentheses
tup = (1, 2, 3, 4, 5)
print(tup[2]) # prints 3 from the tuple
print()
print()

#tup[2] = 'awesome' # results in an error because tuples cannot be set to anything else


## Maps/dict (dictionary)

donut_Orders = {
    'John': 'Plain with glaze',
    'Samantha' : 'Strawberry icing with sprinkles',
    'Rick' : 'Chocolate icing'
}

print(donut_Orders['John']) # Gets the value using the "John" key
print()
print()

# To delete a value from a map, use the key in the del command
del donut_Orders['John']
# print(donut_Orders['John']) # Results in an error because 'John' no longer exists in the dict
print(donut_Orders)
print()
print()


## Challenge 1
games = ['Video games', 'Working out', 'Clay modeling', 'Programming', 'Self improvement']
foods = ['Donut', 'Strawberry', 'Banana', 'Cookies', 'Eggs']
favorites = games + foods

print(favorites)
print()
print()

## Challenge 2
ninja = 3 * 25
samurai = 2 * 40
battleText = 'There are %s ninjas and %s samurai about to do battle.'
print(battleText % (ninja, samurai))

## Challenge 3
firstName = 'Brando'
lastName = 'Ickett'
print('Hi there, %s %s' % (firstName, lastName))