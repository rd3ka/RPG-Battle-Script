import random
from .magic import spell
from .inventory import item

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
   black='\033[40m'
   red='\033[41m'
   green='\033[42m'
   orange='\033[43m'
   blue='\033[44m'
   purple='\033[45m'
   cyan='\033[46m'
   lightgrey='\033[47m'


class Person:
   def __init__(self,name,hp,atk,mp,df,magic,items):
      self.name = name
      self.max_hp = hp
      self.hp  = hp
      self.atkl = atk - 10
      self.atkh = atk + 10
      self.max_mp = mp
      self.mp = mp
      self.df = df
      self.magic = magic
      self.items = items
      self.action = ["ATTACK" , "MAGIC" , "ITEMS"]

   def get_name(self):
       return self.name


   def generate_attack_damage(self):
      return random.randrange(self.atkl,self.atkh)


   def take_damage(self,dmg):
      self.hp = self.hp - dmg
      if self.hp < 0:
         self.hp = 0
      #return self.hp

   def reduce_mp(self,cost):
      self.mp = self.mp - cost

   def heal(self,dmg):
      if self.hp < self.max_hp :
         self.hp = self.hp + dmg
      #return self.hp

   def get_hp(self):
      return self.hp

   def get_mp(self):
      return self.mp

   def get_max_hp(self):
      return self.max_hp

   def get_max_mp(self):
      return self.max_mp

   def choose_action(self):
      i = 1
      for index in self.action:
         print("\t\t"+FG.YELLOW + FG.BOLD + str(i)+":",str(index)+FG.END)
         i += 1

   def choose_magic(self):
      i = 1
      for spell in self.magic:
         print(FG.BOLD + str(i)+" : "+spell.name+"\t\t"+FG.END+"(cost:", str(spell.cost)+")")
         i +=1

   def choose_item(self):
       i = 1
       for item in self.items:
           print(FG.BOLD + str(i)+" : "+item["item"].name + FG.END+"\t\t(Type:", str(item["item"].type)+")" + "\t\t(x"+ str(item["quantity"])+")")
           i+=1

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

       print("\t"+FG.BOLD + FG.LGREEN + str(self.name) + FG.END + " : " + "\t\t" + str(self.hp)+ "/" +str(self.max_hp) + "    " + FG.LGREEN + str(hp_bar) + FG.END
            + "\t"+str(self.mp) + "/" +str(self.max_mp) + "\t" +FG.LBLUE + str(mp_bar) + FG.END + "\n")

   def get_enemy_stats(self):
       print('='*100 + "\n")
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

       while len(mp_bar) < 10 :
           mp_bar += " "

       if len(self.name) > 4 and len(self.name) < 13:
          space = "\t\t"

       if len(self.name) <= 4 :
          space = "\t\t\t"

       if len(self.name) > 13 :
          space = "\t"


       print("\t"+ FG.BOLD + FG.RED + str(self.name) + FG.END + ":" + space + str(self.hp)+ "/" +str(self.max_hp) + "  " + FG.RED + str(hp_bar) + FG.END
            + "  "+str(self.mp) + "/" +str(self.max_mp) + "\t" +FG.PURPLE + str(mp_bar) + FG.END + "\n")
