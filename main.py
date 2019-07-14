#!/usr/bin/env python3
from classes.game import Person, FG
from classes.magic import spell
from classes.inventory import item
from os import system, name
from time import sleep
from urllib.request import urlopen
import subprocess

#Functions To-Ease-Work


def install(name):
    subprocess.call(['pip', 'install', name])


def connection():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return "Active"
    except:
        return "InActive"


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def spaces(spaces):
    t = ""
    for space in range(spaces):
        t += " "
    return t


def tabs(tabs):
    t = ""
    for tab in range(tabs):
        t += "\t"
    return t


try:
    import readchar
except ImportError:
    if(connection() == "InActive"):
        print("\n"+"Installation Of Package ReadChar Failed Due To No-Internet-Connection")
        print('Try Installing It Manually Or Run This Program Again With An Active-Internet-Connection')
        exit()
    elif(connection() == "Active"):
        print("ReadChar Package Not Found, PIP Will Now Install The Lastest Version Of ReadChar For You,Please Wait Till The Installation Completes")
        install('readchar')
        import readchar

clear()
default_actions = ['a', 'm', 'i', 'q', 'A', 'M', 'I', 'Q']
default_magic = [0, 1, 2, 3, 4, 5, 6]
default_items = [0, 1, 2, 3, 4]
magic_choice = 0
item_choice = 0
#Object-Initialization
Shuriken = item("Shuriken", "Weapon",
                "A Ninja Blade Of ATK Type Dealing Damage", 80)
Purple_Rose = item("Purple Rose", "Poison",
                   "A Potion Of Poison Dealing Damage", 100)
Kunai = item("Kunai", "Weapon",
             "A Ninja Blade of ATK Type Dealing 45 Damage", 45)
Ramen = item("Ramen", "Food", "SuperMeal To Increase H.P by 30%", 35)
Elixer = item("Elixer", "Medical", "A Potion To Increase H.P by 50%", 50)
item_list = [{"item": Shuriken, "quantity": 7},
             {"item": Purple_Rose, "quantity": 4},
             {"item": Kunai, "quantity": 5},
             {"item": Ramen, "quantity": 4},
             {"item": Elixer, "quantity": 2}]

fire = spell("FIRE", 10, 100, "Black")
thunder = spell("THUNDER", 10, 100, "Black")
blizzard = spell("BLIZZARD", 10, 100, "Black")
meteor = spell("METEOR", 20, 200, "Black")
quake = spell("QUAKE", 14, 140, "Black")
cure = spell("CURE", 18, 65, "White")
cura = spell("CURA", 24, 80, "White")

magic_list = [fire, thunder, blizzard, meteor, quake, cure, cura]

#Name,Health-Points,Attack,Magic-Points,Defence,Magic-Spells,Items-To-Be-Used
player1 = Person(input(FG.BOLD+FG.YELLOW+tabs(2)+"Enter Your Name Hero : "
                       + FG.END+"\n"+tabs(4)).upper(), 6600, 660, 90, 125, magic_list, item_list)
player2 = Person(input("\n\n"+FG.BOLD+FG.YELLOW+tabs(2)+"Enter The Name Of Your First Ally : "
                       + FG.END+"\n"+tabs(4)).upper(), 2400, 240, 40, 75, magic_list, item_list)
player3 = Person(input("\n\n"+FG.BOLD+FG.YELLOW+tabs(2)+"Enter The Name Of Your First Ally : "
                       + FG.END+"\n"+tabs(4)).upper(), 2400, 240, 40, 75, magic_list, item_list)

players = [player1, player2, player3]
enemy = Person('MELIODUS', 17200, 610, 75, 30, [], [])


running = True
clear()
#GAME-LOOP
while running:
    print("\t"+FG.PINK+FG.BOLD+FG.UNDERLINE+"NAME"+FG.END+tabs(3)+FG.BOLD+FG.PINK+FG.UNDERLINE
          + "H.P"+tabs(4)+FG.END+FG.PINK+FG.BOLD+FG.UNDERLINE + "\t"+"M.P"+FG.END+"\n")
    for player in players:
        player.get_player_stats()

    enemy.get_enemy_stats()
