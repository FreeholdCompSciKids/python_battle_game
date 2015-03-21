
from creature import Creature
import random

class BasicMonster(Creature):

    def __init__(self, name, min_skill, max_skill):
        super(BasicMonster ,self).__init__(name, min_skill, max_skill)

    def do_battle_action(self, target):
        if random.randint(0,100) < 80:
            return self.attack(target)
        else:
            return self.defend()


class Ant(BasicMonster):
    def __init__(self, name, min_skill, max_skill):
        super(Ant ,self).__init__(name, min_skill, max_skill)
        self.max_hp=1
        self.current_hp=1

    def attack(self,target):
        print self.name, "crawls around vigorously"    


class SuperAnt(BasicMonster):
    def __init__(self, name, min_skill, max_skill):
        super(SuperAnt ,self).__init__(name, min_skill, max_skill)
        self.max_hp=100
        self.current_hp=100

    def attack(self,target):
        print self.name, "crawls around vigorously and stings"
        damage = 2
        target.receive_attack(damage, self)
