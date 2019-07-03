#!/usr/bin/env python3
import readchar
from classes.game import Person,FG,BG
from classes.magic import spell
from classes.inventory import item
from os import system, name
from time import sleep

# *Functions-To-Ease-Work*
def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')
def spaces(spaces):
    t=""
    for space in range(spaces):
        t += " "
    return t
def tabs(tabs):
    t=""
    for tab in range(tabs):
        t += "\t"
    return t
            # *End-Of-Block*
clear()
default = [1,2,3]
# *Object-Initialization*
Shuriken = item("Shuriken","Weapon","A Ninja Blade Of ATK Type Dealing 80 Damage",80)
Purple_Rose = item("Purple Rose","Poison", "A Potion Of Poison Dealing 100 Damage",100)
Kunai = item("Kunai","Weapon","A Ninja Blade of ATK Type Dealing 45 Damage",45)
Ramen = item("Ramen","Food","SuperMeal To Increase H.P by 30%",35)
Elixer = item("Elixer","Medical","A Potion To Increase H.P by 50%",50)
item_list = [{"item":Shuriken,"quantity":7},
             {"item":Purple_Rose,"quantity":4},
             {"item":Kunai,"quantity":5},
             {"item":Ramen,"quantity":4},
             {"item":Elixer,"quantity":2}]

fire = spell("FIRE",10,100,"Black")
thunder = spell("THUNDER",10,100,"Black")
blizzard = spell("BLIZZARD",10,100,"Black")
meteor = spell("METEOR",20,200,"Black")
quake = spell("QUAKE",14,140,"Black")

cure = spell("CURE",18,65,"White")
cura = spell("CURA",24,80,"White")
magic_list = [fire,thunder,blizzard,meteor,quake,cure,cura]

# *Name,Health-Points,Attack,Magic-Points,Defence,Magic-Spells,Items-To-Be-Used*
player1 = Person(input(FG.BOLD+FG.YELLOW+tabs(2)+"Enter Your Name Hero! : " +FG.END).upper(),6600,660,90,125,magic_list,item_list)
player2 = Person(input("\n\n"+FG.BOLD+FG.YELLOW+tabs(2)+"Enter The Name Of Your First Ally : "+FG.END).upper(),2400,240,40,75,magic_list,item_list)
player3 = Person(input("\n\n"+FG.BOLD+FG.YELLOW+tabs(2)+"Enter The Name Of Your First Ally : "+FG.END).upper(),2400,240,40,75,magic_list,item_list)

players = [player1,player2,player3]
enemy = Person('MELIODUS',17200,610,75,30,[],[])
                                                # *End-Of-Object-Initialization*

running = True
clear()
            # *G-A-M-E--L-O-O-P*
while running:
    print("\t"+FG.PINK+FG.BOLD+FG.UNDERLINE+"NAME"+FG.END+tabs(3)+FG.BOLD+FG.PINK+FG.UNDERLINE+"H.P"+tabs(4)+FG.END
          +FG.PINK+FG.BOLD+FG.UNDERLINE +"\t"+"M.P"+FG.END+"\n")
    for player in players:
        player.get_player_stats()

    enemy.get_enemy_stats()

# *H-E-R-O*
    for player in players:
        p_name = player.get_name()
        print("\n"+FG.BLACK+FG.BOLD+FG.UNDERLINE+tabs(4)+BG.lightgrey+spaces(5)+p_name.upper()+spaces(5)+tabs(4)+FG.END+"\n")
        player.choose_action()
        print("\n\t"+FG.BOLD+tabs(2)+"USE : "+FG.END)
        player_choice = int(readchar.readchar())

        if player_choice not in default:
            clear()
            continue
        if player_choice == 1:
            player_dmg = player.generate_attack_damage()
            enemy.take_damage(player_dmg)
            print(tabs(3)+FG.BLUE+FG.BOLD+p_name+" Attacked For "+str(player_dmg)+" Damage Points"+FG.END)
            sleep(1)
        elif player_choice == 2:
            player.choose_magic()
            print("\n"+tabs(4)+FG.BOLD+"CHOOSE MAGIC: "+FG.END)
            player_choice = int(readchar.readchar()) - 1
            spell = player.magic[player_choice]
            magical_dmg = spell.generate_spell_damage()

            if spell.type == 'Black':
                enemy.take_damage(magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+p_name+" Attacked For "+str(magical_dmg)+" Damage Points"+FG.END)
                sleep(1)
            if spell.type == 'White':
                player.heal(magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)+" Healed For "+str(magical_dmg)+" H.P "+FG.END)
                player.reduce_mp(spell.cost)
                sleep(1)
            if spell.cost > player.get_mp():
                print(tabs(3)+FG.RED+" You Do Not Have Enough M.P "+FG.END)
                continue

        elif player_choice == 3:
            player.choose_item()
            print("\n"+tabs(4)+FG.BOLD+"CHOOSE ITEM: "+FG.END)
            player_choice = int(readchar.readchar()) - 1
            item = player.items[player_choice]["item"]
            if player_choice == -1:
                continue
                item = player.items[player_choice]["item"]
            if player.items[player_choice]["quantity"] == 0:
             print(FG.BOLD+FG.LGREY+"\nNoNe Left"+FG.END)
             continue
            player.items[player_choice]["quantity"] -= 1
            item_dmg = item.generate_item_dmg()
            if item.type == 'Weapon' or item.type == 'Poison':
                enemy.take_damage(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)+" Attacked For "+str(item_dmg)+" Damage Point "+FG.END)
                sleep(0.5)
            if item.type == 'Medical' or item.type == 'Food':
                player.heal(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)+" Healed For "+str(item_dmg)+" H.P "+FG.END)
                sleep(0.5)
                         # *E-N-D-OF-H-E-R-O*

# *E-N-E-M-Y*
    print("\n"+FG.BLACK+FG.BOLD+FG.UNDERLINE+tabs(4)+ BG.lightgrey +spaces(4)+'MELIODUS'+spaces(4)+tabs(4)+FG.END+"\n")
    enemy.choose_action()
    enemy_choice = 1
    if enemy_choice == 1:
        enemy_dmg = int(enemy.generate_attack_damage() / 3)

        for player in players:
            player.take_damage(enemy_dmg)

        print(tabs(3)+FG.PURPLE+FG.BOLD+"MELIODUS"+" Attacked For "+str(enemy_dmg)+" Damage Points"+FG.END+"\n")
        sleep(2)
        clear()

    if enemy.get_hp() == 0:
        print(FG.GREEN+FG.BOLD+"YOU WIN"+FG.END)
        running = False
    elif player.get_hp() == 0:
        print(FG.RED+FG.BOLD+"YOU LOST , GAME OVER"+FG.END)
        running = False
                       # *E-N-D-OF-E-N-E-M-Y*
                                                # *END-OF-GAME-LOOP*
