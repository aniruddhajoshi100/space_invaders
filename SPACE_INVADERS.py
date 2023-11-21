import random
import pygame
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
mixer.music.load("Downloads/background.wav")
mixer.music.play(-1)
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("Downloads/ufo.png")
pygame.display.set_icon(icon)
bg=pygame.image.load("Downloads/background.png")
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
ysfont=pygame.font.Font("freesansbold.ttf",40)
sx=10
sy=10
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,0,0))
    screen.blit(score,(x,y))
def your_score(x,y):
    ys=ysfont.render('YOUR SCORE: '+ str(score_value),True,(255,255,255))
    screen.blit(ys,(x,y))
over_font=pygame.font.Font("freesansbold.ttf",64)
def game_over_font(x,y):
    go=over_font.render("GAME OVER",True,(255,0,0))
    screen.blit(go,(x,y))
px=370
py=480
pxc=0
def player(x,y):
    plyr=pygame.image.load("Downloads/player.png")
    screen.blit(plyr,(x,y))
ex=[]
ey=[]
exc=[]
eyc=[]
enemyimg=[]
noe=6
for i in range(noe):
    ex.append(random.randint(0,735))
    ey.append(random.randint(50,150))
    exc.append(3)
    eyc.append(40)
    enemyimg.append(pygame.image.load("Downloads/enemy.png"))
def collision(ex,ey,bx,by):
    distance=math.sqrt(math.pow(ex - bx, 2) + (math.pow(ey - by, 2)))
    if distance<27:
        return True
    else:
        return False
def collision1(ex,ey,bx1,by1):
    distance=math.sqrt(math.pow(ex - bx1, 2) + (math.pow(ey - by1, 2)))
    if distance<27:
        return True
    else:
        return False
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
bx=0
by=480
bs='ready'
bullet=pygame.image.load("Downloads/bullet.png")
def fire_bullet(x,y):
    global bs
    bs='fire'
    screen.blit(bullet,(x+16,y+10))
bx1=0
by1=480
bs1='ready'
bullet1=pygame.image.load("Downloads/bullet.png")
def fire_bullet_1(x,y):
    global bs1
    bs1='fire'
    screen.blit(bullet1,(x+16,y+10))
bx2=0
by2=480
bs2='ready'
bullet2=pygame.image.load("Downloads/bullet.png")
def fire_bullet_2(x,y):
    global bs2
    bs2='fire'
    screen.blit(bullet2,(x+16,y+10))
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pxc-=3.5
            if event.key==pygame.K_RIGHT:
                pxc+=3.5
            if event.key==pygame.K_SPACE:
                bsound=mixer.Sound("Downloads/laser.wav")
                bsound.play()
                if bs is 'ready':
                    bx=px 
                    fire_bullet(bx,by)
                elif bs is 'fire':
                    if bs1 is 'ready':
                        bx1=px
                        fire_bullet_1(bx1,by1)
                elif bs is 'fire' and bs1 is 'fire':
                    if bs2 is 'ready':
                        bx2=px
                        fire_bullet_2(bx2,by2)
        if event.type==pygame.KEYUP:
            pxc=0
    px+=pxc
    if px<=0:
        px=0
    elif px>=736:
        px=736
    for i in range(noe):
        if ey[i]>=460:
            for j in range(noe):
                ey[j]=2000
            game_over_font(200,250)
            your_score(220,350)           
            break
        if ex[i]<=0:
            exc[i]=+3
            ey[i]+=eyc[i]
        elif ex[i]>=736:
            exc[i]=-3
            ey[i]+=eyc[i]
        ex[i]+=exc[i]
        c=collision(ex[i],ey[i],bx,by)
        c1=collision1(ex[i],ey[i],bx1,by1)
        if c:
            csound=mixer.Sound("Downloads/explosion.wav")
            csound.play()
            exp=pygame.image.load("Downloads/explosion.png")
            screen.blit(exp,(ex[i],ey[i]))
            bs="ready"
            by=480
            ex[i]=random.randint(0,735)
            ey[i]=random.randint(50,150)    
            score_value+=1
        if c1:
            csound=mixer.Sound("Downloads/explosion.wav")
            csound.play()
            exp=pygame.image.load("Downloads/explosion.png")
            screen.blit(exp,(ex[i],ey[i]))
            bs1="ready"
            by1=480
            ex[i]=random.randint(0,735)
            ey[i]=random.randint(50,150)    
            score_value+=1
        enemy(ex[i],ey[i],i)
    if bs is 'fire':
        fire_bullet(bx,by)
        by-=4
    if bs1 is 'fire':
        fire_bullet_1(bx1,by1)
        by1-=4
    if bs2 is 'fire':
        fire_bullet_2(bx2,by2)
        by2-=4
    if by<=0:
        bs='ready'
        by=480
    if by1<=0:
        bs1='ready'
        by1=480
    if by2<=0:
        bs2='ready'
        by2=480
    player(px,py)
    show_score(sx,sy)
    pygame.display.update()   