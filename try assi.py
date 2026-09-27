def deposit(money):
    try:
        input_amount = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))

        if input_amount <= 0:
            raise ValueError("เกิดข้อผิดพลาด: จำนวนเงินฝากต้องมากกว่า 0")
        
        money += input_amount
        print("ฝากเงินสำเร็จ")
    
    except ValueError:
        print("จำนวนเงินฝากต้องมากกว่า 0")
    else:
        print(f"เงินคงเหลือ:{money}บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")
    return money

money = 1000.00
print(f"เงินคงเหลือ:{money}บาท")
deposit(money)
