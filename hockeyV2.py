#importing the neccessary modules to set up the game. Pygame is a library suited for game development. sys is for exit() function to quit the program. Random is for random() function to generate random number. 
import pygame
import sys, random
#This is a class in python which represents the puck in air hockey. We can make as many instances of this class as we want, however, we only need one for this game. Indention shows which functions are part of the class. 
class Puck:
    # This is the defintion of the init function. The init function takes in parameters passed on during the function call, these parameters are self, speed_x, speed_y,screen_width,screen_height. Self refers to the object being created. 
    def __init__(self, speed_x, speed_y,screen_width,screen_height):
        #We are creating a rectangular surface through the pygame module inn which we will be able to modify the location of the puck. The first two parameters are the initial location of the rectangle's right corner in x and y coordinates. The last two are the width and height of the rectangle.
        self.puck_surface = pygame.Rect(screen_width/2 - 10,screen_height/2 - 10,20,20)
        #here we are creating self.puck_speed_x, which is a variable unique to the Puck class. We set the speed using the speed_x passed in through the init function paramters. 
        self.puck_speed_x = speed_x
        self.puck_speed_y = speed_y
        #Keeping track of the player and opponent score
        self.player_score = 0
        self.opp_score = 0
        #Keeping track of the screen height and screen width 
        self.gameScreenHt = screen_height
        self.gameScreenWid = screen_width
    #everytime update() is called on a Puck object, it will change the x and y coordinates of the puck surface. 
    def update(self):     
        self.puck_surface.x += self.puck_speed_x
        self.puck_surface.y += self.puck_speed_y
    # a "getter" function since it returns the X coordinate of the puck surface. Useful for other parts of the program to access variables within the Puck. 
    def getXcoord(self):
        return self.puck_surface.x
    #returns the y coordinate of the puck surface
    def getYcoord(self):
        return self.puck_surface.y
    #returns the entire puck surface created by PyGame
    def get_puck_surface(self):
        return self.puck_surface
    #returnns player score
    def get_player_score(self):
        return self.player_score
    #returns opponent score
    def get_opp_score(self):
        return self.opp_score
    #function that controls the movement of the puck 
    def puck_animation(self):
        #if statement checks to see if the puck has gone off-screen on the top or bottom of the screen. In terms of coordinates, 0 represents the top of the screen, and screen_height, a variable storinng the screen's height, represents the bottom of the screen. 
        if self.puck_surface.top <= 0 or self.puck_surface.bottom >= screen_height:
            #if either condition is met, then we reverse the direction of the ball by multiplying the variable puck_speed_y by -1
            self.puck_speed_y *= -1
        #similar if statement, but now we're checking the left and right sides of the screen. It's important to note the comparision is <=, not just ==, which ensures that all coordinates past the screen are out of bounds, not just the border.  
        if self.puck_surface.left <= 0 or self.puck_surface.right >= screen_width:
            self.puck_speed_x *= -1 
        #  self refers to the puck, using pyGame we can check if two rectangle surfaces have collided with the colliderect() function. If the puck collides with the player or opponent, then reverse direction.   
        if self.puck_surface.colliderect(player) or self.puck_surface.colliderect(opp):
            self.puck_speed_x *= -1
        #if the puck collides with the player's goal, add a point to the opponent's score and reset the location of the puck.
        if self.puck_surface.colliderect(player_goal):
            self.opp_score += 1
            self.puck_restart()
        #if the puck collides with the opponent's goal, add a point to the player's score and reset the location of the puck.
        if self.puck_surface.colliderect(opp_goal):
            self.player_score += 1
            self.puck_restart()
    #fucntion that resets location of puck
    def puck_restart(self):
        #recenter the puck based on gamescreen dimensions
        self.puck_surface.center = (self.gameScreenWid/2, self.gameScreenHt/2)
        #pick 1 or -1 randomly to adjust the x and y direction of the puck
        self.puck_speed_x *= random.choice((1,-1))
        self.puck_speed_y *= random.choice((1,-1))
        #pauses the game for 2000 milliseconds to give a breather
        pygame.time.wait(2000)
#function that ensures the player movements don't go off screen
def player_animation():
    #0 represents the top of the screen. Player is the red blob on the right side of the rink that is controlled by user. 
    if player.top <= 0:
        player.top = 0
    #screen_height represents bottom of the screen
    if player.bottom >= screen_height:
        player.bottom = screen_height
