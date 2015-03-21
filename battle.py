
import creature
import random

class Battle:

    def __init__(self):
        self.enemies = []
        self.heroes = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)
        enemy.join_battle(self)

    def add_hero(self, hero):
        self.heroes.append(hero)
        hero.join_battle(self)

    def remove_creature(self, creature):
        if creature in self.heroes:
            self.heroes.remove(creature)    
        if creature in self.enemies:
            self.enemies.remove(creature)    

    def append_to_battle_order(self, battle_order, creature_list, is_enemy):
        for creature in creature_list:
            battle_order.append( (creature.battle_position(),
                                  creature,
                                  is_enemy) )
        return battle_order

    def do_enemy_action(self, enemy):
        if len(self.heroes) > 0:
            target = random.choice(self.heroes)
            enemy.do_battle_action(target)
        else:
            print enemy.name, "has no target and does nothing"
        

    def do_hero_action(self, hero):
        print "\nIt is ", hero.name +"'s turn. What should he do? "

        valid_actions = []
        for (cmd_key, cmd_name) in hero.enemy_targeted_actions.iteritems():
            i = 1
            for enemy in self.enemies:
                action = cmd_key+str(i) 
                print "["+ action +"]\t", cmd_name, enemy.name
                valid_actions.append(action)
                i+=1

        for (cmd_key, cmd_name) in hero.hero_targeted_actions.iteritems():
            i = 1
            for fellow_hero in self.heroes:
                action = cmd_key+str(i) 
                print "["+ action +"]\t", cmd_name, fellow_hero.name
                valid_actions.append(action)
                i+=1

        for (cmd_key, cmd_name) in hero.non_targeted_actions.iteritems():
            print "["+cmd_key+"]\t", cmd_name
            valid_actions.append(cmd_key)

        cmd_input = raw_input("> ")
        while not cmd_input in valid_actions:
            cmd_input = raw_input("Invalid command. Try again> ")

        cmd_key = cmd_input[0]
        if cmd_key in hero.enemy_targeted_actions.keys():
           action_is_on_enemy = True
        else:
           action_is_on_enemy = False

        if len(cmd_input) > 1:
            #the user entered a number to identify the target
            targetIdx = int(cmd_input[1:])-1
            if action_is_on_enemy:
                target = self.enemies[targetIdx]
            else:
                target = self.heroes[targetIdx]
        else:
            #no target provided
            target = None
        hero.do_battle_action(cmd_key, target)


    def print_battle_status(self):
        print "\nBattle status: "
        print "  Enemies:\n   ", ",".join( [str(c) for c in self.enemies] )
        print "  Heroes:\n    ", ",".join( [str(c) for c in self.heroes] )


    def next_battle_round(self):
        battle_order = []
        self.append_to_battle_order(battle_order, self.enemies, True)
        self.append_to_battle_order(battle_order, self.heroes, False)

        battle_order.sort(key=lambda x: x[0])
        print "\n\n=== Next Round: ==============", self.print_battle_status()
        for (_,creature, is_enemy) in battle_order:
            if creature.is_active:
                if is_enemy:
                    self.do_enemy_action(creature)
                else:
                    self.do_hero_action(creature)
        
