from classes.game import Person, FF
from classes.magic import spell
from classes.inventory import item
from os import system, name
from time import sleep

'''def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
'''
#Creating Items
Shuriken = item("Shuriken","Weapon", "A Ninja Blade Of ATK Type Dealing 80 Damage",80)
Purple_Rose = item("Purple Rose" , "Poision", "A Potion Of Poistion Dealing 100 Damage",100)
Kunai = item("Kuani","Weapon","A Ninja Blade of ATK Type Dealing 45 Damage",45)
Ramen = item("Ramen","Medical","SuperMeal To Increse H.P by 30%", 35)
item_list = [Shuriken,Poison,Kunai,Ramen]
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

player = Person(400,60,70,34,magic_list,item_list)
enemy = Person(1200,65,45,30,[],[])

running = True

while running:
    print(FF.LGREY + FF.BOLD + "PLAYER H.P : " + str(player.get_hp())+"/"+str(player.get_max_hp()) + "\t\tENEMY H.P : "
    + str(enemy.get_hp())+"/"+str(enemy.get_max_hp())+FF.END)
    print(FF.ORANGE + FF.BOLD + "PLAYER M.P : " + str(player.get_mp())+"/"+str(player.get_max_mp()) + "\t\tENEMY M.P : "
    + str(enemy.get_mp())+"/"+str(enemy.get_max_mp())+FF.END)
    print("\n"+FF.CYAN + FF.BOLD + FF.UNDERLINE + "\t\t\t --PLAYER--\t\t\t\t" + FF.END+"\n")
    player.choose_action()
    player_choice = int(input(FF.BOLD + FF.CYAN + " USE : "))
    if player_choice == 1:
        player_dmg = player.generate_attack_damage()
        enemy.take_damage(player_dmg)
        print(FF.BLUE + FF.BOLD + "You Attacked For "+str(player_dmg)+" Damage Points" + FF.END)
    elif player_choice == 2:
        player.choose_magic()
        player_choice = int(input("Choose Magic: ")) - 1
        spell = player.magic[player_choice]
        magical_dmg = spell.generate_spell_damage()
        if spell.type == 'Black':
            enemy.take_damage(magical_dmg)
        if spell.type == 'White':
            player.heal(magical_dmg)
            print(FF.BLUE + FF.BOLD + str(spell.name) + " Healed For " + str(magical_dmg) + " H.P " + FF.END)
        player.reduce_mp(spell.cost)
        if spell.cost > player.get_mp():
            print(FF.RED + " You Do Not Have Enough M.P " + FF.END)
            continue
        else:
            print(FF.BLUE + FF.BOLD + " You Attacked For " + str(magical_dmg) + " Damage Points" + FF.END)
     elif player.choice == 3:
         player.choose_item()
         player_choice = int(input("Choose Magic: ")) - 1
         item = player.item[player_choice]
         item_dmg = item.item_dmg()
         if item.type == "Weapon" || item.type == "Poision":
             enemy.generate_attack_damage(item_dmg)


    print(FF.RED + FF.BOLD + FF.UNDERLINE + "\t\t\t--ENEMY--\t\t\t\t" + FF.END + "\n")
    enemy.choose_action()
    enemy_choice = 1
    if enemy_choice == 1:
        enemy_dmg = enemy.generate_attack_damage()
        player.take_damage(enemy_dmg)
        print(FF.YELLOW + FF.BOLD + "Enemy Attacked with "+str(enemy_dmg)+" attack point" + FF.END+"\n")

    if enemy.get_hp() == 0:
        print(FF.GREEN + FF.BOLD + "YOU WIN" + FF.END)
        running = False
    elif player.get_hp() == 0:
        print(FF.RED + FF.BOLD + "YOU LOST , GAME OVER" + FF.END)
        running = False
