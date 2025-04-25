def checkPalindrome(text):
    size = len(text)
    j = size - 1
    flag = True
    for i in range(size // 2):
        if text[i] == text[j]:
            j -= 1
            continue
        else:
            flag = False
            break

    if flag:
        print("Palindrome")
    else:
        print("Not Palindrome")


text = input("enter text: ")
checkPalindrome(text)