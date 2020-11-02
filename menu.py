import pygame

pygame.init()
window = pygame.display.set_mode((800,800))
menu_background = pygame.image.load('./assets/menu.png')
eevee = [pygame.image.load('./eevee_sprites2/sr1.png'), pygame.image.load('./eevee_sprites2/sr2.png'), pygame.image.load('./eevee_sprites2/sr3.png'), pygame.image.load('./eevee_sprites2/sr4.png'), pygame.image.load('./eevee_sprites2/sr5.png'), pygame.image.load('./eevee_sprites2/sr6.png')]
gidget = [pygame.image.load('./gidget_sprites/d1.png'),pygame.image.load('./gidget_sprites/d2.png'),pygame.image.load('./gidget_sprites/d3.png')]
crookshanks = [pygame.image.load('./crookshanks_sprites/d1.png'),pygame.image.load('./crookshanks_sprites/d2.png'),pygame.image.load('./crookshanks_sprites/d3.png'),pygame.image.load('./crookshanks_sprites/d4.png')]
basement = pygame.image.load('./room_titles/basement.png')
bedroom = pygame.image.load('./room_titles/bedroom.png')
backyard = pygame.image.load('./room_titles/backyard.png')


anim_num = 0
character_count = 0
room_count = 0




def characters(character):
    global anim_num
    
    if anim_num + 1 > 11:
        anim_num = 0
        
    #eevee character
    if character == 'eevee':
        window.blit(pygame.transform.scale(eevee[anim_num//2], (100, 100)),(350,570))
    if character == 'gidget':
        window.blit(pygame.transform.scale(gidget[anim_num//4], (84, 136)),(367,570))
    if character == 'crookshanks':
        window.blit(pygame.transform.scale(crookshanks[anim_num//3], (75, 96)),(370,570))



def rooms(room):
    if room == 'basement':
        window.blit(basement, (303, 379))
    if room == 'bedroom':
        window.blit(bedroom, (303, 379))
    if room == 'backyard':
        window.blit(backyard, (303, 385))
        
        

def menu():
    window.blit(menu_background,(0,0))
    main()
    



def main():
    
    global character_count
    global anim_num
    global room_count
    anim_num += 1
    if character_count < 0:
        character_count = 2
    if character_count == 0:
           characters('eevee')
    if character_count == 1:
           characters('gidget')
    if character_count == 2:
           characters('crookshanks')
    if character_count == 3:
        character_count = 0
    
    if  room_count< 0:
        room_count = 2
    if room_count == 0:
        rooms('basement')
    if room_count == 1:
        rooms('bedroom')
    if room_count == 2:
        rooms('backyard')
    if room_count == 3:
        room_count = 0
    
        
        
    
   
    

