from __future__ import annotations
from abc import ABC, abstractmethod
from subject import Subject


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self) -> None:
        pass
