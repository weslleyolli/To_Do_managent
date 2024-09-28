import random

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

    def suffer_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        dano_base = random.randint(5, 15)
        dano_total = int(dano_base * (1 + self.__level * 0.05))
        target.suffer_attack(dano_total)
        print(f"\n{self.__name} attacked {target.get_name()} causing {dano_total} of damage!")

class Hero(Character):
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability

    def show_details(self):
        return f"{super().show_details()}\n Ability: {self.get_ability()}\n"

    def especial_attack(self, target):
        dano_base = random.randint(10, 20)
        total_damage = int(dano_base * (1 + self.get_level() * 0.1))
        target.suffer_attack(total_damage)
        print(f"{self.get_name()} used the especial ability {self.get_ability()} in {target.get_name()} and dealt {total_damage}")

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

            if choice == "1":
                self.hero.attack(self.villain)
            elif choice == "2":
                self.hero.especial_attack(self.villain)
            else:
                print("choice invalid")

            if self.villain.get_life() > 0:
                self.villain.attack(self.hero)

        if self.hero.get_life() > 0:
            print("\ncongratulations, you win!")
        else:
            print("\nyou lose!")


# CREATE INSTANCE AND START THE BATTLE
game = Game()
game.init_battle()