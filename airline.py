import matplotlib.pyplot as plt

class Airline:
    def __init__(self, name, fleet, operations):
        self.name = name
        self.fleet = fleet
        self.operations = operations


def PrintAirline(airline):
    print(airline.name)
    print(airline.fleet)
    print(airline.operations)




def PlotFlights(airline):
    hours = []
    counts = []
    h = 0
    while h < 24:
        hours.append(h)
        counts.append(0)  # at the start, 0 flights in every hour
        h = h + 1

    i = 0
    while i < len(airline.operations):
        flight = airline.operations[i]
        departure = TimeToMinutes(flight.departure_time)
        arrival = TimeToMinutes(flight.arrival_time)

        h = 0
        while h < 24:
            # the flight is on air in hour h if it takes off before the hour ends
            # and lands after the hour starts
            if departure < (h + 1) * 60 and arrival > h * 60:
                counts[h] = counts[h] + 1
            h = h + 1
        i = i + 1

    plt.bar(hours, counts)
    plt.xticks(hours)
    plt.xlabel("Hour")
    plt.ylabel("Flights on air")
    plt.title("Flights on air in every hour")
    plt.show()

# test section
if __name__ == "__main__":
    from aircraft import *
    from flight import *

    aircrafts = []
    aircrafts.append(Aircraft("AAAA", "A220-100", 135))
    aircrafts.append(Aircraft("BBBB", "A230-100", 200))

    flights = []
    flights.append(Flight("A11", "LEBL", "EGLL", "12:30", "14:30", 135))
    flights.append(Flight("A12", "EGLL", "LEBL", "16:30", "18:30", 135))

    airline = Airline("Vueling", aircrafts, flights)
    PrintAirline(airline)



