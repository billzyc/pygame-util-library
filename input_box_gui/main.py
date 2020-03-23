import pygame
from input_box import InputBox

pygame.init()
window = pygame.display.set_mode((800,800))

testTextBox = InputBox(40, 100, 200, 50, 'enter text here')

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    testTextBox.runInputBox(event)

  window.fill((54,54,54))
  testTextBox.draw(window)

  pygame.display.update()