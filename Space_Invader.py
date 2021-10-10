# Space Invaders
# Set Up The Screen
import turtle
import os
import math
import random
import winsound
import platform
from pygame import mixer

# Set Up the screen
main_screen =turtle.Screen() #  For The Main Screen
main_screen.bgcolor("black") #  For The Background Color
main_screen.title("Spac ")
# Register The Shapes
main_screen.register_shape("C:/Users/Muhammad Daffa/Documents/Pemrograman/Python/Program/Space_Invader/invader.gif")
# Untuk meregistrasi image yang ingin digunakan
main_screen.register_shape("C:/Users/muham/Documents/Pemrograman/Python/Program/Space_Invader/player.gif")
# Untuk meregistrasi image yang ingin digunakan
main_screen.tracer(0) #To make animation run smoother

#Background Music
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("C:/Users/Muhammad Daffa/Documents/Pemrograman/Python/Program/Space_Invader/BGM.wav") 
  
# Setting the volume 
mixer.music.set_volume(0.5) 
  
# Start playing the song 
mixer.music.play(-1)
#play(-1) agar lagu dilooping secara terus menerus

# Draw Border
border_pen = turtle.Turtle() #  Create a pen
border_pen.speed(0) # adding A border_pen with attribut called "speed" 0 is the fastes speed
border_pen.color("white") # An attribut called color to give the pen white color
border_pen.penup() # the default of the pen is in the center of the screen
# and face to the right side which is it will make a line if we create a border
# so the penup function will make the border perfectly without any miss line
border_pen.setposition(-300,-300) # Its the x,y position
border_pen.pendown()
border_pen.pensize(3) # its about the pen size that set in 3px
# create a square 
for side in range(4):
    border_pen.fd(600) # Its the forward function 
    border_pen.lt(90) # Its the left function whichis set in 90 degrees
border_pen.hideturtle() # if the draw of the border is done this function will be working

# Set The Score to 0
score = 0

# Draw The Score
score_pen =turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score : {}".format(score)
score_pen.write(score_string, False, align="left", font=("Arial", 14 , "normal"))
# Indonesia: func(write) disini berfungsi untuk menampilkan teks dimana terdapat atribut lain
score_pen.hideturtle()
# untuk menhilangkan panah

# create the player turtle  
player = turtle.Turtle() # Create a player object
player.color("blue") # Player color
player.shape("C:/Users/muham/Documents/Pemrograman/Python/Program/Space_Invader/player.gif") # Player shape
player.penup() # for drawing a line
player.speed(0) # Player speed
player.setposition(0, -250) # player position with a x,y position
player.setheading(90) # The Player faces

# Player Movement
player_speed = 5

# Choose The Number of Enemies
number_of_enemies = 40
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create The Enemies
    enemies.append(turtle.Turtle())# Akan menambahkan musuh sejumlah number_of_enemies
    # kedalam list "enemies" berdasarkan looping diatas

#Create the first enemy coordinate
enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

# The Enemy
for enemy in enemies: # Dari loopingan diatas didapat 5 enemies didalam game
    # yang masuk kedalam list
    # dari sini setiap musuh yang masuk list diberi atribut berupa berikut
    enemy.color("red")
    enemy.shape("C:/Users/muham/Documents/Pemrograman/Python/Program/Space_Invader/invader.gif")
    enemy.penup() # If you want the enemy wont draw anything use this func()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number) # ini memberikan x posisi awal pada tiap musuh yang di spawn
    y = enemy_start_y 
    enemy.setposition(x, y) # This is where the enemy location start in the firt time
    # Update the enemy number
    enemy_number +=1
    if enemy_number == 10: # Jika musuh sudah mencapai 10
        enemy_start_y -= 50 # Maka posisi y musuh diubah sebanyak - 50
        enemy_number = 0  # Reset ke 10 sebanyak number_of_enemies



# The Enemy Speed
enemy_speed = 0.125 # The Enemy Current Speed

# The Player's Weapon/Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90) # The bullet faces/heading
bullet.shapesize(0.2, 0.2) # This is for the size of shape which is 
# The it's used x,y px.X for the width, adn y for the height  
bullet.hideturtle() # To hide the bullet when the game started

# Bullet Speed
bullet_speed = 3 

# Define the bullet state 
# Indonesia : Menentukan status peluru
# Ready == ready to fire
# fire == the bulllet is firing -- its mean the bullet start to move
bullet_state = "ready"  

# The Movement
def move_left():
    x = player.xcor() # player x coordinat will be setting up 0 by the default
    x -=player_speed # it will move to the x = -15,-30,-45,....
    if x < -280: # jika x kurang dari -280
        x = - 280  # maka ini merupakan titik x terkecil yang dapat di tempuh
    player.setx(x) # this func will set player movement to -15,... by the x -=pspeed has decrease
    # indonesia : fungsi ini akan menetapkan posisi player dari x = 0 ke x = 15,dst
    # berdasarkan perubahan x -= player_speed

def move_up():
    y = player.ycor()
    y +=player_speed
    if y > -200:
        y = -200
    player.sety(y)

def move_down():
    y = player.ycor()
    y -=player_speed
    if y < -260:
        y = -260
    player.sety(y)
    
