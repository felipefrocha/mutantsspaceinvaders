from .Positionable import Positionable
from .SuperShot import SuperShot
from .NormalShot import NormalShot

class SpaceShip(Positionable):
  def __init__(self, pos_x, pos_y):
    Positionable.__init__(self, pos_x, pos_y)
    self.list_of_normal_shots = []
    self.list_of_super_shots = []
    self.max_number_of_normal_shots = 3
    self.max_number_of_super_shots = 3
    self.current_number_of_super_shots = 3
  def shot(self):
    if (len(self.get_list_of_normal_shots()) < self.max_number_of_normal_shots):
      self.list_of_normal_shots.append(NormalShot(self.get_pos_x(), 425))
  def super_shot(self):
    if (self.current_number_of_super_shots > 0):
      self.list_of_super_shots.append(SuperShot(self.get_pos_x(), 425))
      self.current_number_of_super_shots -= 1
  def get_list_of_normal_shots(self):
    return self.list_of_normal_shots
  def get_list_of_super_shots(self):
    return self.list_of_super_shots
  def get_current_number_of_super_shots(self):
    return self.current_number_of_super_shots
  def update_space_ship_shots(self):
    SpaceShip.update_space_ship_list_of_shots(self.get_list_of_normal_shots())
    SpaceShip.update_space_ship_list_of_shots(self.get_list_of_super_shots())
    
  def update_space_ship_list_of_shots(list_of_shots):
    shotsToRemove = []
    for i, shot in enumerate(list_of_shots):
        new_pos_y = shot.move()
        if new_pos_y <= 0:
            shotsToRemove.append(i)
    for i in shotsToRemove:
        del list_of_shots[i]

