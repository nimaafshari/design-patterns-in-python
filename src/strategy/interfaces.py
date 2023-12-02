from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self) -> None:
        pass
