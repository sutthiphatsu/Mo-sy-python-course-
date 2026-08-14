#เขียนฟังชั่นแปลงหน่วยสกุลเงินที่สามารถแปลงเงินจาก Thb <-> Usb=35,Thb<->Jyp 100=22thb
def funtion_convers_THB_To_USB(Money):
    USB=Money//35
    return USB
def funtion_convers_USB_To_THB(Money):
    THB=Money*35
    return THB
def funtion_convers_THB_To_JPY(Money):
    JPY=Money/22*100
    return JPY
def funtion_convers_JPY_To_THB(Money):
    THB=Money/100*22
    return THB
op=int(input("choose you money to change:\n1.THB to USB\n2.THB to JPY\n"))
if op == 1:
    sec_op=int(input("choose you option to change:\n1.THB TO USB\n2.USB to THB\n"))
    if sec_op == 1:
        Money=int(input("Enter your money:"))
        result=funtion_convers_THB_To_USB(Money)
        print(f"THB to USB:{result}")
    elif sec_op ==2:
        money=int(input("Enter your money:"))
        funtion_convers_USB_To_THB(money)
        result=funtion_convers_THB_To_USB(Money)
        print(f"USB to THB:{result}")
if op == 2:
    sec_op=int(input("choose you option to change:\n1.THB TO USB\n2.USB to THB\n"))
    if sec_op == 1:
        money=int(input("Enter your money:"))
        funtion_convers_THB_To_JPY(money)
        result=funtion_convers_THB_To_JPY(Money)
        print(f"THB to JPY:{result}")
    elif sec_op ==2:
        money=int(input("Enter your money:"))
        funtion_convers_JPY_To_THB(money)
        result=funtion_convers_JPY_To_THB(Money)
        print(f"JPY to THB:{result}")
        