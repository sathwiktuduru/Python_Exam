def factorial(number):
    #The number itseld multiplied and stored until it reaches 1
    if number < 0:
        return 0
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def main():
    number = int(input("Enter a number: "))
    # print(f"The factorial of {number} is {factorial(number)}")
    check=factorial(number)
    if check:
        print(f"Factorial of {number} is {check}: ")
    else:
        print("Factorial connot be performed on negative numbers")
main()