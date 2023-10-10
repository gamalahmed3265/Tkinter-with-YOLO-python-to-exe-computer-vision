
import tkinter as tk
from tkinter.ttk import *
import cv2
from PIL import Image, ImageTk
import pandas as pd
# from ultralytics import YOLO
# import cvzone
import threading










# Create the main Tkinter window
root = tk.Tk()
root.title("YOLO v8 My App")

# Create a Canvas widget to display the webcam feed or video
canvas = tk.Canvas(root, width=1020, height=500)
canvas.pack(fill='both', expand=True)

class_list = read_classes_from_file('coco.txt')

class_selection = tk.StringVar()
class_selection.set("All")  # Default selection is "All"
class_selection_label = tk.Label(root, text="Select Class:")
class_selection_label.pack(side='left')
class_selection_entry = tk.OptionMenu(root, class_selection, "All", *class_list)  # Populate dropdown with classes from the text file
class_selection_entry.pack(side='left')

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill='x')

# Create a "Play" button to start the webcam feed
# play_button = tk.Button(button_frame, text="Play", command=start_webcam)
# play_button.pack(side='left')

# Create a "Stop" button to stop the webcam feed
# stop_button = tk.Button(button_frame, text="Stop", command=stop_webcam)
# stop_button.pack(side='left')

# Create a "Select File" button to choose a video file
# file_button = tk.Button(button_frame, text="Select File", command=select_file)
# file_button.pack(side='left')

# Create a "Pause/Resume" button to pause or resume video
# pause_button = tk.Button(button_frame, text="Pause/Resume", command=pause_resume_video)
# pause_button.pack(side='left')

# Create a "Quit" button to close the application
# quit_button = tk.Button(button_frame, text="Quit", command=quit_app)
# quit_button.pack(side='left')

# Display an initial image on the canvas (replace 'initial_image.jpg' with your image)
# initial_image = Image.open('yolo.jpg')  # Replace 'initial_image.jpg' with your image path
# initial_photo = ImageTk.PhotoImage(image=initial_image)
# canvas.img = initial_photo
# canvas.create_image(0, 0, anchor=tk.NW, image=initial_photo)

# Start the Tkinter main loop
root.mainloop()