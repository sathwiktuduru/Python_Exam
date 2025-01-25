def second_largest(numbers):
    #The number which is 2nd larget in the list is printed
    if len(numbers)<2:
        return 0
    first=0
    second=0
    for i in numbers:
        if i>first:
            second=first
            first=i
        elif first>i>second:
            second=i
    return second

def main():
    print("Enter the list of numbers: ")
    numbers=list(map(int,input().split()))
    second_number=second_largest(numbers)
    if second_number == 0:
        print("There is no second largest")
    else:
        print(f"The second largest number is: {second_number}")   
main()