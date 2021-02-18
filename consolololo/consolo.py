import pygame

WHITE   = [255, 255, 255]
BLACK   = [0, 0, 0]

RED     = [255, 0, 0]
ORANGE  = [255, 128, 0]
YELLOW  = [255, 255, 0]
GREEN   = [0, 255, 0]
CYAN    = [0, 255, 128]
AQUA    = [0, 255, 255]
BLUE    = [0, 0, 255]
PURPLE  = [128, 0, 255]
MAGENTA = [255, 0, 128]
GRAY    = [128, 128, 128]

DRED     = [128, 0, 0]
DORANGE  = [128, 64, 0]
DYELLOW  = [128, 128, 0]
DGREEN   = [0, 128, 0]
DCYAN    = [0, 128, 64]
DAQUA    = [0, 128, 128]
DBLUE    = [0, 0, 128]
DPURPLE  = [64, 0, 128]
DMAGENTA = [128, 0, 64]
DGRAY    = [64, 64, 64]

LRED     = [255, 64, 64]
LORANGE  = [255, 180, 64]
LYELLOW  = [255, 255, 64]
LGREEN   = [64, 255, 64]
LCYAN    = [64, 255, 180]
LAQUA    = [64, 255, 255]
LBLUE    = [64, 64, 255]
LPURPLE  = [180, 64, 255]
LMAGENTA = [255, 64, 180]
LGRAY = [180, 180, 180]


def font_width(font, scale=1.0) -> int:
  width = font.get_rect(chr(1))[2] * scale
  return round(width)


def font_height(font, scale=1.0) -> int:
  height = font.get_rect(chr(1))[3] * scale
  return round(height)
