# advanced loops
def Board(rows, coloumns):
    for row in range(rows+1):
        if row%2 == 0:
            for coloumn in range(coloumns+1):
                if coloumn % 2  == 1:
                    if coloumn != len(range(coloumns)):
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
            # print(" | | ")
            #      12345
        else:
            print(" ")
            print("-----")
    return True

Board(4, 4)
print("")
