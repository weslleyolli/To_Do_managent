class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Name: {self.get_name()}\n Life: {self.get_life()}\n Level: {self.get_level()}"

class Hero(Character):
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability

    def show_details(self):
        return f"{super().show_details()}\n Ability: {self.get_ability()}\n"

class Villain(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}\n Type: {self.get_type()}\n"

hero = Hero(name="Spiderman", life=100, level=5, ability="shoot webs")
print(hero.show_details())
villain =Villain(name="green elf", life=80, level=3, type="fly")
print(villain.show_details())