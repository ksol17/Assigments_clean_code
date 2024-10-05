from weather_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.parser = parser

    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        else:
            return self.parser.parse_weather_data(data)
