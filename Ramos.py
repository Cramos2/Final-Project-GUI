import tkinter as tk
import time


timer_running = False
start_time = None
elapsed_time = 0

def update_time():
    current_time = time.strftime('%I:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

def update_date():
    current_date = time.strftime('%A, %B %d, %Y')
    date_label.config(text=current_date)

def start_timer():
    global timer_running, start_time, elapsed_time
    if not timer_running:
        timer_running = True
        start_time = time.time() - elapsed_time
        update_timer()

def stop_timer():
    global timer_running, elapsed_time
    if timer_running:
        timer_running = False
        elapsed_time = time.time() - start_time

def resume_timer():
    global timer_running, start_time
    if not timer_running:
        timer_running = True
        start_time = time.time() - elapsed_time
        update_timer()

def update_timer():
    global elapsed_time
    if timer_running:
        elapsed_time = time.time() - start_time
        timer_label.config(text=format_time(elapsed_time))
        timer_label.after(1000, update_timer)

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds))

root = tk.Tk()
root.title("Personal Digi Clock")

time_label = tk.Label(root, font=('Arial', 45), bg="blue", fg='white')
time_label.pack(padx=15, pady=10)

date_label = tk.Label(root, font=('Arial', 20), bg='blue', fg='white')
date_label.pack(padx=10, pady=10)

timer_label = tk.Label(root, font=('Helvetica', 20), bg='blue', fg='white')
timer_label.pack(padx=5, pady=5)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(padx=10, pady=5)

stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
stop_button.pack(padx=10, pady=5)

resume_button = tk.Button(root, text="Resume Timer", command=resume_timer)
resume_button.pack(padx=10, pady=5)

update_time()
update_date()

root.mainloop()
