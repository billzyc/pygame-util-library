import pygame

def drawPixel(window, x, y, color = (255,0,0)):
  pygame.draw.rect(window, color, (x, y, 1, 1))
