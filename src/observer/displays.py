from __future__ import annotations
from typing import Dict

from display_interface import DisplayElement
from observer_interface import Observer
from weather_data import WeatherData
from subject import Subject


class CurrentConditionsDisplay(Observer, DisplayElement):
    """The CurrentConditionsDisplay class implements the DisplayElement and Observer interface."""

    def __init__(self, weather_data: WeatherData) -> None:
        """
        The constructor for the CurrentConditionsDisplay class.

        Parameters:
            self: The instance of the object.
            weather_data: The weather data subject to be observed.
        """
        self._state: Dict = None
        weather_data.register_observer(self)

    def update(self, subject: Subject) -> None:
        """
        The update method is called when the weather data changes.

        Parameters:
            self: The instance of the object.
            subject: The weather data subject.
        """
        self._state = subject._state
        self.display()

    def display(self):
        """
        The display method prints the current conditions.

        Parameters:
            self: The instance of the object.
        """
        print(
            f"""Current condition: {self._state["temperature"]}F degrees and 
            {self._state["humidity"]}% humidity"""
        )


class ForecastDisplay(Observer, DisplayElement):
    """
    The ForecastDisplay class implements the DisplayElement and Observer interface.
    """

    def __init__(self, weather_data: WeatherData) -> None:
        """
        The constructor for the ForecastDisplay class.

        Parameters:
            self: The instance of the object.
            weather_data: The weather data subject to be observed.
        """
        weather_data.register_observer(self)
        self._current_pressure: float = 29.92
        self._last_pressure: float = None

    def update(self, subject: Subject) -> None:
        """
        The update method is called when the weather data changes.

        Parameters:
            self: The instance of the object.
            subject: The weather data subject.
        """
        self._last_pressure = self._current_pressure
        self._current_pressure = subject._state["pressure"]

        self.display()

    def display(self):
        """
        The display method prints the forecast.

        Parameters:
            self: The instance of the object.
        """
        print(
            f"""Forecast:
            {'Improving weather on the way' if self._current_pressure > self._last_pressure else
             'More of the same' if self._current_pressure == self._last_pressure else
             'Watch out for cooler, rainy weather'}
            """
        )


class StatisticsDisplay(Observer, DisplayElement):
    """
    The StatisticsDisplay class implements the DisplayElement and Observer interface.
    """

    def __init__(self, weather_data: WeatherData) -> None:
        """
        The constructor for the StatisticsDisplay class.

        Parameters:
            self: The instance of the object.
            weather_data: The weather data subject to be observed.
        """
        weather_data.register_observer(self)
        self._max_temp: int = 0
        self._min_temp: int = 200
        self._temp_sum: int = 0
        self._num_readings: int = 0

    def update(self, subject: Subject) -> None:
        """
        The update method is called when the weather data changes.

        Parameters:
            self: The instance of the object.
            subject: The weather data subject.
        """
        temp = subject._state["temperature"]
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        """
        The display method prints the statistics.

        Parameters:
            self: The instance of the object.
        """
        print(
            f"""Avg/Max/Min temperature = 
            {(self._temp_sum/self._num_readings)}/{self._max_temp}/{self._min_temp}
            """
        )
