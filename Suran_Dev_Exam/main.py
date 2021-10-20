# Clifton Lindsey
# CSC 499 Career Prep
# October 20, 2021
# written on MacOS Big Sur so hopefully it will run in linux

# function for sort
def sort(fileIn, num):

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

    if (num == "1"):
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

    if (num == "2"):
        # sorts the text that was read in reverse-alphabetical order
        text.sort(reverse=True)

        # sorts the text by length of name/word and sets the result as an array, longest first
        sortedText = sorted(text, key=len, reverse=True)

        # creates word document that will be wrote to and sets it as a variable
        fileOut = open("reverseOutput.txt", "w")

        # for loop to iterate through the sorted array and write it to the output file
        for i in sortedText:
            fileOut.writelines(i)
            fileOut.writelines("\n")

        # closes the output file
        fileOut.close()


# boolean used to check input
correctInput = False

# prints options for user
print("1: Alphabetical sort, smallest to largest\n2: Reverse alphabetical sort, largest to smallest")

# gets user input
val = input("Choose option one or two: ")

if val == "1":
    correctInput = True

if val == "2":
    correctInput = True

# input check
while correctInput == False:
    print("Not a valid input\nPlease try again")

    # prints options for user
    print("1: Alphabetical sort, smallest to largest\n2: Reverse alphabetical sort, largest to smallest")

    # gets user input
    val = input("Choose option one or two: ")

    if val == "1":
        correctInput = True

    if val == "2":
        correctInput = True

# function call
if val == "1":
    print("option 1")
    sort("Sort Me.txt", val)

# reversed function call
if val == "2":
    print("option 2")
    sort("Sort Me.txt", val)

