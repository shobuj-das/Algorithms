
def checkPalindrome(number):
    actualNumber = number
    result = 0

    while number > 0:
        reminder = number % 10
        result = (result * 10) + reminder
        number = int(number / 10)

    if actualNumber == result:
        return "Palindrome"
    else:
        return "Not Palindrome"

number = int(input("enter number: "))
print(checkPalindrome(number))