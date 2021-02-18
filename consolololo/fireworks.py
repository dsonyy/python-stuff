import pygame as pg
import pygame.freetype as pgft
import consolo as c
from random import randrange, uniform, choice
from math import sqrt
from ascii import *

WIDTH = 60
HEIGHT = 60
SCALE = 1
FONT_PATH = "fonts/unscii-8-fantasy.pcf"

X = 0
Y = 1
R = 0
G = 1
B = 2

font = None
font_width = None
font_height = None
window = None
keys = {}

class Firework:
  def __init__(self, pos, ticks_per_update):
    self.pos = pos
    self.pos_px = 0
    self.ticks_per_update = ticks_per_update
    self.ticks_per_update_base = ticks_per_update
    self.start_time = pg.time.get_ticks()
    self.clock = self.start_time + self.ticks_per_update
    self.color = c.WHITE
    if pos[X] > 0.66 * WIDTH:
      self.direction = choice([-1, 0])
    elif pos[X] < 0.33 * WIDTH:
      self.direction = choice([0,  1])
    else:
      self.direction = choice([-1, 0, 1])
    self.alive = True

  def update(self):
    #if pg.time.get_ticks() >= self.clock:
      self.move()
      self.clock += self.ticks_per_update
      
    # self.clock += self.ticks_per_update
    # if self.clock >= 1:
    #   self.clock -= 1
    #   self.move()
    #   if self.alive:
    #     self.ticks_per_update -= 0.03 * self.ticks_per_update
    #   else:
    #     self.ticks_per_update += 0.03
    #   if self.ticks_per_update < 0.2:
    #     self.alive = False

  def move(self):
    self.pos[X] += 0 
    #self.pos[Y] = HEIGHT - 1 - int((pg.time.get_ticks() - self.start_time) / self.ticks_per_update)
    self.pos[Y] = HEIGHT - 1 - 1/((pg.time.get_ticks() - self.start_time)/ 1000)**4

    # self.pos_px += self.direction
    # if self.pos_px >= 1:
    #   self.pos[X] += int(self.pos_px)    
    #   self.pos_px -= 1
    # elif self.pos_px <= -1:
    #   self.pos[X] += int(self.pos_px)    
    #   self.pos_px += 1
    # if self.alive:
    #   self.pos[Y] -= 1
    # else:
    #   self.pos[Y] += 1 
  

  def write(self):
    self.color = [55+randrange(200), 55+randrange(200), 55+randrange(200)]
    if self.direction < -0.25: write("\\", self.pos, self.color)
    elif self.direction > 0.25: write("/", self.pos, self.color)
    else: write("│", self.pos, self.color)


  def get_light_delta(self, point):
    if not self.alive:
      return [0, 0, 0] 

    mul = 0.5
    color = [self.color[R] * mul, self.color[G] * mul, self.color[B] * mul]
    delta = light(self.pos, point, color)
    return delta
    
  def kill(self):
    self.alive = False

# scene
cursor = [5,5]
fireworks = [Firework([30,60], 50),
             Firework([5,60], 3),
             Firework([20,60], 6),
             Firework([40,60], 6)]

def to_px(x, y):
  x_px = x * SCALE * font_width
  y_px = y * SCALE * font_height
  return [x_px, y_px]

def to_char_pos(x, y):
  x_ch = int(x / (font_width))
  y_ch = int(y / (font_height))
  return [x_ch, y_ch]

def update_title(pos):
  if pos in [cursor, [cursor[0] - 1, cursor[1]], [cursor[0] + 1, cursor[1]]]:
    pg.display.set_caption("It's a cursor")
  else:
    print(pos)
    pg.display.set_caption(str(pos[0]) + " " + str(pos[1]))

def write(t, pos, fg=c.WHITE, bg=None):
  txt = font.render(t, fg, bg)[0]
  txt = pg.transform.scale(txt, (len(t) * font_width, font_height))
  window.blit(txt, [pos[0] * font_width, pos[1] * font_height])

def write_cursor(pos):
  write("> <", [pos[0] - 1, pos[1]])


