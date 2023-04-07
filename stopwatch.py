import tkinter as tk
from tkinter import messagebox
import time

bg_colour = "#3d6466"
dark_bg = "#28393a"
act_fg = "#badee2"

root = tk.Tk()
root.title("Knock-off stopwatch")
root.resizable(0, 0)
root.eval("tk::PlaceWindow . center")

is_running = False
l_lst = []

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def clear_list():
    l_lst.clear()
    load_frame1()

def start():
    global is_running
    global start_time
    if is_running is False:
        is_running = True
        start_time = time.time()
        laps()

def stop():
    global is_running
    last_lap = time_label.cget("text")
    l_lst.append(last_lap)
    is_running = False
    time_label.configure(text="0.00")

def laps():
    if is_running:
        lap_time = round(time.time() - start_time, 2)
        str_lap = str(lap_time)
        time_label.configure(text=f"{str_lap}")
        time_label.after(50, laps)

def new_lap():
    global start_time
    if is_running:
        current_lap = time_label.cget("text")
        l_lst.append(current_lap)
        start_time = time.time()
        time_label.configure(text="0.00")
        laps()

def laps_list(l_lst):
    for item in l_lst:
        print(item)

def load_frame2():
    if time_label.cget("text") != "0.00":
        messagebox.showerror(title="Erro",
                             message="In order to see the laps, please stop the stopwatch first")
    else:
        clear_widgets(frame2)
        frame2.tkraise()

        heading_label = tk.Label(frame2, 
                                text="LAPS LIST", 
                                bg=bg_colour, 
                                fg="white", 
                                font=("TkHeadingFont", 30, 'bold'))
        heading_label.pack(pady=20)

        for indx, l_time in enumerate(l_lst):
            label = tk.Label(frame2,
                    text=f"Lap №{indx+1}: {l_time} seconds",
                    bg=dark_bg,
                    fg="white",
                    font=("TkMenuFont", 16))
            label.pack(padx=20, fill="both")
        
        back_button = tk.Button(frame2,
                                text="Back",
                                font=("TkMenuFont", 14),
                                bg=dark_bg,
                                fg="white",
                                activebackground="black",
                                activeforeground=act_fg,
                                cursor="hand2",
                                borderwidth=0,
                                width=10,
                                command=clear_list)
        back_button.pack(pady=20)

def load_frame1():
    global time_label

    clear_widgets(frame1)
    frame1.tkraise()

    heading_label = tk.Label(frame1, 
                             text="STOPWATCH", 
                             bg=bg_colour, 
                             fg="white", 
                             font=("TkHeadingFont", 30, 'bold'))
    heading_label.place(x=70, y=10)

    text_frame = tk.LabelFrame(frame1, bg=dark_bg, bd=0, width=200, height=100)
    text_frame.place(x=100, y=110)
    text_frame.pack_propagate(False)

    time_label = tk.Label(text_frame, 
                          text="0.00", 
                          bg=dark_bg, 
                          fg="white", 
                          font=("ds-digital", 60))
    time_label.pack(pady=5)

    str_button = tk.Button(frame1, 
                         text="Start", 
                         bg=dark_bg, 
                         activebackground="black", 
                         fg="white", 
                         activeforeground=act_fg,
                         font=("TkMenuFont", 14),
                         cursor="hand2",
                         borderwidth=0,
                         width=8,
                         command=start)
    str_button.place(x=10, y=280)

    stp_button = tk.Button(frame1, 
                         text="Stop", 
                         bg=dark_bg, 
                         activebackground="black", 
                         fg="white", 
                         activeforeground=act_fg,
                         font=("TkMenuFont", 14),
                         cursor="hand2",
                         borderwidth=0,
                         width=8,
                         command=stop)
    stp_button.place(x=115, y=280)

    lst_button = tk.Button(frame1, 
                         text="New lap", 
                         bg=dark_bg, 
                         activebackground="black", 
                         fg="white", 
                         activeforeground=act_fg,
                         font=("TkMenuFont", 14),
                         cursor="hand2",
                         borderwidth=0,
                         width=8,
                         command=new_lap)
    lst_button.place(x=220, y=280)

    lst_button = tk.Button(frame1, 
                         text="List", 
                         bg=dark_bg, 
                         activebackground="black", 
                         fg="white", 
                         activeforeground=act_fg,
                         font=("TkMenuFont", 14),
                         cursor="hand2",
                         borderwidth=0,
                         width=5,
                         command=load_frame2)
    lst_button.place(x=325, y=280)

# lambda x=l_lst: laps_list(x)

frame1 = tk.Frame(root, height=350, width=400, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()

root.mainloop()