# Clifton Lindsey
# CSC 499 Career Prep
# October 20, 2021
# written on MacOS Big Sur so hopefully it will run in linux

# function for sort
def sort(fileIn):

    # read in the text file
    inFile = open(fileIn)
    text = []

    # for loop that adds the names/words to the text array
    for words in inFile:
        temp = words.split()
        for i in temp:
            text.append(i)

    # closes the read in document
    inFile.close()

    # sorts the text that was read in alphabetical order
    text.sort()

    # sorts the text by length of name/word and sets the result as an array, shortest first
    sortedText = sorted(text, key = len)

    # creates word document that will be wrote to and sets it as a variable
    fileOut = open("output.txt", "w")

    # for loop to iterate through the sorted array and write it to the output file
    for i in sortedText:
        fileOut.writelines(i)
        fileOut.writelines("\n")

    # closes the output file
    fileOut.close()

sort("Sort Me.txt")

