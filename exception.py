try:
    frist = float(input("Enter Number: "))
    sec = float(input("Enter Number Again: "))
    last = input("Enter + - * /: ")
    final = 0

    if last == "+":
        final = frist + sec
    elif last == "-":
        final = frist - sec
    elif last == "*":
        final = frist * sec
    elif last == "/":
        final = frist / sec
    else:
        raise ValueError("+ - * /")
except ZeroDivisionError:# กรณีผู้ใช่หารด้วย 0
    print("หารด้วย0ไม่ได้")
except ValueError: # กรณีผู้ใช้ไม่ยอมใส่เลข
    print("ใส่เลข")
except Exception:#ไม่รู้
    print("กูไม่รู้")
else: #รู้
    print("Success!")
finally:#ปิดท้ายเสนอขึ้นตลอด
        print(f"{frist}{last}{sec}={final}\nจบการทำงาน")