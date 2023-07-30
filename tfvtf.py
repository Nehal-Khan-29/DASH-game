import tkinter as tk
import random
import time
import pandas as pd
import os
from PIL import Image, ImageTk

CANVAS_WIDTH = 1500
CANVAS_HEIGHT = 760
PLAYER_SIZE = 50 
CIRCLE_SIZE = 30
GAME_DURATION = 120 * 1000

PLAYER_SPEED1 = 5
PLAYER_SPEED2 = 5
PLAYER_SPEED3= 5
PLAYER_SPEED4 = 5

player1_x = 300
player1_y = 300
player1_dx = 0
player1_dy = 0

player2_x = 300
player2_y = 400
player2_dx = 0
player2_dy = 0

player3_x = 1100
player3_y = 300
player3_dx = 0
player3_dy = 0

player4_x = 1100
player4_y = 400
player4_dx = 0
player4_dy = 0

circle_x = 735
circle_y = 350

score_player1 = 0
score_player2 = 0
score_player3 = 0
score_player4 = 0


directory = "E:\\NK programs\\Python\\python save\\DASH game"
filename = "dashpoints.xlsx"
filepathx = os.path.join(directory, filename)

goal_post1_x = 0
goal_post1_y = CANVAS_HEIGHT / 2 - 100
goal_post2_x = 1491
goal_post2_y = CANVAS_HEIGHT / 2 - 100







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



GOAL_POST_WIDTH = 10
GOAL_POST_HEIGHT = 200
GOAL_POST_COLOR = "black"

MID_x = 745
MID_y = 0
MID_WIDTH = 10
MID_HEIGHT = 770
MID_COLOR = "White"

hold_0 = False
hold_3 = False
hold_space = False
hold_p = False
last_frame_space = False
last_frame_3 = False
last_frame_p = False
last_frame_0 = False







def move_players():
    global player1_x, player1_y, player2_x, player2_y, player3_x, player3_y, player4_x, player4_y, current_player

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







def handle_key_press(event):
    global player1_dx, player1_dy, player2_dx, player2_dy, player3_dx, player3_dy, player4_dx, player4_dy, hold_0,hold_space,hold_p,hold_3, last_frame_3,last_frame_0,last_frame_space,last_frame_p

    if event.char == 'w':
        player1_dy = -PLAYER_SPEED1
    elif event.char == 's':
        player1_dy = PLAYER_SPEED1
    elif event.char == 'a':
        player1_dx = -PLAYER_SPEED1
    elif event.char == 'd':
        player1_dx = PLAYER_SPEED1

    if event.char == 'i':
        player3_dy = -PLAYER_SPEED3
    elif event.char == 'k':
        player3_dy = PLAYER_SPEED3
    elif event.char == 'j':
        player3_dx = -PLAYER_SPEED3
    elif event.char == 'l':
        player3_dx = PLAYER_SPEED3

    if event.keysym == 'Up':
        player2_dy = -PLAYER_SPEED2
    elif event.keysym == 'Down':
        player2_dy = PLAYER_SPEED2
    elif event.keysym == 'Left':
        player2_dx = -PLAYER_SPEED2
    elif event.keysym == 'Right':
        player2_dx = PLAYER_SPEED2

    if event.keysym == '8':
        player4_dy = -PLAYER_SPEED4
    elif event.keysym == '5':
        player4_dy = PLAYER_SPEED4
    elif event.keysym == '4':
        player4_dx = -PLAYER_SPEED4
    elif event.keysym == '6':
        player4_dx = PLAYER_SPEED4
        
    if event.keysym == '0':
        hold_0 = True
        
    if event.keysym == '3':
        hold_3 = True
        
    if event.keysym == 'space':
        hold_space = True
        
    if event.keysym == 'p':
        hold_p = True











def reset_players_positions_g2():
    global player1_x, player1_y, player2_x, player2_y, player3_x, player3_y, player4_x, player4_y

    player1_x = 300
    player1_y = 300
    player2_x = 300
    player2_y = 400

    # Move the players to their starting positions
    canvas.coords(player1, player1_x, player1_y, player1_x + PLAYER_SIZE, player1_y + PLAYER_SIZE)
    canvas.coords(player2, player2_x, player2_y, player2_x + PLAYER_SIZE, player2_y + PLAYER_SIZE)









def reset_players_positions_g1():
    global player1_x, player1_y, player2_x, player2_y, player3_x, player3_y, player4_x, player4_y

    player3_x = 1100
    player3_y = 300
    player4_x = 1100
    player4_y = 400

    # Move the players to their starting positions
    canvas.coords(player3, player3_x, player3_y, player3_x + PLAYER_SIZE, player3_y + PLAYER_SIZE)
    canvas.coords(player4, player4_x, player4_y, player4_x + PLAYER_SIZE, player4_y + PLAYER_SIZE)












