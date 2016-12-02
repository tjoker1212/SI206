#### I want to create game where a player runs forward and then obstacles get in his way and 
# the player needs to avoid getting hit by jumping over the obstacle. 
# If the player fails to jump over it and collides with the obstacle, then the player loses. 

__author__ = 'Francisco "Paco" Gallardo'

from pygame import *
from pygame.sprite import *
from random import * 
from pygame.locals import K_RETURN, KEYDOWN, K_RIGHT, K_LEFT, K_r, K_ESCAPE
import os



screen = display.set_mode((1000, 600)) # I am creating a screen to be 1000 pixels wide by 600 pixels long
display.set_caption('T-rex vs Cacti') #setting the caption of my screen
DELAY = 1000; 

bg = pygame.image.load(os.path.join('images', 'desert.bmp')) # uploading my background image to from the images folder and assigning it to the variable "bg"
bg_x = 0 # the x coordinate of where I want my background image to start
bg_y = -200 # the Y-coordinate of where I want my background to start

WIDTH = 1000 #the width of my screen
HEIGHT = 800 # the height of my screen

# Create an instance of Dinosaur – will be the character that the user controls in the game
class Dinosaur(Sprite): # inherit from Sprite class
    def __init__(self): # when it is time to creat a new peice of gold, then initialize with this code
        Sprite.__init__(self) # make a brand new sprite for me and now I'm going to update it with the information that I want
        self.image = pygame.image.load(os.path.join("images","2.bmp")).convert_alpha() # this is the file that i want to use #this is an attribute
        self.rect = self.image.get_rect() #create a rectangle #this is an attribute thats calls a method on it
        self.x = WIDTH - 300 # setting the X-coordinate of this class instance to be the width minus 300 pixels, so 700 pixels from the left side of the screen
        self.y = 400 # setting the Y-coordinate of this class instance to be 400 pixels below the bottom of my screen
        self.jump = False # setting the boolean of this class instance to be False so that when I call the jump method, it can change it to true and then when it gos back down, it will be set to false
        self.rect.center = (self.x, self.y) # setting the center of my class instance to be at the X and Y coordinates that I mentioned on line 31 and 32



    # move Dinosaur instance to a new location
    def moveup(self): # sprites do not have a move method so we need to define it
        randY = 200 # setting the variable randY to 200 so that when I call this method, the Y-coordinate of my instance moves up by 200 pixels
        self.rect.center = (self.x ,(self.y - randY)) # setting the center of the rectangle (Dinosaur instance) to be the same X-coordinate as the instance variable and only change the Y-variable to be at 200 (400 - 200 = 200)
        self.jump = True # If this method is called, then I want to change this instance variable to True so that in the while loop below, it can can know when to bring my Dinosaur instance down by calling the movedown method
    
    # move my Dinosaur instance to the original location it started off at
    def movedown(self): 
    	self.rect.center = (self.x, self.y) # set the center of my Dinosaur instance back to the original coordinates, the X and Y instance variables
    	self.jump = False # update the boolean value to False so that I can jump again

        # Did my Dinosaur instance collide with anything?
    def hit(self, target):
        return self.rect.colliderect(target) #if my dinosaur instance collided with anything, the return True


# Create an instance of Cactus – will be the object that the user avoids (jumps over) in the game to avoid losing
class Cactus(Sprite): # inherit from Sprite class
    def __init__(self): # when it is time to creat a new peice of gold, then initialize with this code
        Sprite.__init__(self) # make a brand new sprite for me and now I'm going to update it with the information that I want
        self.image = pygame.image.load(os.path.join("images","cactus.bmp")).convert_alpha() # this is the file that i want to use #this is an attribute
        self.rect = self.image.get_rect() #create a rectangle #this is an attribute thats calls a method on it
        self.initialy  = 390 # setting the initial Y-coordinate of this class instance to be 390 pixels below the top of my screen
        self.initialx = -20 # setting the initial X-coordinate of this class instance to be 20 pixels off the left left side my screen
        self.x = -20 # setting the initial X-coordinate of this class instance to be 20 pixels off the left left side my screen
        self.y = 390 # setting the initial Y-coordinate of this class instance to be 390 pixels below the top of my screen
        self.rect.center = (self.x, self.y)# setting the center of my class instance to be at the X and Y coordinates that I mentioned on line 63 and 64
        
    # move the Cactus instance to a new location
    def update(self):
        self.x += 40 # update the X-coordinate of the Cactus instance by adding 40 pixels (it will move 40 pixels to the right)
        self.rect.center = (self.x , self.initialy) # update the center of the Cactus instance

