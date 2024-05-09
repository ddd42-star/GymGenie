import tkinter as tk
from PIL import ImageTk, Image #You need to install Pillow
import tkcalendar #Installing is needed
from tkinter import messagebox
import datetime
import workout
import random


#color palette
black = "BLACK"
white = "WHITE"
dark_red = "#9B2226"
red = "#AE2012"
brown = "#BB3E03"
orange = "#CA6702"
yellow = "#EE9B00"
dark_blue = "#005F73"
blue = "#357F93"
light_blue = "#5d99a9"


root = tk.Tk()
root.geometry("500x400")


#####
#Other functions (need to be on top)
def select_date(date, calendar, date_window):
    """
    Updates the provided Tkinter variable with the selected date from a calendar widget.

    Parameters
    ----------
    date : tkinter.StringVar
        The Tkinter variable to be updated with the selected date.

    calendar : tkcalendar.Calendar
        The calendar widget used for selecting the date.

    date_window : tkinter.Toplevel
        The window containing the calendar widget.
    """
    selected_date = calendar.selection_get()
    date.set(selected_date)
    date_window.destroy()

def open_calendar(root, date):
    """
    Opens a new window where you can choose a date and updates the provided date variable with the 
    chosen date.

    Parameters
    ----------
    root : tkinter.Tk or tkinter.Toplevel
        The root or top-level window where the calendar window will be opened.

    date : tkinter.StringVar
        A tkinter StringVar variable that stores the selected date.
    """


    date_window = tk.Toplevel(root)
    date_window.title("Pick a Date")

    calendar = tkcalendar.Calendar(date_window)
    calendar.pack(padx=10, pady=10)

    confirm_button = tk.Button(date_window, text="Confirm", command=lambda: select_date(date, calendar, date_window))
    confirm_button.pack(pady=10)



