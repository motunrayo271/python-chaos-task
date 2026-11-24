
    word = input("Enter word: ")
    reverse =""
    for character in word:
	    reverse = character + reverse;

        if reverse != word:
            print("it is not a palindrome")
        else :
            print("it is a palindrome")