# Create the instance of the background image so that it can move
class MovingBackground(Sprite):
    # Initializing the image, the X and Y coordinates, creating a rectangle of the image, and placing the center of the image at the X and Y coordinates of the screen
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "desert.bmp")).convert_alpha()
        self.rect = self.image.get_rect()
        self.initialx = 160
        self.initialy = 80
        self.x = 160
        self.y = 80
        self.rect.center = (self.x, self.y)
        
    # updating the image to move 10 pixels to the right 
    def move_left(self):
        self.x += 10
        self.rect.center = (self.x, self.y)


# creating a subclass of the Cactus class so that I can create a coin and it can update differently than the Cactus class.
# This class also has a new instance "Kill" so that whenever the dinosaur instance jumps at the same time that the coin is above him and they collide, then it can go back off the screen (essentially disappear from the screen) 
class Coin(Cactus):
    # this update method, when called, only moves the X-coordinate of the image 20 pixels to the right of where it was before
    def update(self):
        self.x += 20
        self.rect.center = (self.x, self.y)

    # this Kill method resets the Coin instance to go off the screen whenever the Dinosaur instance and the Coin instance collide
    def Kill(self):
        self.x = -10
        self.rect.center = (self.x, self.y)
init() # starts the game

#creating instances of each class I defined above
pic = MovingBackground()
cactus = Cactus()
trex = Dinosaur()
cac = Cactus()
cac.image = pygame.image.load(os.path.join("images","1.bmp")).convert_alpha() # changes the image of the cac instance
coin = Coin()
coin.image = pygame.image.load(os.path.join("images","coint.bmp")).convert_alpha() # changes the image if the coin instance
coin.y = 200 # setting the Y-coordinate of the Coin instance to always be 200 pixels below the top edge of the screen

# creating font instance so that I place them on the screen
f = font.Font(None, 36)
f1 = font.Font(None, 36)
f2 = font.Font(None, 48)
title = font.Font(None, 36)
restarttext = font.Font(None, 36)

# creates individual sprites so I can update each one of them whenever I want
sprite1 = RenderPlain(pic)
sprites2 = RenderPlain(cactus)
sprites3 = RenderPlain(trex)
sprite4 = RenderPlain(cac)
sprite5 = RenderPlain(coin)



pas = 0 # setting a counter so that in the while loop below, it can get updated and when the counter is a certain number, then an action occurs
score = 0 # setting the counter for the score of the game
time.set_timer(USEREVENT + 1, DELAY) # sets the timer of the game


gameOver = False # Boolean sets the game to not end
restartAgain = False # When a user loses, this boolean will update to true and prompt the user if they want to restart the game or end the game
reallyRestart = False # if the user decides to restart the game again, then it update this value to true and actually restart the game

x = 0 # sets a counter of all the times the while loop gets called # when it is equal to 0, then a "welcome" screen will appear on the game screen before the game begins

