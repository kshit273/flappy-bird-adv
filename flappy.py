# Importing the libraries
import pygame
import sys
import time
import random
import sqlite3
import mysql.connector as mc
from mysql.connector import Error

# Initializing the database
def initialize_database():
    connection = sqlite3.connect("flappy_bird.db") 
    cursor = connection.cursor()

    # Create the users table 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        highscore INTEGER DEFAULT 0
    )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("Database initialized successfully!")

# Call the initialize_database function
initialize_database()

# Inserting data
def register_user(connection, username, password):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
    cursor.close()

# Updating data
def update_highscore(connection, high_score, username):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET highscore = ? WHERE username = ?", (high_score, username))
    connection.commit()
    cursor.close()

# Retrieving data
def get_user(connection, username):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    cursor.close()
    return user

# Create a single connection for the entire script
connection = sqlite3.connect("flappy_bird.db")

# Initialize the cursor
my_cursor = connection.cursor()

# Initializing the pygame 
pygame.init()

# Frames per second
clock = pygame.time.Clock()

# Sounds for flappy bird
pygame.mixer.init()
die = pygame.mixer.Sound("Sounds/die.mp3")
swoosh = pygame.mixer.Sound("Sounds/swosh.mp3")
flap = pygame.mixer.Sound("Sounds/flap.mp3")
hit = pygame.mixer.Sound("Sounds/hit.mp3")
music2 = pygame.mixer.music.load("Sounds/music2.mp3")
point = pygame.mixer.Sound("Sounds/point.mp3")

# First screen
base_font = pygame.font.Font(None, 32) 
username = ''
password = '' 
input_rect = pygame.Rect(549,217,427,60)
input_rect2 = pygame.Rect(550,302,427,59)
login_rect = pygame.Rect(706,384,130,34)
color = pygame.Color('white')

# Some functions for login
def draw_text_box():
    pygame.draw.rect(screen, color, input_rect, 1)
    text_surface = base_font.render(username, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+10)) 
    
def draw_text_box2():
    pygame.draw.rect(screen, color, input_rect2, 1)
    text_surface = base_font.render(password, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect2.x+5, input_rect2.y+10))

# Function to draw floor
def draw_floor():
    screen.blit(floor_img, (floor_x, 590))
    screen.blit(floor_img2, (floor_x2, 590))

# Function to create pipes
def create_pipes():
    pipe_y = random.choice(pipe_height)
    top_pipe = pipe_img.get_rect(midbottom=(1667, pipe_y - 300))
    bottom_pipe = pipe_img.get_rect(midtop=(1667, pipe_y))
    return top_pipe, bottom_pipe

# Function for animation
def pipe_animation():
    global game_over, score_time
    for pipe in pipes:
        if pipe.top < 0:
            flipped_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped_pipe, pipe)
        else:
            screen.blit(pipe_img, pipe)

        pipe.centerx -= 3 
        if pipe.right < 0:
            pipes.remove(pipe)

        if bird_rect.colliderect(pipe):
            pygame.mixer.Sound.play(hit).set_volume(0.5)
            game_over = True

