import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from aircraft import *
from flight import *
from airline import *

aircrafts = []
flights = []


# ---------- AIRCRAFT FUNCTIONS ----------
def ShowAircrafts():
    listAircrafts.delete(0, tk.END)
    i = 0
    while i < len(aircrafts):
        a = aircrafts[i]
        listAircrafts.insert(tk.END, a.callsign + " " + a.type + " " + str(a.capacity))
        i = i + 1



# ---------- FLIGHT FUNCTIONS ----------
def ShowFlights():
    listFlights.delete(0, tk.END)
    i = 0
    while i < len(flights):
        f = flights[i]
        text = f.id + " " + f.departure_airport + " " + f.arrival_airport
        text = text + " " + f.departure_time + " " + f.arrival_time
        text = text + " " + str(f.passengers)
        listFlights.insert(tk.END, text)
        i = i + 1

def LoadA():
    loaded = LoadAircrafts("Aircrafts.txt")
    i = 0
    while i < len(loaded):
        AddAircraft(aircrafts, loaded[i])
        i = i + 1
    ShowAircrafts()


def AddA():
    parts = entryA.get().split()
    if len(parts) == 3:
        AddAircraft(aircrafts, Aircraft(parts[0], parts[1], int(parts[2])))
    ShowAircrafts()


def RemoveA():
    RemoveAircraft(aircrafts, entryA.get())
    ShowAircrafts()


def SaveA():
    SaveAircrafts(aircrafts, "aircrafts_saved.txt")

def LoadF():
    loaded = LoadFlights("Flights.txt")
    i = 0
    while i < len(loaded):
        AddFlight(flights, loaded[i])
        i = i + 1
    ShowFlights()


def AddF():
    p = entryF.get().split()              # "A99 LEBL LEMD 10:30 11:45 150"
    if len(p) == 6:
        AddFlight(flights, Flight(p[0], p[1], p[2], p[3], p[4], int(p[5])))
    ShowFlights()


def RemoveF():
    RemoveFlight(flights, entryF.get())
    ShowFlights()


def SaveF():
    SaveFlights(flights, "flights_saved.txt")


def Plot():
    airline = Airline("Vueling", aircrafts, flights)
    PlotFlights(airline)


# ---------- WINDOW ----------
window = tk.Tk()
window.title("Airline")

tk.Label(window, text="AIRCRAFTS").pack()
listAircrafts = tk.Listbox(window, width=50)
listAircrafts.pack()
tk.Label(window, text="Add: callsign type capacity.  Remove: callsign").pack()
entryA = tk.Entry(window, width=50)
entryA.pack()
tk.Button(window, text="Load aircrafts", command=LoadA).pack()
tk.Button(window, text="Add aircraft", command=AddA).pack()
tk.Button(window, text="Remove aircraft", command=RemoveA).pack()
tk.Button(window, text="Save aircrafts", command=SaveA).pack()

tk.Label(window, text="FLIGHTS").pack()
listFlights = tk.Listbox(window, width=50)
listFlights.pack()
tk.Label(window, text="Add: id from to departure arrival passengers.  Remove: id").pack()
entryF = tk.Entry(window, width=50)
entryF.pack()
tk.Button(window, text="Load flights", command=LoadF).pack()
tk.Button(window, text="Add flight", command=AddF).pack()
tk.Button(window, text="Remove flight", command=RemoveF).pack()
tk.Button(window, text="Save flights", command=SaveF).pack()

tk.Button(window, text="Plot flights per hour", command=Plot).pack()

window.mainloop()