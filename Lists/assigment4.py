# lists
myUniqueList = []
myLeftovers = []
def addThingsToList(elem):
    if elem in myUniqueList:
        myLeftovers.append(elem)
        return False
    else:
        myUniqueList.append(elem)
        return True

addThingsToList(1)
addThingsToList('string')
addThingsToList(1)
addThingsToList('unu')
addThingsToList('string')
print(myUniqueList)
print(myLeftovers)
