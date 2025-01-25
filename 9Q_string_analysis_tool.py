def string_analysing(string):
    #Analyzing the given string and displaying each and every required information this function is used
    vowels="aeiouAEIOU"
    numbers="0123456789"
    vowel_count=0
    digit_count=0
    consonant_count=0
    special_character_count=0
    for char in string:
        if char in vowels:
            vowel_count +=1
        elif char in numbers:
            digit_count +=1
        elif char.isalpha():
            consonant_count +=1
        else:
            special_character_count +=1
    reverse_string=string[::-1]
    #It helps in identifying the numbers of vowels, consonant, digits, special character are present in the string
    print(f"Vowels present: {vowel_count}")
    print(f"Consonant count: {consonant_count}")
    print(f"Digits count: {digit_count}")
    print(f"Special character count: {special_character_count}")
    print(f"String after reverse: {reverse_string}")
    
def main():
    string=input("Enter the string: ")
    string_analysing(string)
main()