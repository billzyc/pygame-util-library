import pygame

class TextBox:
  def __init__(self, x, y ,width, height, content, fontSize = 20, bgColor = False, textColor = (0,0,0)):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.image = pygame.Surface((width, height))
    self.fontSize = fontSize
    self.bgColor = bgColor
    self.textColor = textColor
    self.content = pygame.font.SysFont('arial', 15).render(content, 1, self.textColor)

  def draw(self, window):
    if(self.bgColor):
      self.image.fill(self.bgColor)
      window.blit(self.image, (self.x, self.y))
    window.blit(self.content, (self.x, self.y))
