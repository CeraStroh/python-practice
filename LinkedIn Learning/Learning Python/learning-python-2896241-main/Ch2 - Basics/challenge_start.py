def main():
    run = True
    
    while (run):
        word = input("Enter string to test for palindrome or 'exit':")
        test = ""
        if word == "exit":
            run = False
        elif word.isalnum():
            print("num")
        else:
            for w in word:
                test += w
            if test == test[::-1]:
                print("Palindrome test: True")
            else:
                print("Palindrome test: False")

if __name__ == "__main__":
    main()