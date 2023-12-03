from __future__ import annotations
from abc import ABC, abstractmethod
from subject import Subject


class Observer(ABC):
    """Interface for the Observer."""

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Abstract method for the update behaviour.

        Parameters:
            self: The instance of the object.
            subject: The subject that is being observed.
        """
        pass
