#a)
##Write a program that requests the name of a
##country as input and then displays the name
##of its currency and its exchange rate.


#open file
xfile = open('Exchrate.txt')

#get user input
userCountry = input('Enter the name of a country: ')

for line in xfile:
    line = line.rstrip()
    if line.startswith(userCountry):
        countryArray = line.split(',')

#format answer
print('Currency: ', countryArray[1], '\nExchange rate: ',countryArray[2])
        
