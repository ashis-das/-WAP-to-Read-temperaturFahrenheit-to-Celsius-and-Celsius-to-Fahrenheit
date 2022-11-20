# WAP to Read temperature fahrenheit to Celsius and Celsius to fahrenheit
#take two user input
temp1 = int(input("Input the  temperature in Fahrenheit: "))
temp2=int(input("Input the  temperature in celcius: "))
print("conversion from fahrenheit to celcius")
celcius = (5/9) * (temp1 - 32)
print("The temperature in celcious",celcius ,"degrees.")
print("conversion from celcius to fahrenheit")
fahrenheit = (9/5) * (temp2) + (32)
print("The temperature in fahrenheit",fahrenheit ,"F.")