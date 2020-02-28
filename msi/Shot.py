from .Positionable import Positionable

class Shot(Positionable):
  def __init__(self, pos_x, pos_y):
    Positionable.__init__(self, pos_x, pos_y)
  def move(self):
    pos_y = self.get_pos_y() - 3
    self.set_pos_y(pos_y)
    return pos_y
