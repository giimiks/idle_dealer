import pygame
from abc import ABC, abstractmethod


class UI_Element(ABC):
    def __init__(self, size: tuple[float, float], coords: tuple[float, float], on_click=None, label=str, texture = None):
        self.width = size[0]
        self.height = size[1]
        self.x = coords[0]
        self.y = coords[1]
        self.label = label
        self.onclick = on_click
        self.texture = texture
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    @abstractmethod
    def on_click(self):
        pass

    @abstractmethod
    def on_hover(self):
        pass
    
    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return self.on_hover()

    def check_click(self, event: pygame.event.EventType):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.on_click()
    
    def render(self, screen: pygame.SurfaceType):
        if self.texture:
            screen.blit(self.texture, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (200, 200, 200), self.rect) 
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  

            # Render the label if available
            if self.label:
                font = pygame.font.Font(None, 24)
                text_surface = font.render(self.label, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)


class Tooltip(UI_Element):
    def __init__(self, size, coords, on_click=None, label=str, texture=None, screen=None):
        super().__init__(size, coords, on_click, label, texture)
        self.screen = screen
    
    def on_click(self):
        return super().on_click()
    
    def on_hover(self):
        return super().on_hover()

    def update_position(self, mouse_pos):
        self.x, self.y = mouse_pos
        self.rect.bottomright = mouse_pos
        
    def show(self, screen: pygame.SurfaceType):
        if self.texture:
            screen.blit(self.texture, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (200, 200, 200), self.rect) 
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  

            if self.label:
                font = pygame.font.Font(None, 24)
                text_surface = font.render(self.label, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)



class Button(UI_Element):
    def __init__(self, size, coords, on_click=None, label: str = "", texture=None, tooltip: Tooltip | None = None):
        super().__init__(size, coords, on_click, label, texture)
        self.tooltip = tooltip
        
    def on_click(self):
        return self.onclick()
    
    def on_hover(self):
        if self.tooltip is None:
            return super().on_hover()
        else:
            self.tooltip.update_position(pygame.mouse.get_pos())  # Aktualizuje pozici tooltipu
            self.tooltip.show(self.tooltip.screen)
            
            
    
    def render(self, screen: pygame.Surface):
        if self.texture:
            screen.blit(self.texture, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (200, 200, 200), self.rect) 
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  

            if self.label:
                font = pygame.font.Font(None, 24)
                text_surface = font.render(self.label, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=self.rect.center)
                screen.blit(text_surface, text_rect)
