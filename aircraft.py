

class Aircraft:
    def __init__(self, callsign, type, capacity):
        self.callsign = callsign
        self.type = type
        self.capacity = capacity


def PrintAircraft(aircraft):
    print(aircraft.callsign)
    print(aircraft.type)
    print(aircraft.capacity)

def LoadAircrafts(filename):
    aircrafts = []
    try:
        file = open(filename, "r")
    except:
        return aircrafts
    lines = file.readlines()
    file.close()

    i = 0
    while i < len(lines):
        parts = lines[i].split()
        if len(parts) == 3:
            try:
                capacity = int(parts[2])
                aircrafts.append(Aircraft(parts[0], parts[1], capacity))
            except:
                print("Line ignored:", lines[i])
        i = i + 1
    return aircrafts

def SaveAircrafts(aircrafts, filename):
        file = open(filename, "w")
        i = 0
        while i < len(aircrafts):
            a = aircrafts[i]
            file.write(a.callsign + " " + a.type + " " + str(a.capacity) + "\n")
            i = i + 1
        file.close()

def PrintAircrafts(aircrafts):
        i = 0
        while i < len(aircrafts):
            PrintAircraft(aircrafts[i])
            i = i + 1

def AddAircraft(aircrafts, aircraft):
        aircrafts.append(aircraft)

def RemoveAircraft(aircrafts, callsign):
        i = 0
        while i < len(aircrafts):
            if aircrafts[i].callsign == callsign:
                aircrafts.remove(aircrafts[i])
                return 0
            i = i + 1
        return -1

if __name__ == "__main__":
    aircraft = Aircraft("AAAA", "A220-100", 135)
    PrintAircraft(aircraft)
    aircrafts = LoadAircrafts("Aircrafts.txt")
    PrintAircrafts(aircrafts)
    AddAircraft(aircrafts, Aircraft("CCCC", "B737", 189))
    print(RemoveAircraft(aircrafts, "CCCC"))  # 0
    print(RemoveAircraft(aircrafts, "ZZZZ"))  # -1
    SaveAircrafts(aircrafts, "aircrafts_saved.txt")