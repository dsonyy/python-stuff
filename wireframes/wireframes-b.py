import pygame
from pygame import Vector2 as v2
from pygame import Vector3 as v3
import random
import copy

WIDTH = 1280
HEIGHT = 720
X = 0
Y = 1
S = 0.005

window = pygame.display.set_mode([WIDTH, HEIGHT])

poly = [
  v3(40,40, 5), v3(40,200, 5), v3(200, 200, 5), v3(200, 40, 5)
]

poly2 = [
  v3(0,0,0), v3(0,100, 0), v3(100, 0, 0), v3(100,100,0)
]

polys = []

origin = v3(0,0,0)
goffset = v3(0,0,0)

def v3_to_v2(v, origin, offset=v3()) -> v2:
  x = v.x + offset.x
  y = v.y + offset.y
  x -= (origin.x - x) * S * (v.z + offset.z)
  y -= (origin.y - y) * S * (v.z + offset.z)

  return v2(x, y)

def draw_walls(p0, p1, color=[255,255,255], width=1) -> list:
  if len(p0) != len(p1):
    return []

  walls = []
  for i in range(len(p0)):
    a = v2(p0[i].x, p0[i].y)
    b = v2(p1[i].x, p1[i].y)
    walls.append([a, b])
    pygame.draw.line(window, color, a, b, width)
  return walls

def draw(poly, origin, color=[255,255,255], offset=v3(), width=1) -> list:
  global goffset
  p0, p1 = [], []
  for i in range(len(poly)):
    a = v3_to_v2(poly[i - 1], origin, offset + goffset)
    b = v3_to_v2(poly[i], origin, offset + goffset)
    p0.append(poly[i] + goffset)
    p1.append(v3(b.x, b.y, 0))

    pygame.draw.line(window, color, a, b, width)
  return [p0, p1]

def main():
  global goffset
  pygame.init()
  running = True
  select = None
  keys = {}
  mode = 0
  tick = 0

  while running:
    for ev in pygame.event.get(): 
      if ev.type == pygame.QUIT:
        running = False
      elif ev.type == pygame.MOUSEBUTTONDOWN:
        if select == None:
          select = v3(ev.pos[0], ev.pos[1], 0) - goffset
          polys.append([select, select, select, select])
        else:
          select = None
      elif ev.type == pygame.MOUSEMOTION:
        if select != None:
          mouse = v3(ev.pos[0], ev.pos[1], 0) - goffset
          polys[-1] = [
            v3(2 * select.x - mouse.x, mouse.y, 0),
            v3(2 * select.x - mouse.x, 2 * select.y - mouse.y, 0),
            v3(mouse.x, 2 * select.y - mouse.y, 0),
            v3(mouse.x, mouse.y, 0),
          ]
      elif ev.type == pygame.KEYDOWN:
        if ev.key not in list(keys.keys()):
          keys[ev.key] = pygame.time.get_ticks()
        if ev.key == pygame.K_0: mode = 0
        elif ev.key == pygame.K_1: mode = 1
        elif ev.key == pygame.K_2: mode = 2
        elif ev.key == pygame.K_3: mode = 3
        elif ev.key == pygame.K_4: mode = 4
        elif ev.key == pygame.K_5: mode = 5
        elif ev.key == pygame.K_6: mode = 6
        elif ev.key == pygame.K_7: mode = 7
        elif ev.key == pygame.K_8: mode = 8
        elif ev.key == pygame.K_9: mode = 9
      elif ev.type == pygame.KEYUP:  
        if ev.key in list(keys.keys()):
          del keys[ev.key]

    if pygame.time.get_ticks() >= tick:
      tick += 10
      for key in list(keys.keys()):
        if key == pygame.K_RIGHT: goffset.x -= 3
        elif key == pygame.K_LEFT: goffset.x += 3
        elif key == pygame.K_UP: goffset.y += 3
        elif key == pygame.K_DOWN: goffset.y -= 3
          
          
    origin = v3(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 0)
    window.fill([10,10,10])
    
    if mode == 0:
      for p in polys:
        draw(p, origin)

    elif mode == 1:
      for p in polys:
        for i in range(5, 20, 5):
          draw(p, origin, color=[20,20,50], offset=v3(0,0,-i))
      for p in polys:
        for i in range(0, 20, 5):
          draw(p, origin, offset=v3(0,0,i))
      if select != None:
        draw(polys[-1], v3(0,0,0), color=[0,0,255], offset=v3(0,0,0))

    elif mode == 2:
      for p in polys:
        new = draw(p, origin, color=[20,20,50], offset=v3(0,0,-15))
        draw_walls(new[0], new[1], color=[20,20,50])
      for p in polys:
        draw(p, origin)
        new = draw(p, origin, offset=v3(0,0,15))
        draw_walls(new[0], new[1])

    pygame.display.flip()

if __name__ == "__main__":
  main()
