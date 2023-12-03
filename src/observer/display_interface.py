from __future__ import annotations
from abc import ABC, abstractmethod


class DisplayElement(ABC):
    """Interface for the DisplayElement."""

    @abstractmethod
    def display(self) -> None:
        """
        Abstract method for the display behaviour.

        Parameters:
            self: The instance of the object.
        """
        pass
