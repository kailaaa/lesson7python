print('-' * 65)
print('100th Birthday Program: ')
print('Description: this program asks you for your current age and tells you the year that you will turn 100.')

age = input('What is your age today? ')
age = int(age)

year = (100 - age) + 2018

year = str(year)
print('You will turn 100 in the year ' + year)
print('-' * 65)