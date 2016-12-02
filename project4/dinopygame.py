#### I want to create game where a player runs forward and then obstacles get in his way and 
# the player needs to avoid getting hit by jumping over the obstacle. 
# If the player fails to jump over it and collides with the obstacle, then the player loses. 
# Each time the player successfully jumps over the obstacle, then the score increases by one.


from pygame import *
from pygame.sprite import *
from random import * 
from pygame.locals import K_RETURN, KEYDOWN, K_RIGHT, K_LEFT, K_r, K_ESCAPE
import os



screen = display.set_mode((1000, 600))
display.set_caption('T-rex vs Cacti')
DELAY = 1000; 

bgcolor = (0,42,196)    #Color taken from background of sprite
bg = pygame.image.load(os.path.join('images', 'desert.bmp'))
bg_x = 0
bg_y = -200
x_pos = 0
y_pos = 200
WIDTH = 1000
HEIGHT = 800

class Dinosaur(Sprite): # inherit from Sprite class
    def __init__(self): # when it is time to creat a new peice of gold, then initialize with this code
        Sprite.__init__(self) # make a brand new sprite for me and now I'm going to update it with the information that I want
        self.image = pygame.image.load(os.path.join("images","2.bmp")).convert_alpha() # this is the file that i want to use #this is an attribute
        self.rect = self.image.get_rect() #create a rectangle #this is an attribute thats calls a method on it
        self.x = WIDTH - 300
        self.y = 400
        self.jump = False
        self.rect.center = (self.x, self.y)

    def pause(self):
        self.rect.center = (self.x, self.y)

    # move gold to a new location
    def moveup(self): # sprites do not have a move method so we need to define it
        randY = 200 # this is a function that is getting a random number and saving it under the variable randY and randX
        self.rect.center = (self.x ,(self.y - randY)) # setting the center of the rectangle to be the the random numbers created above
        self.jump = True 
    def movedown(self):
    	self.rect.center = (self.x, self.y)
    	self.jump = False

        # Did shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target) #if i call the hit method, this is a question: did I hit it? Did we collide? 



class Cactus(Sprite): # inherit from Sprite class
    def __init__(self): # when it is time to creat a new peice of gold, then initialize with this code
        Sprite.__init__(self) # make a brand new sprite for me and now I'm going to update it with the information that I want
        self.image = pygame.image.load(os.path.join("images","cactus.bmp")).convert_alpha() # this is the file that i want to use #this is an attribute
        self.rect = self.image.get_rect() #create a rectangle #this is an attribute thats calls a method on it
        self.initialy  = 390
        self.initialx = -20
        self.x = -20
        self.y = 390
        self.rect.center = (self.x, self.y)
        

    def update(self):
        self.x += 40
        self.rect.center = (self.x , self.initialy) # whereve the mous is, that is where I want the shovel to move

class MovingBackground(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "desert.bmp")).convert_alpha()
        self.rect = self.image.get_rect()
        self.initialx = 160
        self.initialy = 80
        self.x = 160
        self.y = 80
        self.rightside = self.image.get_size()[0]
        self.rect.center = (self.x, self.y)
        

    def move_left(self):
        self.x += 10
        self.rect.center = (self.x, self.y)

class Coin(Cactus):
    def update(self):
        self.x += 20
        self.rect.center = (self.x, self.y)

    def Kill(self):
        self.x = -10
        self.rect.center = (self.x, self.y)
init()

pic = MovingBackground()
cactus = Cactus()
trex = Dinosaur()
cac = Cactus()
cac.image = pygame.image.load(os.path.join("images","1.bmp")).convert_alpha()
coin = Coin()
coin.image = pygame.image.load(os.path.join("images","coint.bmp")).convert_alpha()
coin.y = 200


f = font.Font(None, 36)
f1 = font.Font(None, 36)
f2 = font.Font(None, 48)
title = font.Font(None, 36)
restarttext = font.Font(None, 36)
# print (cactus.y)
# creates a group of sprites so all can be updated at once

sprite1 = RenderPlain(pic)
sprites2 = RenderPlain(cactus)
sprites3 = RenderPlain(trex)
sprite4 = RenderPlain(cac)
sprite5 = RenderPlain(coin)

pas = 0
hits = 0
time.set_timer(USEREVENT + 1, DELAY)


