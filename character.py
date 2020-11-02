import pygame

#eevee pictures
eevee_walk_right = [pygame.image.load('./eevee_sprites2/r1.png'), pygame.image.load('./eevee_sprites2/r2.png'), pygame.image.load('./eevee_sprites2/r3.png'), pygame.image.load('./eevee_sprites2/r4.png'), pygame.image.load('./eevee_sprites2/r5.png'), pygame.image.load('./eevee_sprites2/r6.png'), pygame.image.load('./eevee_sprites2/r7.png')] 
eevee_left_standing = [pygame.image.load('./eevee_sprites2/s1.png'), pygame.image.load('./eevee_sprites2/s2.png'), pygame.image.load('./eevee_sprites2/s3.png'), pygame.image.load('./eevee_sprites2/s4.png'), pygame.image.load('./eevee_sprites2/s5.png'), pygame.image.load('./eevee_sprites2/s6.png')]
eevee_right_standing = [pygame.image.load('./eevee_sprites2/sr1.png'), pygame.image.load('./eevee_sprites2/sr2.png'), pygame.image.load('./eevee_sprites2/sr3.png'), pygame.image.load('./eevee_sprites2/sr4.png'), pygame.image.load('./eevee_sprites2/sr5.png'), pygame.image.load('./eevee_sprites2/sr6.png')]
eevee_walk_left = [pygame.image.load('./eevee_sprites2/l1.png'), pygame.image.load('./eevee_sprites2/l2.png'), pygame.image.load('./eevee_sprites2/l3.png'), pygame.image.load('./eevee_sprites2/l4.png'), pygame.image.load('./eevee_sprites2/l5.png'), pygame.image.load('./eevee_sprites2/l6.png'), pygame.image.load('./eevee_sprites2/l7.png')] 
eevee_jumping = [pygame.image.load('./eevee_sprites2/j1.png'),pygame.image.load('./eevee_sprites2/j2.png'),pygame.image.load('./eevee_sprites2/j3.png'), pygame.image.load('./eevee_sprites2/j4.png')]
eevee_sitting = pygame.image.load('./eevee_sprites2/sitting1.png')

#gidget pictures
gidget_down = [pygame.image.load('./gidget_sprites/d1.png'),pygame.image.load('./gidget_sprites/d2.png'),pygame.image.load('./gidget_sprites/d3.png')]
gidget_up = [pygame.image.load('./gidget_sprites/u1.png'),pygame.image.load('./gidget_sprites/u2.png'),pygame.image.load('./gidget_sprites/u3.png')]
gidget_right = [pygame.image.load('./gidget_sprites/r1.png'),pygame.image.load('./gidget_sprites/r2.png'),pygame.image.load('./gidget_sprites/r3.png')]
gidget_left = [pygame.image.load('./gidget_sprites/l1.png'),pygame.image.load('./gidget_sprites/l2.png'),pygame.image.load('./gidget_sprites/l3.png')]

#crookshanks picutres
crookshanks_down = [pygame.image.load('./crookshanks_sprites/d1.png'),pygame.image.load('./crookshanks_sprites/d2.png'),pygame.image.load('./crookshanks_sprites/d3.png'),pygame.image.load('./crookshanks_sprites/d4.png')]
crookshanks_up = [pygame.image.load('./crookshanks_sprites/u1.png'),pygame.image.load('./crookshanks_sprites/u2.png'),pygame.image.load('./crookshanks_sprites/u3.png'),pygame.image.load('./crookshanks_sprites/u4.png')]
crookshanks_left = [pygame.image.load('./crookshanks_sprites/l1.png'),pygame.image.load('./crookshanks_sprites/l2.png'),pygame.image.load('./crookshanks_sprites/l3.png'),pygame.image.load('./crookshanks_sprites/l4.png')]
crookshanks_right = [pygame.image.load('./crookshanks_sprites/r1.png'),pygame.image.load('./crookshanks_sprites/r2.png'),pygame.image.load('./crookshanks_sprites/r3.png'),pygame.image.load('./crookshanks_sprites/r4.png')]
crookshanks_standing = [pygame.image.load('./crookshanks_sprites/s1.png'),pygame.image.load('./crookshanks_sprites/s2.png')]
crookshanks_lay = pygame.image.load('./crookshanks_sprites/lay.png')
crookshanks_sit = pygame.image.load('./crookshanks_sprites/sit.png')


