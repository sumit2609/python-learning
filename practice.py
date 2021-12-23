class student:
    name = "Sumit Sharma"
    __rollno = "ue198105"

    def __show(self):
        print("Name: ", self.name)

    def display(self):
        print("Roll number: ", self.__rollno)
        self.__show()


ob = student()
# ob.__show()
ob.display()


class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print("Name: ", self.name)
        print("roll number: ", self.rollno)


name = input("enter name ")
rollno = input("enter roll number ")

ob = student(name, rollno)
ob.show()
