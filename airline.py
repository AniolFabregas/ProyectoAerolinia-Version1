import matplotlib.pyplot as plt
from aircraft import *
from flight import *

class Airline:
    def __init__(self, name, fleet, operations):
        self.name = name
        self.fleet = fleet
        self.operations = operations


def PrintAirline(airline):
    print("Airline:", airline.name)
    print("Fleet:")
    PrintAircrafts(airline.fleet)
    print("Operations:")
    PrintFlights(airline.operations)




def PlotFlights(airline):
    hours = []
    counts = []
    h = 0
    while h < 24:
        hours.append(h)
        counts.append(0)
        h = h + 1

    i = 0
    while i < len(airline.operations):
        flight = airline.operations[i]  # aquesta línia és la que falta
        departure = TimeToMinutes(flight.DepartureTime)
        arrival = departure + FlightDuration(flight)

        h = 0
        while h < 24:
            if departure < (h + 1) * 60 and arrival > h * 60:
                counts[h] = counts[h] + 1
            if arrival > 1440 and arrival - 1440 > h * 60:
                counts[h] = counts[h] + 1
            h = h + 1
        i = i + 1

    plt.bar(hours, counts)
    plt.xlabel("Hour")
    plt.ylabel("Flights on air")
    plt.title("Flights on air in every hour")
    plt.show()

# test section
if __name__ == "__main__":

    aircrafts = []
    aircrafts.append(Aircraft("AAAA", "A220-100", 135))
    aircrafts.append(Aircraft("BBBB", "A230-100", 200))

    flights = []
    flights.append(Flight("A11", "LEBL", "EGLL", "12:30", "14:30", 135))
    flights.append(Flight("A12", "EGLL", "LEBL", "16:30", "18:30", 135))

    airline = Airline("Vueling", aircrafts, flights)
    PrintAirline(airline)
    aircrafts = LoadAircrafts("Aircrafts.txt")
    flights = LoadFlights("operations.txt")
    airline = Airline("Vueling", aircrafts, flights)
    PrintAirline(airline)
    PlotFlights(airline)


