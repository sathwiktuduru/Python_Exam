#Bill splitter can be used to calculate the amount that each person needs to be paid by including all the expenses
bill=int(input("Enter the total bill amount: "))

persons=int(input("Enter the number of persons: "))

tip=int(input("Enter the tip percentage: "))

tip_amount=(tip/100)*bill

total_bill=(bill+tip_amount)/persons

print(f"Amount each person has to pay: {total_bill}")