def move_right():
    x = player.xcor() # Same as the left func,it will be set the curent player position
    x +=player_speed # it will move to the x = 15,30,45,....
    if x > 280: # jika x kurang dari +280
        x = 280  # maka ini merupakan titik x terkecil yang dapat di tempuh
    player.setx(x) # # this func will set player movement to 15,30,... by the x +=pspeed has decrease

def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bullet_state
    if bullet_state == "ready": # So the logic is like this.
        # First if we push the spacebar
        # The bullet_state will be check
        # if its ready
        # it will be firing
        winsound.PlaySound("C:/Users/muham/Documents/Pemrograman/Python/Program/Space_Invader/laser.wav", winsound.SND_ASYNC)
        # diberikan windsound.SND_ASYNC agar saat audio diputar tidak terjadi lag/delay
        bullet_state = "fire"
        # Move the bullet to the just above the player
        x = player.xcor() # The first thing that we gonna need to do is the player
        y = player.ycor() # you can add + 10 between this func() # x,y position
        bullet.setposition(x,y + 10) # then the bullet position based on player current state
        #  and the y position will be increased by 10
        bullet.showturtle()# it will show the bullet

def isCollision(t1, t2): # The func() that have an argument which is t1 and t2 for the turtle 1-2
    # untuk membuat powers.
    distace = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) # Ini adalah rumus pitagoras
            # pow merupakan panel untuk menuliskan rumus matematika,seperti halnya diatas yaitu rumus pitagoras
            # sqrt merupakan akar yang biasa disebut square root  
            #  jadinya rumus diatas seperti akar x^2 + y^2             
    if distace < 15:
        return True
    else :
        return False 
# Keyboard Bindings
main_screen.listen()
main_screen.onkeypress(move_left, "Left") # This function will make the keyboard works by the user press the left button
# so when arrow key has been press the player movement will be go to the left direction
main_screen.onkeypress(move_right, "Right") # This function will make the keyboard works by the user press the right button
main_screen.onkey(move_up, "Up")
main_screen.onkey(move_down, "Down")
main_screen.onkeypress(fire_bullet, "space")
# Indonesia : ada dua hal yang berbeda dalam penggunaan onkey
# 1.onkey func():fungsi ini hanya bisa menekan tombol satu kali.Jika ini masih dijalankan maka 
# User tidak bisa menekan terus menerus
# 2.Sedangkan onkeypress : fungsi ini mampu membuat tombol dapat ditekan lebih daris satu kali
# dan ini tidak akan mengganggu tombol lainnya

# Main Game Loop 
# This is will begin all our programming is going to go 
while True:
    
    main_screen.update() #To apply the smoother animation

    for enemy in enemies: # untuk membuat musuh didalam list bergerak dan memiliki atribut
        # Enemy Movement
        x = enemy.xcor()
        x +=enemy_speed # It will make the enemy position change from 0,2,4...
        enemy.setx(x) # Indonesia : ini akan membuat fungsi x += berjalan
        # dengan merubah posisi x musuh

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for i in enemies:
                y = i.ycor() # Indonesia : Menetapkan posisi y enemy
                y -= 40 # Merubah posisi y enemy berdasarkan nilai -40
                # we need to use some if condition with multiply by minus 1
                # it will make the enemy position change to 2 into -2 
                i.sety(y) # Menetapkan posisi y baru musuh yang telah diubah
            # Change Enemy Direction
            enemy_speed *= -1 # if we want the enemy across to the left side

        if enemy.xcor() < -280:
            # Move all enemies down
            for i in enemies:
                y = i.ycor() 
                y -= 40
                # This condition will make enemy position change from -2 into 2 by multiply -1 
                i.sety(y)
            # Change Enemy Direction
            enemy_speed *= -1 # Same with the first condition when enemy reach the -280 position

        # check for a coliision/hit box between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("C:/Users/muham/Documents/Pemrograman/Python/Program/Space_Invader/explosion.wav", winsound.SND_ASYNC)
            # Reset the bullet 
            bullet.hideturtle() # Jika bullet sudah mengenai hitbox,maka akan dihilangkan
            bullet_state = "ready" # statement diganti menjadi "ready"
            bullet.setposition(0, -400) # bullet dikembalikan ke posisi x,y (0,-400)
            # Reset the enemy
            enemy.setposition(0, 10000) #  This is where the enemy location start in the firt time
            # --> Old code for only 1 enemies #  enemy.setposition(-200, 250) # Jika musuh tertembak.Reset musuh dengan cara kembali ke posisi awal
            score +=10
            score_string = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14 , "normal"))
            # Indonesia: func(write) disini berfungsi untuk menampilkan teks dimana terdapat atribut lain
            # berupa : false yang berfungsi sebagai agar posisi score tetap berada di kiri
            # jika diTrue kan maka posisi setiap score +10 maka akan merubah posisi score
                
        if isCollision(player, enemy):
            winsound.PlaySound("C:/Users/muham/Documents/Pemrograman/Python/Program/Space_Invader/explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor() # this will make the bullet position based on the player position
        y += bullet_speed # The bullet position will be changed based on the var "bullet_speed"
        bullet.sety(y) #  and this one will be set the current position of bullet by the the y position is increased

    #  check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

        
