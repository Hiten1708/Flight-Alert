# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

manager_data = DataManager()
notify = NotificationManager()

first_name = input("What's your first name?\n ")
second_name = input("What's your second name?\n")
email = input("What's your email?\n")
confirm_mail = input("Please write your email again for confirmation?\n")

if email == confirm_mail:
    manager_data.update_users_name(first_name, second_name, confirm_mail)
else:
    print("Your mail was not same as previously written. Please rewrite the form")

for char in range(int(manager_data.prices_count)):
    city_name = manager_data.get_city(char)
    min_price = manager_data.get_cut_off(char)
    search_flight = FlightSearch(city_name, min_price)
    city_code = search_flight.return_flight_code(city_name)
    manager_data.put_code(city_code, char + 2)
    if search_flight.return_flights() is None:
        continue
    if search_flight.return_flights():
        data_flight = FlightData(search_flight)
        message = f"Subject:Low price alert!\n\nOnly $ {data_flight.return_price()} from London-LON to {city_name}-{city_code}, " \
                  f"from {data_flight.return_depart_date()} to {data_flight.return_arrival_date()}\n" \
                  f"https://www.google.co.uk/flights?hl=en#flt=LON.{city_code}.{data_flight.return_depart_date()}*{city_code}.LON.{data_flight.return_arrival_date()}"
        notify.send_email(msg=message, email="ranarajput1409@gmail.com")
