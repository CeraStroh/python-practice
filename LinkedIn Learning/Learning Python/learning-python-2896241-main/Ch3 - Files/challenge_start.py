# results -> results.txt that gives bytecount, lists all files
import os

def main():
    bytecount = 0
    dirlist = os.listdir()
    for entry in dirlist:
        if os.path.isfile(entry):
            filesize = os.path.getsize(entry)
            bytecount += filesize
    os.mkdir("result")
    myFile = open("results/results.txt", "w+")
    if myFile.mode == "w+":
        myFile.write("Total bytecount:" + str(bytecount) + "\nFiles list:\n")
        for i in range(10):
            myFile.write("-")
        myFile.write("\n")
        for entry in dirlist:
            if os.path.isfile(entry):
                myFile.write(entry + "\n")

    myFile.close()

if __name__ == "__main__":
    main()