def check_collision():
    global score_player1, score_player2, score_player3, score_player4, circle_x, circle_y, hold_0,hold_3,hold_space,hold_p, last_frame_p,last_frame_3,last_frame_0,last_frame_space,PLAYER_SPEED1,PLAYER_SPEED2,PLAYER_SPEED3,PLAYER_SPEED4

    player1_coords = canvas.coords(player1)
    player2_coords = canvas.coords(player2)
    player3_coords = canvas.coords(player3)
    player4_coords = canvas.coords(player4)
    football_coords = canvas.coords(circle)

    # Check collision with player 1
    if player1_coords[0] < football_coords[2] and player1_coords[2] > football_coords[0] and \
            player1_coords[1] < football_coords[3] and player1_coords[3] > football_coords[1]:
        if hold_space:
            PLAYER_SPEED1 = 2
            dx = player1_dx * 10
            dy = player1_dy * 10

        else:
            PLAYER_SPEED1 = 5
            dx = player1_dx * 20
            dy = player1_dy * 20
        move_smoothly(circle, dx, dy)

    # Check collision with player 2
    if player2_coords[0] < football_coords[2] and player2_coords[2] > football_coords[0] and \
            player2_coords[1] < football_coords[3] and player2_coords[3] > football_coords[1]:
        if hold_0:
            PLAYER_SPEED2 = 2
            dx = player2_dx * 10
            dy = player2_dy * 10
        else:
            PLAYER_SPEED2 = 5
            dx = player2_dx * 20
            dy = player2_dy * 20
        move_smoothly(circle, dx, dy)

    # Check collision with player 3
    if player3_coords[0] < football_coords[2] and player3_coords[2] > football_coords[0] and \
            player3_coords[1] < football_coords[3] and player3_coords[3] > football_coords[1]:
        if hold_p:
            PLAYER_SPEED3 = 2
            dx = player3_dx * 10
            dy = player3_dy * 10
        else:
            PLAYER_SPEED3 = 5
            dx = player3_dx * 20
            dy = player3_dy * 20
        move_smoothly(circle, dx, dy)

    # Check collision with player 4
    if player4_coords[0] < football_coords[2] and player4_coords[2] > football_coords[0] and \
            player4_coords[1] < football_coords[3] and player4_coords[3] > football_coords[1]:
        if hold_3:
            PLAYER_SPEED4 = 2
            dx = player4_dx * 10
            dy = player4_dy * 10
        else:
            PLAYER_SPEED4 = 5
            dx = player4_dx * 20
            dy = player4_dy * 20
        move_smoothly(circle, dx, dy)
        
    if last_frame_space:
        last_frame_space = False
        
    if last_frame_0:
        last_frame_0 = False
    
    if last_frame_3:
        last_frame_3 = False
    
    if last_frame_p:
        last_frame_p = False

    # Define the coordinates for the goal text
    goal_text_x = 750
    goal_text_y = 400

    # Check collision with goal post 1
    if football_coords[0] <= goal_post1_x + GOAL_POST_WIDTH and \
            goal_post1_y <= football_coords[1] + CIRCLE_SIZE / 2 <= goal_post1_y + GOAL_POST_HEIGHT:
        score_player3 += 1
        score_player4 += 1
        update_points()
        circle_x = 200
        circle_y = 350

        canvas.coords(circle, circle_x, circle_y, circle_x + CIRCLE_SIZE, circle_y + CIRCLE_SIZE)
        reset_players_positions_g1()
        goal_text = canvas.create_text(goal_text_x, goal_text_y, text="GOAL!", font=("Arial", 24), fill="red")
        canvas.after(2000, lambda: canvas.delete(goal_text)) 

    # Check collision with goal post 2
    if football_coords[2] >= goal_post2_x and \
            goal_post2_y <= football_coords[1] + CIRCLE_SIZE / 2 <= goal_post2_y + GOAL_POST_HEIGHT:
        score_player1 += 1
        score_player2 += 1
        update_points()
        circle_x = 1300
        circle_y = 350
        
        canvas.coords(circle, circle_x, circle_y, circle_x + CIRCLE_SIZE, circle_y + CIRCLE_SIZE)
        reset_players_positions_g2()
        goal_text = canvas.create_text(goal_text_x, goal_text_y, text="GOAL!", font=("Arial", 24), fill="red")
        canvas.after(2000, lambda: canvas.delete(goal_text))  


    canvas.itemconfig(score_label_player2, text="TEAM 2: {}".format(score_player3))
    canvas.itemconfig(score_label_player3, text="TEAM 1: {}".format(score_player1))


    canvas.after(10, check_collision)










