import tkinter as tk
from tkinter import *


running = False

hours = 0
minutes = 0
seconds = 0


def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

    """Setting var back to 0"""
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0

    """set label back to 0"""
    stopwatch_label.config(text="00:00:00")

def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f"{hours}" if hours > 9 else f"0{hours}"
    min_string = f"{minutes}" if minutes > 9 else f"0{minutes}"
    sec_string = f"{seconds}" if seconds > 9 else f"0{seconds}"

    stopwatch_label.config(text=hours_string + ":" + min_string + ":" + sec_string)

    global update_time
    update_time = stopwatch_label.after(1000, update)

root = tk.Tk()
root.geometry("350x500")
root.title("My StopWatch")


stopwatch_label = tk.Label(root, text='00:00:00', font=("Ariel", 60))
stopwatch_label.pack()


start_btn = tk.Button(root, text="START", height=3, width=7, font=("Ariel", 20), command=start)
start_btn.place(x=30, y=220)
pause_btn = tk.Button(root, text="PAUSE", height=3, width=7, font=("Ariel", 20), command=pause)
pause_btn.place(x=180, y=220)
reset_btn = Button(root, text="RESET", height=3, width=7, font=("Ariel", 20), command=reset)
reset_btn.place(x=30, y=350)
exit_btn = tk.Button(root, text="EXIT", height=3, width=7, font=("Ariel", 20), command=root.quit)
exit_btn.place(x=180, y=350)



root.mainloop()