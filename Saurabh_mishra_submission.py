aDict = dict()
file = open("airlines.csv","r")#place the .csv in the same file
#driver function for all the work simultaneously(min,max too)
for i in file:
    i = i.split(",")
    air_name = str(i[1]+","+i[2])[1:-1]
    if aDict.get(air_name):
        aDict[air_name] += 1
    else:
        aDict[air_name] = 1
#removing first extra line
aDict.pop("irport.Name,Time.Yea")

print(aDict,"\n")#All airport names

minimum = min(list(aDict.values()))#minimum value
maximum = max(list(aDict.values()))#maximum value

#finding min and max airport name
for i in aDict:
    if aDict[i] == minimum:
        minimum = i
    if aDict[i] == maximum:
        maximum = i

#printing min and max airport names
print(minimum,aDict[minimum])
print(maximum,aDict[maximum])

