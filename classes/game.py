from .d3katool import *

try:
    import readchar
except ModuleNotFoundError:
    if connection() == "InActive":
        print("\n" + "Installation Of Package ReadChar Failed Due To No-Internet-Connection")
        print('Try Installing It Manually Or Run This Program Again With An Active-Internet-Connection')
        exit()
    elif connection() == "Active":
        print("ReadChar Package Not Found, PIP Will Now Install The Lastest Version Of "
              + "ReadChar For You,Please Wait Till The Installation Completes")
        install('readchar')
        import readchar

import random


class Banner:
    def banner():
        print(nLine(1) + tabs(3) + " ██████╗██╗     ██╗      ██████╗ ██████╗  ██████╗" + nLine(1) + tabs(
            3) + "██╔════╝██║     ██║      ██╔══██╗██╔══██╗██╔════╝" + nLine(1) +
              tabs(3) + "██║     ██║     ██║█████╗██████╔╝██████╔╝██║  ███╗" + nLine(1) + tabs(
            3) + "██║     ██║     ██║╚════╝██╔══██╗██╔═══╝ ██║   ██║" + nLine(1) +
              tabs(3) + "╚██████╗███████╗██║      ██║  ██║██║     ╚██████╔╝" + nLine(1) + tabs(
            3) + " ╚═════╝╚══════╝╚═╝      ╚═╝  ╚═╝╚═╝      ╚═════╝ ")

    def Over():
        print(nLine(7) + tabs(2) + " _____   ___  ___  ___ _____       _____  _   _ ___________ _ " + nLine(1) + tabs(
            2) + "|  __ \ / _ \ |  \/  ||  ___|     |  _  || | | |  ___| ___ \ |" + nLine(1) +
              tabs(2) + "| |  \// /_\ \| .  . || |__ ______| | | || | | | |__ | |_/ / |" + nLine(1) + tabs(
            2) + "| | __ |  _  || |\/| ||  __|______| | | || | | |  __||    /| |" + nLine(1) +
              tabs(2) + "| |_\ \| | | || |  | || |___      \ \_/ /\ \_/ / |___| |\ \|_|" + nLine(1) + tabs(
            2) + " \____/\_| |_/\_|  |_/\____/       \___/  \___/\____/\_| \_(_)")


class FG:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LGREY = '\033[37m'
    DGREY = '\033[90m'
    LRED = '\033[91m'
    LGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LBLUE = '\033[94m'
    PINK = '\033[95m'
    LCYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class BG:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'


