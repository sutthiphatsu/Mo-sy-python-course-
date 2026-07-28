Choose = int(input("Choose conversion\n1.THB to USD\n2.USD To THB\n"))
if Choose == 1:
    print("35 THB = 1 USD")
    Money = int(input("how much you gonna exchange\n"))
    Money=Money/35
    print("Money=Money/35")
    print(f"you have {Money:.2f} USD")
if Choose == 2:
    print("1 USD = 35 THB")
    Money = int(input("how much you gonna exchange\n"))
    Money=Money*35
    print(f"you have {Money:.2f} THB")
    print("Money=Money*35")