def display_set_goal():
    """
    Displays the start page of setting the goal. 
    The user can choose between 3 types of objectives that appears as buttons:
        Distance
        Duration
        Calories burned
    After clicking each button a new page is displayed.
    
    """
    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)


    #Create goal label
    goal_label = tk.Label(main_frame, text="Set your goal based on:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)

    goal_label.grid(column=0, row=0)

    #Create goal buttons based on the type of objective
    GOALS_TYPES = ['Distance', 'Duration', 'Calories burned']
    commands = [display_distance, display_duration, display_calories]
    for i, goal_type in enumerate(GOALS_TYPES):
        btn = tk.Button( main_frame, 
            command= commands[i],
            text = goal_type, 
            font =("Arial", 12, "bold"),
            background=white,
            foreground=dark_blue,
            activebackground=light_blue,
            activeforeground=white,
            width=20,
            height=2, 
            border=0,
            cursor="hand2",
            borderwidth=1, #Add border width
            relief="solid") #Add relief style 

        btn.grid(column=0, row=1+i) 





def display_duration():

    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Configure columns and rows
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.columnconfigure(4, weight=1)
    main_frame.columnconfigure(5, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

    #create duration label
    duration_label = tk.Label(main_frame, text="Duration:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    duration_label.grid(column=0, row=0)

    #create hours and minutes entry
    e_hours = tk.Entry(main_frame)
    e_hours.insert(tk.END, "h")
    e_min = tk.Entry(main_frame)
    e_min.insert(tk.END, "min")
    e_hours.grid(column=1, row=0)
    e_min.grid(column=2, row=0)

    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)


def display_distance():
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Configure columns and rows
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.columnconfigure(4, weight=1)
    main_frame.columnconfigure(5, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

    #create distance label
    distance_label = tk.Label(main_frame, text="Distance:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    distance_label.grid(column=0, row=0)

    #create km, m, miles  entries
    e_km = tk.Entry(main_frame)
    e_km.insert(tk.END, "km")
    e_m = tk.Entry(main_frame)
    e_m.insert(tk.END, "m")
    e_miles = tk.Entry(main_frame)
    e_miles.insert(tk.END, "miles")
    e_km.grid(column=1, row=0)
    e_m.grid(column=2, row=0)
    e_miles.grid(column=3, row=0)

    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)


def display_calories():

    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Configure columns and rows
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.columnconfigure(4, weight=1)
    main_frame.columnconfigure(5, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

    #create duration label
    calories_label = tk.Label(main_frame, text="Calories burned:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    calories_label.grid(column=0, row=0)

    #create kcal and kJ entries
    e_kcal = tk.Entry(main_frame)
    e_kcal.insert(tk.END, "kcal")
    e_kJ = tk.Entry(main_frame)
    e_kJ.insert(tk.END, "kJ")
    e_kcal.grid(column=1, row=0)
    e_kJ.grid(column=2, row=0)

    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)



def display_timeframe(main_frame, col , row):
    """
    Displays the timeframe label and its entries to set the start and end to fix the goal dates.

    Args:
        main_frame : frame where to be displayed.
        col (int) : column number of the grid of the actual frame.
        row (int) : row number of the grid of the actual frame.
    
    """
    #create timeframe, start and end label
    timeframe_label = tk.Label(main_frame, text="Timeframe:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    
    start_button = tk.Button(main_frame, text="Start date",
                    font =("Arial", 12, "bold"),
                    background=white,
                    foreground=black,
                    width=20,
                    height = 1,
                    command=lambda: open_calendar(root, start_date))
    
    end_button = tk.Button(main_frame, text="End date",
                font =("Arial", 12, "bold"),
                background=white,
                foreground=black,
                width=20,
                height = 1,
                command=lambda: open_calendar(root, end_date))

    #Create start date 
    start_date = tk.StringVar()
    start_date.set(datetime.date.today()) # Set the date initial date to todays date.
    start_date_label = tk.Label(main_frame,
                font =("Arial", 12, "bold"),
                background=blue,
                foreground=white,
                width=20,
                height = 1, 
                textvariable=start_date)
    
    #Create end date 
    end_date = tk.StringVar()
    end_date.set(datetime.date.today()) # Set the date initial date to todays date.
    end_date_label = tk.Label(main_frame,
                font =("Arial", 12, "bold"),
                background=blue,
                foreground=white,
                width=20,
                height = 1, 
                textvariable=end_date)
    
    #Configure columns and rows and display widgets
    timeframe_label.grid(column=col, row=row)
    start_button.grid(column=col+1, row=row)
    start_date_label.grid(column=col+2, row=row)
    end_button.grid(column=col+3, row=row)
    end_date_label.grid(column=col+4, row=row)

def display_exercise_type(main_frame):
    #Create label
    timeframe_label = tk.Label(main_frame, 
                        text="Type of workout:",
                        font =("Arial", 16, "bold"),
                        background=blue,
                        foreground=white,
                        width=20,
                        height = 1)
    timeframe_label.grid(column=0 , row = 3)

    # Create list containing the names of all the workout types of class Workout.
    workout_types = [subclass.__name__ for subclass in workout.Workout.__subclasses__()]

    # Variable to keep track of the option 
    # selected in OptionMenu 
    value_inside = tk.StringVar(main_frame) 

    # Set the default value of the variable 
    value_inside.set("Select") 

    # Create the optionmenu widget and passing the workout_types and value_inside to it. 
    question_menu = tk.OptionMenu(main_frame, value_inside, *workout_types, ) 
    question_menu.grid(column = 1, row = 3) 



#Maybe do a button and from button pop up a message?

def display_smarttips(main_frame, col = 3, row = 3):
    """
    Displays the SMART tips button and the pop up message.

    Args:
        main_frame : frame where to be displayed.
        col (int) : column number of the grid of the actual frame.
        row (int) : row number of the grid of the actual frame.
    
    """
    #Create button
    tip_button = tk.Button(main_frame, text="SMART TIP", command=popup_smarttips,
                           width= 15, height=10,
                            activebackground=yellow, 
                            activeforeground="white",
                            anchor="center",
                            bd=3,
                            bg='turquoise1',
                            cursor="hand2",
                            disabledforeground=light_blue,
                            fg="black",
                            font=("Tahoma", 12, "bold"),
                            highlightbackground="black",
                            highlightcolor="green",
                            highlightthickness=2,
                            justify="center",
                            overrelief="raised")
    tip_button.grid(column=col, row=row)



def popup_smarttips():
    """
    It creates a message box that contains a SMART tip randomly selected between a list of different statements.
    
    """
    TIPS = ["S - Specific: What will you achieve? ",
            "M - Measurable: What data will you use to decide whether you have met your goal?",
            "A - Achievable: Do you have the right skills to achieve this?",
            "A - Achievable: Are you sure you can do it?",
            "A - Achievable: Don't set goals where achieving lies in someone else’s power, it should be entirely down to you.",
            "R - Relevant: Does the goal align with those of your team or organization?",
            "T - Time bound: What is the deadline for accomplishing the goal?What is the deadline for accomplishing the goal?"]
    tk.messagebox.showinfo("BE SMART !", random.choice(TIPS))
    
    
    



#run it
display_set_goal()

# Create and display exit button
button_quit = tk.Button(root, text = "Exit", command=root.quit)
button_quit.pack()
root.mainloop()






#NOTES FOR ME
#Fix entries in distance and calories, create button to select the unit
#Exit button for all the pages


#Add picture


#In the second page, add options for the type of exercise.

# my_img = ImageTk.PhotoImage(Image.open(""))
# my_img.pack()