class Person:
    def __init__(self, name, hp, atk, mp, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.max_mp = mp
        self.mp = mp
        self.df = df
        self.magic = magic
        self.items = items
        self.action = [FG.YELLOW + "Press" + FG.BOLD + " [A] " + FG.END + FG.YELLOW + "To Attack" + FG.END,
                       FG.YELLOW + "Press" + FG.BOLD +
                       " [M] " + FG.END + FG.YELLOW + "To Cast Magic" + FG.END,
                       FG.YELLOW + "Press" + FG.BOLD + " [I] " + FG.END + FG.YELLOW + "To Use Items" + FG.END,
                       FG.YELLOW + "Press" + FG.BOLD + " [Q] " + FG.END + FG.YELLOW + "To Quit" + FG.END]

    def get_name(self):
        return self.name

    def generate_attack_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0

    def reduce_mp(self, cost):
        self.mp = self.mp - cost

    def heal(self, dmg):
        if self.hp < self.max_hp:
            self.hp = self.hp + dmg

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_max_hp(self):
        return self.max_hp

    def get_max_mp(self):
        return self.max_mp

    def choose_action(self):
        i = "*"
        for index in self.action:
            print(tabs(4) + FG.BOLD + str(i) + FG.END, str(index))

    def choose_magic(self):
        i = 1
        for spl in self.magic:
            if (len(spl.name) >= 6):
                gap = 1
            if (len(spl.name) < 5):
                gap = 2
            print(tabs(4) + str(i) + ": " + FG.LCYAN + FG.BOLD + spl.name
                  + tabs(gap) + FG.END + "(cost:", str(spl.cost) + ")")
            i += 1
        print("")

    def choose_item(self):
        i = 1
        for itm in self.items:
            if (len(itm["item"].name) >= 6):
                gap = 2
            if (len(itm["item"].name) < 5):
                gap = 3
            print(tabs(4) + str(i) + ": " + FG.BLUE + FG.BOLD + itm["item"].name + FG.END + tabs(gap) + "(Type:",
                  str(itm["item"].type)
                  + ")" + tabs(2) + "(x" + str(itm["quantity"]) + ")")
            i += 1
        print("")

    def choose_target(self, enemies):
        choice = 0
        i = 1
        print(tabs(4) + FG.RED + FG.BOLD + "TARGET" + ":" + FG.END + "\n")
        for tgt in enemies:
            if tgt.get_hp != 0:
                print(tabs(4) + str(i) + ": " + FG.PURPLE + FG.BOLD + tgt.name + FG.END)
                i += 1
        print("\n" + tabs(5) + FG.BOLD + "LOCK TARGET : " + "\n")
        try:
            buffer = readchar.readchar()
            choice = int(buffer) - 1
        except ValueError:
            while buffer.isdigit() != True:
                if buffer.isdigit() != True:
                    buffer = readchar.readchar()
                else:
                    continue
            while choice not in range(0, 4):
                if choice not in range(0, 4):
                    try:
                        buffer = readchar.readchar()
                        choice = int(buffer) - 1
                    except ValueError:
                        while buffer.isdigit() != True:
                            if buffer.isdigit() != True:
                                buffer = readchar.readchar()
                            else:
                                continue
                else:
                    continue
        return choice

    def get_player_stats(self):
        hp_bar = ''
        hp_tick = (self.hp / self.max_hp) * 100 / 4
        mp_bar = ''
        mp_tick = (self.mp / self.max_mp) * 100 / 10

        while hp_tick > 0:
            hp_bar += '█'
            hp_tick -= 1
        while len(hp_bar) < 25:
            hp_bar += " "
        while mp_tick > 0:
            mp_bar += '█'
            mp_tick -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        if len(self.name) > 4 and len(self.name) < 13:
            space = '\t\t'
        if len(self.name) < 5:
            space = '\t\t\t'
        if len(self.name) > 13:
            space = '\t'

        print("\t" + FG.BOLD + FG.LGREEN + str(self.name) + FG.END + " : " + str(space) + str(self.hp) + "/" + str(
            self.max_hp) + spaces(4) + FG.LGREEN + str(hp_bar) + FG.END
              + "\t" + str(self.mp) + "/" + str(self.max_mp) + "\t" + FG.LBLUE + str(mp_bar) + FG.END + "\n")

    def get_enemy_stats(self):
        hp_bar = space = ''
        hp_tick = (self.hp / self.max_hp) * 100 / 4
        mp_bar = ''
        mp_tick = (self.mp / self.max_mp) * 100 / 10

        while hp_tick > 0:
            hp_bar += '█'
            hp_tick -= 1
        while len(hp_bar) < 25:
            hp_bar += " "
        while mp_tick > 0:
            mp_bar += '█'
            mp_tick -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        if len(self.name) > 3 and len(self.name) < 13:
            space = '\t\t'
        if len(self.name) < 5:
            space = '\t\t\t'
        if len(self.name) > 13:
            space = '\t'

        print("\t" + FG.BOLD + FG.RED + str(self.name) + FG.END + " : " + str(space) + str(self.hp) + "/" + str(
            self.max_hp) + spaces(2) + FG.RED + str(hp_bar) + FG.END
              + "\t" + str(self.mp) + "/" + str(self.max_mp) + "\t" + FG.PURPLE + str(mp_bar) + FG.END + "\n")