def move_smoothly(item, dx, dy):
    num_steps = 10
    step_dx = dx / num_steps
    step_dy = dy / num_steps

    for _ in range(num_steps):
        coords = canvas.coords(item)  
        next_x = coords[0] + step_dx
        next_y = coords[1] + step_dy

        if next_x < 0 or next_x > CANVAS_WIDTH - 30 or next_y < 10 or next_y > CANVAS_HEIGHT - 30:
            return  

        new_coords = [next_x, next_y, next_x + CIRCLE_SIZE, next_y + CIRCLE_SIZE]

        canvas.coords(item, *new_coords)
        canvas.update()
        time.sleep(0.01)

    remaining_dx = dx - step_dx * num_steps
    remaining_dy = dy - step_dy * num_steps

    final_coords = canvas.coords(item)
    final_x = final_coords[0] + remaining_dx
    final_y = final_coords[1] + remaining_dy

    if final_x >= 0 and final_x <= CANVAS_WIDTH and final_y >= 0 and final_y <= CANVAS_HEIGHT:
        new_final_coords = [final_x, final_y, final_x + CIRCLE_SIZE, final_y + CIRCLE_SIZE]
        canvas.coords(item, *new_final_coords)










def handle_key_release(event):
    global player1_dx, player1_dy, player2_dx, player2_dy, player3_dx, player3_dy, player4_dx, player4_dy, hold_0,hold_3,hold_space,hold_p, last_frame_3,last_frame_p,last_frame_0,last_frame_space

    if event.char == 'w' or event.char == 's':
        player1_dy = 0
    elif event.char == 'a' or event.char == 'd':
        player1_dx = 0

    if event.char == 'i' or event.char == 'k':
        player3_dy = 0
    elif event.char == 'j' or event.char == 'l':
        player3_dx = 0

    if event.keysym == 'Up' or event.keysym == 'Down':
        player2_dy = 0
    elif event.keysym == 'Left' or event.keysym == 'Right':
        player2_dx = 0

    if event.keysym == '8' or event.keysym == '5':
        player4_dy = 0
    elif event.keysym == '4' or event.keysym == '6':
        player4_dx = 0
        
    if event.keysym == 'space':
        hold_space = False
        last_frame_space = True
        
    if event.keysym == '0':
        hold_0 = False
        last_frame_0 = True
        
    if event.keysym == '3':
        hold_3 = False
        last_frame_3 = True
        
    if event.keysym == 'p':
        hold_p = False
        last_frame_p = True            
        
        
        
        
        
        

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

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,bg="green")
canvas.pack()

goal_post1 = canvas.create_rectangle(goal_post1_x, goal_post1_y, goal_post1_x + GOAL_POST_WIDTH,
                                     goal_post1_y + GOAL_POST_HEIGHT, fill="white",outline="white")
goal_post2 = canvas.create_rectangle(goal_post2_x, goal_post2_y, goal_post2_x + GOAL_POST_WIDTH,
                                     goal_post2_y + GOAL_POST_HEIGHT, fill="white",outline="white")


MID = canvas.create_rectangle(MID_x, MID_y, MID_x + MID_WIDTH,
                                     MID_y + MID_HEIGHT, fill=MID_COLOR, outline="white")



player1 = canvas.create_rectangle(player1_x, player1_y, player1_x + PLAYER_SIZE, player1_y + PLAYER_SIZE, fill="red")
player2 = canvas.create_rectangle(player2_x, player2_y, player2_x + PLAYER_SIZE, player2_y + PLAYER_SIZE, fill="purple")
player3 = canvas.create_rectangle(player3_x, player3_y, player3_x + PLAYER_SIZE, player3_y + PLAYER_SIZE, fill="blue")
player4 = canvas.create_rectangle(player4_x, player4_y, player4_x + PLAYER_SIZE, player4_y + PLAYER_SIZE, fill="yellow")

circle = canvas.create_oval(circle_x, circle_y, circle_x + CIRCLE_SIZE, circle_y + CIRCLE_SIZE, fill="white")





score_label_player3 = canvas.create_text(300, 30, text="TEAM 1: {}".format(score_player1), font=("Arial", 16), anchor="w", fill="purple")
score_label_player2 = canvas.create_text(1100, 30, text="TEAM 2: {}".format(score_player3), font=("Arial", 16), anchor="w", fill="blue")


time_label = canvas.create_text(CANVAS_WIDTH // 2, 30, text="Time: 01:00", font=("Arial", 16), anchor="center")

start_time = time.time()

root.bind('<KeyPress>', handle_key_press)
root.bind('<KeyRelease>', handle_key_release)

move_players()
check_collision()
update_time()

root.mainloop()

