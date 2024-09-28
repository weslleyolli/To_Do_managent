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
        return f" Name: {self.get_name()}\n Life: {self.get_life()}\n Level: {self.get_level()}"

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

class Game():
    def __init__(self):
        self.hero = Hero(name="Spiderman", life=100, level=5, ability="shoot webs")
        self.villain = Villain(name="green elf", life=80, level=3, type="fly")

    def init_battle(self):
        print("Starting battle!")
        while self.hero.get_life() > 0 and self.villain.get_life() > 0:
            print("\nCharacter details:")
            print(self.hero.show_details())
            print(self.villain.show_details())

            input("Press enter to attack...")
            choice = input("Choice (1- normal attack, 2- especial attack):")


# CREATE INSTANCE AND START THE BATTLE
game = Game()
game.init_battle()