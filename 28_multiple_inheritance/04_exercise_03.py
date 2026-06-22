class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hi I'm {self.name}")

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
    def work(self):
        print(f"{self.name} is working at {self.company}")

class Manager(Employee):
    def __init__(self, name, company, department):
        super().__init__(name, company)
        self.department = department
    def manage(self):
        print(f"{self.name} manages the {self.department} department")

manager = Manager("Alice", "Google", "Engineering")
manager.introduce()
manager.work()
manager.manage()