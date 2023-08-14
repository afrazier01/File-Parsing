#b)
##Write a program that displays the names of the countries in
##ascending order determined by the number of units that can
##be purchased for one American dollar. 

#open file
xfile = open('Exchrate.txt')

#remove currency from line and then store country and exchrate in a dictionary
xList = []
xDict = dict()
for line in xfile:
    line = line.rstrip()
    newLine = line.split(',')
    removeCurrency = newLine.remove(newLine[1])
    xList.append(newLine)
    country = newLine[0]

    if country not in xDict:
        xDict[country] = float(newLine[1])

#sort key based on value
sortxDict = sorted(xDict.items(), key=lambda x:x[1])

#create dictionary to format output
newDict = dict(sortxDict)
for key, value in newDict.items():
    print(key)

    

    
