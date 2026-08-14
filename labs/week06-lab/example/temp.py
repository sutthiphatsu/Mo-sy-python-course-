def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temp, scale):
    """Converts temperature between scales"""
    if scale.upper() == "C":
        converted = celsius_to_fahrenheit(temp)
        return f"{temp}°C = {converted:.1f}°F"
    elif scale.upper() == "F":
        converted = fahrenheit_to_celsius(temp)
        return f"{temp}°F = {converted:.1f}°C"
    else:
        return "Invalid scale. Use 'C' or 'F'"

print("Temperature Converter:")
print(convert_temperature(25, "C"))
print(convert_temperature(77, "F"))
print(convert_temperature(0, "C"))
print(convert_temperature(32, "F"))
print()

#เขียนฟังชั่นแปลงหน่วยสกุลเงินที่สามารถแปลงเงินจาก Thb <-> Usb=35,Thb<->Jyp 100=22thb
def funtion_convers_THB_To_USB(Money):
    USB=money*35
    return USB
def funtion_convers_USB_To_THB(Money):
    THB=money%35
    return THB
def funtion_convers_THB_To_JPY(Money):
    JPY=money/22*100
    return JPY
def funtion_convers_JPY_To_THB(Money):
    THB=money/100*22
    return THB
op=int(input("choose you money to change:\n1.THB to USB\n2.THB to JPY"))
if op == 1:
    sec_op=int(input("choose you option to change:\n1.THB TO USB\n2.USB to THB"))
    if sec_op == 1:
        money=int(input("Enter your money:"))
        funtion_convers_THB_To_USB(Money)
    elif sec_op ==2:
        money=int(input("Enter your money:"))
        funtion_convers_USB_To_THB(Money)
if op == 2:
    sec_op=int(input("choose you option to change:\n1.THB TO USB\n2.USB to THB"))
    if sec_op == 1:
        money=int(input("Enter your money:"))
        funtion_convers_THB_To_JPY(Money)
    elif sec_op ==2:
        money=int(input("Enter your money:"))
        funtion_convers_JPY_To_THB(Money)
        
