import pygame
from text_box import TextBox

pygame.init()
window = pygame.display.set_mode((800, 800))

testTextBox = TextBox(40, 100, 200, 50, "this is a text")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((54, 54, 54))
    testTextBox.draw(window)

    pygame.display.update()
