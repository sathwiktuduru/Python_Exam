#Taking the information about the students and marks of the student
student_name=input("Enter the student name: ")
print("Note: Marks should be ranging from 0-100")
subject_1=int(input("Enter marks of subject 1: "))
subject_2=int(input("Enter marks of subject 2: "))
subject_3=int(input("Enter marks of subject 3: "))
subject_4=int(input("Enter marks of subject 4: "))
subject_5=int(input("Enter marks of subject 5: "))
total_marks=(subject_1+subject_2+subject_3+subject_4+subject_5)
percentage=((subject_1+subject_2+subject_3+subject_4+subject_5)/500)*100
print(f"Total Marks: {total_marks}")
print(f"Percentage is: {percentage}")
#After calculating the percentage the grade are assigned as per the regulations
if percentage>=85:
    print("Grade: A")
elif percentage>=70 and percentage<85:
    print("Grage B")
elif percentage>=55 and percentage<70:
    print("Grade C")
else:
    print("Fail")