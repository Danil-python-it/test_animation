from pygame import *
from random import randint


Width = 1200
Heigth = 800
FPS = 60
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
window = display.set_mode((Width,Heigth))
background = transform.scale(image.load("png/background.png"),(Width,Heigth))
clock = time.Clock()
display.set_caption("test_animation")
stutus_fight = False
stutus_xp = False
init()
timer = 45
stutus = True
text = 1
all_sprite = sprite.Group()
all_player = list()
all_angry = list()

Rogue = {
    "body":image.load("png/attack_rogue/rogueAttack1.png"),
    
    "attack":[image.load("png/attack_rogue/rogueAttack1.png"),image.load("png/attack_rogue/rogueAttack2.png"),image.load("png/attack_rogue/rogueAttack3.png"),image.load("png/attack_rogue/rogueAttack4.png"),image.load("png/attack_rogue/rogueAttack5.png"),image.load("png/attack_rogue/rogueAttack6.png"),image.load("png/attack_rogue/rogueAttack7.png"),image.load("png/attack_rogue/rogueAttack1.png")],
    
    "death":[image.load("png/death_rogue/death1.png"),image.load("png/death_rogue/death2.png"),image.load("png/death_rogue/death3.png"),image.load("png/death_rogue/death4.png"),image.load("png/death_rogue/death5.png"),image.load("png/death_rogue/death6.png"),image.load("png/death_rogue/death7.png"),image.load("png/death_rogue/death8.png"),image.load("png/death_rogue/death9.png"),image.load("png/death_rogue/death10.png")],
    
    "hurt":[image.load("png/hurt_rogue/hurt1.png"),image.load("png/hurt_rogue/hurt2.png"),image.load("png/hurt_rogue/hurt3.png"),image.load("png/hurt_rogue/hurt4.png"),image.load("png/attack_rogue/rogueAttack1.png")]
}


Knight = {
    "body":image.load("png/attack_knight/attack0.png"),
    
    "attack":[image.load("png/attack_knight/attack0.png"),image.load("png/attack_knight/attack1.png"),image.load("png/attack_knight/attack2.png"),image.load("png/attack_knight/attack3.png"),image.load("png/attack_knight/attack4.png"),image.load("png/attack_knight/attack0.png")],
    
    "death":[image.load("png/death_knight/death1.png"),image.load("png/death_knight/death2.png"),image.load("png/death_knight/death3.png"),image.load("png/death_knight/death4.png"),image.load("png/death_knight/death5.png"),image.load("png/death_knight/death6.png"),image.load("png/death_knight/death7.png"),image.load("png/death_knight/death8.png"),image.load("png/death_knight/death9.png"),image.load("png/death_knight/death10.png"),],
    
    "hurt":[image.load("png/hurt_knight/hurt1.png"),image.load("png/hurt_knight/hurt2.png"),image.load("png/hurt_knight/hurt3.png"),image.load("png/hurt_knight/hurt4.png"),image.load("png/attack_knight/attack0.png")]
}

class GameSprite(sprite.Sprite):
    def __init__(self, x_coor, y_coor, time, animation_array, width, length, health, attack, list_attack=None):
        super().__init__() 
        self.Font = font.SysFont('arial', 15)
        self.x = x_coor
        self.y = y_coor
        self.animation_body = animation_array
        self.timer = self.num_body = 0
        self.time = time
        self.w = width
        self.xp = health
        self.attack = attack
        self.l = length
        self.body = self.animation_body["body"]
        self.name = "attack"
        self.stutus_life = True
        self.stutus_public = False
        if self.x > Width//2:
            self.body = transform.flip(self.body,True,False)
        self.image = transform.scale(self.body,(self.w,self.l))
        self.rect = Rect(x_coor,y_coor,self.w,self.l)
        self.stutus_animation = False
        self.leader_rect = Rect(0,Heigth-100,Width,100)
        self.rect_attack1 = Rect(self.leader_rect.x+self.leader_rect.height/4,self.leader_rect.top+self.leader_rect.height/4,self.leader_rect.height/2,self.leader_rect.height/2)
        self.rect_attack2 = Rect(self.leader_rect.x+self.leader_rect.height,self.leader_rect.top+self.leader_rect.height/4,self.leader_rect.height/2,self.leader_rect.height/2)
    #region update
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

        if self.stutus_animation != False:
            if self.timer > 0:
                self.timer -= 1
            if self.timer == 0:
                if self.num_body < len(self.animation_body[self.name]):
                    self.body = self.animation_body[self.name][self.num_body]
                    if self.x > Width//2:
                        self.body = transform.flip(self.body,True,False)
                    self.num_body += 1
                    self.timer = 2
                    self.image = transform.scale(self.body,(self.w,self.l))
                
                elif self.num_body == len(self.animation_body[self.name]):
                    
                    self.timer = self.num_body = 0
                    if self.name == "death":
                        self.stutus_life = False
                    self.stutus_animation = False

        if self.xp < 0:
            self.xp *= 0
        self.text = self.Font.render(str(self.xp)+"%", False, (0,0,0))
        rect_red = Rect(self.rect.left,self.rect.bottom,self.rect.width/100*self.xp,5)
        rect_white = Rect(self.rect.left,self.rect.bottom,self.rect.width,5)
        draw.rect(window,WHITE,rect_white)
        draw.rect(window,RED,rect_red)
        window.blit(self.text,(rect_white.x,self.rect.bottom-15))
        
        if self.stutus_public == True:
            draw.rect(window,(0,0,0),self.leader_rect)
            draw.rect(window,(255,255,255),self.rect_attack1)
            draw.rect(window,(255,255,255),self.rect_attack2)

