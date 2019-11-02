from .Shot import Shot

class NormalShot(Shot):
  def __init__(self, pos_x, pos_y):
    Shot.__init__(self, pos_x, pos_y)
    