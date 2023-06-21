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
GAME_DURATION = 90 * 1000

player1_x = 100
player1_y = 100
player1_dx = 0
player1_dy = 0

player2_x = 200
player2_y = 100
player2_dx = 0
player2_dy = 0

player3_x = 1120
player3_y = 100
player3_dx = 0
player3_dy = 0

player4_x = 1320
player4_y = 100
player4_dx = 0
player4_dy = 0

circle_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
circle_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

score_player1 = 0
score_player2 = 0
score_player3 = 0
score_player4 = 0

circle_xall = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
circle_yall = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

directory = "E:\\NK programs\\Python\\python save\\DASH game"
filename = "dashpoints.xlsx"
filepathx = os.path.join(directory, filename)


def update_points():
    df = pd.read_excel(filepathx)
    df.loc[0, 'POINTS'] = score_player1
    df.loc[1, 'POINTS'] = score_player2
    df.loc[2, 'POINTS'] = score_player3
    df.loc[3, 'POINTS'] = score_player4

    if score_player1 + score_player2 > score_player3 + score_player4:
        df.loc[5, 'POINTS'] = "TEAM 1"
    elif score_player1 + score_player2 < score_player3 + score_player4:
        df.loc[5, 'POINTS'] = "TEAM 2"
    else:
        df.loc[5, 'POINTS'] = "DRAW"

    df.to_excel(filepathx, index=False)


def move_players():
    global player1_x, player1_y, player2_x, player2_y, player3_x, player3_y, player4_x, player4_y

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

    player3_x += player3_dx
    player3_y += player3_dy

    if player3_x < 0:
        player3_x = 0
    elif player3_x > CANVAS_WIDTH - PLAYER_SIZE:
        player3_x = CANVAS_WIDTH - PLAYER_SIZE
    if player3_y < 0:
        player3_y = 0
    elif player3_y > CANVAS_HEIGHT - PLAYER_SIZE:
        player3_y = CANVAS_HEIGHT - PLAYER_SIZE

    canvas.coords(player3, player3_x, player3_y, player3_x + PLAYER_SIZE, player3_y + PLAYER_SIZE)

    player4_x += player4_dx
    player4_y += player4_dy

    if player4_x < 0:
        player4_x = 0
    elif player4_x > CANVAS_WIDTH - PLAYER_SIZE:
        player4_x = CANVAS_WIDTH - PLAYER_SIZE
    if player4_y < 0:
        player4_y = 0
    elif player4_y > CANVAS_HEIGHT - PLAYER_SIZE:
        player4_y = CANVAS_HEIGHT - PLAYER_SIZE

    canvas.coords(player4, player4_x, player4_y, player4_x + PLAYER_SIZE, player4_y + PLAYER_SIZE)

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


def move_player3_up(event):
    global player3_dy
    player3_dy = -PLAYER_SPEED


def move_player3_down(event):
    global player3_dy
    player3_dy = PLAYER_SPEED


def move_player3_left(event):
    global player3_dx
    player3_dx = -PLAYER_SPEED


def move_player3_right(event):
    global player3_dx
    player3_dx = PLAYER_SPEED


def move_player4_up(event):
    global player4_dy
    player4_dy = -PLAYER_SPEED


def move_player4_down(event):
    global player4_dy
    player4_dy = PLAYER_SPEED


def move_player4_left(event):
    global player4_dx
    player4_dx = -PLAYER_SPEED


