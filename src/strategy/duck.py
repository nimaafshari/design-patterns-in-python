from __future__ import annotations
from abc import ABC, abstractmethod

from behaviour_interfaces import FlyBehaviour, QuackBehaviour


class Duck(ABC):
    """
    Superclass for the Ducks. Provides the common functionality for the ducks with proper abstract and concrete methods, and interfaces. 
    """
    def __init__(
        self, fly_behaviour: FlyBehaviour, quack_behaviour: QuackBehaviour
    ) -> None:
        """
        Initializes the object with the provided fly behaviour and quack behaviour.
        The behaviours are added to the abstract class to avoid duplicating the setter, getter on each concrete class

        Parameters:
            self: The instance of the object being initialized.
            fly_behaviour (FlyBehaviour): The fly behaviour for the object.
            quack_behaviour (QuackBehaviour): The quack behaviour for the object.

        Returns:
            None
        """
        self._fly_behaviour = fly_behaviour
        self._quack_behaviour = quack_behaviour

    @property
    def fly_behaviour(self) -> FlyBehaviour:
        """
        Returns the fly behaviour of the object.

        Parameters:
            self: The instance of the object.

        Returns:
            FlyBehaviour: The fly behaviour of the object.
        """
        return self._fly_behaviour

    @fly_behaviour.setter
    def fly_behaviour(self, fly_behaviour: FlyBehaviour) -> None:
        """
        Sets the fly behaviour of the object.

        Parameters:
            self: The instance of the object.
            fly_behaviour (FlyBehaviour): The fly behaviour to set.

        Returns:
            None
        """
        self._fly_behaviour = fly_behaviour

    @property
    def quack_behaviour(self) -> QuackBehaviour:
        """
        Returns the quack behaviour of the object.

        Parameters:
            self: The instance of the object.

        Returns:
            QuackBehaviour: The quack behaviour of the object.
        """
        return self._quack_behaviour

    @quack_behaviour.setter
    def quack_behaviour(self, quack_behaviour: QuackBehaviour) -> None:
        """
        Sets the quack behaviour of the object.

        Parameters:
            self: The instance of the object.
            quack_behaviour (QuackBehaviour): The quack behaviour to set.

        Returns:
            None
        """
        self._quack_behaviour = quack_behaviour

    @abstractmethod
    def display(self) -> None:
        """
        Abstract method for displaying the object.

        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        pass

    def perform_fly(self) -> None:
        """
        Performs the fly behaviour of the object from the FlyBehaviour interface.

        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        self._fly_behaviour.fly()

    def perform_quack(self) -> None:
        """
        Performs the quack behaviour of the object from the QuackBehaviour interface.

        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        self._quack_behaviour.quack()

    def swim(self) -> None:
        """
        Implements the swim behaviour of the object which is common between all the Ducks.

        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        print("All ducks float, even decoy!")
