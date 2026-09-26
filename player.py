import random

options =("Options: \n (1) Use Item\n (2) Shoot yourself\n (3) Shoot Opponent then self\n (4) roll barrel\n (5) Call for Item")
          
temporary_items = ["a","b","c","d"]

class HP:
  def __init__(self, hp):
    self.hp = hp

  def display_hp(self):
    print(f"HP = {self.hp}")

class Items():
  def __init__(self,items):
    self.items = []

  def add_temporary_items(self):
    self.items.append(temporary_items[random.randint(0,4)])

  def add_starting_items(items,added_items):
    self.items.append(added_item)

  def display_items(self, items):
    print("Items: ")
    for i in range(len(self.items)):
      print(f"({i+1}) : {self.items[i]}")

  def delete_temporary_items(self, items):
    for i in range(len(self.items)):
      if self.items[i] in temporary_items:
        self.items.pop(i)

    
class Player(HP, Items):
  def __init__(self ,name, options, hp, items=None ):
    HP.__init__(self,hp)
    Items.__init__(self,items)
    self.name = name
    self.options = options
  def print_options(self):
    print(self.options)
  def print_stats(self):
    print("Stats: ")
    self.display_hp()
    self.display_items(self.items)

player = Player("Player1", options, 3)

player.add_temporary_items()

player.print_options()
player.print_stats()
    
