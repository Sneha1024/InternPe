#from ast import Lambda
from tkinter import *
import random
game_width=700
game_height=700
speed=200
space_size=50
body_parts=3
snake_color='#964B00'
food_color='#Ffff00'
bg_color='#f5fffa'
class Snake:
    def __init__(self):
        self.body_size=body_parts
        self.coordinates=[]
        self.squares=[]
        for i in range(0,body_parts):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color,tag='snake')
            self.squares.append(square)
class Food:
    def __init__(self):
        x=random.randint(0,(game_width/space_size-1))*space_size
        y=random.randint(0,(game_height/space_size-1))*space_size
        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+space_size,y+space_size,fill=food_color,tag='food')



def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction=='up':
        y-=space_size
    elif direction=='down':
        y+=space_size
    elif direction=='left':
        x-=space_size
    elif direction=='right':
        x+=space_size

    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color)
    snake.squares.insert(0,square)   
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text='Score:{}'.format(score))
        canvas.delete('food') #del food obj
        food=Food()
    else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(speed,next_turn,snake,food)
    


def change_dir(new_dir):
    global direction
    if new_dir=='left':
        if direction!='right':
            direction=new_dir
    elif new_dir=='right':
        if direction!='left':
            direction=new_dir
    elif new_dir=='up':
        if direction!='down':
            direction=new_dir
    elif new_dir=='down':
        if direction!='up':
            direction=new_dir
def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=game_width:
        print('Game Over!')
        return True
    elif y<0 or y>=game_height:
        print('Game Over!')
        return True
    

    for body_parts in snake.coordinates[1:]:
        if x==body_parts[0] and y==body_parts[1]:
            print('Game Over!')
            return True
    return False    
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text='Game Over!',fill='#ffa07a',tag='Game Over!')
window =Tk()
window.title('Snake game')
window.resizable(False,False)
score=0
direction='down'
label=Label(window,text='Score:{}'.format(score),font=('consolas',40))
canvas=Canvas(window,bg=bg_color,height=game_height,width=game_width)
canvas.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda event:change_dir('left'))
window.bind('<Right>',lambda event:change_dir('right'))
window.bind('<Down>',lambda event:change_dir('down'))
window.bind('<Up>',lambda event:change_dir('up'))

snake=Snake()
food=Food()
next_turn(snake,food)
label.pack()
window.mainloop()