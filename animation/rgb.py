from pygame import *
from random import randint


Width = 1000
Heigth = 600
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
    def __init__(self, x_coor, y_coor, time, animation_array, width, length, health, attack):
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
        if self.x > Width//2:
            self.body = transform.flip(self.body,True,False)
        self.image = transform.scale(self.body,(self.w,self.l))
        self.rect = Rect(x_coor,y_coor,self.w,self.l)
        self.stutus_animation = False

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
        rect_black = Rect(self.rect.x,self.rect.bottom-5,self.rect.width,25)
        rect_white = Rect(self.rect.x+2,self.rect.bottom-7,self.rect.width,21)
        rect_red = Rect(self.rect.x+4,self.rect.bottom-9,self.xp*2,17)

        draw.rect(window,BLACK,rect_black)
        draw.rect(window,WHITE,rect_white)
        draw.rect(window,RED,rect_red)
        window.blit(self.text,(self.rect.x+90,self.rect.bottom-9))



class public():
    def __init__(self,x_coor,y_coor,color,width,height):
        self.rect = Rect(x_coor,y_coor,width,height)
        self.color = color
        self.color_window = (204, 102, 0)
        self.Font = font.SysFont('arial', 36)
    
    def draw(self):
        self.rect_one = Rect(self.rect.x+20,self.rect.y+25,50,50)
        self.rect_two = Rect(self.rect.x+90,self.rect.y+25,50,50)
        self.rect_three = Rect(self.rect.x+160,self.rect.y+25,50,50)

        draw.rect(window,self.color_window,self.rect)
        draw.rect(window,(0,255,0),self.rect_one)
        draw.rect(window,(0,0,255),self.rect_two)
        if player.xp < 50 and stutus_xp == False:
            draw.rect(window,(255,0,0),self.rect_three)


player = GameSprite(332,200,10,Knight,200,200,100,10)
angry = GameSprite(682,200,10,Rogue,200,200,100,10)
windwo = public(0,500,BLACK,Width,100)




game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        

        if i.type == MOUSEBUTTONDOWN:
            x,y = i.pos
            res = windwo.rect_one.collidepoint(x,y)
            ras = windwo.rect_two.collidepoint(x,y)
            rus = windwo.rect_three.collidepoint(x,y)
            if res == 1 and stutus_fight == True and timer == 0:
                player.name = "attack"
                angry.name = "hurt"
                player.stutus_animation = True
                angry.stutus_animation = True
                angry.xp -= player.attack
                stutus_fight = False
                timer = 35
            elif ras == 1 and stutus_fight == True and timer == 0:
                
                player.name = "attack"
                angry.name = "hurt"
                player.stutus_animation = True
                angry.stutus_animation = True
                angry.xp -= randint(0,30)
                stutus_fight = False
                timer = 35
            elif rus == 1 and stutus_fight == True and timer == 0 and player.xp < 50 and stutus_xp == False: 
                player.xp += 25
                stutus_fight = False
                stutus_xp  = True
                timer = 35


    going = key.get_pressed()
    window.blit(background,(0,0))
    
    player.update()
    angry.update()
    windwo.draw()


    if timer > 0 and stutus == True:
        timer -= 1


    if stutus_fight == False and angry.stutus_animation == False and timer == 0:
        angry.name = "attack"
        player.name = "hurt"
        angry.stutus_animation = True
        player.stutus_animation = True
        player.xp -= angry.attack
        stutus_fight = True
        timer = 35
    
    if player.xp == 0 and player.stutus_life != False :
        player.stutus_animation = True
        player.name = "death"
        stutus = False


    if angry.xp == 0 and angry.stutus_life != False :
        angry.stutus_animation = True
        angry.name = "death"
        stutus = False
        


    display.update()
    clock.tick(FPS)
