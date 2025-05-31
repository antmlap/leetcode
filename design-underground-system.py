class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # id → (stationName, time)
        self.travel_times = {}  # (startStation, endStation) → [totalTime, tripCount]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_ins.pop(id)
        trip = (startStation, stationName)
        duration = t - startTime
        if trip not in self.travel_times:
            self.travel_times[trip] = [0, 0]
        self.travel_times[trip][0] += duration  # total time
        self.travel_times[trip][1] += 1         # trip count

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.travel_times[(startStation, endStation)]
        return totalTime / count

