

class Employee:

    raiseAmount = 1.04  # class variable - some for all instances of the class

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + '.' + self.lname + '@company.com'

    def fullName(self):
        return f'{self.fname} {self.lname}'

    def applyRaise(self):
        self.pay = int(self.pay * Employee.raiseAmount)  
        # could use self.raisemount as well


emp_1 = Employee('Doug', 'Suida', 50000)
emp_2 = Employee('Stacy', 'Suida', 65000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullName())  # same output as line 22
print(emp_2.fullName())  # same output as line 23
print(Employee.fullName(emp_1))  # call class with method and pass in instance
print(Employee.fullName(emp_2))  # call class with method and pass in instance
print(emp_1.pay)  # print original pay
emp_1.applyRaise()  # apply method
print(emp_1.pay)  # print out new pay amount
