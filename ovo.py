import tkinter as tk
import random
import time
import pandas as pd
import os

CANVAS_WIDTH = 1520     
CANVAS_HEIGHT = 768     
PLAYER_SIZE = 50
PLAYER_SPEED = 5
CIRCLE_SIZE = 30
CIRCLE_SPAWN_TIME = 5000
GAME_DURATION = 60 * 1000

player1_x = 100
player1_y = 100         
player1_dx = 0
player1_dy = 0

player2_x = 1320      
player2_y = 100
player2_dx = 0
player2_dy = 0

circle_xall = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
circle_yall = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

circle_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
circle_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

score_player1 = 0
score_player2 = 0


directory = "E:\\NK programs\\Python\\python save\\DASH game"
filename = "dashpoints.xlsx"
filepathx = os.path.join(directory, filename)

def update_points():
    df = pd.read_excel(filepathx)
    df.loc[0, 'POINTS'] = score_player1
    df.loc[1, 'POINTS'] = score_player2

    if score_player1 > score_player2:
        df.loc[5, 'POINTS'] = "PLAYER 1"
    elif score_player1 < score_player2:
        df.loc[5, 'POINTS'] = "PLAYER 2"
    else:
        df.loc[5, 'POINTS'] = "DRAW"
    
    df.to_excel(filepathx, index=False)
    
    
    
def move_players():
    global player1_x, player1_y, player2_x, player2_y

    player1_x += player1_dx
    player1_y += player1_dy

    if player1_x < 0:
        player1_x = 0
    elif player1_x > CANVAS_WIDTH - PLAYER_SIZE:
        player1_x = CANVAS_WIDTH - PLAYER_SIZE
    if player1_y < 0:
        player1_y = 0
    elif player1_y > CANVAS_HEIGHT - PLAYER_SIZE:
        player1_y = CANVAS_HEIGHT - PLAYER_SIZE

    canvas.coords(player1, player1_x, player1_y, player1_x + PLAYER_SIZE, player1_y + PLAYER_SIZE)

    player2_x += player2_dx
    player2_y += player2_dy

    if player2_x < 0:
        player2_x = 0
    elif player2_x > CANVAS_WIDTH - PLAYER_SIZE:
        player2_x = CANVAS_WIDTH - PLAYER_SIZE
    if player2_y < 0:
        player2_y = 0
    elif player2_y > CANVAS_HEIGHT - PLAYER_SIZE:
        player2_y = CANVAS_HEIGHT - PLAYER_SIZE

    canvas.coords(player2, player2_x, player2_y, player2_x + PLAYER_SIZE, player2_y + PLAYER_SIZE)

    canvas.after(10, move_players)


def move_player1_up(event):
    global player1_dy
    player1_dy = -PLAYER_SPEED


def move_player1_down(event):
    global player1_dy
    player1_dy = PLAYER_SPEED


def move_player1_left(event):
    global player1_dx
    player1_dx = -PLAYER_SPEED


def move_player1_right(event):
    global player1_dx
    player1_dx = PLAYER_SPEED


def move_player2_up(event):
    global player2_dy
    player2_dy = -PLAYER_SPEED


def move_player2_down(event):
    global player2_dy
    player2_dy = PLAYER_SPEED


def move_player2_left(event):
    global player2_dx
    player2_dx = -PLAYER_SPEED


def move_player2_right(event):
    global player2_dx
    player2_dx = PLAYER_SPEED


last_spawn_time = time.time()

def spawn_circle():
    global circle_x, circle_y, last_spawn_time
    current_time = time.time()
    if current_time - last_spawn_time >= CIRCLE_SPAWN_TIME / 1000:
        circle_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
        circle_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
        canvas.coords(circle, circle_x, circle_y, circle_x + CIRCLE_SIZE, circle_y + CIRCLE_SIZE)
        last_spawn_time = current_time
    canvas.after(10, spawn_circle)


def check_collision():
    global score_player1, score_player2
    player1_coords = canvas.coords(player1)
    player2_coords = canvas.coords(player2)
    circle_center_x = circle_x + CIRCLE_SIZE / 2
    circle_center_y = circle_y + CIRCLE_SIZE / 2

    if (player1_coords[0] <= circle_center_x <= player1_coords[2] and
            player1_coords[1] <= circle_center_y <= player1_coords[3]):
        score_player1 += 1
        canvas.itemconfig(score_text1, text="Player 1: {}".format(score_player1))
        canvas.after(CIRCLE_SPAWN_TIME, spawn_circle)

    if (player2_coords[0] <= circle_center_x <= player2_coords[2] and
            player2_coords[1] <= circle_center_y <= player2_coords[3]):
        score_player2 += 1
        canvas.itemconfig(score_text2, text="Player 2: {}".format(score_player2))
        canvas.after(CIRCLE_SPAWN_TIME, spawn_circle)

    canvas.after(10, check_collision)


def update_time():
    elapsed_time = int(time.time() * 1000 - start_time)
    remaining_time = max(0, GAME_DURATION - elapsed_time)
    minutes = remaining_time // 60000
    seconds = (remaining_time % 60000) // 1000
    time_text = "Time: {:02d}:{:02d}".format(minutes, seconds)
    canvas.itemconfig(time_label, text=time_text)
    
    if remaining_time <= 0:
        end_game()

    canvas.after(100, update_time)


def end_game():
    update_points()
    root.destroy()


root = tk.Tk()
root.geometry('1366x768')
root.title("1 vs 1 Game")
root.state('zoomed')
    
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

player1 = canvas.create_rectangle(player1_x, player1_y, player1_x + PLAYER_SIZE, player1_y + PLAYER_SIZE, fill="red")
player2 = canvas.create_rectangle(player2_x, player2_y, player2_x + PLAYER_SIZE, player2_y + PLAYER_SIZE, fill="green")

for i in range(100):
    circle_all = canvas.create_oval(circle_xall, circle_yall, circle_xall + CIRCLE_SIZE, circle_yall + CIRCLE_SIZE, fill="white")
    circle_xall = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    circle_yall = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    
circle = canvas.create_oval(circle_x, circle_y, circle_x + CIRCLE_SIZE, circle_y + CIRCLE_SIZE, fill="white")

score_text1 = canvas.create_text(100, 30, text="Player 1: {}".format(score_player1), font=("Arial", 16), anchor="w", fill="red")
score_text2 = canvas.create_text(1320, 30, text="Player 2: {}".format(score_player2), font=("Arial", 16), anchor="w", fill="green")

time_label = canvas.create_text(CANVAS_WIDTH // 2, 30, text="Time: 01:00", font=("Arial", 16), anchor="center")

root.bind("w", move_player1_up)
root.bind("s", move_player1_down)
root.bind("a", move_player1_left)
root.bind("d", move_player1_right)

root.bind("<Up>", move_player2_up)
root.bind("<Down>", move_player2_down)
root.bind("<Left>", move_player2_left)
root.bind("<Right>", move_player2_right)

start_time = time.time() * 1000
spawn_circle()
check_collision()
move_players()
update_time()

root.mainloop()
