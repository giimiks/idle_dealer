import pygame
import assets.ui
from assets.game_state import GameState

FPS = 60

pygame.init()
screen = pygame.display.set_mode(size=(1280, 720), vsync = 1)
clock = pygame.time.Clock()
running = True

def bg_color_change(game_state: GameState):
    if game_state.background == "purple":
        game_state.background="orange"
    else:
        game_state.background="purple"

game_state = GameState(background="orange")

button = assets.ui.Button((80,80), (600,600),on_click=lambda:bg_color_change(game_state), label="test")



ui_elements = [button]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for element in ui_elements:
            element.check_click(event)
    
    
    
    screen.fill(game_state.background)
    
    for element in ui_elements:
            element.render(screen)
    

    pygame.display.flip()


pygame.quit()