import tkinter as tk
import pyautogui
import threading
import time

# Flag to control the loop
running = False

# Function to start the loop of left click and scroll
def start_auto_click_scroll():
    global running
    running = True
    auto_click_scroll()

# Function to stop the loop
def stop_auto_click_scroll():
    global running
    running = False

# Function to perform left click and scroll in a loop
def auto_click_scroll():
    if running:
        pyautogui.click()         # Perform left click
        time.sleep(0.5)           # Pause to register the click
        pyautogui.scroll(-75)    # Scroll down a small amount
        time.sleep(0.5)           # Pause between actions
        # Repeat the function in a separate thread to keep GUI responsive
        threading.Thread(target=auto_click_scroll).start()

# Create the main application window
root = tk.Tk()
root.title("Auto Click and Scroll System")
root.geometry("300x200")

# Button to start the auto click and scroll loop
start_button = tk.Button(root, text="Start Auto Click & Scroll", command=start_auto_click_scroll)
start_button.pack(pady=10)

# Button to stop the auto click and scroll loop
stop_button = tk.Button(root, text="Stop", command=stop_auto_click_scroll)
stop_button.pack(pady=10)

# Run the main event loop
root.mainloop()

