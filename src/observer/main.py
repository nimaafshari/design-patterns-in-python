from weather_data import WeatherData
from displays import CurrentConditionsDisplay, ForecastDisplay, StatisticsDisplay


if __name__ == "__main__":
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    test_state_1 = {
        "temperature": 80,
        "humidity": 67,
        "pressure": 30.4,
    }
    weather_data.state = test_state_1

    test_state_2 = {
        "temperature": 82,
        "humidity": 70,
        "pressure": 29.2,
    }
    weather_data.state = test_state_2

    test_state_3 = {
        "temperature": 78,
        "humidity": 90,
        "pressure": 29.2,
    }
    weather_data.state = test_state_3

    weather_data.remove_observer(forecast_display)

    test_state_4 = {
        "temperature": 62,
        "humidity": 90,
        "pressure": 28.1,
    }
    weather_data.state = test_state_4
