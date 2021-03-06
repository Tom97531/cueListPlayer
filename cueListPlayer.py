import tkinter as tk
import time

import cues

def inSeconds(input_str):
    return int(input_str[5:7]) + int(input_str[2:4]) * 60 + int(input_str[:1]) * 3600

def Refresher():
    global current_cue

    current_time = time.time()
    next_cue_time = inSeconds(cues.cues[current_cue][0])

    # switch to red 10s before
    if current_time - start_time > next_cue_time - 10:
        next.configure(bg="red")

    if current_time - start_time > next_cue_time:
        current.configure(text=f"{cues.cues[current_cue][0]} {cues.cues[current_cue][1]}")
        next.configure(text=f"{cues.cues[current_cue+1][0]} {cues.cues[current_cue+1][1]}",
                        bg="white")
        next_2.configure(text=f"{cues.cues[current_cue+2][0]} {cues.cues[current_cue+2][1]}")
        next_3.configure(text=f"{cues.cues[current_cue+3][0]} {cues.cues[current_cue+3][1]}")
        current_cue = current_cue + 1

    root.after(1000, Refresher)

if __name__ == "__main__":
    root=tk.Tk()
    root.configure(background='black')

    start_time = time.time()
    current_cue = 0

    current = tk.Label(root,
        text=f"{cues.cues[current_cue][0]} {cues.cues[current_cue][1]}",
        font=("Helvetica", 100),
        background="yellow",
        width=100)
    current.pack()

    next = tk.Label(root,
            text=f"{cues.cues[current_cue+1][0]} {cues.cues[current_cue+1][1]}",
            font=("Helvetica", 100),
            background="white",
            width=100)
    next.pack()

    next_2 = tk.Label(root,
            text=f"{cues.cues[current_cue+2][0]} {cues.cues[current_cue+2][1]}",
            font=("Helvetica", 100),
            background="white",
            width=100)
    next_2.pack()

    next_3 = tk.Label(root,
            text=f"{cues.cues[current_cue+3][0]} {cues.cues[current_cue+3][1]}",
            font=("Helvetica", 100),
            background="white",
            width=100)
    next_3.pack()

    Refresher()
    root.mainloop()