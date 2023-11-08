import pyautogui
import tkinter as tk


def update_coordinates_label():
    x, y = pyautogui.position()
    coordinates_label.config(text=f"X = {x}, Y = {y}")
    root.after(100, update_coordinates_label)  # Update every 100 milliseconds


root = tk.Tk()
root.title("Mouse Cursor Coordinates")

coordinates_label = tk.Label(root, text="X = 0, Y = 0")
coordinates_label.pack()

update_coordinates_label()

root.mainloop()
