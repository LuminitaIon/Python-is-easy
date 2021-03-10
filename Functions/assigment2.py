# functions
def Genre():
    print("Pop")

Genre()

def Artist():
    print("Celine Dion")

Artist()

def Year():
    print(1993)

Year()

def IsThatTheSong(Title):
    if Title == "To Love You More":
        return True
    else:
        return False

var = IsThatTheSong("To Love You More")
print(var)
var2 = IsThatTheSong("I surrender")
print(var2)
