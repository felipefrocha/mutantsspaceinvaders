from .Constants import *
from .SuperShot import SuperShot
from .NormalShot import NormalShot
import random
import math

class Screen:
  def __init__(self, pygame):
    self.pygame = pygame
    self.screen = pygame.display.set_mode(SIZE)
    self.init_background()
  def init_background(self):
    self.star_list = []
    for i in range(50):
      x = random.randrange(0, 700)
      y = random.randrange(0, 500)
      self.star_list.append([x, y])
  def clear(self):
    self.screen.fill(BLACK)
  def draw_space_ship(self, space_ship):
    x = space_ship.get_pos_x()
    y = space_ship.get_pos_y()
    self.pygame.draw.polygon(self.screen, BLUE, [[x - 6, y], [x + 1, y - 25], [x + 8, y]])
    self.pygame.draw.rect(self.screen, BLUE, [x - 2, y, 3, 5])
    self.pygame.draw.rect(self.screen, BLUE, [x + 3 , y, 3, 5])
    self.draw_space_ship_shots(space_ship)
  def draw_shots(self, shot_list):
    for shot in shot_list:
      if type(shot) is NormalShot:
        self.pygame.draw.rect(self.screen, YELLOW, [shot.get_pos_x(), shot.get_pos_y(), 2, 6])
      elif type(shot) is SuperShot:
        self.pygame.draw.circle(self.screen, RED, [shot.get_pos_x(), shot.get_pos_y()], 10)
  def draw_space_ship_shots(self, space_ship):
    self.draw_shots(space_ship.get_list_of_normal_shots())
    self.draw_shots(space_ship.get_list_of_super_shots())
  def draw_score(self, value):
    fontScore = self.pygame.font.SysFont('Calibri', 25, True, False)
    text = fontScore.render("Score: " + str(value), True, WHITE)
    self.screen.blit(text, [550, 30])
  def draw_super_shot(self, value):
    fontSuperShot = self.pygame.font.SysFont('Calibri', 18, True, False)
    text = fontSuperShot.render("Super shot: " + str(value), True, WHITE)
    self.screen.blit(text, [10, 50])
  def draw_background_stars(self):
    for i in range(len(self.star_list)):
      self.pygame.draw.circle(self.screen, WHITE, self.star_list[i], 2)
      self.star_list[i][1] += 1    
      self.star_list[i][0] += int(math.sin(self.star_list[i][1]))
      if self.star_list[i][1] > 500:
          y = random.randrange(-50, -10)
          self.star_list[i][1] = y
          x = random.randrange(0, 700)
          self.star_list[i][0] = x
  def draw_enemies(self, enemy_list):
    for enemy in enemy_list:
      self.pygame.draw.rect(self.screen, GREEN, [enemy.get_pos_x(), enemy.get_pos_y(), 50, 50])


