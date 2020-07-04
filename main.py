import pygame
from infoBox import InfoBox as info
pygame.init()

window_width = 500
window_height = 500

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pokémon Battle')

info_box_width = 250
info_box_heigth = 100


enemy_info = info(info_box_width, info_box_heigth, { 'x': 0, 'y': 0 })
player_info = info(info_box_width, info_box_heigth, { 'x': window_width / 2, 'y': window_height - info_box_heigth })

run = True

while run:
    pygame.time.delay(100)  # Clock

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Check if X-Button has been clicked
            run = False

    keys = pygame.key.get_pressed()
    win.fill((20, 20, 20))

    enemy_info.drawInfoBox(win, (255, 255, 255))
    player_info.drawInfoBox(win, (255, 255, 255))

    pygame.display.update()
