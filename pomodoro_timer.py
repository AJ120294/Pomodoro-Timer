import tkinter as tk  # Import the tkinter library for GUI
from tkinter import ttk  # Import the ttk module for themed widgets
from PIL import Image, ImageTk  # Import Image and ImageTk from the PIL library for image handling
import time  # Import time library (not directly used in this code, but can be helpful for time-related functions)

# Constants for the Pomodoro Timer
WORK_MIN = 25  # Duration for work session in minutes
SHORT_BREAK_MIN = 5  # Duration for short break in minutes
LONG_BREAK_MIN = 15  # Duration for long break in minutes
FONT_NAME = "Courier"  # Font used for the timer display
CHECK_MARK = "✔"  # Check mark symbol for completed work sessions

# Global variables to track the number of repetitions and the timer object
reps = 0  # Number of repetitions completed
timer = None  # Timer variable for controlling countdown

# Initialize the main GUI window
root = tk.Tk()  # Create the main application window
root.title("Pomodoro Timer")  # Set the title of the window
root.config(padx=100, pady=50, bg="#f7f5dd")  # Configure the window padding and background color

# Load the tomato image for the timer display
img = Image.open("/Users/amanjain/Desktop/Practice Python Projects/Pomodoro/tomato.png")  # Open the tomato image file
img = img.resize((200, 200))  # Resize the image to fit the canvas
tomato_img = ImageTk.PhotoImage(img)  # Convert the image to PhotoImage for tkinter compatibility

# Countdown function to handle the timer countdown
def countdown(count):
    global reps  # Access the global reps variable
    minutes = count // 60  # Calculate minutes from the count
    seconds = count % 60  # Calculate seconds from the count
    if seconds < 10:  # Add leading zero if seconds are less than 10
        seconds = f"0{seconds}"
    
    # Update the timer text displayed in the center of the tomato image
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count > 0:  # If there's time left in the countdown
        global timer  # Access the global timer variable
        timer = root.after(1000, countdown, count - 1)  # Call countdown again after 1 second with reduced count
    else:
        # When the countdown reaches zero, start the next timer session
        start_timer()
        # Display check marks for completed work cycles
        marks = ""  # Initialize an empty string for check marks
        work_sessions = reps // 2  # Calculate the number of work sessions completed
        for _ in range(work_sessions):  # Loop through each completed work session
            marks += CHECK_MARK  # Add a check mark for each completed work session
        check_mark_label.config(text=marks)  # Update the check mark label

# Timer mechanism to determine the type of session and start the countdown
def start_timer():
    global reps  # Access the global reps variable
    reps += 1  # Increment the repetition count

    # Determine if it's time for work, short break, or long break
    if reps == 3:  # On the third repetition, take a long break
        label.config(text="Long Break", fg="#e7305b")  # Update label text and color for long break
        countdown(LONG_BREAK_MIN * 60)  # Start the countdown for long break
    elif reps % 2 == 0:  # Every 2nd repetition is a short break
        label.config(text="Short Break", fg="#e2979c")  # Update label text and color for short break
        countdown(SHORT_BREAK_MIN * 60)  # Start the countdown for short break
    else:  # All other repetitions are work sessions
        label.config(text="Work", fg="#9bdeac")  # Update label text and color for work session
        countdown(WORK_MIN * 60)  # Start the countdown for work session

    # Disable the start button to prevent multiple timers from running simultaneously
    start_button.config(state=tk.DISABLED)

# Reset the timer to its initial state
def reset_timer():
    root.after_cancel(timer)  # Stop the current timer if it's running
    global reps  # Access the global reps variable
    reps = 0  # Reset the repetition count to 0
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer display to 00:00
    label.config(text="Timer")  # Reset the label text to "Timer"
    check_mark_label.config(text="")  # Clear the check mark label
    
    # Re-enable the start button after resetting
    start_button.config(state=tk.NORMAL)

# UI Setup
label = tk.Label(root, text="Timer", font=(FONT_NAME, 35, "bold"), fg="#9bdeac", bg="#f7f5dd")  # Create a label for the timer
label.grid(column=1, row=0)  # Place the label in the grid layout

canvas = tk.Canvas(root, width=200, height=224, bg="#f7f5dd", highlightthickness=0)  # Create a canvas for the tomato image and timer text
canvas.create_image(100, 112, image=tomato_img)  # Add the tomato image to the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Create text for the timer display
canvas.grid(column=1, row=1)  # Place the canvas in the grid layout

# Check mark label to display completed work cycles
check_mark_label = tk.Label(root, fg="#9bdeac", bg="#f7f5dd", font=(FONT_NAME, 20, "bold"))  # Create a label for check marks
check_mark_label.grid(column=1, row=3)  # Place the check mark label in the grid layout

# Start button to initiate the timer
start_button = tk.Button(root, text="Start", highlightthickness=0, command=start_timer)  # Create a button for starting the timer
start_button.grid(column=0, row=2)  # Place the start button in the grid layout

# Reset button to stop and reset the timer
reset_button = tk.Button(root, text="Reset", highlightthickness=0, command=reset_timer)  # Create a button for resetting the timer
reset_button.grid(column=2, row=2)  # Place the reset button in the grid layout

# Start the Tkinter event loop to keep the GUI running
root.mainloop()  # Enter the main event loop to run the application