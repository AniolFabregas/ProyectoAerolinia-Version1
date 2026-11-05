from tkinter import *
from aircraft import *
from flight import *
from airline import *
from tkinter import messagebox

aircrafts = []
flights = []


# ---------- AIRCRAFTS ----------
def ShowAircrafts():
    text = ""
    i = 0
    while i < len(aircrafts):
        text = text + aircrafts[i].callsign + " " + aircrafts[i].type + " " + str(aircrafts[i].capacity) + "\n"
        i = i + 1
    aircraftsLabel.config(text=text)


def LoadAClick():
    global aircrafts  # així no es dupliquen si carregues dues vegades
    aircrafts = LoadAircrafts("Aircrafts.txt")
    if len(aircrafts) == 0:
        messagebox.showerror("Error", "File not found or empty")
    ShowAircrafts()


def AddAClick():
    parts = aircraftEntry.get().split()
    if len(parts) != 3:
        messagebox.showerror("Error", "Format: callsign type capacity")
        return
    try:
        capacity = int(parts[2])
    except:
        messagebox.showerror("Error", "Capacity must be a number")
        return
    AddAircraft(aircrafts, Aircraft(parts[0], parts[1], capacity))
    ShowAircrafts()


def RemoveAClick():
    result = RemoveAircraft(aircrafts, aircraftEntry.get())
    if result == -1:
        messagebox.showerror("Error", "Callsign not found")
    ShowAircrafts()


def SaveAClick():
    SaveAircrafts(aircrafts, "aircrafts_saved.txt")


# ---------- FLIGHTS ----------
def ShowFlights():
    text = ""
    i = 0
    while i < len(flights):
        f = flights[i]
        text = text + f.id + " " + f.DepartureAirport + " " + f.ArrivalAirport + " "
        text = text + f.DepartureTime + " " + f.ArrivalTime + " " + str(f.passengers) + "\n"
        i = i + 1
    flightsLabel.config(text=text)


def LoadFClick():
    global flights
    flights = LoadFlights("operations.txt")
    if len(flights) == 0:
        messagebox.showerror("Error", "File not found or empty")
    ShowFlights()


def AddFClick():
    p = flightEntry.get().split()
    if len(p) != 6:
        messagebox.showerror("Error", "Format: id depTime arrTime depAirport arrAirport passengers")
        return
    try:
        passengers = int(p[5])
    except:
        messagebox.showerror("Error", "Passengers must be a number")
        return
    AddFlight(flights, Flight(p[0], p[3], p[4], p[1], p[2], passengers))
    ShowFlights()


def RemoveFClick():
    result = RemoveFlight(flights, flightEntry.get())
    if result == -1:
        messagebox.showerror("Error", "Flight ID not found")
    ShowFlights()


def SaveFClick():
    SaveFlights(flights, "flights_saved.txt")



def PlotClick():
    if len(flights) == 0:
        messagebox.showerror("Error", "Load the flights first")
        return
    airline = Airline("Vueling", aircrafts, flights)
    PlotFlights(airline)

# ---------- WINDOW ----------
window = Tk()
window.title("Airline")
window.geometry("900x800")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=6)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

titleLabel = Label(window, text="Airline", font=("Courier", 20, "italic"))
titleLabel.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=N + S + E + W)

# aircrafts part (left)
aircraftsTitle = Label(window, text="AIRCRAFTS")
aircraftsTitle.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

aircraftsLabel = Label(window, text="", bg="white", justify=LEFT)
aircraftsLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

aircraftEntry = Entry(window)
aircraftEntry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

LoadAButton = Button(window, text="Load", bg='green', fg="white", command=LoadAClick)
LoadAButton.grid(row=4, column=0, padx=5, pady=5, sticky=N + S + E + W)
AddAButton = Button(window, text="Add", bg='green', fg="white", command=AddAClick)
AddAButton.grid(row=4, column=1, padx=5, pady=5, sticky=N + S + E + W)
RemoveAButton = Button(window, text="Remove", bg='green', fg="white", command=RemoveAClick)
RemoveAButton.grid(row=5, column=0, padx=5, pady=5, sticky=N + S + E + W)
SaveAButton = Button(window, text="Save", bg='green', fg="white", command=SaveAClick)
SaveAButton.grid(row=5, column=1, padx=5, pady=5, sticky=N + S + E + W)


flightsTitle = Label(window, text="FLIGHTS")
flightsTitle.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

flightsLabel = Label(window, text="", bg="white", justify=LEFT)
flightsLabel.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

flightEntry = Entry(window)
flightEntry.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

LoadFButton = Button(window, text="Load", bg='green', fg="white", command=LoadFClick)
LoadFButton.grid(row=4, column=2, padx=5, pady=5, sticky=N + S + E + W)
AddFButton = Button(window, text="Add", bg='green', fg="white", command=AddFClick)
AddFButton.grid(row=4, column=3, padx=5, pady=5, sticky=N + S + E + W)
RemoveFButton = Button(window, text="Remove", bg='green', fg="white", command=RemoveFClick)
RemoveFButton.grid(row=5, column=2, padx=5, pady=5, sticky=N + S + E + W)
SaveFButton = Button(window, text="Save", bg='green', fg="white", command=SaveFClick)
SaveFButton.grid(row=5, column=3, padx=5, pady=5, sticky=N + S + E + W)


PlotButton = Button(window, text="Plot flights per hour", bg='grey', fg="black", command=PlotClick)
PlotButton.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky=N + S + E + W)

window.mainloop()