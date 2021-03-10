# if statement
def Equal(param1, param2, param3):
    if int(param1) == int(param2) or int(param1) == int(param3) or int(param2) == int(param3) or int(param1) == int(param2) == int(param3):
        return True
    else:
        return False

print(Equal(6,5,"5"))