def light(pos_a, pos_b, color_weights):
  dist = sqrt((pos_a[0] - pos_b[0])**2 + (pos_a[1] - pos_b[1])**2)
  if dist < 1:
    dist = 1
  delta_r = color_weights[0] * (1 / dist)
  delta_g = color_weights[1] * (1 / dist)
  delta_b = color_weights[2] * (1 / dist)
  return [delta_r, delta_g, delta_b]

def merge_deltas(deltas, color):
  delta_r = 0
  delta_g = 0
  delta_b = 0
  
  for delta in deltas:
    delta_r += delta[0]
    delta_g += delta[1]
    delta_b += delta[2]

  return [color[0] + delta_r, color[1] + delta_g, color[2] + delta_b]

def write_city():
  city = buildings[2]

  for row in range(len(city)):
    for col in range(len(city[row])):
      color = c.DGRAY
      color = merge_deltas([c.get_light_delta([col, WIDTH - len(city) + row]) for c in fireworks], color)
      
      if color[0] > 255: color[0] = 255
      if color[1] > 255: color[1] = 255
      if color[2] > 255: color[2] = 255
        
      if color[0] < 0: color[0] = 0
      if color[1] < 0: color[1] = 0
      if color[2] < 0: color[2] = 0        
      
      write(city[row][col], [col, WIDTH - len(city) + row], color, None)


def write_score(score):
  strs = [
    ["  **  * *  |▄̸̷/",
     "*       * *|│",
     " *       * ",
     "*         *",
     " **      * ",
     "   * *  *  "],
    
    ["    * ",
     "  **  ",
     " *   * ",
     "    *  ",
     "    *  ",
     "   *   "],
    
    ["    *  *  ",
     "  *    *  ",
     "       *  ",
     "        * ",
     "      *   ",
     " **   *  *"],
  ]

  y = 5

  no = 0
  x = (WIDTH / 2 + 1) - len(strs[no][0]) - 1
  for row in range(len(strs[no])):
    write(strs[no][row], [x,y + row], c.DGRAY)

  no = 1
  x = (WIDTH / 2 + 1)
  for row in range(len(strs[no])):
    write(strs[no][row], [x ,y + row], c.DGRAY)

def flash():
  window.fill(c.WHITE)
  write_cursor(cursor)
  pg.display.flip()
  pg.time.wait(50)

def init():
  print("Initializing game.")
  pg.init()
  pgft.init()

  global font, font_width, font_height, window

  font = pgft.Font(FONT_PATH)
  font_width = c.font_width(font, SCALE) 
  font_height = c.font_height(font, SCALE) 
  
  window = pg.display.set_mode([font_width * WIDTH, font_height * HEIGHT])
  window.fill(c.BLACK)
  pg.display.flip()

def loop():
  running = True
  redraw = True
  global keys, window
  tick = pg.time.get_ticks()

  while running:
    for event in pg.event.get(): 
      if event.type == pg.QUIT:
        running = False
      elif event.type == pg.KEYDOWN:
        if event.key not in list(keys.keys()):
          keys[event.key] = pg.time.get_ticks()
      elif event.type == pg.KEYUP:  
        if event.key in list(keys.keys()):
          del keys[event.key]
      elif event.type == pg.MOUSEBUTTONDOWN:
        pos = to_char_pos(event.pos[0], event.pos[1])
        update_title(pos)

    if pg.time.get_ticks() >= tick:
      tick += 50
      for key in list(keys.keys()):
        if key == pg.K_RIGHT and cursor[0] < WIDTH - 1:
          cursor[0] += 1
        elif key == pg.K_LEFT and cursor[0] > 0:
          cursor[0] -= 1
        if key == pg.K_UP and cursor[1] > 0:
          cursor[1] -= 1
        elif key == pg.K_DOWN and cursor[1] < HEIGHT - 1:
          cursor[1] += 1
        elif key == pg.K_z:
          if keys[key] != None:
            flash()
            keys[key] = None
  
    for fw in fireworks:
      fw.update()
      
    if redraw:
      window.fill(c.BLACK)
      write_score(0)
      write_city()
      write_cursor(cursor)    
      for fw in fireworks:
        fw.write()
      pg.display.flip()      



def main():
  init()
  loop()


if __name__ == "__main__":
  main()
