"""
2 tpyes of promgaming
1) structurd progarmming ==> การเขียนโปรแกรมเชิงโครงสร้างทำงานจาก บน -> ล่าง ##C,java,PSP,python
2) object-oriented progarming ==> การเขียนโปรแกรมเชิงวัตถุ java,C#,python 
"""
# วิธีการแก้ปัญหา เป็นแนวทาง template แม่แบบ เป็นเหมือนตรายาง
class ClassName: 
    """Class docstring"""
    # ข้อมูลที่ต้องใช้ในการแก้ปัญหา ระบุไว้ใน construtor method ต้องมี (self):self.
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value
    # การกระทำ ==> method
    def method_name(self):
        # Instance method
        return something

    def method_name(self):
        pass

# การสร้างวัตถุคลาส ==> เอาคลาสมาใช้
myObj = ClassName(parameters)
# การใช้งานวัตถุจาก class
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method_name2()

myObj = ClassName(paraneters)
print(myObj2.attribute)
print(myObj2.method_name())
print.method_name2()