def move_player4_right(event):
    global player4_dx
    player4_dx = PLAYER_SPEED


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
    global score_player1, score_player2, score_player3, score_player4
    player1_coords = canvas.coords(player1)
    player2_coords = canvas.coords(player2)
    player3_coords = canvas.coords(player3)
    player4_coords = canvas.coords(player4)
    circle_coords = canvas.coords(circle)

    if player1_coords[0] < circle_coords[2] and player1_coords[2] > circle_coords[0] and \
            player1_coords[1] < circle_coords[3] and player1_coords[3] > circle_coords[1]:
        score_player1 += 1
        canvas.coords(score_label_player1, 100, 30)

    if player2_coords[0] < circle_coords[2] and player2_coords[2] > circle_coords[0] and \
            player2_coords[1] < circle_coords[3] and player2_coords[3] > circle_coords[1]:
        score_player2 += 1
        canvas.coords(score_label_player2, 300, 30)

    if player3_coords[0] < circle_coords[2] and player3_coords[2] > circle_coords[0] and \
            player3_coords[1] < circle_coords[3] and player3_coords[3] > circle_coords[1]:
        score_player3 += 1
        canvas.coords(score_label_player3, 1120, 30)

    if player4_coords[0] < circle_coords[2] and player4_coords[2] > circle_coords[0] and \
            player4_coords[1] < circle_coords[3] and player4_coords[3] > circle_coords[1]:
        score_player4 += 1
        canvas.coords(score_label_player4, 1320, 30)
        
    canvas.itemconfig(score_label_player1, text="Player 1: {}".format(score_player1))
    canvas.itemconfig(score_label_player2, text="Player 2: {}".format(score_player2))
    canvas.itemconfig(score_label_player3, text="Player 3: {}".format(score_player3))
    canvas.itemconfig(score_label_player4, text="Player 4: {}".format(score_player4))



    canvas.after(10, check_collision)



def update_time():
    global GAME_DURATION, time_label
    elapsed_time = int((time.time() - start_time) * 1000)
    remaining_time = max(GAME_DURATION - elapsed_time, 0)
    minutes = remaining_time // (60 * 1000)
    seconds = (remaining_time % (60 * 1000)) // 1000
    canvas.itemconfigure(time_label, text=f"Time: {minutes:02d}:{seconds:02d}")
    if remaining_time <= 0:
        end_game()
        update_points()
    canvas.after(100, update_time)
    



def end_game():
    update_points()
    root.destroy()

root = tk.Tk()
root.geometry('1366x768')
root.title("2 vs 2 Game")
root.state('zoomed')

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,bg="white")
canvas.pack()

player1 = canvas.create_rectangle(player1_x, player1_y, player1_x + PLAYER_SIZE, player1_y + PLAYER_SIZE, fill="red")
player2 = canvas.create_rectangle(player2_x, player2_y, player2_x + PLAYER_SIZE, player2_y + PLAYER_SIZE, fill="green")
player3 = canvas.create_rectangle(player3_x, player3_y, player3_x + PLAYER_SIZE, player3_y + PLAYER_SIZE, fill="blue")
player4 = canvas.create_rectangle(player4_x, player4_y, player4_x + PLAYER_SIZE, player4_y + PLAYER_SIZE, fill="yellow")

for i in range(100):
    circle_all = canvas.create_oval(circle_xall, circle_yall, circle_xall + CIRCLE_SIZE, circle_yall + CIRCLE_SIZE, fill="white")
    circle_xall = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    circle_yall = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    
circle = canvas.create_oval(circle_x, circle_y, circle_x + CIRCLE_SIZE, circle_y + CIRCLE_SIZE, fill="white")

score_label_player1 = canvas.create_text(100, 30, text="Player 1: {}".format(score_player1), font=("Arial", 16), anchor="w", fill="red")
score_label_player2 = canvas.create_text(300, 30, text="Player 2: {}".format(score_player2), font=("Arial", 16), anchor="w", fill="green")
score_label_player3 = canvas.create_text(1120, 30, text="Player 3: {}".format(score_player3), font=("Arial", 16), anchor="w", fill="blue")
score_label_player4 = canvas.create_text(1320, 30, text="Player 4: {}".format(score_player4), font=("Arial", 16), anchor="w",fill="orange")

time_label = canvas.create_text(CANVAS_WIDTH // 2, 30, text="Time: 01:00", font=("Arial", 16), anchor="center")

start_time = time.time()

root.bind("<Up>", move_player2_up)
root.bind("<Down>", move_player2_down)
root.bind("<Left>", move_player2_left)
root.bind("<Right>", move_player2_right)

root.bind("w", move_player1_up)
root.bind("s", move_player1_down)
root.bind("a", move_player1_left)
root.bind("d", move_player1_right)

root.bind("i", move_player3_up)
root.bind("k", move_player3_down)
root.bind("j", move_player3_left)
root.bind("l", move_player3_right)

root.bind("8", move_player4_up)
root.bind("5", move_player4_down)
root.bind("4", move_player4_left)
root.bind("6", move_player4_right)

move_players()
spawn_circle()
check_collision()
update_time()

root.mainloop()
