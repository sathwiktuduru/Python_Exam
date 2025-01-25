def table_generator(number,start,end):
    #According to the given range table is printed
    for i in range(start,end+1):
        answer=number*i
        print(f"{number} * {i} = {answer}")

def main():
    number=int(input("Enter the number to be multiplied: "))
    start=int(input("Enter the start range: "))
    end=int(input("Enter the end range: "))
    table_generator(number,start,end)
main()