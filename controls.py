import pygame
import rooms
import menu


def controls(character):
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and character.y >= 0:
        if rooms.top_left_wall(character.x,character.y) == False and rooms.top_right_wall(character.x, character.y) == False:
            character.y = character.y-6
            
            character.up = True
            character.down = False
            character.left = False
            character.right = False
            character.isSit = False
            character.isLay = False
            character.isJump = False
            character.walking = True
    elif keys[pygame.K_ESCAPE]:
        menu.menu()

    elif keys[pygame.K_c]:
        character.up = False
        character.down = False
        character.left = False
        character.right = False
        character.isSit = True
        character.isLay = False
        character.isJump = False
        character.walking = False
    elif keys[pygame.K_l]:
        character.up = False
        character.down = False
        character.left = False
        character.right = False
        character.isSit = False
        character.isLay = True
        character.isJump = False
        character.walking = False
  
    elif keys[pygame.K_m]:
        if rooms.is_dark == True:
            rooms.is_dark = False
        elif rooms.is_dark == False:
            rooms.is_dark = True
            
    elif keys[pygame.K_s]:
        if rooms.bottom_left_wall(character.x,character.y)== False and rooms.bottom_right_wall(character.x,character.y)== False:
            character.y = character.y+6
            character.up = False
            character.down = False
            character.left = False
            character.right = False
            character.isSit = False
            character.isLay = False
            character.isJump = False
            character.walking = False
     
    elif keys[pygame.K_d]:
        if rooms.top_right_wall(character.x,character.y) == False and rooms.bottom_right_wall(character.x,character.y) == False:
            character.x = character.x+6
            
            character.up = False
            character.down = False
            character.left = False
            character.right = True
            character.isSit = False
            character.isLay = False
            character.isJump = False
            character.walking = True
 
            character.last_walk = 1
            character.walk_count += 1
        
    elif keys[pygame.K_a]:
        if rooms.top_left_wall(character.x,character.y) == False and rooms.bottom_left_wall(character.x,character.y)== False:
            character.x = character.x-6
            
            character.up = False
            character.down = False
            character.left = True
            character.right = False
            character.isSit = False
            character.isLay = False
            character.isJump = False
            character.walking = True
          
            character.last_walk = 0
            character.walk_count += 1
    
    
    elif keys[pygame.K_e]:
        character.x = 355
        character.y = 535
    
    elif keys[pygame.K_SPACE]:
        if not(character.isJump):
            character.up = False
            character.down = False
            character.left = False
            character.right = False
            character.isSit = False
            character.isLay = False
            character.isJump = True
            character.walking = False
            if character.jump_count >= -10:
                neg = 1
                if character.jump_count < 0:
                    neg = -1
                character.y -= (character.jump_count**2)*0.6*neg
                if character.jump_animation_count < 20:
                    character.jump_animation_count +=1
                character.jump_count -=1
            else:
                print('hello')
                character.isJump = False
                character.jump_count = 10
                character.jump_animation_count = 0
    else:
        character.up = False
        character.down = False
        character.left = False
        character.right = False
        character.isSit = False
        character.isLay = False
        character.isJump = False
        character.walking = False
        character.stand_count += 1