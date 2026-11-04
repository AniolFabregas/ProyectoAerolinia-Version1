
class Flight:
    def __init__(self, id, DepartureAirport, ArrivalAirport, DepartureTime, ArrivalTime, passengers):
        self.id = id
        self.DepartureAirport = DepartureAirport
        self.ArrivalAirport = ArrivalAirport
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.passengers = passengers

def PrintFlight(Flight):
    print(Flight.id)
    print(Flight.DepartureAirport)
    print(Flight.ArrivalAirport)
    print(Flight.DepartureTime)
    print(Flight.ArrivalTime)
    print(Flight.passengers)

def TimeToMinutes(time):
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours * 60 + minutes

def FlightDuration(flight):
    duration = TimeToMinutes(flight.ArrivalTime - flight.DepartureTime)
    return duration

def LoadFlights(filename):
    flights = []
    try:
        file = open(filename, "r")
    except:
        return flights

    lines = file.readlines()
    file.close()

    i = 1                       # skip the header line
    while i < len(lines):
        parts = lines[i].split()
        if len(parts) == 6:
            flight = Flight(parts[0], parts[1], parts[2], parts[3], parts[4], int(parts[5]))
            flights.append(flight)
        i = i + 1
    return flights


def SaveFlights(flights, filename):
    file = open(filename, "w")
    i = 0
    while i < len(flights):
        f = flights[i]
        line = f.id + " " + f.departure_airport + " " + f.arrival_airport
        line = line + " " + f.departure_time + " " + f.arrival_time
        line = line + " " + str(f.passengers) + "\n"
        file.write(line)
        i = i + 1
    file.close()


def PrintFlights(flights):
    i = 0
    while i < len(flights):
        PrintFlight(flights[i])
        i = i + 1


def AddFlight(flights, flight):
    flights.append(flight)


def RemoveFlight(flights, id):
    i = 0
    while i < len(flights):
        if flights[i].id == id:
            flights.remove(flights[i])
            return 0
        i = i + 1
    return -1


# test section
if __name__ == "__main__":
    flight = Flight("A11", "LEBL", "EGLL", "12:30", "14:30", 135)
    PrintFlight(flight)
    print(FlightDuration(flight))

if __name__ == "__main__":
    flights = LoadFlights("Flights.txt")  # use the real name of your file
    PrintFlights(flights)
    AddFlight(flights, Flight("A99", "LEBL", "LEMD", "10:30", "11:45", 150))
    print(RemoveFlight(flights, "A99"))  # 0
    print(RemoveFlight(flights, "ZZZ"))  # -1
    SaveFlights(flights, "flights_saved.txt")