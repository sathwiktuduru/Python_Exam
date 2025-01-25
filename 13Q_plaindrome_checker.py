def is_palindrome(number):
    #If the reverse of a number is same and given number then it is a palindrome
    number_reverse=number[::-1] #The number is loaded in a variable in reverse format
    print(number_reverse)
    if number == number_reverse:
        return True
    else:
        return False
    
def main():
    while True:
        print("Enter number to check it is palindrom")
        print("Enter 0 to exit or quit")
        number=input()
        if number == '0':
            break
        if is_palindrome(number):
            print(f"{number} is palindrome")
        else:
            print(f"{number} is not plindrome")
main()