# Calculations
##multiplication = 10 * 10
##division = 10 / 10
##addition = 10 + 10
##subtraction = 10 - 10
##print(multiplication)
##print(division)
##print(addition)
##print(subtraction)

# ORDER of Operations

##op_1 = 5 + 30 * 20
##op_2 = (5 + 30) * 20

##print(op_1, op_2)

# Nested paranthesis 
##print(((5 + 30) * 20 ) / 10)
# Without nesting
##print(5 + 30 * 20 / 10)

# Variables
##hundred = 100
##print(hundred + hundred)
##print(2==3)
##f2 = 2==3

##if f2 == False:
##    print('f2 is false')

##hun = 100
##hun = 200
##print(hun)

##john = 100
##fred = john
##print(fred)

##num_cn = 200
##print(num_cn)

##found_coins = 20
##magic_coins = 10
##stolen_coins = 2

##print(found_coins + magic_coins * 365 - stolen_coins * 52)

# Strings, Lists, Tuples, and Maps

##str = 'My favorite food is pizza.'
##str2 = "My favorite food is burgers."
##str3 = '''How do dinosaurs pay their bills?
##With tyrannosaurus checks!'''
##print(str, str2)
##print(str3)

##conf_string = 'He said, "Aren't can't shouldn't wouldn't."'
##conf_string = "He said, "Aren't can't shouldn't wouldn't.""
##conf_string = '''He said, "Aren't can't shouldn't wouldn't."'''
##conf_string = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
##conf_string = "He said, \"Aren't can't shouldn't wouldn't.\""
##print(conf_string)

##gorilla = 'trouble'
##print(gorilla)


# Embedded Values in Strings (string substitution)

##myname = 'invQ'
##message = 'My name is %s'

##print(message % myname)

##myscore = 1000
##message = 'You have %s points'
##print(message % myscore)

##jkTxt = '%s: a device for finding furniture in the dark. %s also'
##bdPt1 = 'Knee'
##bdPt2 = 'Shin'
##print(jkTxt % bdPt1)
##print(jkTxt % bdPt2)
##print(jkTxt % (bdPt1, bdPt2))

# Multiplying strings

##print(10 * 'a')

##spaces = ' ' * 25
##print('%s 12 Butts Wynd' % spaces)
##print('%s West Snoring' % spaces)
##print()
##print()
##print('Dear Sir')
##print('')
##print('I wish to report that tiles are missing from the')
##print('outside toilet roof')
##print('I think it was bad wind the other night that blew them away.')
##print('')
##print('Regards')
##print('Malcolm Dithering')

##print(1000 * 'snirt')


# Lists

##wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
##from operator import itemgetter
##wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
##wizard_list[2] = 'David Goggins'
##wizard_list[0] = 'snail tongue'
##print(itemgetter(0, 2)(wizard_list))

##wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
##print(wizard_list[2:5])

##smNum = [1, 2, 5, 10, 20]
##smStr = ['Which', 'Witch', 'Is', 'Which']
##nmStrList = ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]

##print(smNum, smStr, nmStrList)

##nums = [1, 2, 3, 4, 5, 6, 120321]
##strgs = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
##numsStrgs = [nums, strgs]
##print(numsStrgs)

# Addings Items to a List


##wizard_list.append('bear burp')
##print(wizard_list)

# .append function at the end of a list variable adds whatever is in between the ()

##wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']

##wizard_list.append('mandrake')
##wizard_list.append('hemlock')
##wizard_list.append('swamp gas')

##print(wizard_list[3])
##del wizard_list[3]
##print(wizard_list[3])

##print(wizard_list)
##del wizard_list[8]
##del wizard_list[7]
##del wizard_list[6]
##print(wizard_list)

##list1 = [1, 2, 3, 4, 5]
##list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
##list3 = list1 + list2

##print(list1 + 20)
##FINALa = [list1, list2]
##print(FINALa)
##print(list1 + list2)

##fibs = (0, 1, 1, 2, 3)
##fibs[3] = 59 ~ attempt at overiding a tuple element
##print(fibs[3])


# Maps 

##favSports = ['Ralph Williams, Football',
##             'Michael Tippett, Basketball',
##             'Edward Edgar, Baseball',
##             'Rebecca Clarke, Netball',
##             'Ethel Smyth, Badminton',
##             'Frank Bridge, Rugby']

##print(favSports)

favSports = {'Ralph William' : 'Football',
             'Michael Tippett' : 'Basketball',
             'Edward Edgar' : 'Baseball',
             'Rebecca Clarke' : 'Netball',
             'Ethel Smyth' : 'Badminton',
             'Frank Bridge' : 'Rugby'}

favColors = {'Malcolm Warner' : 'Pink Polka dots',
             'James Baxter' : 'Orange striples',
             'Sue Lee' : 'Purple paisley'}

#~ Cannot add together Maps
##favMaps = favSports + favColors
##print(favMaps)

print(favSports['Frank Bridge'])
##del favSports['Frank Bridge']
favSports['Frank Bridge'] = 'Ice Hockey'
print(favSports['Frank Bridge'])