
import random

class CreatureBase(object):

    def __init__(self, name, min_skill, max_skill):
        self.name = name
        self.strength = self.skill = self.speed = 1
        self.max_attack_damage = self.min_attack_damage = 1
        self.current_hp = self.max_hp = 1

        self.is_defending = False
        self.is_active = True
        self.battle = None 

        self.enemy_targeted_actions = {}
        self.hero_targeted_actions = { }
        self.non_targeted_actions = {}




    def __str__(self):
        s = ( self.name + "(" + str(self.current_hp)
              + "/" + str(self.max_hp) + ")"  )
        return s

    def big_print(self):
        print "***********************************"
        print " ", self.name
        print "-----------------------------------"
        print "  HP: ", self.current_hp, "/", self.max_hp
        print "  Strength: ", self.strength
        print "  Skill:    ", self.skill
        print "  Speed:    ", self.speed
        print "  Attack damage range: ", self.min_attack_damage, \
               " - ", self.max_attack_damage
        print "***********************************"

    #------------------------------------------------------------ 
    # battle actions

    def defend(self):
        print self.name, " does nothing"
        
    def attack(self, target):
        print self.name, " does nothing"
        return 0

    def run_away(self):
        print self.name, " does nothing"


    enemy_targeted_actions = {
            "a": attack.__name__,
        }
    
    hero_targeted_actions = {
        }
    
    non_targeted_actions = {
            "d": defend.__name__,
            "r": run_away.__name__,
        }


    #------------------------------------------------------------ 
    # utility methods for battle

    def dies(self):
        print self.name, "dies"
        self.is_active = False
        self.max_hp = 0
        self.current_hp = 0
        if not self.battle is None:
            self.battle.remove_creature(self)

    def do_battle_action(self, action_key, target=None):
        self.is_defending = False
        if target is None:
            action_name =  self.non_targeted_actions[action_key]
            return getattr(self, action_name, target)()
        else:             
            if action_key in self.enemy_targeted_actions.keys():
                action_name =  self.enemy_targeted_actions[action_key]
            else:
                action_name =  self.hero_targeted_actions[action_key]
            return getattr(self, action_name, target)(target)

    def battle_position(self):
        return 100 -  random.randint(2*self.speed, 6*self.speed)

    def defense_value(self):
        dv = (2*self.skill + self.speed)/3
        if self.is_defending:
            dv *= 2                
        return dv

    def attack_value(self):
        return random.randint(self.skill, 2*self.strength+self.strength)
    
    def receive_attack(self, damage, attacker):
        if attacker.attack_value() > self.defense_value():
            print self.name, "received", damage, "HP damage"
            self.current_hp -= damage
            if self.current_hp <= 0:
                self.dies() 
        else:
            print self.name, "blocked the attack"

    def join_battle(self, battle):
        print self.name, "joins the battle"
        self.battle = battle
