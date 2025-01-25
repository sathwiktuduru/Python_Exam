#Gives a idea about that a person can get the loan or not when applied
salary=int(input("Enter the salary: "))
age=int(input("Enter the age: "))
credit_score=int(input("Enter the credit score: "))
if(salary<20000 and age<18 and credit_score<700):
    print("Not Eligible for loan as you are not meeting the Salary, Age, Credit score requirements")
elif(salary>20000 and age>18 and credit_score>700):
    print("Eligible for Loan")
