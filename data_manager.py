#     #This class is responsible for talking to the Google Sheet.
import requests


class DataManager:
    def __init__(self):
        self.price_list = requests.get(url="https://api.sheety.co/b9b0db9f88960288df01fbbdd6125b4e/flights/prices")
        self.prices_count = len(self.price_list.json()["prices"])

    def get_city(self, num: int):
        city = self.price_list.json()["prices"][num]["city"]
        return city

    def get_cut_off(self, num: int):
        cut_off = self.price_list.json()["prices"][num]["lowestPrice"]
        return cut_off

    def put_code(self, iata, num: int):
        parameters = {
            "price": {
                "iataCode": iata
            }
        }
        codes = requests.put(url=f"https://api.sheety.co/b9b0db9f88960288df01fbbdd6125b4e/flights/prices/{num}", json=parameters)
        codes.raise_for_status()

    def update_users_name(self, fname, lname, email):
        new_data = {
          "user": {
              "firstName": fname,
              "lastName": lname,
              "email": email
          }
        }
        response = requests.post(
                          url="https://api.sheety.co/b9b0db9f88960288df01fbbdd6125b4e/flights/users",
                          json=new_data
                    )
        print(response.json())