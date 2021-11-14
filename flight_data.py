
class FlightData:
    def __init__(self, cls):
        self.data = cls.return_flights()

    def return_price(self):
        price = self.data[0]["price"]
        return price

    def return_depart_date(self):
        depart_time = self.data[0]["route"][0]["local_departure"]
        depart_time = depart_time.split("T")
        return depart_time[0]

    def return_arrival_date(self):
        arrival_time = self.data[0]["route"][1]["local_departure"]
        arrival_time = arrival_time.split("T")
        return arrival_time[0]
