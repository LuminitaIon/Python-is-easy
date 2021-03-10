# input/output 
import os.path
noteFile = input("Please enter a file name: ")

if os.path.isfile(noteFile) == True:
    # print("Exists")
    chosenMode = input("Please choose a letter: \nA) Read the file \nB) Delete the file and start over \nC) Append the file\n")
    if chosenMode == 'A':
        tempFile = open(noteFile, "r")
        print("The file content is: ", tempFile.read())
        # print(tempFile.read())
        tempFile.close()
    elif chosenMode == 'B':
        os.remove(noteFile)
        print("The file was removed and it was create a new file with the same name!")
        tempFile = open(noteFile, "w+")
        tempFile.close()
    elif chosenMode == 'C':
        tempFile = open(noteFile, "a")
        # inTxt = input("Add more text: ")
        tempFile.write(input("Add more text: " "\n"))
        # tempFile.write("\n")
        tempFile.close()

else:
    # print("Don't exists")
    myFile = open(noteFile, "w")
    myFile.write(input("Enter some text here: "))
    myFile.close()
