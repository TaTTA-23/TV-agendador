import tkinter as tk
import tkinter
top = tkinter.Tk()
from tkinter import messagebox

def handle_reservation():
    person = entry_person.get()
    day = entry_day.get()
    hour = entry_hour.get()
    reservation_system.make_reservation(day, hour, person)
    messagebox.showinfo("Reservation", "Reservation successful!")
# Create an instance of the reservation system
reservation_system = ReservationSystem()

# Create the GUI window
window = tk.Tk()

# Create input fields and labels
label_person = tk.Label(window, text="Person:")
entry_person = tk.Entry(window)

label_day = tk.Label(window, text="Day:")
entry_day = tk.Entry(window)

label_hour = tk.Label(window, text="Hour:")
entry_hour = tk.Entry(window)

# Create the reservation button
reservation_button = tk.Button(window, text="Make Reservation", command=handle_reservation)

# Grid layout for the elements
label_person.grid(row=0, column=0)
entry_person.grid(row=0, column=1)
label_day.grid(row=1, column=0)
entry_day.grid(row=1, column=1)
label_hour.grid(row=2, column=0)
entry_hour.grid(row=2, column=1)
reservation_button.grid(row=3, columnspan=2)

# Start the GUI event loop
window.mainloop()
