Weight=float(input("how much your weight ?"))
Hight=float(input("how much your hight ?"))
Hight = Hight/100
BMI = Weight / (Hight ** 2)
print(f"BMI IS:{BMI:.1f}")
if BMI <= 18.5:
    print("Underweight")
elif BMI <=24.9:
    print("Nomal weight")
elif BMI <= 29.9:
    print("Overweight")
else:
    print ("Obese")  