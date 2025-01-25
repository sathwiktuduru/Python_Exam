
def pattern_generate(n,reverse):
    #As per the user requirements the patter is either printed reverse or normal according to the user input
    if reverse:
        for i in range(n,0,-1):
            print('*'*i)
    else:
        for i in range(1,n+1):
            print('*'*i)

def main():
    number=int(input("Enter number of rows: "))
    reverse=int(input("Enter 1 for reverse or 0 for default: "))
    pattern_generate(number,reverse)
main()