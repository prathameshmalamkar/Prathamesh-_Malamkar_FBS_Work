str = ('FirstBit Solutions')

#1. str.isupper() - Convert string into uppercase
print(str.isupper())

#2. str.islower() - Convert string into lowercase
print(str.islower())

#3. str.capitalize() - Convert first character to uppercase
print(str.capitalize())

#4. str.count() - Count the occurrence of a specified character or substring
print(str.count('Bit'))

#5. str.endswith() - Check whether string ends with specified value
print(str.endswith('ions'))

#6. str.find() - Returns the index of the first occurrence 
print(str.find('bit'))

#7. str.index() - Return the index of the first occurrence
print(str.index('Bit'))

#8. str.isalnum() - Check whether all characters are alphabets or numbers
print(str.isalnum())      # alphabetic or numeric

#9. str.isalpha() - Checks whether character are alphabets
print(str.isalpha())

#10. str.isdigit() - Check whether all character are digit
print(str.isdigit())

#11. str.isspace() - Check whether all character are spaces
print(str.isspace())

#12. str.join() - Joins elements using the specified separator 
data = ','.join(['101', 'ABC', 'IT'])
print (data)

#13. str.replace() - Replace a specified value with another value
print(str.replace('Bit', 'Byte'))

#14. str.split() - Splits the strings into a list
print(data.split(' , '))

#15. str.startswith() - Check whether strings starts with specified value
print(str.startswith('Fir'))

#16. str.lstrip() - Remove space from the left side
print(str.lstrip(    '[FirstBit solutions]'))  

#17. str.strip() - Remove space from both sides
print(str.strip(' []'))

#18. str.swapcase() - Convert uppercase to lowercase and lowercase to uppercase
print(str.swapcase())

#19. str.title() - Convert first character of each word to uppercase
print(str.title())

#20. str.rstrip() - Remove space from the right sides
print(str.rstrip('[FirstBit solution]'   ))  

