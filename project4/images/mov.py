#### I want to create game where a player runs forward and then obstacles get in his way and 
# the player needs to avoid getting hit by jumping over the obstacle. 
# If the player fails to jump over it and collides with the obstacle, then the player loses. 
# Each time the player successfully jumps over the obstacle, then the score increases by one.


from pygame import *
from pygame.sprite import *
from random import * 
from pygame.locals import K_RETURN, KEYDOWN, K_RIGHT, K_LEFT
import os

WIDTH = 800
HEIGHT = 800

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

DELAY = 1000; 

x_pos = 0
y_pos = 200
bg_x = 0
bg_y = -200

# Create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

# Set image as the background
bg = pygame.image.load(os.path.join('images', 'pizel.bmp'))
display.set_caption('T-rex vs Cacti')

def redraw():
	gameDisplay.fill(white)

pygame.display.update()		#only updates portion specified


class Dinosaur(Sprite): # inherit from Sprite class
    def __init__(self): # when it is time to creat a new peice of gold, then initialize with this code
        Sprite.__init__(self) # make a brand new sprite for me and now I'm going to update it with the information that I want
        self.image = pygame.image.load(os.path.join("images","trex1.bmp")).convert_alpha() # this is the file that i want to use #this is an attribute
        self.rect = self.image.get_rect() #create a rectangle #this is an attribute thats calls a method on it
        self.x = 150
        self.y = 250
        self.jump = False

    def moveright(self):
    	self.x+= 200
    	self.rect.center = (self.x + 20, self.y)

    def moveleft(self):
    	self.x -= 200
    	self.rect.center = (self.x, self.y)

    # move trex up
    def moveup(self): # sprites do not have a move method so we need to define it
        randY = 100 # this is a function that is getting a random number and saving it under the variable randY and randX
        self.rect.center = (self.x,self.y - randY) # setting the center of the rectangle to be the the random numbers created above
        self.jump = True 
    def movedown(self):
    	randY = 100
    	self.rect.center = (self.x, self.y + randY)
    	self.jump = False

        # Did shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target) #if i call the hit method, this is a question: did I hit it? Did we collide? 


init()

trex = Dinosaur() # actually creating the data/things that I can do stuff with

f = font.Font(None, 25)
hits = 0 

sprites = RenderPlain(trex)

while True:
	#redraw()
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
			break

		elif event.type == KEYDOWN:
			if event.key == K_RIGHT:
				trex.moveright()
			elif event.key == K_LEFT:
				trex.moveleft()
			elif event.key == K_RETURN:
				trex.moveup()


		elif event.type == USEREVENT + 1: # TIME has passed # how you update the timer
			if trex.jump == True:
				trex.movedown()





	gameDisplay.blit(bg, (bg_x, bg_y))

	if x_pos>=WIDTH:
		poop_x = random.randrange(0, WIDTH) 
		poop_y = random.randrange(200, HEIGHT) 
		x_pos = 0
		if bg_x == 0:
			bg_x -=200
		else:
			bg_x = 0
	pygame.display.update()	



	# update and redraw sprites
	sprites.update() # always update the sprites
	sprites.draw(gameDisplay) # alway update the screen
	display.update() # alway update the screen
print ("quitting game..")
pygame.quit()
quit()				#exits python