gameOver = False
restartAgain = False
reallyRestart = False
x = 0
killedCoin = False
while not gameOver:
    if x == 0:
        Title= title.render('''Press ENTER to jump. Good Luck!''', False, (255,255,255))
        screen.blit(Title, (200,200))
        display.update()
        pygame.time.delay(3000)
    x+=1
    
    for event in pygame.event.get():

        if event.type == QUIT:
            gameOver = True
            quit()
            break

        elif event.type == KEYDOWN:

            if event.key == K_RETURN:
                trex.moveup()
                mixer.Sound("spin_jump-Brandino.wav").play()

                if trex.hit(cactus) or trex.hit(cac):
                    mixer.Sound("BellSoundRing.wav").play()
                    pygame.time.delay(1500)
                    print ("You died when you jumped")
                    restartAgain = True
                    break

                if trex.hit(coin):
                    hits += 50
                    mixer.Sound("MarioCoin.wav").play() # play this sound if my dinosaur class hits the coin class
                    print ("You hit the coin")
                    coin.Kill()

        elif event.type == USEREVENT + 1:
            if trex.jump == True:
               
                trex.movedown()
                mixer.Sound("Close-Vault-Or-Jail-Door.wav").play()
                if trex.hit(cactus) or trex.hit(cac):
                    mixer.Sound("BellSoundRing.wav").play()
                    pygame.time.delay(1500)
                    print ("you died coming down!")
                    restartAgain = True
                    break

    if trex.hit(cactus) or trex.hit(cac):
        print ("you died because you did not jump!")
        mixer.Sound("BellSoundRing.wav").play()
        fail = f2.render("You hit the cactus. You lose!", False, (0, 0,255))
        screen.blit(fail, (250,300))
        display.update()
        pygame.time.delay(4000)
        restartAgain = True
        # gameOver = True
        # quit()
        # break

    if x % 5 ==0:
        hits +=1

    pic.move_left()
    if pic.x >= 800:
        pic.x = 160

    if cactus.x >= 1000:
        pas +=1
        cactus.x = -10

    if cac.x >= 1000:
        pas +=1
        cac.x = -10

    if coin.x >= 1000:
        coin.x = -10

    screen.blit(bg, (bg_x, bg_y))


    t = f.render("SCORE = " + str(hits), False, (0,0,0))
    pic.update()
    trex.update()
    coin.update()
    

    if pas %3 == 0:
        cac.update()
    else:
        cactus.update()
    


    sprite1.draw(screen)
    sprites2.draw(screen)
    sprites3.draw(screen)
    sprite4.draw(screen)
    sprite5.draw(screen)

    screen.blit(t, (320,0))
    display.update()

    while restartAgain==True:
        restarttext1 = restarttext.render('Your score is: ' + str(hits) + ' To play again press "R" or press "Escape" to leave the game', False, (255,255,255))
        screen.blit(restarttext1, (50, 200))
        display.update()

        for event in pygame.event.get():

            if event.type == QUIT:
                gameOver = True
                break

            elif event.type == KEYDOWN:
                if event.key == K_r:
                    reallyRestart = True
                    restartAgain = False
                    print("pressed R")
                    break

                elif event.key == K_ESCAPE:
                    gameOver = True
                    break
        if gameOver == True:
            quit()
            break

    if reallyRestart == True:
        print("I'm here")
        pic = MovingBackground()
        cactus = Cactus()
        trex = Dinosaur()
        cac = Cactus()
        cac.image = pygame.image.load(os.path.join("images","1.bmp")).convert_alpha()
        coin = Coin()
        coin.image = pygame.image.load(os.path.join("images","coint.bmp")).convert_alpha()
        coin.y = 200


        f = font.Font(None, 36)
        f1 = font.Font(None, 36)
        f2 = font.Font(None, 48)
        title = font.Font(None, 36)
        restarttext = font.Font(None, 36)
        # creates a group of sprites so all can be updated at once

        sprite1 = RenderPlain(pic)
        sprites2 = RenderPlain(cactus)
        sprites3 = RenderPlain(trex)
        sprite4 = RenderPlain(cac)
        sprite5 = RenderPlain(coin)

        pas = 0
        hits = 0

        restartAgain = False
        reallyRestart = False






quit()
print ("Your score was : " + str(hits))
print (pas)
print ("Quitting game...")
pygame.quit()
quit()


