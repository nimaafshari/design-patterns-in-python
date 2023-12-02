from __future__ import annotations
from abc import ABC, abstractmethod

from interfaces import FlyBehaviour, QuackBehaviour


class Duck(ABC):
    def __init__(
        self, fly_behaviour: FlyBehaviour, quack_behaviour: QuackBehaviour
    ) -> None:
        self._fly_behaviour = fly_behaviour
        self._quack_behaviour = quack_behaviour

    @property
    def fly_behaviour(self) -> FlyBehaviour:
        return self._fly_behaviour

    @fly_behaviour.setter
    def fly_behaviour(self, fly_behaviour: FlyBehaviour) -> None:
        self._fly_behaviour = fly_behaviour

    @property
    def quack_behaviour(self) -> QuackBehaviour:
        return self._quack_behaviour

    @quack_behaviour.setter
    def quack_behaviour(self, quack_behaviour: QuackBehaviour) -> None:
        self._quack_behaviour = quack_behaviour

    @abstractmethod
    def display(self) -> None:
        pass

    def perform_fly(self) -> None:
        self._fly_behaviour.fly()

    def perform_quack(self) -> None:
        self._quack_behaviour.quack()

    def swim(self) -> None:
        print("All ducks float, even decoy!")
