import random


class Character:
    def init(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power * random.uniform(0.3, 0.9)
        other.hp -= damage
        print(f"{self.name} attacks {other.name} for {damage:.2f} damage!")

    def is_alive(self):
        return self.hp > 0

    def str(self):
        return f"{self.name}: {self.hp:.2f} HP"