#HERO
    for player in players:
        p_name = player.get_name()
        print("\n"+FG.BOLD+tabs(4)+spaces(5)+FG.UNDERLINE
              + p_name.upper()+FG.END+spaces(5)+tabs(4)+"\n")
        player.choose_action()
        print("\n\t"+FG.BOLD+tabs(2)+"USE : "+FG.END)
        player_choice = readchar.readchar()

        while player_choice not in default_actions:
            if player_choice not in default_actions:
                player_choice = readchar.readchar()
            else:
                continue
        if player_choice == 'Q' or player_choice == 'q':
            print(tabs(4)+FG.BOLD
                  + str("Do You Really Want To Quit,Press Y/N").upper()+"\n")
            decision = readchar.readchar()
            if decision == 'Y' or decision == 'y':
                clear()
                print("\n"*10+tabs(5)+FG.BOLD+" GAME OVER! "*5)
                exit()
            elif decision == 'N' or decision == 'n':
                pass
        if player_choice == 'A' or player_choice == 'a':
            player_dmg = player.generate_attack_damage()
            enemy.take_damage(player_dmg)
            print(tabs(3)+FG.BLUE+FG.BOLD+p_name+" Attacked For "
                  + str(player_dmg)+" Damage Points"+FG.END)
            sleep(1)
        elif player_choice == 'M' or player_choice == 'm':
            player.choose_magic()
            print("\n"+tabs(4)+FG.BOLD+"CHOOSE MAGIC: "+FG.END+"\n")
            try:
                buffer = readchar.readchar()
                magic_choice = int(buffer) - 1
            except ValueError:
                while buffer.isdigit() != True:
                    if buffer.isdigit() != True:
                        buffer = readchar.readchar()
                    else:
                        continue
            while magic_choice not in default_magic:
                if magic_choice not in default_magic:
                    try:
                        buffer = readchar.readchar()
                        magic_choice = int(buffer) - 1
                    except ValueError:
                        while buffer.isdigit() != True:
                            if buffer.isdigit() != True:
                                buffer = readchar.readchar()
                            else:
                                continue
                else:
                    continue
            spell = player.magic[magic_choice]
            magical_dmg = spell.generate_spell_damage()

            if spell.type == 'Black':
                enemy.take_damage(magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)+" Attacked For "
                      + str(magical_dmg)+" Damage Points"+FG.END)
                sleep(1)
            if spell.type == 'White':
                player.heal(magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)
                      + " Healed For "+str(magical_dmg)+" H.P "+FG.END)
                sleep(1)

            player.reduce_mp(spell.cost)

            if spell.cost > player.get_mp():
                print(tabs(3)+FG.RED+" You Do Not Have Enough M.P "+FG.END)
                continue

        elif player_choice == 'I' or player_choice == 'i':
            player.choose_item()
            print("\n"+tabs(4)+FG.BOLD+"CHOOSE ITEM: "+FG.END+"\n")
            try:
                buffer = readchar.readchar()
                item_choice = int(buffer) - 1
            except ValueError:
                while buffer.isdigit != True:
                    if buffer.isdigit != True:
                        buffer = readchar.readchar()
                    else:
                        continue
            while item_choice not in default_items:
                if item_choice not in default_items:
                    try:
                        buffer = readchar.readchar()
                        item_choice = int(buffer) - 1
                    except ValueError:
                        while buffer.isdigit() != True:
                            if buffer.isdigit() != True:
                                buffer = readchar.readchar()
                            else:
                                continue
                else:
                    continue
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(FG.BOLD+FG.LGREY+"\nNoNe Left"+FG.END)
                continue
            player.items[item_choice]["quantity"] -= 1
            item_dmg = item.generate_item_dmg()
            if item.type == 'Weapon' or item.type == 'Poison':
                enemy.take_damage(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)
                      + " Attacked For "+str(item_dmg)+" Damage Point "+FG.END)
                sleep(0.5)
            if item.type == 'Medical' or item.type == 'Food':
                player.heal(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)
                      + " Healed For "+str(item_dmg)+" H.P "+FG.END)
                sleep(0.5)
#ENEMY
    print("\n"+FG.BOLD+tabs(4)+spaces(4)+FG.UNDERLINE
          + 'MELIODUS'+FG.END+spaces(4)+tabs(4)+"\n")
    enemy.choose_action()
    enemy_choice = 1
    if enemy_choice == 1:
        enemy_dmg = int(enemy.generate_attack_damage()/3)

        for player in players:
            player.take_damage(enemy_dmg)

        print(tabs(3)+FG.PURPLE+FG.BOLD+"MELIODUS"+" Attacked For "
              + str(enemy_dmg)+" Damage Points"+FG.END+"\n")
        sleep(2)
        clear()

    if enemy.get_hp() == 0:
        print(FG.GREEN+FG.BOLD+"YOU WIN"+FG.END)
        running = False
    elif player.get_hp() == 0:
        print(FG.RED+FG.BOLD+"YOU LOST , GAME OVER"+FG.END)
        running = False