#function that controls the CPU movements
def opponent_animation(game_puck):
    #check if the puck's y coordinate is greater than the y coordinate of the top of the opponent's blob
    if game_puck.getYcoord() > opp.top:
        #increase the y coord of the opponent's top to move towards location of puck
        opp.top += opp_speed
    #similar to above,but reversed
    if game_puck.getYcoord() < opp.bottom:
        opp.bottom -= opp_speed
    #prevents the opponent's blob from moving past the goal posts. 
    if opp.top <= opp_goal.top:
        opp.top = opp_goal.top
    if opp.bottom >= opp_goal.bottom:
        opp.bottom = opp_goal.bottom

#init pygame modules
pygame.init()
clock = pygame.time.Clock()

#main window
screen_width = 550
screen_height = 350
#display surface to draw shapes on, unique
screen = pygame.display.set_mode((screen_width, screen_height))
#caption of the game window
pygame.display.set_caption('Air Hockey')
#set a font for text in game
font = pygame.font.SysFont(None,25)

#Game Rectangles coords are defined by top left
#Rect(x location, y loc, ht of ball, wid of ball)

#This is how we create an instance of the Puck class. Now we have a game_puck which has all the attributes and functions within the Puck class. 
game_puck = Puck(3,3,screen_width,screen_height)
#creating surfaces for the player and opponent blob's and their goals
player = pygame.Rect(screen_width - 40,screen_height/2 - 25,20,50)
opp = pygame.Rect(20, screen_height/2 - 25, 20, 50)
player_goal = pygame.Rect(screen_width - 10,screen_height/2 - 75,10, 150)
opp_goal = pygame.Rect(0,screen_height/2 - 75,10, 150)
#setting colors for the background using .Color() and (R,G,B) methods
bg_color = pygame.Color('blue')
red = (255,0,0)
white = (255,255,255)

#setting initial values for player and opponent speeds. Try changing the opp_speed variable to 10 for a more difficult game. 
player_speed = 0
opp_speed = 3
#this while loop has the condition True, meaning it will run forever
while True:
    #handling user input through pygame.event
    for event in pygame.event.get():
        #if we click the x on the right side of the window, we will close the window and end the while loop. 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #check to see if a key was pressed
        if event.type == pygame.KEYDOWN:
            #if the key pressed was down arrow, move the player's blob down
            if event.key == pygame.K_DOWN:
                player_speed += 7
            #if the key pressed was up arrow, move the player's blob up
            if event.key == pygame.K_UP:
                player_speed -= 7
            #check to see when key stops being pressed
        if event.type == pygame.KEYUP:
            #reverse of above to essentially reverse the last loop, and the player blob will stay in place. 
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    #calling the update() function for game_puck so that the puck will move
    game_puck.update()
    #calling puck_animation() function for game_puck to check for out of bounds, or collisions with player/opponent blob's or goals. 
    game_puck.puck_animation()
    #change the player's y coordinate based on the variable player_speed which was manipulated earlier in the while loop when we pressed keys
    player.y += player_speed
    #calling the function which moves the player
    player_animation()
    #calling the function to move the opponent, passing in the game_puck so that the function can access the location of the puck and can move the opponent accordingly
    opponent_animation(game_puck)
    

    
    
    #visuals
    screen.fill(bg_color) #first line of code is drawn first, background
    #player blob
    pygame.draw.ellipse(screen,red, player)
    #opponent blob
    pygame.draw.ellipse(screen,red, opp)
    #puck
    pygame.draw.ellipse(screen, white, game_puck.get_puck_surface())
    #player goal
    pygame.draw.rect(screen, white, player_goal)
    #opponnent goals
    pygame.draw.rect(screen, white, opp_goal)
    #draw halfcourt
    pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2, screen_height))
    pygame.draw.circle(screen, white, (screen_width/2, screen_height/2), 100,2)
    #display the score 
    scoreboard = font.render("Home: "+str(game_puck.get_opp_score())+" Away: "+str(game_puck.get_player_score()),1,white)
    #use blit() function to set where the scoreboard is going on the screen
    img = screen.blit(scoreboard, (0, 10))
    #update the screen to show the scoreboard
    pygame.display.update(img)


    
    #updating entire window using flip() function
    pygame.display.flip()
    #limit to 60 frames per second
    clock.tick(60)
