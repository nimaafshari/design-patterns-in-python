from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from subject import Subject
from weather_data import WeatherData
from interfaces import Observer, DisplayElement


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self._state: Dict = None
        weather_data.register_observer(self)

    def update(self, subject: Subject) -> None:
        self._state = subject._state
        self.display()

    def display(self):
        print(
            f"""Current condition: {self._state["temperature"]}F degrees and 
            {self._state["humidity"]}% humidity"""
        )


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        weather_data.register_observer(self)
        self._current_pressure: float = 29.92
        self._last_pressure: float = None

    def update(self, subject: Subject) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = subject._state["pressure"]

        self.display()

    def display(self):
        print(
            f"""Forecast:
            {'Improving weather on the way' if self._current_pressure > self._last_pressure else
             'More of the same' if self._current_pressure == self._last_pressure else
             'Watch out for cooler, rainy weather'}
            """
        )


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        weather_data.register_observer(self)
        self._max_temp: int = 0
        self._min_temp: int = 200
        self._temp_sum: int = 0
        self._num_readings: int = 0

    def update(self, subject: Subject) -> None:
        temp = subject._state["temperature"]
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        print(
            f"""Avg/Max/Min temperature = 
            {(self._temp_sum/self._num_readings)}/{self._max_temp}/{self._min_temp}
            """
        )


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