player = GameSprite(Width//2-200,200,10,Knight,200,200,100,10)
angry = GameSprite(player.rect.x+500,200,10,Rogue,200,200,100,10)
player2 = GameSprite(Width//2-200,400,10,Knight,200,200,100,10)
angry2 = GameSprite(player.rect.x+500,400,10,Rogue,200,200,100,10)

all_sprite.add(player)
all_sprite.add(angry)
all_sprite.add(player2)
all_sprite.add(angry2)

all_player.append(player)
all_angry.append(angry)
all_player.append(player2)
all_angry.append(angry2)

game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        

        if i.type == MOUSEBUTTONDOWN:
            x,y = i.pos
            

            for i in all_player:
                if i.rect.collidepoint(x,y) == 1 and stutus_fight == True and angry.stutus_animation == False :
                    i.stutus_public = True
                
                if stutus_fight == True and angry.stutus_animation == False:
                    print(6)
                    if i.stutus_public == True and timer == 0 and i.rect_attack1.collidepoint(x,y) == 1 :
                        angry3 = all_angry[randint(0,len(all_angry)-1)]
                        angry3.name = "hurt"
                        i.name = "attack"
                        angry3.stutus_animation = True
                        i.stutus_animation = True
                        angry3.xp -= i.attack
                        stutus_fight = False
                        i.stutus_public = False
                        timer = 35
                    elif i.stutus_public == True and timer == 0 and i.rect_attack2.collidepoint(x,y) == 1:
                        angry3 = all_angry[randint(0,len(all_angry)-1)]
                        angry3.name = "hurt"
                        i.name = "attack"
                        angry3.stutus_animation = True
                        i.stutus_animation = True
                        angry3.xp -= randint(0,i.attack*3)
                        stutus_fight = False
                        i.stutus_public = False
                        timer = 35

    going = key.get_pressed()
    if going[K_7]:
        for i in all_player:
            i.xp = 100
    window.blit(background,(0,0))
    
    for i in all_sprite:
        i.update()


    if timer > 0 :
        timer -= 1

    if stutus_fight == False and timer == 0 and len(all_angry)>0:
        print(1)
        angry3 = all_angry[randint(0,len(all_angry)-1)]
        player3 = all_player[randint(0,len(all_player)-1)]
        if angry3.stutus_animation == False :
            angry3.name = "attack"
            player3.name = "hurt"
            angry3.stutus_animation = True
            player3.stutus_animation = True
            player3.xp -= angry3.attack
            stutus_fight = True
            timer = 35
        
    for i in all_sprite:
        if i.xp == 0 and i.stutus_life == False:
            i.kill()

        if i.xp == 0 and i.stutus_life == True :
            i.name = "death"
            i.stutus_animation = True

        if i.body == i.animation_body["death"][len(i.animation_body["death"])-1]:
            i.stutus_life = False
    if len(all_angry)>0:
        for i in all_angry:
            if i.xp == 0 and i.stutus_life == False:
                all_angry.remove(i)
    if len(all_player)>0:
        for i in all_player:
            if i.xp == 0 and i.stutus_life == False:
                all_player.remove(i)
    
    display.update()
    clock.tick(FPS)
