import random
from .magic import spell
from .inventory import item
class FF:
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


class Person:

   def __init__(self,hp,atk,mp,df,magic,items):
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
         print(FF.LGREEN + FF.BOLD + str(i)+":",str(index)+FF.END)
         i += 1
      print(FF.UNDERLINE + FF.LGREY + "\t\t\t\t\t\t\t\t\t" + FF.END)

   def choose_magic(self):
      i = 1
      for spell in self.magic:
         print(FF.BOLD + str(i)+" : "+spell.name+"\t\t"+FF.END+"(cost:", str(spell.cost)+")")
         i +=1
      print(FF.UNDERLINE + FF.LGREY + "\t\t\t\t\t\t\t\t\t" + FF.END)

   def choose_item(self):
       i = 1
       for item in self.items:
           print(FF.BOLD + str(i)+" : "+item.name+"\t\t"+FF.END+"(Type:", str(item.type)+")")
           i+=1
       print(FF.UNDERLINE + FF.LGREY + "\t\t\t\t\t\t\t\t\t" + FF.END)