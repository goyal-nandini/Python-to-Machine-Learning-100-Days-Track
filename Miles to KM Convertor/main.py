from tkinter import *

MY_FONT = ("Ink Free", 18, "bold")
COLORS = {
    "bg": "#2c3e50",  
    "fg": "#ecf0f1",  
    "entry_bg": "#34495e",  
    "entry_fg": "#ecf0f1", 
    "button_bg": "#3498db", 
    "button_fg": "#ffffff",  
    "button_active": "#2980b9",  
    "result_bg": "#1abc9c",  
    "placeholder": "#95a5a6"  
}

def on_entry_click(event):
    """Function that gets called when entry is clicked"""
    if miles_input.get() == 'Enter miles here...':
        miles_input.delete(0, END)  # delete all the text in the entry
        miles_input.config(fg=COLORS["entry_fg"])  # change text color

def on_focusout(event):
    """Function that gets called when entry loses focus"""
    if miles_input.get() == '':
        miles_input.insert(0, 'Enter miles here...')
        miles_input.config(fg=COLORS["placeholder"])

def miles_to_km():
    value = miles_input.get()
    
    # Check if it's the placeholder text
    if value == 'Enter miles here...' or value.strip() == '':
        kilometer_result_label.config(text="0", bg="#e74c3c", fg="white")
        return
    
    try:
        miles = float(value)
        km = round(miles * 1.609, 2)
        kilometer_result_label.config(text=f"{km}", bg=COLORS["result_bg"], fg="white")
    except ValueError:
        kilometer_result_label.config(text="Invalid input", bg="#e74c3c", fg="white")

def on_button_hover(event):
    """Change button color on hover"""
    calculate_button.config(bg=COLORS["button_active"])

def on_button_leave(event):
    """Revert button color when not hovering"""
    calculate_button.config(bg=COLORS["button_bg"])

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=400, height=250)
window.config(padx=30, pady=30, bg=COLORS["bg"])

# Configure grid weights for better responsiveness
for i in range(3):
    window.grid_columnconfigure(i, weight=1)
for i in range(3):
    window.grid_rowconfigure(i, weight=1)

# Entry widget with placeholder
miles_input = Entry(
    width=20,
    font=MY_FONT,
    bg=COLORS["entry_bg"],
    fg=COLORS["placeholder"],
    borderwidth=3, # borderwidth: Thickness of border in pixels
    relief="ridge", # 3D raised border style -> relief: Border style  ("flat", "raised", "sunken", "ridge", "groove")
    justify="center"
)
miles_input.insert(0, 'Enter miles here...')
miles_input.grid(column=1, row=0, pady=10, sticky="ew")
# miles_input.grid(column=1, row=0, pady=10, sticky="ns")
# sticky="ew": Widget stretches East-West (left-right)
miles_input.bind('<FocusIn>', on_entry_click) # When entry gets focus (clicked)
miles_input.bind('<FocusOut>', on_focusout) # When entry loses focus
# bind(): Connects an event (like mouse click) to a function
# '<FocusIn>': Event when widget gets keyboard focus
# '<FocusOut>': Event when widget loses keyboard focus

miles_label = Label(
    text="Miles", 
    font=MY_FONT,
    bg=COLORS["bg"],
    fg=COLORS["fg"]
)
miles_label.grid(column=2, row=0, padx=10)

is_equal_label = Label(
    text="is equal to", 
    font=MY_FONT,
    bg=COLORS["bg"],
    fg=COLORS["fg"]
)
is_equal_label.grid(column=0, row=1, padx=10)

kilometer_result_label = Label(
    text="0", 
    font=("Ink Free", 20, "bold"),
    width=15,
    relief="sunken", # Looks pressed in
    bg=COLORS["result_bg"],
    fg="white",
    padx=10,
    pady=5
)
kilometer_result_label.grid(column=1, row=1, pady=15)

kilometer_label = Label(
    text="Km", 
    font=MY_FONT,
    bg=COLORS["bg"],
    fg=COLORS["fg"]
)
kilometer_label.grid(column=2, row=1, padx=10)

calculate_button = Button(
    text="Calculate", 
    font=MY_FONT,
    command=miles_to_km,
    bg=COLORS["button_bg"],
    fg=COLORS["button_fg"],
    activebackground=COLORS["button_active"], # Color when clicked
    activeforeground="white", # Text color when clicked
    relief="raised",
    borderwidth=3, # Border thickness
    padx=20, # Internal horizontal padding
    pady=10 # Internal vertical padding
)
calculate_button.grid(column=1, row=2, pady=20)
calculate_button.bind("<Enter>", on_button_hover) 
calculate_button.bind("<Leave>", on_button_leave)
# "<Enter>": Mouse enters the widget area
# "<Leave>": Mouse leaves the widget area

# Add keyboard binding for Enter key
window.bind('<Return>', lambda event: miles_to_km())
# '<Return>': Enter key pressed

window.mainloop()
