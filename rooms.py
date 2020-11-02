import pygame
import menu

basement_image = pygame.image.load('./assets/background.png')
bedroom_image = pygame.image.load('./assets/bedroom.png')
dark_mode = pygame.image.load('./assets/dark_mode_bedroom.png')
backyard_image = pygame.image.load('./assets/backyard.png')
is_dark = False

def bottom_right_wall(x,y):
    product = (-.5*x) + 887
    if y+60>= product:
        return True
    else:
        return False

def top_right_wall(x,y):
    product = (.5*x) + 123
    if y <= product:
        return True
    else:
        return False
    
def top_left_wall(x,y):
    product = (-0.519*x)+526.5
    if y <= product:
        return True
    else:
        return False
  
def bottom_left_wall(x,y):
    product = (.519*x) + 480
    if y +40 >= product:
        return True
    else:
        return False





def basement(window, character):
    window.blit(basement_image,(0,0))
    character.draw(window)

def main(window,character):
    if menu.room_count == 0:
        basement(window, character)
    if menu.room_count == 1:
        bedroom(window, character)
    if menu.room_count == 2:
        backyard(window, character)
    
    
    
    
    
def bedroom(window, character):
    window.blit(bedroom_image, (0,0))
    
    character.draw(window)
    
    if is_dark:
        window.blit(dark_mode,(0,0))
        
        
        
def backyard(window, character):
    window.blit(backyard_image,(0,0))
    character.draw(window)
        
        
