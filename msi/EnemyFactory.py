from .Enemy import Enemy
import random

class EnemyFactory():
  def create(type):
    return EnemyFactory.create_rectangle()

  def create_rectangle():
    rect_x = random.randrange(100, 550)
    rect_y = random.randrange(100, 350)
    rect_change_x = 3 * random.choice([1, -1])
    rect_change_y = 2 * random.choice([1, -1])
    return Enemy(rect_x, rect_y, rect_change_x, rect_change_y)
    