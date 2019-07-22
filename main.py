#!/usr/bin/env python3
from classes.game import Person, FG
from classes.magic import spell
from classes.inventory import item
from classes.d3katool import install, connection, clear, spaces, tabs
from time import sleep
import random

try:
    import readchar
except ImportError:
    if(connection() == "InActive"):
        print("\n"+"Installation Of Package ReadChar Failed Due To No-Internet-Connection")
        print('Try Installing It Manually Or Run This Program Again With An Active-Internet-Connection')
        exit()
    elif(connection() == "Active"):
        print("ReadChar Package Not Found, PIP Will Now Install The Lastest Version Of "
              + "ReadChar For You,Please Wait Till The Installation Completes")
        install('readchar')
        import readchar

clear()
default_actions = ['a', 'm', 'i', 'q', 'A', 'M', 'I', 'Q']
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
                       + FG.END+"\n\n"+tabs(4)).upper(), 6600, 660, 90, 125, magic_list, item_list)
player2 = Person(input("\n\n"+FG.BOLD+FG.YELLOW+tabs(2)+"Enter The Name Of Your First Ally : "
                       + FG.END+"\n\n"+tabs(4)).upper(), 2400, 240, 40, 75, magic_list, item_list)
player3 = Person(input("\n\n"+FG.BOLD+FG.YELLOW+tabs(2)+"Enter The Name Of Your First Ally : "
                       + FG.END+"\n\n"+tabs(4)).upper(), 2400, 240, 40, 75, magic_list, item_list)

players = [player1, player2, player3]

enemy1 = Person('RAKTIM', 17200, 610, 75, 125, magic_list, item_list)
enemy2 = Person('sample1', 5500, 300, 45, 80, magic_list, item_list)
enemy3 = Person('sample2', 5500, 300, 45, 80, magic_list, item_list)

enemies = [enemy1, enemy2, enemy3]
running = True
clear()
#GAME-LOOP
while running:
    print("\t"+FG.PINK+FG.BOLD+FG.UNDERLINE+"NAME"+FG.END+tabs(3)+FG.BOLD+FG.PINK+FG.UNDERLINE
          + "H.P"+tabs(4)+FG.END+FG.PINK+FG.BOLD+FG.UNDERLINE + "\t"+"M.P"+FG.END+"\n")
    for player in players:
        player.get_player_stats()

    print(tabs(1)+'-'*82 + "\n")

    for enemy in enemies:
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
                  + str("Do You Really Want To Quit? Press Y/N").upper()+"\n")
            decision = readchar.readchar()
            if decision == 'Y' or decision == 'y':
                clear()
                print("\n"+FG.BOLD+" GAME OVER! "*10+"\n")
                sleep(3)
                exit()

            elif decision == 'N' or decision == 'n':
                pass
        if player_choice == 'A' or player_choice == 'a':
            target = player.choose_target(enemies)
            if enemies[target].get_hp() == 0:
                print(str(enemies[target].name).upper()+" Has Perished")
                del enemies[target]
            player_dmg = player.generate_attack_damage()
            enemies[target].take_damage(player_dmg)
            print(tabs(3)+FG.BLUE+FG.BOLD+p_name+" Attacked "
                  + enemies[target].name+" For "+str(player_dmg)+" Damage Points"+FG.END)
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
            while magic_choice not in range(0, 7):
                if magic_choice not in range(0, 7):
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
            target = player.choose_target(enemies)

            if spell.type == 'Black':
                enemies[target].take_damage(magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)+" Attacked "
                      + enemies[target].name+" For "+str(magical_dmg)+" Damage Points"+FG.END)
                sleep(1)
            if spell.type == 'White':
                player.heal(magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)
                      + " Healed For "+" "+str(magical_dmg)+" H.P "+FG.END)
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
            while item_choice not in range(0, 5):
                if item_choice not in range(0, 5):
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
            target = player.choose_target(enemies)
            if player.items[item_choice]["quantity"] == 0:
                print(FG.BOLD+FG.LGREY+"\nNoNe Left"+FG.END)
                continue
            player.items[item_choice]["quantity"] -= 1
            item_dmg = item.generate_item_dmg()
            if item.type == 'Weapon' or item.type == 'Poison':
                enemies[target].take_damage(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)
                      + " Attacked "+enemies[target].name+" For "+str(item_dmg)+" Damage Point "+FG.END)
                sleep(0.5)
            if item.type == 'Medical' or item.type == 'Food':
                player.heal(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)
                      + " Healed For "+str(item_dmg)+" H.P "+FG.END)
                sleep(0.5)

    fallen_enemies = 0
    fallen_players = 0
    for enemy in enemies:
        if enemy.get_hp == 0:
            fallen_enemies += 1
    for player in players:
        if player.get_hp == 0:
            fallen_players += 1
    if fallen_enemies == 2:
        print(FG.GREEN+FG.BOLD+"YOU WIN"+FG.END)
        running = False
    elif fallen_players == 2:
        print(FG.RED+FG.BOLD+"YOU LOST , GAME OVER"+FG.END)
        running = False

    clear()

