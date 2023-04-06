def main():
    word = input("Enter string to test for palindrome or 'exit':")
    test = ""
    if word == "exit":
        exit()
    elif word.isalnum:
        print("num")
    else:
        for w in word:
            test += w
        if test == word:
            print("Palindrome test: True")
        else:
            print("Palindrome test: False")

if __name__ == "__main__":
    main()