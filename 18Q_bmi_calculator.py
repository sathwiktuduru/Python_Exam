#The BMI(Body Mass Index) calculates the body weight to mass ration and give the result 
weight=float(input("Enter your weight in pounds: "))
height=int(input("Enter your height in inches: "))
bmi=((weight*703)/height)/height

if bmi<=18.5:
    print(f"{bmi} Underweight")
elif bmi<=25 and bmi>18.5:
    print(f"{bmi} Normal")
elif bmi>25 and bmi<=30:
    print(f"{bmi} Overweight")
else:
    print(f"{bmi} Obese")