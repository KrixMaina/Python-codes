import math
#create class Employee
class Employee:
    #define the constructors for the employee class
    def _init_(self, id, name):
        #assign the attributes provided
        self.id = id
        self.name = name
        self.id = input("Enter ID: ")
        self.name = input("Enter name: ")

#create another class Hourly_employee which inherits attributes and methods from the class Employee
class Hourly_employee(Employee):
    #initialize the newly added attributes
    def _init_(self, id, name, hours_worked, hourly_pay,hourly_rate):
        super().__init__(id,name)
        self.hours_worked = hours_worked
        self.hourly_pay = hourly_pay
        hourly_payroll = self.hours_worked *self.hourly_pay
        self.hours_worked = float(input("Enter hours worked: "))
        #the super function is called to call the constructors of the superclass(Employee) and passes the arguments id, name
        

    def calculate_pay(self):
        hourly_rate = float(input("Enter hourly rate: "))
        
        print("Hourly salary:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Hourly pay:", math.trunc(hourly_payroll))
        return
#calculate the payroll by multiplying hours worked and hourly pay,and also prints the employee details

#create another class Salary_employee which inherits attributes and methods from Employee class as well
class Salary_employee(Employee):
    def _init_(self, id, name, basic_salary, allowances):
        self.basic_salary = basic_salary
        self.allowances = allowances
        self.basic_salary = float(input("Enter basic salary: "))
        self.allowances = float(input("Enter allowances: "))
        #the super function is called to call the constructors of the superclass(Employee) and passes the arguments id, name
        super()._init_(id, name)

    def calculate_payroll(self):
        salary = self.basic_salary + self.allowances
        print("Basic salary:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", math.trunc(salary))
        return
#calculate the payroll by adding basic salary  and allowances to get total salary,and also prints the employee details
#create another class Commission_employee which inherits attributes and methods from Salary_employee class as well
class Commission_employee(Salary_employee):
    def _init_(self, id, name, commission_rate, basic_salary, allowances):
        self.commission_rate = commission_rate
        super()._init_(id, name, basic_salary, allowances) 
        self.commission_rate = float(input("Enter commission rate: "))
        #the super function is called to call the constructors of the superclass(Salary_employee) and passes the arguments id, name,basic_salary, allowances

    def calculate_payroll(self):
        commission = (self.basic_salary + self.allowances) * self.commission_rate
        print("Commission:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Commission:", math.trunc(commission))
        return
#calculate the payroll by adding basic salary  and allowances and multiply the total with commission rate to get total commission,and also prints the employee details
#the above lines of code prompt the user to input the employee details
Employeedetails1 = Hourly_employee()
Employeedetails1.calculate_pay()

