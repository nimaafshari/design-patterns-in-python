from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    """Interface for the Subject."""

    @abstractmethod
    def register_observer(self) -> None:
        """
        Abstract method for the registration of observers.

        Parameters:
            self: The instance of the object.
        """
        pass

    @abstractmethod
    def remove_observer(self) -> None:
        """
        Abstract method for the removal of observers.

        Parameters:
            self: The instance of the object.
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Abstract method for the notification of observers.

        Parameters:
            self: The instance of the object.
        """
        pass
