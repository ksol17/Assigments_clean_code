from weather_fetcher import WeatherDataFetcher
from data_parser import DataParser
from user_interface import UserInterface

def main():
    fetcher = WeatherDataFetcher()  # Create instance of WeatherDataFetcher
    parser = DataParser()           # Create instance of DataParser
    ui = UserInterface(fetcher, parser)  # Create instance of UserInterface
    
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = ui.get_detailed_forecast(city)
        else:
            forecast = ui.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
