import requests
import dateutil
from dateutil.relativedelta import relativedelta
from datetime import datetime


class FlightSearch:
    def __init__(self, to_city, budget, from_city_code="LON"):
        self.KIWI_API = "XXSgtmDboIj5ko8DJnaoH_u2BIbeligW"
        self.KIWI_END = "http://tequila-api.kiwi.com/v2/search"
        self.KIWI_HEAD = {
            'apikey': self.KIWI_API
        }
        self.KIWI_QUERY = "https://tequila-api.kiwi.com/locations/query"
        self.today = datetime.now()
        self.delta = dateutil.relativedelta.relativedelta(months=6)
        self.six_months_later = self.today + self.delta
        self.today = self.today.strftime('%d/%m/%Y')
        self.six_months_later = self.six_months_later.strftime('%d/%m/%Y')
        self.kiwi_para = {
            "fly_from": from_city_code,
            "fly_to": self.return_flight_code(to_city),
            "date_from": self.today,
            "date_to": self.six_months_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "price_to": budget,
            "one_for_city": 1,
            "max_stopovers": 0,
            "sort": "price",
            "curr": "USD"
        }
        self.flights_response = requests.get(url=self.KIWI_END, params=self.kiwi_para, headers=self.KIWI_HEAD)
        self.flights_response.raise_for_status()

    def return_flights(self):
        if self.flights_response.json()["data"]:
            return self.flights_response.json()["data"]
        else:
            return None

    def return_flight_code(self, city):
        kiwi_para = {
            "term": f"{city}"
        }
        query_response = requests.get(url=self.KIWI_QUERY, params=kiwi_para, headers=self.KIWI_HEAD)
        to_city_code = query_response.json()["locations"][0]["code"]
        return to_city_code