# Function to draw score
def draw_score(game_state):
    if game_state == "game_on":
        score_number_text = score_number_font.render(str(score), True, "Black")
        score_number_rect = score_number_text.get_rect(center=((width // 2), 66))
        screen.blit(score_number_text, score_number_rect)
    elif game_state == "game_over":
        score_text = score_font.render("Score", True, "Black")
        score_rect = score_text.get_rect(center=((width // 2)-560, 50))
        score_number_text = score_number_font.render(str(score), True, "Black")
        score_number_rect = score_number_text.get_rect(center=((width // 2)-480, 50))
        screen.blit(score_text, score_rect)
        screen.blit(score_number_text, score_number_rect)

        high_score_text = score_font.render("High Score", True, "Black")
        high_score_rect = high_score_text.get_rect(center=((width // 2)+430, 50))
        high_score_number_text = score_number_font.render(str(high_score), True, "Black")
        high_score_number_rect = score_number_text.get_rect(center=((width // 2)+550, 50))
        screen.blit(high_score_text, high_score_rect)
        screen.blit(high_score_number_text, high_score_number_rect)

# Function to update the score
def score_update():
    global score, score_time, high_score
    if pipes:
        for pipe in pipes:
            if 65 < pipe.centerx < 69 and score_time:
                pygame.mixer.Sound.play(point).set_volume(0.5)
                score += 1
                score_time = False
            if pipe.left <= 0:
                score_time = True

    if score > high_score:
        high_score = score

# Game window
width, height = 1280, 680
w, h = 150, 200
alpha = 255
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird by K")
icon = pygame.image.load("Game window/icon.jpg").convert_alpha()
pygame.display.set_icon(icon)

# Welcome screen
R = pygame.image.load("Welcome screen/r.png").convert_alpha()
P = pygame.image.load("Welcome screen/p.png").convert_alpha()
Y = pygame.image.load("Welcome screen/y.png").convert_alpha()
B = pygame.image.load("Welcome screen/b.png").convert_alpha()

# Setting background and base image
back_img = pygame.image.load("__maingame__/Background.jpg").convert_alpha()
back_img2 = pygame.image.load("img1.jpg").convert_alpha()
floor_img = pygame.image.load("__maingame__/img_52.png").convert_alpha()
floor_img2 = pygame.image.load("__maingame__/img_52.png").convert_alpha()

#new_level = pygame.image.load("new level text2.png").convert_alpha()
#new_level.set_alpha(alpha)
floor_x = 0
floor_x2 = 1017

# Different stages of bird
bird_up = pygame.image.load("Sprites/img_47.png").convert_alpha()
bird_down = pygame.image.load("Sprites/img_48.png").convert_alpha()
bird_mid = pygame.image.load("Sprites/img_49.png").convert_alpha()

bird_r_up = pygame.image.load("Sprites/red_1.png").convert_alpha()
bird_r_down = pygame.image.load("Sprites/red_2.png").convert_alpha()
bird_r_mid = pygame.image.load("Sprites/red_3.png").convert_alpha()

bird_y_up = pygame.image.load("Sprites/yellow_1.png").convert_alpha()
bird_y_down = pygame.image.load("Sprites/yellow_2.png").convert_alpha()
bird_y_mid = pygame.image.load("Sprites/yellow_3.png").convert_alpha()

bird_p_up = pygame.image.load("Sprites/pink_1.png").convert_alpha()
bird_p_down = pygame.image.load("Sprites/pink_2.png").convert_alpha()
bird_p_mid = pygame.image.load("Sprites/pink_3.png").convert_alpha()

birds = [bird_up, bird_mid, bird_down]
bird_index = 0
bird_flap = pygame.USEREVENT
pygame.time.set_timer(bird_flap, 200)
bird_img = birds[bird_index]
bird_rect = bird_img.get_rect(center=(167, 622 // 2))
bird_movement = 0
gravity = 0.17

# Loading pipe image
pipe_img = pygame.image.load("Sprites/2.png").convert_alpha()
pipe_height = [400, 350, 533, 490]

# For the pipes to appear
pipes = []
create_pipe = pygame.USEREVENT + 1
pygame.time.set_timer(create_pipe, 1200)

# Displaying game over image
game_over = True
over_img = pygame.image.load("Welcome screen/img_45.png").convert_alpha()
x, y = 987, 289

# Setting variables and font for score
score = 0
high_score = 0
my_cursor.execute("select highscore from users where username = ?", (username,))
for j in my_cursor:
    for i in j:
        high_score = i
        print(i)
score_time = True
continue_font = pygame.font.Font("Fonts/BotsmaticRegularDemo.ttf", 27)
score_font = pygame.font.Font("Fonts/BotsmaticRegularDemo.ttf", 27)
score_number_font = pygame.font.Font("Fonts/flappy-bird-font.ttf", 40)

# Game loop
running = False 
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

welcomescreen = True
active_username = False 
active_passwd = False 

while welcomescreen:
    # For checking the events
    clock.tick(120)
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE or event.type == pygame.QUIT:  # QUIT event
            welcomescreen = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if input_rect.collidepoint(event.pos):
                active_username = True
                active_passwd = False
            else:
                active_username = False
                          
            if input_rect2.collidepoint(event.pos):
                active_passwd = True
                active_username = False
            else:
                active_passwd = False
                        
            if login_rect.collidepoint(event.pos):
                login_tup = (username, password)
                my_cursor.execute("select username, password from users")
                for i in my_cursor:
                    if i == login_tup:
                        welcomescreen = False
                        running = True
                        
        if event.type == pygame.KEYDOWN and active_username == True: 
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
                # Get text input from 0 to -1 i.e. end. 
                username = username[:-1] 
                
            elif event.key == pygame.K_KP_ENTER:
                active_username = False

            # Unicode standard is used for string formation 
            else: 
                username += event.unicode
                        
        if event.type == pygame.KEYDOWN and active_passwd == True: 
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
                # Get text input from 0 to -1 i.e. end. 
                password = password[:-1] 

            elif event.key == pygame.K_KP_ENTER:
                active_passwd = False
                
            # Unicode standard is used for string formation 
            else: 
                password += event.unicode    
                        
                
    screen.blit(pygame.transform.scale(back_img2, (1280, 680)), (0, 0))
    draw_text_box()
    draw_text_box2()
    pygame.draw.rect(screen, color, login_rect, 1, 15)
    pygame.display.flip()    
    # Update the game window
    pygame.display.update()

while running: 
    # For checking the events
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE or event.type == pygame.QUIT:  # QUIT event
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 420 and mx < 510:
                if my > 350 and my < 440:
                    R = pygame.image.load("Welcome screen/R_h.png").convert_alpha()
                    P = pygame.image.load("Welcome screen/p.png").convert_alpha()
                    Y = pygame.image.load("Welcome screen/y.png").convert_alpha()
                    B = pygame.image.load("Welcome screen/b.png").convert_alpha()
                    birds = [bird_r_up, bird_r_mid, bird_r_down]

            elif mx > 529 and mx < 610:
                if my > 350 and my < 440:
                    Y = pygame.image.load("Welcome screen/Y_h.png").convert_alpha()
                    P = pygame.image.load("Welcome screen/p.png").convert_alpha()
                    B = pygame.image.load("Welcome screen/b.png").convert_alpha()
                    R = pygame.image.load("Welcome screen/r.png").convert_alpha()
                    birds = [bird_y_up, bird_y_mid, bird_y_down] 

            elif mx > 627 and mx < 711:
                if my > 350 and my < 440:
                    B = pygame.image.load("Welcome screen/B_h.png").convert_alpha()
                    P = pygame.image.load("Welcome screen/p.png").convert_alpha()
                    R = pygame.image.load("Welcome screen/r.png").convert_alpha()
                    Y = pygame.image.load("Welcome screen/y.png").convert_alpha()
                    birds = [bird_up, bird_mid, bird_down] 

            elif mx > 729 and mx < 811:
                if my > 350 and my < 440:
                    P = pygame.image.load("Welcome screen/P_h.png").convert_alpha()
                    R = pygame.image.load("Welcome screen/r.png").convert_alpha()
                    Y = pygame.image.load("Welcome screen/y.png").convert_alpha()
                    B = pygame.image.load("Welcome screen/b.png").convert_alpha()
                    birds = [bird_p_up, bird_p_mid, bird_p_down] 
                    
        if event.type == pygame.KEYDOWN:  # Key pressed event
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_k and not game_over:  # If space key is pressed
                pygame.mixer.Sound.play(flap).set_volume(0.3)
                bird_movement = 0
                bird_movement = -7
            
            if event.key == pygame.K_k and game_over:  
                game_over = False
                pipes = []
                bird_movement = 0
                bird_rect = bird_img.get_rect(center=(67, 622 // 2))
                score_time = True
                score = 0
        
        # Creating a new level 'spring world'       
        if score > 30:
            if not game_over:
                back_img = pygame.image.load("__maingame__/spring world.jpg").convert_alpha()
                pipe_img = pygame.image.load("Sprites/3.png").convert_alpha()
                #screen.blit(new_level, (width // 2, height // 2))
        
        # To load different stages
        if event.type == bird_flap:
            bird_index += 1

            if bird_index > 2:
                bird_index = 0

            bird_img = birds[bird_index]
            bird_rect = bird_up.get_rect(center=bird_rect.center)

        # To add pipes in the list
        if event.type == create_pipe:
            pipes.extend(create_pipes())
    
    screen.blit(floor_img, (floor_x, 550))
    screen.blit(floor_img2, (floor_x2, 550))
    screen.blit(back_img, (0, 0))

    # Game over conditions
    if not game_over:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        rotated_bird = pygame.transform.rotozoom(bird_img, bird_movement * -6, 1)

        if bird_rect.top < 5 or bird_rect.bottom >= 570:
            pygame.mixer.Sound.play(die).set_volume(0.3)
            game_over = True

        screen.blit(rotated_bird, bird_rect)
        pipe_animation()
        score_update()
        draw_score("game_on")
        
    elif game_over:  
        if w < 280 and h < 300: 
            h -= 1
            w += 1
            x -= 2.4
            y -= 0.8
            
        my_cursor.execute("select highscore from users")
        for i in my_cursor:
            if i[0] < high_score:
                update_highscore(connection, high_score, username)
                
        connection.commit()

        over_small_image = pygame.transform.scale(over_img, (x, y))
        screen.blit(over_small_image, (w, h))
        back_img = pygame.image.load("__maingame__/Background.jpg").convert_alpha()
        pipe_img = pygame.image.load("Sprites/2.png").convert_alpha()
        draw_score("game_over")
        continue_text = continue_font.render("Press K to continue", True, "Black")
        continue_rect = continue_text.get_rect(center=((width // 2), 550))
        screen.blit(continue_text, continue_rect)
        screen.blit(R, (420, 350))
        screen.blit(Y, (520, 350))
        screen.blit(B, (620, 350))
        screen.blit(P, (720, 350))

    # To move the base
    floor_x -= 3
    if floor_x < -754:
        floor_x = 0

    floor_x2 -= 3
    if floor_x2 < 264:
        floor_x2 = 1017
    draw_floor()

    # Update the game window
    pygame.display.update()

# Quitting the pygame and sys
pygame.quit()
sys.exit()