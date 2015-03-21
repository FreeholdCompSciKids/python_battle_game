
from battle import Battle
import monsters 
import heroes 
        

if __name__ == "__main__":

    #creates a battle
    battle = Battle()  

    #create enemies
    battle.add_enemy(monsters.BasicMonster("evil bert", 10, 20))
    battle.add_enemy(monsters.BasicMonster("evil ernie", 5, 8))
    battle.add_enemy(monsters.BasicMonster("chicken", 5,8))
    battle.add_enemy(monsters.Ant("ant", 1, 1))
    battle.add_enemy(monsters.SuperAnt("super ant", 1, 1))

    #create heroes
    battle.add_hero(heroes.Coward("super grover", 21, 28))
    battle.add_hero(heroes.Healer("big bird", 35 ,38 ))
 
    #start battle
    while  len(battle.heroes) > 0 and len(battle.enemies) > 0 :
        battle.next_battle_round();

    print "\n===== THE BATTLE IS OVER ===="
