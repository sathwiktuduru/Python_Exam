import math
def is_prime(n):
    #From the given range each number is checked and notifies the number is prime or not
    flag=True
    i=2
    while(i<int(math.sqrt(n)+1)):
        if n%i==0:
            flag=False
            break
        i=i+1
    return flag

def main():
    start=int(input("Enter the starting range: "))
    end=int(input("Enter the ending range: "))
    count=0
    #if the number is prime and present in the given range, then the number is displayed in terminal
    for i in range(start,end):
        check=is_prime(i)
        if check==True:
            print(f"{i} is prime number")
main()