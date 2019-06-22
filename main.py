#!/usr/bin/env python3
from classes.game import Person, FF
from classes.magic import spell
from classes.inventory import item
from os import system, name
from time import sleep

def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
default = [1,2,3]
#Creating Items
Shuriken = item("Shuriken","Weapon", "A Ninja Blade Of ATK Type Dealing 80 Damage",80)
Purple_Rose = item("Purple Rose" , "Poison", "A Potion Of Poison Dealing 100 Damage",100)
Kunai = item("Kunai","Weapon","A Ninja Blade of ATK Type Dealing 45 Damage",45)
Ramen = item("Ramen","Food","SuperMeal To Increase H.P by 30%", 35)
Elixer = item("Elixer","Medical","A Potion To Increase H.P by 50%",50)
item_list = [{"item" : Shuriken , "quantity" : 7},
             {"item" : Purple_Rose , "quantity" : 4},
             {"item" : Kunai , "quantity" : 5},
             {"item" : Ramen , "quantity" : 4},
             {"item" : Elixer , "quantity" : 2}]

# Creating Magic Type : Black
fire = spell("FIRE",10,100,"Black")
thunder = spell("THUNDER",10,100,"Black")
blizzard = spell("BLIZZARD",10,100,"Black")
meteor = spell("METEOR",20,200,"Black")
quake = spell("QUAKE",14,140,"Black")

# Creating Magic Type : White
cure = spell("CURE",18,65,"White")
cura = spell("CURA",24,80,"White")
magic_list = [fire,thunder,blizzard,meteor,quake,cure,cura]

player_name = str(input("\t\t\t\t Enter Your Name : "))

player = Person(player_name.upper(),6600,660,90,37,magic_list,item_list)
enemy = Person('MORIS',5200,610,75,30,[],[])

running = True

clear()

while running:
    print(FF.PINK + FF.BOLD + FF.UNDERLINE + "NAME" + FF.END  + "\t"+ FF.BOLD + FF.PINK + FF.UNDERLINE+"H.P"+"\t\t\t\t"+ FF.END
          +FF.PINK + FF.BOLD + FF.UNDERLINE +"\t"+"M.P"+ FF.END+"\n")
    player.get_stats()
    enemy.get_stats()
    print("\n"+FF.CYAN + FF.BOLD + FF.UNDERLINE + "\t\t\t\t" + '----' +player_name.upper()+ '----' + "\t\t\t\t"+FF.END+"\n")
    player.choose_action()
    player_choice = int(input(FF.BOLD + FF.CYAN + "USE : " + FF.END))

    if player_choice not in default:
        clear()
        continue

    if player_choice == 1:
        player_dmg = player.generate_attack_damage()
        enemy.take_damage(player_dmg)
        print("\t\t\t"+FF.BLUE + FF.BOLD + "You Attacked For "+str(player_dmg)+" Damage Points" + FF.END)
        sleep(2)
    elif player_choice == 2:
        player.choose_magic()
        player_choice = int(input("Choose Magic: ")) - 1
        spell = player.magic[player_choice]
        magical_dmg = spell.generate_spell_damage()
        if spell.type == 'Black':
            enemy.take_damage(magical_dmg)
            print("\t\t\t"+FF.BLUE + FF.BOLD + " You Attacked For " + str(magical_dmg) + " Damage Points" + FF.END)
        sleep(2)

        if spell.type == 'White':
            player.heal(magical_dmg)
            print("\t\t\t"+FF.BLUE + FF.BOLD + str(spell.name) + " Healed For " + str(magical_dmg) + " H.P " + FF.END)
            sleep(2)

        player.reduce_mp(spell.cost)

        if spell.cost > player.get_mp():
            print("\t\t\t"+FF.RED + " You Do Not Have Enough M.P " + FF.END)
            continue

    elif player_choice == 3:
         player.choose_item()
         player_choice = int(input("Choose Item: ")) - 1
         item = player.items[player_choice]["item"]
         if player_choice == -1:
             continue
         item = player.items[player_choice]["item"]

         if player.items[player_choice]["quantity"] == 0:
             print(FF.BOLD + FF.LGREY + "\nNoNe Left" + FF.END)
             continue

         player.items[player_choice]["quantity"] -= 1
         item_dmg = item.generate_item_dmg()
         if item.type == 'Weapon' or item.type == 'Poison':
             enemy.take_damage(item_dmg)
             print("\t\t\t"+FF.BLUE + FF.BOLD + str(item.name) + " Attacked For " + str(item_dmg) + " Damage Point " + FF.END)
             sleep(2)

         if item.type == 'Medical' or item.type == 'Food':
             player.heal(item_dmg)
             print(FF.BLUE + FF.BOLD + str(item.name) + " Healed For " + str(item_dmg) + " H.P " + FF.END)
             sleep(2)


    print(FF.RED + FF.BOLD + FF.UNDERLINE + "\t\t\t\t----MORIS----\t\t\t\t" + FF.END + "\n")
    enemy.choose_action()
    enemy_choice = 1
    if enemy_choice == 1:
        enemy_dmg = enemy.generate_attack_damage()
        player.take_damage(enemy_dmg)
        print("\t\t\t"+FF.YELLOW + FF.BOLD + "Enemy Attacked with "+str(enemy_dmg)+" Damage Points" + FF.END+"\n")
        sleep(2)
        clear()

    if enemy.get_hp() == 0:
        print(FF.GREEN + FF.BOLD + "YOU WIN" + FF.END)
        running = False
    elif player.get_hp() == 0:
        print(FF.RED + FF.BOLD + "YOU LOST , GAME OVER" + FF.END)
        running = False
