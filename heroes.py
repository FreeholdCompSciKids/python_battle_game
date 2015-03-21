
from creature import Creature
import random

class BasicHero(Creature):

    def __init__(self, name, min_skill, max_skill):
        super(BasicHero ,self).__init__(name, min_skill, max_skill)


class FourHandedHero(BasicHero):  

    def __init__(self, name, min_skill, max_skill):
        super(FourHandedHero ,self).__init__(name, min_skill, max_skill)
        self.speed = self.speed / 2
        self.skill = self.skill / 2
        self.strength = self.strength / 2
   
    def attack(self,target):
        damage = random.randint(self.min_attack_damage,
                                self.max_attack_damage)
        print self.name, "attacks", target.name, "for", damage, "HP"
        target.receive_attack(damage, self)

        damage = 5
        print self.name, "attacks", target.name, " again for", damage, "HP"
        target.receive_attack(damage, self)
        target.receive_attack(damage, self)
        target.receive_attack(damage, self)


class ClumsyHero(BasicHero):

    def attack(self,target):
        super(ClumsyHero,self).attack(target)
        if random.randint(1,100) <= 60: #do this with 60% probability
            print self.name, "tripps"
            self.current_hp = self.current_hp - 1
 

class Healer(BasicHero):

    def __init__(self, name, min_skill, max_skill):
        super(Healer ,self).__init__(name, min_skill, max_skill)
        self.hero_targeted_actions["h"]= self.heals.__name__
                # ^^ adds the 'heal' function below as an action

    def heals(self,target):
        target.current_hp += 2
        print self.name, "heals", target.name


class Coward(BasicHero):

    def __init__(self, name, min_skill, max_skill):
        super(Coward ,self).__init__(name, min_skill, max_skill)
        self.non_targeted_actions["h"]= self.hides.__name__
                # ^^ adds the 'heal' function below as an action
        self.is_hidden = False
     
    def hides(self):
       print self.name, "hides"
       self.is_hidden=True

    def attack(self,target):
        self.is_hidden = False  
                #if he attacks, he is not longer hidden
        super(Coward, self).attack(target)

    def receive_attack(self, damage, attacker):
        if self.is_hidden:
            print self.name, "is hidden. Nothing happens"
        else:
            super(Coward, self).receive_attack(damage,attacker)



        
