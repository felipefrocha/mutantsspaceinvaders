from .Positionable import Positionable

class Enemy(Positionable):
  def __init__(self, pos_x, pos_y, speed_x, speed_y):
    Positionable.__init__(self, pos_x, pos_y)
    self.speed_x = speed_x
    self.speed_y = speed_y
  def update(self):
    self.update_pos()
  def update_pos(self):
    self.set_pos_x(self.get_pos_x() + self.get_speed_x())
    self.set_pos_y(self.get_pos_y() + self.get_speed_y())
    rect_y = self.get_pos_y()
    rect_x = self.get_pos_x()
    if rect_y > 450 or rect_y < 0:
        self.flip_speed_y()
    if rect_x > 650 or rect_x < 0:
        self.flip_speed_x()
  def get_speed_x(self):
    return self.speed_x
  def get_speed_y(self):
    return self.speed_y
  def flip_speed_x(self):
    self.speed_x *= -1
  def flip_speed_y(self):
    self.speed_y *= -1
    