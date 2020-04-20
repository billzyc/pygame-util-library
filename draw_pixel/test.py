import pygame
from draw_pixel import drawPixel

pygame.init()
window = pygame.display.set_mode((800, 800))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((54, 54, 54))
    drawPixel(window, 50, 50, (255, 255, 255))

    pygame.display.update()
