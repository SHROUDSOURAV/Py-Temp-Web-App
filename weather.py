from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# loading the .env file
load_dotenv()


# code file to send request to the open weather app to fetch city weather details


def getWeather(city="Kolkata"):
    #the request url sent to open weather app
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #storing the received data of the city weather which was given as input
    weather_data = requests.get(request_url).json()

    #returning the weather data
    return weather_data

# main method
# when this code is imported
# this main part is skipped
# if the python file run directly then the code excutes the main block(eg: python filename.py)
# otherwise skips
if __name__ == "__main__":
    print("\n*** Get weather Conditions***\n")
    city = input("Enter the city name :\n")

    weather_data = getWeather(city)
    pprint(weather_data)