# This while loop will actually make the game run
while not gameOver:
    # when the counter is 0, then a "welcome/warning" text will appear. It only lasts 3 seconds long
    if x == 0:
        Title= title.render('''Press ENTER to jump. Good Luck!''', False, (255,255,255))
        screen.blit(Title, (200,200))
        display.update()
        pygame.time.delay(3000)

    x+=1
    # check to see if there is any user input
    for event in pygame.event.get():
        # if the user clicks on the "X" of the screen, then set the gameOver variable to True and exit this for loop to end the game
        if event.type == QUIT:
            gameOver = True
            break

    
        elif event.type == KEYDOWN:

            # check idf the user hit the "enter/return" key on the key board. If so, tell the trex (Dinosaur instance ) to jump by calling the moveup method
            # and make a jumping sound

            if event.key == K_RETURN:
                trex.moveup()
                mixer.Sound("spin_jump-Brandino.wav").play()

                # if the trex instance hit any of the cacti instance, then delay the game for 1.5 seconds to play a sound
                # then update the "restartAgain" value to True and break the for loop so that it prompts the user if they would like to play again or quit the game
                # also print out (on the gitbash/terminal) that the user died when the trex was jumping up
                if trex.hit(cactus) or trex.hit(cac):
                    mixer.Sound("BellSoundRing.wav").play()
                    pygame.time.delay(1500)
                    print ("You died when you jumped")
                    restartAgain = True
                    break

                # If the trex collides with the coin instance, then update the score (add 50 points) and play a nois.
                # also print out (on gitbash/terminal) that the user hit the coin
                # lastly, call the Kill method on the coin so that it restarts at the -10 X-coordinate
                if trex.hit(coin):
                    score += 50
                    mixer.Sound("MarioCoin.wav").play() # play this sound if my dinosaur class score the coin class
                    print ("You hit the coin") # print 
                    coin.Kill()

        elif event.type == USEREVENT + 1:

            # if the trex jumped and the user did not press enter again, then call the movedown method on the trex instance and play a sound when it lands
            if trex.jump == True:
                trex.movedown()
                mixer.Sound("Close-Vault-Or-Jail-Door.wav").play()

                # if the trex instance hit any of the cacti instance, then delay the game for 1.5 seconds to play a sound
                # then update the "restartAgain" value to True and break the for loop so that it prompts the user if they would like to play again or quit the game
                # Also print out (on the Terminal/Gitbash) that the user died when they were returning from the their jump
                if trex.hit(cactus) or trex.hit(cac):
                    mixer.Sound("BellSoundRing.wav").play()
                    pygame.time.delay(1500)
                    print ("you died coming down!")
                    restartAgain = True
                    break

    # if the trex instance hit any of the cacti instance, then delay the game for 1.5 seconds to play a sound
    # then update the "restartAgain" value to True and break the for loop so that it prompts the user if they would like to play again or quit the game
    if trex.hit(cactus) or trex.hit(cac):
        print ("you died because you did not jump!")
        mixer.Sound("BellSoundRing.wav").play()
        fail = f2.render("You hit the cactus. You lose!", False, (0, 0,255))
        screen.blit(fail, (250,300))
        display.update()
        pygame.time.delay(4000)
        restartAgain = True
    
    # if the user, hit the "X" icon on the screen to exit the screen, then break this while loop and end the game
    if gameOver == True:
        break

    # for every 5 loops this while loop happens, update the score (by adding one to it)
    if x % 5 ==0:
        score +=1

    # for every loop, call the move_left method on the pic instance so that the background image moves right
    pic.move_left()

    # if the X-coordinate is equal to or greater than 800, then reset the X-coordinate of the image back to 160 pixels from the edge of the left side of the screen
    if pic.x >= 800:
        pic.x = 160

    # If the X-coordinate of the cactus instance is 1000 (size of the Width of the screen) or greater than 1000, then update the pas counter and reset the X-coordinate to -10 
    if cactus.x >= 1000:
        pas +=1
        cactus.x = -10

    # If the X-coordinate of the cac instance is 1000 (size of the Width of the screen) or greater than 1000, then update the pas counter and reset the X-coordinate to -10 
    if cac.x >= 1000:
        pas +=1
        cac.x = -10

    # If the X-coordinate of the coin instance is 1000 (size of the Width of the screen) or greater than 1000, then reset the X-coordinate to -10 
    if coin.x >= 1000:
        coin.x = -10

    screen.blit(bg, (bg_x, bg_y)) # updating the screen with the background image at the coordiates associated with "bg_x" and "bg_y" which are defined on line 20 and 21, respectively

    # place text that has the score in black colo
    t = f.render("SCORE = " + str(score), False, (0,0,0))

    # update the screen with the pic, trex and coin instances
    pic.update() 
    trex.update()
    coin.update()
    
    # if the pas counter is divisible by 3, then call the update method on the cac instance (will move the cac instance across the screen)
    # if not, then call the update method on the cactus instance (will move the cactus instance across the scree)
    if pas %3 == 0:
        cac.update()
    else:
        cactus.update()
    

    # draw each instance on the screen
    sprite1.draw(screen)
    sprites2.draw(screen)
    sprites3.draw(screen)
    sprite4.draw(screen)
    sprite5.draw(screen)

    # draw the score (from line 248) on the screen and update the entire screen
    screen.blit(t, (320,0))
    display.update() # acually updates the screen

    # if the user lost, then prompt the user if they would like to restart the game or exit the game
    # also, plae text on the screen that gives them the directions of what they would like to do next

    while restartAgain==True:
        restarttext1 = restarttext.render('Your score is: ' + str(score) + ' To play again press "R" or press "Escape" to leave the game', False, (255,255,255))
        screen.blit(restarttext1, (50, 200))
        display.update()

        # Listen to the user input in this for loop
        # if they press the "escape" key or exit out of the game then update the gameOver boolean value and exit the for loop
        # if the user pressed the "R"key, then update the reallyRestart boolean value to True and exit the for loop and also update the restartAgain value to False
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
        # if the user hit "escape" key or hit the "X" on the screen, then quit the game and exit this for loop
        if gameOver == True:
            quit()
            break

    # if the user pressed the "r" key on the keyboard, then  restart the game by creating new instances of all the classes, 
    # new text variables, restart the pas and score counters, and reassign the restartAgain and reallyRestart values to False to play the game again
    # continue with the while loop
    if reallyRestart == True:

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
        score = 0

        restartAgain = False
        reallyRestart = False



# Quit the game and print out (on the terminal/gitbash) the user's score and print out that they game is exiting.
print ("Your score was : " + str(score))
print ("Quitting game...")
pygame.quit()


