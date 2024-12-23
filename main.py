import pygame
import assets.ui
from assets.game_state import GameState

def bg_color_change(game_state: GameState):
    if game_state.background == "purple":
        game_state.background = "orange"
    else:
        game_state.background = "purple"

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(1280, 720), vsync=1)
    running = True

    game_state = GameState(background="orange")
    tooltip = assets.ui.Tooltip(
        (120, 80),
        (600, 600),
        label="tooltip",
        screen=screen
    )

    button = assets.ui.Button(
        (80, 80), 
        (600, 600), 
        on_click=lambda: bg_color_change(game_state), 
        label="test", 
        tooltip=tooltip
    )
    button2 = assets.ui.Button(
        (120, 100), 
        (400, 100), 
        on_click=lambda: bg_color_change(game_state), 
        label="test", 
        tooltip=tooltip
    )


    ui_elements = [button, button2]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for element in ui_elements:
                element.check_click(event)
        
        screen.fill(game_state.background)

        for element in ui_elements:
            element.render(screen)
            element.check_hover()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