class eevee(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.walking = True
        self.last_walk = 0
        self.walk_count = 0
        self.stand_count = 0
        self.jump_animation_count = 0
        self.jump_count = 10
        self.isJump = False
        self.isSit = False
        self.isLay = False
        self.up = False
        self.down = False
        
    def draw(self,window):
        if self.walk_count +1 >= 14:
            self.walk_count = 0
        if self.stand_count + 1 >=12:
            self.stand_count = 0
        if self.jump_animation_count <=8:
            self.jump_animation_count = 0
        #below is right animation
        if self.left == False and self.right == True and self.up == False and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            right_t = pygame.transform.scale(eevee_walk_right[self.walk_count//2],(64,64))
            window.blit(right_t,(self.x,self.y))\
        #below is left
        if self.left == True and self.right == False and self.up == False and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            left_t = pygame.transform.scale(eevee_walk_left[self.walk_count//2],(64,64))
            window.blit(left_t,(self.x,self.y))
        #below is standing 
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == False:
            if self.last_walk == 0:
                standingL_t = pygame.transform.scale(eevee_left_standing[self.stand_count//2],(64,64))
                window.blit(standingL_t,(self.x,self.y))
            if self.last_walk == 1:
                standingR_t = pygame.transform.scale(eevee_right_standing[self.stand_count//2],(64,64))
                window.blit(standingR_t,(self.x,self.y))
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == True and self.isSit == False and self.isLay == False:
            jumpingUR = pygame.transform.scale(eevee_jumping[self.jump_animation_count//2],(64,64))
            window.blit(jumpingUR, (self.x, self.y))
            
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == True and self.isLay == False:
            window.blit(pygame.transform.scale(eevee_sitting, (64,64)), (self.x, self.y))
            
        #below is up animation
        if self.left == False and self.right == False and self.up == True and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            window.blit(pygame.transform.scale(eevee_walk_right[self.walk_count//2], (64,64)),(self.x, self.y))
        #below is down animation
        if self.left == False and self.right == False and self.up == False and self.down == True and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            window.blit(pygame.transform.scale(eevee_walk_left[self.walk_count//2], (64,64)),(self.x, self.y))
            
            
class gidget(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walking = True
        self.last_walk = 0
        self.walk_count = 0
        self.stand_count = 0
        self.jump_animation_count = 0
        self.jump_count = 10
        self.isJump = False
        self.isSit = False
        
    def draw(self,window):
        #self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == False
        
        if self.walk_count +1 >= 7: #walk animation
            self.walk_count = 0
        if self.stand_count + 1 >= 7: #stand animation
            self.stand_count = 0
        if self.jump_animation_count <=7: #jump animation
            self.jump_animation_count = 0
        #below is right animation
        if self.left == False and self.right == True and self.up == False and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            right_t = pygame.transform.scale(gidget_right[self.walk_count//2],(64,64))
            window.blit(right_t,(self.x,self.y))
        #below is left animation
        if self.left == True and self.right == False and self.up == False and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            left_t = pygame.transform.scale(gidget_left[self.walk_count//2],(64,64))
            window.blit(left_t,(self.x,self.y))
        #below is standing animation
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == False:
                standingL_t = pygame.transform.scale(gidget_down[self.stand_count//2],(64,64))
                window.blit(standingL_t,(self.x,self.y))
        #below is jumping animation
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == True and self.isSit == False and self.isLay == False:
            jumpingUR = pygame.transform.scale(gidget_down[self.jump_animation_count//2],(64,64))
            window.blit(jumpingUR, (self.x, self.y))
        #below is up animation
        if self.left == False and self.right == False and self.up == True and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            window.blit(pygame.transform.scale(gidget_up[self.walk_count//2], (64,64)),(self.x, self.y))
        #below is down animation
        if self.left == False and self.right == False and self.up == False and self.down == True and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            window.blit(pygame.transform.scale(gidget_down[self.walk_count//2], (50,64)),(self.x, self.y))
# =============================================================================
#         #below is sit animation
#         if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == True and self.isLay == False:
#             window.blit(pygame.transform.scale(crookshanks_sit, (64,64)), (self.x, self.y))
#         #below is lay animation
#         if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == True:
#             window.blit(pygame.transform.scale(crookshanks_lay, (64,64)), (self.x, self.y))    
# =============================================================================
            

class crookshanks(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walking = True
        self.walk_count = 0
        self.stand_count = 0
        self.jump_animation_count = 0
        self.jump_count = 10
        self.isJump = False
        self.isSit = False
        self.isLay = False
        
    def draw(self,window):
        
        #self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == False
        
        if self.walk_count +1 >= 11: #walk animation
            self.walk_count = 0
        if self.stand_count + 1 > 11: #stand animation
            self.stand_count = 0
        if self.jump_animation_count <=11: #jump animation
            self.jump_animation_count = 0
        #below is right animation
        if self.left == False and self.right == True and self.up == False and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            right_t = pygame.transform.scale(crookshanks_right[self.walk_count//3],(64,64))
            window.blit(right_t,(self.x,self.y))
        #below is left animation
        if self.left == True and self.right == False and self.up == False and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            left_t = pygame.transform.scale(crookshanks_left[self.walk_count//3],(64,64))
            window.blit(left_t,(self.x,self.y))
        #below is standing animation
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == False:
                print('hello')
                standingL_t = pygame.transform.scale(crookshanks_down[self.stand_count//3],(64,64))
                window.blit(standingL_t,(self.x,self.y))
        #below is jumping animation
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == True and self.isSit == False and self.isLay == False:
            jumpingUR = pygame.transform.scale(crookshanks_down[self.jump_animation_count//3],(64,64))
            window.blit(jumpingUR, (self.x, self.y))
        #below is up animation
        if self.left == False and self.right == False and self.up == True and self.down == False and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            window.blit(pygame.transform.scale(crookshanks_up[self.walk_count//3], (64,64)),(self.x, self.y))
        #below is down animation
        if self.left == False and self.right == False and self.up == False and self.down == True and self.walking == True and self.isJump == False and self.isSit == False and self.isLay == False:
            window.blit(pygame.transform.scale(crookshanks_down[self.walk_count//3], (50,64)),(self.x, self.y))
        #below is sit animation
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == True and self.isLay == False:
            window.blit(pygame.transform.scale(crookshanks_sit, (64,64)), (self.x, self.y))
        #below is lay animation
        if self.left == False and self.right == False and self.up == False and self.down == False and self.walking == False and self.isJump == False and self.isSit == False and self.isLay == True:
            window.blit(pygame.transform.scale(crookshanks_lay, (64,64)), (self.x, self.y))    
            
            

