import pygame

pygame.init()

window= pygame.display.set_mode((800, 800))

run = True


#changed spawn coordinates so that she spawns on the groun
x = 400
y = 400
walkRight = [pygame.image.load('./eevee_sprites/r1.png'), pygame.image.load('./eevee_sprites/r2.png'), pygame.image.load('./eevee_sprites/r3.png'), pygame.image.load('./eevee_sprites/r4.png'), pygame.image.load('./eevee_sprites/r5.png'), pygame.image.load('./eevee_sprites/r6.png'), pygame.image.load('./eevee_sprites/r7.png')] 
left_standing = [pygame.image.load('./eevee_sprites/s1.png'), pygame.image.load('./eevee_sprites/s2.png'), pygame.image.load('./eevee_sprites/s3.png'), pygame.image.load('./eevee_sprites/s4.png'), pygame.image.load('./eevee_sprites/s5.png'), pygame.image.load('./eevee_sprites/s6.png')]
right_standing = [pygame.image.load('./eevee_sprites/sr1.png'), pygame.image.load('./eevee_sprites/sr2.png'), pygame.image.load('./eevee_sprites/sr3.png'), pygame.image.load('./eevee_sprites/sr4.png'), pygame.image.load('./eevee_sprites/sr5.png'), pygame.image.load('./eevee_sprites/sr6.png')]
walkLeft = [pygame.image.load('./eevee_sprites/l1.png'), pygame.image.load('./eevee_sprites/l2.png'), pygame.image.load('./eevee_sprites/l3.png'), pygame.image.load('./eevee_sprites/l4.png'), pygame.image.load('./eevee_sprites/l5.png'), pygame.image.load('./eevee_sprites/l6.png'), pygame.image.load('./eevee_sprites/l7.png')] 
background = (pygame.image.load('background.png'))

left = False
right = False
last_walk = 0
walking = True
walk_count = 0
stand_count = 0

#collision system for walls
def tl_wall(x,y):
    product1 = (x*-0.5)+526.5
    if y<= product1:
        return True
    else:
       return False
        

def redraw_game_window():
    global walk_count
    global stand_count
    window.blit(background,(0,0))
    
    if walk_count + 1 >= 14:
        walk_count = 0
    if stand_count + 1 >= 12:
        stand_count = 0
    if right == True:
        #Using transform to make eevee bigger
        right_t = pygame.transform.scale(walkRight[walk_count//2], (128, 128)) 
        window.blit(right_t,(x, y))
    if left == True:
        left_t = pygame.transform.scale(walkLeft[walk_count//2], (128, 128)) 
        window.blit(left_t, (x,y))
    if walking == False:
        if last_walk == 0:
            idleLeft_t = pygame.transform.scale(left_standing[stand_count//2], (128, 128)) 
            window.blit(idleLeft_t,(x, y))
        if last_walk == 1:
            idleRight_t = pygame.transform.scale(right_standing[stand_count//2], (128, 128)) 
            window.blit(idleRight_t,(x, y))
            
            
    pygame.display.update()


while run == True:
    
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    
    keys = pygame.key.get_pressed()
    
    tl_wall(x,y)
      
    if keys[pygame.K_w] and y >= 0:
          y = y - 6
    elif keys[pygame.K_s] and y <=736:
          y = y + 6
    elif keys[pygame.K_a] and x >=0:
        if(tl_wall == False):
            x = x - 6
            right = False
            left = True
            last_walk = 0
            walk_count +=1
            walking = True
           
        
        
       
    elif keys[pygame.K_d] and x <=736:
          x = x + 6
          right = True
          left = False
          last_walk = 1
          walk_count +=1
          walking = True
    else:
        right = False
        left = False
        walk_count = 0
        stand_count += 1
        walking = False
          
    redraw_game_window()
   
pygame.quit()