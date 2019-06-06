import  random
class item:

    def __init__(self,name,type,description,dmg):
        self.name = name
        self.type = type
        self.description = description
        self.dmg = dmg

    def generate_item_dmg(self):
        low = self.dmg - 10
        hi = self.dmg + 10
        return random.randrange(low,hi)
