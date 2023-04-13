#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # myFile = open("textfile", "w+")
    
    # Open the file for appending text to the end
    # myFile = open("textfile", "a+")

    # write some lines of data to the file
    # for i in range(10):
    #     myFile.write("This is some new text\n")
    
    # close the file when done
    # myFile.close()
    
    # Open the file back up and read the contents
    myFile = open("textfile", "r")
    if myFile.mode == 'r':
        # contents = myFile.read()
        # print(contents)
        fileLine = myFile.readlines()
        for x in fileLine:
            print(x)
    
if __name__ == "__main__":
    main()
