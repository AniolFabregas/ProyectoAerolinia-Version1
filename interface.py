from tkinter import *
from aircraft import *
from flight import *
from airline import *

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
    loaded = LoadAircrafts("Aircrafts.txt")
    i = 0
    while i < len(loaded):
        AddAircraft(aircrafts, loaded[i])
        i = i + 1
    ShowAircrafts()


def AddAClick():
    parts = aircraftEntry.get().split()
    if len(parts) == 3:
        aircraft = Aircraft(parts[0], parts[1], int(parts[2]))
        AddAircraft(aircrafts, aircraft)
    ShowAircrafts()


def RemoveAClick():
    RemoveAircraft(aircrafts, aircraftEntry.get())
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
    loaded = LoadFlights("operations.txt")
    i = 0
    while i < len(loaded):
        AddFlight(flights, loaded[i])
        i = i + 1
    ShowFlights()


def AddFClick():
    p = flightEntry.get().split()
    if len(p) == 6:
        flight = Flight(p[0], p[3], p[4], p[1], p[2], int(p[5]))
        AddFlight(flights, flight)
    ShowFlights()


def RemoveFClick():
    RemoveFlight(flights, flightEntry.get())
    ShowFlights()


def SaveFClick():
    SaveFlights(flights, "flights_saved.txt")



def PlotClick():
    airline = Airline("Vueling", aircrafts, flights)
    PlotFlights(airline)


# ---------- WINDOW ----------
window = Tk()
window.title("Airline")
window.geometry("800x600")
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