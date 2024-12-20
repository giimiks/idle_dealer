import pygame
import assets.ui

FPS = 60
bg = ["purple"]

pygame.init()
screen = pygame.display.set_mode(size=(1280, 720), vsync = 1)
clock = pygame.time.Clock()
running = True

def bg_color_change(bg_color_variable):
    if bg_color_variable[0] == "purple":
        bg_color_variable[0]="orange"
    else:
        bg_color_variable[0]="purple"

button = assets.ui.Button((80,80), (600,600),on_click=lambda:bg_color_change(bg), label="test")

ui_elements = [button]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for element in ui_elements:
            element.check_click(event)
    
    
    
    screen.fill(bg[0])
    
    for element in ui_elements:
            element.render(screen)
    

    pygame.display.flip()


pygame.quit()