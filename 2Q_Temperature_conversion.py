def fahrenheit_celcius(temperature):
    # converting temperature from fahrenheight to celcius
    celcius=(temperature-32)*(5/9)
    return celcius

def fahrenheit_kelvin(temperature):
    # converting temperature from fahrenheit to kelvin
    kelvin=(temperature-32)*(5/9) + 273.15
    return kelvin
    
def celcius_fahrenheit(celcius):
    # converting the temperature from celcius to fahrenheit
    fahrenheit=(9/5)*celcius+32
    return fahrenheit

def celcius_kelvin(celcius):
    #converting the temperature from celcius to kelvin
    kelvin = celcius + 273.15
    return kelvin

def kelvin_fahrenheit(kelvin):
    #converting the temperature from kelvin to fahrenheit
    fahrenheit=(kelvin-273.15)*1.8+32
    return fahrenheit

def kelvin_celcius(kelvin):
    # converting the temperature from kelvin to celcius
    celcius=kelvin-273.15
    return celcius

def main():
    #Takes the input from use and convert the temperature with accordingly to get temperature in other two formats
    print("Enter 1 to convert Celcius to other temperature")
    print("Enter 2 to convert Fahrenheit to other temperature")
    print("Enter 3 to convert Kelvin to other temperature")
    choice=int(input("Enter the choice: "))
    temperature=int(input("Enter the temperature: "))
    if(choice==1):
        fahrenheit=celcius_fahrenheit(temperature)
        kelvin=celcius_kelvin(temperature)
        print(f"Temperature from celcius to fahrenheit: {fahrenheit}")
        print(f"Temperature from celcius to kelvin: {kelvin}")
    elif(choice==2):
        celcius=fahrenheit_celcius()
        kelvin=fahrenheit_kelvin()
        print(f"Temperature from fahrenheit to celcius: {celcius}")
        print(f"Temperature from fahrenheit tp kelvin: {kelvin}")
    elif(choice==3):
        celcius=kelvin_celcius()
        fahrenheit=kelvin_fahrenheit()
        print(f"Temperature from kelvin to celcius: {celcius}")
        print(f"Temperature from kelvin to fahrenheit: {fahrenheit}")
    else:
        print("Option not available")
main()
        
        
        