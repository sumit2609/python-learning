class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def show(self):
        print("Name: ",self.name)
        print("roll number: ",self.rollno)

name = input("enter name")
rollno = input("enter roll number")

ob = student(name,rollno)
ob.show()