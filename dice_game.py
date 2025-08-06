import tkinter as tk
import random

# Dice faces
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅",
}

roll_history = []

def update_history(roll):
    roll_history.append(roll)
    if len(roll_history) > 5:
        roll_history.pop(0)
    history_label.config(
        text="Last Rolls: " + " ".join(dice_faces[r] for r in roll_history),
        fg="#7c4dff"
    )

def clear_history():
    roll_history.clear()
    history_label.config(text="Last Rolls:", fg="#7c4dff")

def animate_dice(rolls=10, delay=80):
    if rolls > 0:
        dice_label.config(text=dice_faces[random.randint(1, 6)])
        root.after(delay, animate_dice, rolls - 1, delay)
    else:
        final_roll = random.randint(1, 6)
        dice_label.config(text=dice_faces[final_roll])
        update_history(final_roll)

def roll_dice():
    animate_dice(10, 80)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Let's Roll Some Dice!")
root.configure(bg="#fff8e1")
root.geometry("600x700")

# Add this line to bind the spacebar to rolling the dice
root.bind("<space>", lambda event: roll_dice())

# Title label
title_label = tk.Label(
    root,
    text="🎲 Let's Roll! 🎲",
    font=("Segoe Print", 20, "bold"),
    bg="#fff8e1",
    fg="#7c4dff"
)
title_label.pack(pady=(20, 5))

# Subtitle label
subtitle_label = tk.Label(
    root,
    text="Feeling lucky?",
    font=("Segoe Print", 12, "italic"),
    bg="#fff8e1",
    fg="#ff7043"
)
subtitle_label.pack(pady=(0, 10))

# Display the dice
dice_label = tk.Label(
    root,
    text="⚀",
    font=("Segoe Print", 80, "bold"),
    bg="#fff8e1",
    fg="#ffd600"
)
dice_label.pack(pady=10)

# Button to roll the dice
roll_button = tk.Button(
    root,
    text="Roll Dice!",
    font=("Segoe Print", 16, "bold"),
    bg="#aed581",
    fg="#4e342e",
    activebackground="#81c784",
    activeforeground="#fff",
    bd=0,
    relief="ridge",
    padx=20,
    pady=5,
    highlightthickness=0,
    command=roll_dice
)
roll_button.pack(pady=10)

# Roll history label
history_label = tk.Label(
    root,
    text="Last Rolls:",
    font=("Segoe Print", 12, "bold"),
    bg="#fff8e1",
    fg="#7c4dff"
)
history_label.pack(pady=5)

# Clear history button
clear_button = tk.Button(
    root,
    text="Clear History",
    font=("Segoe Print", 10, "bold"),
    bg="#ffcc80",
    fg="#4e342e",
    activebackground="#ffb74d",
    activeforeground="#fff",
    bd=0,
    relief="ridge",
    padx=10,
    pady=2,
    highlightthickness=0,
    command=clear_history
)
clear_button.pack(pady=5)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Segoe Print", 10, "bold"),
    bg="#ef9a9a",
    fg="#fff",
    activebackground="#e57373",
    activeforeground="#fff",
    bd=0,
    relief="ridge",
    padx=10,
    pady=2,
    highlightthickness=0,
    command=exit_app
)
exit_button.pack(pady=10)

root.mainloop()

