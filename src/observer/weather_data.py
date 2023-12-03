from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict

from subject import Subject
from interfaces import Observer


class WeatherData(Subject):
    _state: Dict = {
        "temperature": None,
        "humidity": None,
        "pressure": None,
    }

    _observers: List[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state: Dict) -> None:
        self._state = state
        self.notify_observers()
