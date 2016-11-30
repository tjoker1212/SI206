#### I want to create game where a player runs forward and then obstacles get in his way and 
# the player needs to avoid getting hit by jumping over the obstacle. 
# If the player fails to jump over it and collides with the obstacle, then the player loses. 
# Each time the player successfully jumps over the obstacle, then the score increases by one.


from pygame import *
from pygame.sprite import *
from random import * 
from pygame.locals import K_RETURN, KEYDOWN, K_RIGHT, K_LEFT
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
dino = pygame.image.load(os.path.join('images', 'real.bmp'))
print (dino.get_size())
cac = pygame.image.load(os.path.join('images', 'cactus.bmp'))
print (cac.get_size())


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


    def moveright(self):
        self.x+= 200
        self.rect.center = (self.x + 20, self.y)

    def moveleft(self):
        self.x -= 200
        self.rect.center = (self.x, self.y)

    # move gold to a new random location
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
        self.y  = 390
        self.x = 10
        self.rect.center = (self.x, self.y)

    def update(self):
        self.x += 20
        self.rect.center = (self.x, self.y) # whereve the mous is, that is where I want the shovel to move

class MovingBackground(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "desert.bmp")).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 160
        self.y = 80
        self.rightside = self.image.get_size()[0]
        self.rect.center = (self.x, self.y)

    def move_left(self):
        self.x += 10
        self.rect.center = (self.x, self.y)
        

init()

# trex = Dinosaur() # actually creating the data/things that I can do stuff with
# cactus = Cactus() # actually creating the data/things that I can do stuff with
pic = MovingBackground()
cactus = Cactus()
trex = Dinosaur()


f = font.Font(None, 25)

# creates a group of sprites so all can be updated at once
#sprites = RenderPlain( pic,cactus, trex) # render these two things
# sprites = sprites.OrderUpdates()
sprite1 = RenderPlain(pic)
sprites2 = RenderPlain(cactus)
sprites3 = RenderPlain(trex)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)
timer2 = time.set_timer(USEREVENT + 1, DELAY)


gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
            quit()
            break

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                trex.moveleft()
                if trex.hit(cactus):
                    gameOver = True
                    quit()
                    break

            elif event.key == K_RIGHT:
                trex.moveright()
                if trex.hit(cactus):
                    gameOver = True
                    quit()
                    break

            elif event.key == K_RETURN:
                trex.moveup()
                mixer.Sound("spin_jump-Brandino.wav").play()
                # trex.pause()
                if trex.hit(cactus):
                    gameOver = True
                    quit()
                    break

        elif event.type == USEREVENT + 1:
            if trex.jump == True:
                # trex.pause()
                # trex.pause()
                # trex.pause()
                # trex.pause()
                trex.movedown()
                if trex.hit(cactus):
                    gameOver = True
                    quit()
                    break

            if trex.hit(cactus):
                gameOver = True
                quit()
                break
    if trex.hit(cactus):
        gameOver = True
        quit()
        break
    hits +=1

    pic.move_left()
    if pic.x >= 800:
        pic.x = 160
    cactus.update()
    if cactus.x >= WIDTH:
        cactus.x = -10


    screen.blit(bg, (bg_x, bg_y))


    t = f.render("SCORE = " + str(hits), False, (0,0,0))

    pic.update()
    cactus.update()
    trex.update()

    sprite1.draw(screen)
    sprites2.draw(screen)
    sprites3.draw(screen)

    screen.blit(t, (320,0))
    display.update()

print ("Quitting game...")
pygame.quit()
quit()


