# COMP1878 Coursework
#Task 1 - API Class

#import libraries
import json
import requests

#creating class for OpenWeatherMap Air Pollution:
class OpenWeatherAirPollution:
    #defining url for openweathermap.org
    url = "http://api.openweathermap.org/data/2.5/air_pollution"

#initialising reader/client with a valid API key from OpenWeatherMap.org:
# api_key= non-empty string contains the API key
#raises a value error if key is not a non-empty string
    def __init__(self, api_key):
        if not isinstance(api_key, str) or not api_key.strip():
            raise ValueError("api_key must be a non-empty string")
        self.api_key = api_key


#fetching the air pollution data for given locations from the API:
# lat= latitude, lon = longitude, returns a dictionary containing JSON response
    def get_air_pollution_data(self, lat, lon):
        complete_url = f"{self.url}?lat={lat}&lon={lon}&appid={self.api_key}"

        try:
            response = requests.get(complete_url, timeout=10)
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            print(f"Error {response.status_code}")
            return None

        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
            return None


#returning human readable description for the AQI integer value
# aqi=Ineger AQI value(1-5), returnd string with 'good' or 'poor' or 'unknown' if value not in range
    def get_aqi_description(self,  aqi):
        descriptions = {1: "Good", 2:"Fair", 3:"Moderate", 4:"Poor", 5:"Very Poor"}
        return descriptions.get(aqi, "Unknown")


if __name__ == "__main__":
    API_KEY = "c505f05a165be7de4240dafd319fbf62"

    api = OpenWeatherAirPollution(API_KEY)
    r = api.get_air_pollution_data(51.5, -0.1)

    if r is not None:
        print(json.dumps(r, indent=4))

        aqi_value = r["list"][0]["main"]["aqi"]
        print("AQI value:", aqi_value)
        print("AQI description:", api.get_aqi_description(aqi_value))
