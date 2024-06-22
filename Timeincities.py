import pytz
from datetime import datetime

def get_time_in_city(city):
    
        timezones = pytz.all_timezones

        city_timezone = None
        for tz in timezones:
            if city.lower() in tz.lower():
                city_timezone = tz
                break

        if not city_timezone:
            return f"City '{city}' not found."

        
        city_time_zone = pytz.timezone(city_timezone)
        city_time = datetime.now(city_time_zone)

        
        formatted_time = city_time.strftime("%H:%M:%S")
        return f"The current time in {city} is {formatted_time}."

   
city = input("Enter the city name: ")
print(get_time_in_city(city))