#ENEMY
    for player in players:
        player.get_player_stats()

    print(tabs(1)+'-'*82 + "\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for enemy in enemies:
        print("\n"+FG.BOLD+tabs(4)+spaces(4)+FG.UNDERLINE
              + str(enemy.name).upper()+FG.END+spaces(4)+tabs(4)+"\n")

        enemy.choose_action()
        enemy_choice = random.randrange(1, 4)

        if enemy_choice == 1:
            enemy_dmg = enemy.generate_attack_damage()
            target = random.randrange(0, 3)
            players[target].take_damage(enemy_dmg)
            print("\n"+tabs(3)+FG.PURPLE+FG.BOLD+str(enemy.name).upper()+" Attacked "
                  + str(players[target].name)+" For "+str(enemy_dmg)+" Damage Points"+FG.END+"\n")
            sleep(2)

        elif enemy_choice == 2:
            enemy.choose_magic()
            enemy_spell_choice = random.randrange(0, len(magic_list))
            #print("magic",enemy_spell_choice)
            spell = enemy.magic[enemy_spell_choice]
            enemy_magical_dmg = spell.generate_spell_damage()
            target = random.randrange(0,4)

            if spell.type == 'Black':
                players[target].take_damage(enemy_magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)+" Attacked "
                      + str(players[target].name)+" For "+str(enemy_magical_dmg)+" Damage Points"+FG.END)
                sleep(1.8)
            if spell.type == 'White':
                enemy.heal(enemy_magical_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(spell.name)
                      + " Healed For "+str(enemy_magical_dmg)+" H.P "+FG.END)
                sleep(1.8)

                enemy.reduce_mp(spell.cost)

            if spell.cost > enemy.get_mp():
                #print(tabs(3)+FG.RED+" You Do Not Have Enough M.P "+FG.END)
                continue
        elif enemy_choice == 3:
            enemy.choose_item()
            enemy_item_choice = random.randrange(0, len(item_list))
            item = enemy.items[enemy_item_choice]["item"]
            target = random.randrange(0, 3)
            if enemy.items[enemy_item_choice]["quantity"] == 0:
                #print(FG.BOLD+FG.LGREY+"\nNoNe Left"+FG.END)
                continue
            enemy.items[enemy_item_choice]["quantity"] -= 1
            item_dmg = item.generate_item_dmg()
            print(item_dmg)

            if item.type == 'Weapon' or item.type == 'Poison':
                print(target)
                players[target].take_damage(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)
                      + " Attacked "+str(players[target].name)+" For "+str(item_dmg)+" Damage Point "+FG.END)
                sleep(1.8)

            if item.type == 'Medical' or item.type == 'Food':
                enemy.heal(item_dmg)
                print(tabs(3)+FG.BLUE+FG.BOLD+str(item.name)
                      + " Healed For "+str(item_dmg)+" H.P "+FG.END)
                sleep(1.8)
    clear()
