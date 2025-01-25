def separate_odd_even(numbers):
    #From the given list of numbers, each number present in the list are separated in even if the number divisible by and if not it is stored in odd numbers list
    odd_numbers = []
    even_numbers = []
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    print(f"Odd numbers are: {odd_numbers}")
    print(f"Even numbers are: {even_numbers}")

# Example usage
def main():
    print("Enter numbers separated by space: ")
    numbers=list(map(int,input().split()))
    separate_odd_even(numbers)
    
main()