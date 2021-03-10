# dictionaries and sets
D = {"Artist":"Celine Dion", "SongName":"To Love You More", "Gendre":"Pop", "YearRelease":1993, "DurationInSec":328, "Album":"The Colour of My Love"}

for pair in D.items():
    print(pair)

def Func(Key, Value):
    for i in D:
        if i == Key and D[i] == Value:
            return True
        else:
            return False

print(Func("Artist", "Justin Bieber"))
