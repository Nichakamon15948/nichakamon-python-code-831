class ClassName:
    """Class docstring"""
    
    # constructor method
    def __init__(self, parameters): #ทุกอันต้องมีคำว่า self
        # Constructor method
        self.attribute = value

    
    def method_name(self):
        # Instance method
        return something


myObj = ClassName(parameters)  #สร้างวัตถุของclass
print(myObj.attribute) #การเข้าถึง
resultFromMethod = myObj.method_name()