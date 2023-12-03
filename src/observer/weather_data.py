from __future__ import annotations
from typing import List, Dict

from subject import Subject
from observer_interface import Observer


class WeatherData(Subject):
    """
    The WeatherData class implements the Subject interface.
    """

    _state: Dict = {
        "temperature": None,
        "humidity": None,
        "pressure": None,
    }

    _observers: List[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        """
        The register_observer method adds an observer to the list of observers.

        Parameters:
            self: The instance of the object.
            observer: The observer to be added.
        """
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """
        The remove_observer method removes an observer from the list of observers.

        Parameters:
            self: The instance of the object.
            observer: The observer to be removed.
        """
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        The notify_observers method notifies all observers of an update.

        Parameters:
            self: The instance of the object.
        """
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self) -> Dict:
        """
        The getter method of the state property.
        """
        return self._state

    @state.setter
    def state(self, state: Dict) -> None:
        """
        The setter method of the state property.
        """
        self._state = state
        self.notify_observers()
