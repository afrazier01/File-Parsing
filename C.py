#c)
##Write a program that requests the names of two
##countries and an amount of money, and then converts
##the amount from the first country’s currency to the
##equivalent amount in the second country’s currency.

#open file
xfile = open('Exchrate.txt')

##Get user inputs
userCountry1 = input('Enter name of first country: ')
userCountry2 = input('Enter name of second country: ')
currencyConversion = float(input('Amount of money to convert: '))



##get currency
for line in xfile:
    line = line.rstrip()
    if line.startswith(userCountry1):
        countryArray = line.split(',')
        currency1 = countryArray[1]
        exchange1 = float(countryArray[2])
    if line.startswith(userCountry2):
        countryArray2 = line.split(',')
        currency2 = countryArray2[1]
        exchange2 = float(countryArray2[2])



##calculation
conversionSoln = (currencyConversion * (1/exchange1))/(1/exchange2)



#format output
conversionSoln = round(conversionSoln,2)
print(round(currencyConversion), currency1.lower()+'s', 'from', userCountry1, 'equals', '{:,}'.format(conversionSoln), currency2.lower()+'s', 'from',userCountry2)
#https://www.geeksforgeeks.org/python-add-comma-between-numbers/

