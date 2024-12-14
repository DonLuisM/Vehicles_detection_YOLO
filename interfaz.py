import tkinter
import tkinter.messagebox
from tkinter import font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import model_function as main

#* Function to activate real-time detection
def start_real_time_detect():
    main.start_real_time_detect()
    
#* Function to perform file detection (MP4, JPEG, JPG, etc.)
def detection_archives():
    main.detection_archives()

"""BASE CODE FOR WINDOW"""
height = 500
weight = 300

######## MAIN WINDOW CODE #########  
ventana = Tk()                # Creates an instance of the Tk class for the main window
ventana.title("Vehicle Detection")   # Sets the title of the main window
ventana.geometry(f"{height}x{weight}")     # Sets the initial dimensions of the window

# FONT CONFIGURATION FOR TEXT IN THE INTERFACE USING TK FONT
Helvfont1 = font.Font(family="ITALIC", size=12, weight="bold")      # Configures the Helvfont1 font with type, size, and bold style
Helvfont2 = font.Font(family="KACSTART", size=10,  weight="bold")    # Configures the Helvfont2 font with type, size, and bold style
Helvfont3 = font.Font(family="Helvetica", size=10, weight="bold")   # Configures the Helvfont3 font with type, size, and bold style

x = (height/5)
y = weight/16

# MAIN TEXTS OF THE INTERFACE
TextTitle = Label(text="Real-Time Vehicle Detection", font=Helvfont1).place(x=x, y=y) # Creates a Label widget on tab 0 with a title text in the window
TextTitle2 = Label(text="(Cars, Buses, Trucks, Helicopters, and Boats)", font=Helvfont2).place(x=x-7, y=y+25)

## BASIC MODE, INFORMATION ON PARAMETERS TO BE ENTERED BY THE USER
# In the following lines of code: 
# A Label widget is created on tab 0 (initial tab) with specific texts (interface titles and contents) and positioned at a specific location
Division1 = Label(text="______________________________________________", font=Helvfont3).place(x=0, y=y+50) # Creates a Label widget with "separation" text and positions it in the window
TextParametros = Label(text="(Modes: Video or Upload File):", font=Helvfont3).place(x=20, y=y+82)  # Creates a Label widget with parameter text and positions it in the window
Division2 = Label(text="______________________________________________", font=Helvfont3).place(x=0, y=y+100) # Creates a Label widget with "separation" text and positions it in the window


# BUTTONS TO START THE SIMULATION (SIMULATION COMMAND) OR STOP IT (STOP COMMAND)
# Creates two buttons on the initial tab, with their texts "START" and "STOP" with a specific command and positions them at a specific location
Boton00 = Button(text="UPLOAD FILE \n FOR DETECTION", height=7, width=20, anchor="center", cursor='X_cursor', command=detection_archives, bg='green', fg='white').place(x=70, y=y+140) # The "START" button activates the "Simulated_ECG" command when pressed
Boton01 = Button(text="ACTIVATE \n REAL-TIME \n RECORDING", height=7, width=20, anchor="center", cursor='X_cursor', command=start_real_time_detect, bg='green', fg='white').place(x=270, y=y+140)  # The "STOP" button activates the "Stop" command when pressed

# ACTIVATE WINDOW 
ventana.mainloop()  # Starts the main loop of the graphical user interface
