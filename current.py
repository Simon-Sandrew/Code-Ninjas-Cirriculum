import pygame
import character
import rooms
import controls
import menu

pygame.init()
window = pygame.display.set_mode((800,800))
run = True
display_menu = True
         
eevee = character.eevee(400,400)
gidget = character.gidget(400,400)
crookshanks = character.crookshanks(400,400)

  
character_list = [eevee, gidget, crookshanks]


def redraw_game_window():
    rooms.main(window, character_list[menu.character_count])
    controls.controls(character_list[menu.character_count])
    
def menu_screen():
    global display_menu
    menu.menu()
    
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= 248 and mouseX <= 248+46 and mouseY >= 383 and mouseY <= 383+49:
            menu.room_count +=1
            pygame.time.delay(50)
        if mouseX >= 536 and mouseX <= 536+46 and mouseY >= 383 and mouseY <= 383+49:
            menu.room_count -=1
            pygame.time.delay(50)
        if mouseX >= 536 and mouseX <= 536+46 and mouseY >= 605 and mouseY <= 605+49:
           menu.character_count -= 1
           pygame.time.delay(50)
        if mouseX >= 248 and mouseX <= 248+46 and mouseY >= 605 and mouseY <= 605+49:
            menu.character_count += 1
            pygame.time.delay(50)
        if mouseX >= 360 and mouseX <= 560 and mouseY >= 733 and mouseY <= 763:
            display_menu = False
        
while run == True:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    if display_menu == True:
         menu_screen()
        
    if display_menu == False:
        redraw_game_window()
    
    pygame.display.update()
    
pygame.quit()
