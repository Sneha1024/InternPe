from tkinter import *  #is used for creating graphical user interfaces (GUIs) in Python
from time import *  #provides time-related functions.

def update():
    time_string = strftime("%I:%M:%S %p")  #Uses the strftime function from the time module to get the current time in the format of hours, minutes, and seconds, followed by AM or PM.
    time_label.config(text=time_string)  #updates with current time

    day_string = strftime("%A") #gets current day of the week 
    day_label.config(text=day_string)#updates day_label with current day of the week

    date_string = strftime("%B %d, %Y") #gets current date
    date_label.config(text=date_string)#updates the date_label with current date

    window.after(1000,update) #update function is called after 1000 milliseconds to ensure the time label is updated


window = Tk()# main window object of the GUI application is created

time_label = Label(window,font=("Arial",50),fg="#2B3EDA",bg="pink")#style
time_label.pack()#packs the time_label widget into the window, making it visible.

day_label = Label(window,font=("Times New Roman",25,"bold"))#style
day_label.pack()#packs the day_label widget into the window, making it visible.

date_label = Label(window,font=("Times New Roman",30))#style
date_label.pack()#packs the date_label widget into the window, making it visible.

update()#called to initialize the labels with current time,day and date.

window.mainloop()