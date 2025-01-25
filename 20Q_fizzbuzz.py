#if the number is divisible by both 3 and 5 then it is buss. If the number only divisible by 3 fizz. If the number only divisible by 5 then it is Buzz
number=int(input("Enter a number: "))
if(number%3==0 and number%5==0):
    print("FizzBuzz")
elif(number%5==0):
    print("Buzz")
elif(number%3==0):
    print("Fizz")
else:
    print("Not multiple of 3 or 5")