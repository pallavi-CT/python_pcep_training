class Person:
    def __init__(self, name, age, email, salary):
        self.name = name
        self.age = age
        self.email = email
        self._salary = salary
        self.__id = 1

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")

p = Person('Pallavi', 30, 'pallavi@example.com', 234500)
# p1 = Person('Prasad', 40, 'prasad@example.com')

print(p.name)
print(p._salary)
# print(p.__id)

# p.print_details()

# print(p.name)
# print(p1.name)
