#POO

#Class exemple
class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        return f'Hello, my name is {self.name} and my age is {self.age}!'

#objetc
pessoa1 = Pessoa("Weslley", 26)
message = pessoa1.greetings()
print(message)

pessoa2 = Pessoa("Camile", 22)
message = pessoa2.greetings()
print(message)


#exemple of heranca
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"The Animal {self.name} walks")
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "au au"

class Cat(Animal):
    def sound(self):
        return "miau"

dog = Dog("Bob")
cat = Cat("Jack")

print("\n exemple of polimorf")
animals = [dog, cat]

for animal in animals:
    print(f"{animal.name} faz: {animal.sound()}")

print("\n exemple of encapsulation")
class BankerAccount:
    def __init__(self, balance):
        self.__balance = balance #privateAtribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def view_balance(self):
        return self.__balance

account = BankerAccount(balance=1000)
print(account.view_balance())
account.withdraw(100)
print(account.view_balance())
account.withdraw(-100)
print(account.view_balance())
account.deposit(100)
print(account.view_balance())
account.deposit(-100)
print(account.view_balance())
