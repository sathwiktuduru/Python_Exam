def password_strength(password):
    #The strenght of the password is notified by the use, if the password strenght is low then it show low and if the password strength is good then it displays strength is high
    digits="0123456789"
    password_length=len(password)
    uppercase_count=0
    lowercase_count=0
    digits_count=0
    special_character_count=0
    for char in password:
        if char.isupper():
            uppercase_count +=1
        elif char.islower():
            lowercase_count +=1
        elif char in digits:
            digits_count +=1
        else:
            special_character_count +=1
    if password_length>=8 and uppercase_count>0 and lowercase_count>0 and digits_count>0 and special_character_count>0:
        print("Password strength is high")
    elif password_length>=8 and uppercase_count>0 and lowercase_count>0 and digits_count>0 and special_character_count < 0:
        print("assword strength is medium")
    else:
        print("Password strength is low")
        
def main():
    password=input("Enter the password")
    password_strength(password)
main()