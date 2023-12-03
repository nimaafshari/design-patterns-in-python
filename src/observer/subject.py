from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self) -> None:
        pass

    @abstractmethod
    def remove_observer(self) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass
