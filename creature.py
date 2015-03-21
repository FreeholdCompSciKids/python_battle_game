
import random

from creature_base import CreatureBase

class Creature(CreatureBase):

    def __init__(self, name, min_skill, max_skill):
        super(Creature ,self).__init__(name, min_skill, max_skill)

        self.name = name
        self.strength = random.randint(min_skill, max_skill)
        self.skill = random.randint(min_skill, max_skill)
        self.speed = random.randint(min_skill, max_skill)

        self.max_attack_damage = (2*self.skill + self.strength) / 20
        self.min_attack_damage = self.skill / 20

        self.max_hp = random.randint(10+min_skill,
                                     10+max_skill)
        self.current_hp = self.max_hp

        self.is_defending = False
        self.is_active = True

        self.battle = None #starting out not part of a battle

        self.enemy_targeted_actions ["a"] = self.attack.__name__

        self.non_targeted_actions["d"] = self.defend.__name__
        self.non_targeted_actions["r"] =  self.run_away.__name__







    #------------------------------------------------------------ 
    # battle actions

    def defend(self):
        print self.name, " is defending"
        self.is_defending = True
        
    def attack(self, target):
        damage = random.randint(self.min_attack_damage,
                                self.max_attack_damage)
        print self.name, "attacks", target.name, "for", damage, "HP"
        target.receive_attack(damage, self)
        return damage

    def run_away(self):
        print self.name, "runs away"
        self.is_active = False
        if not self.battle is None:
            self.battle.remove_creature(self)


