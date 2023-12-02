from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    """ Interface for the Fly behaviour. """
    @abstractmethod
    def fly(self) -> None:
        """ 
        Abstract method for the fly behaviour.
        
        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        pass


class QuackBehaviour(ABC):
    """ Interface for the Quack behaviour. """
    @abstractmethod
    def quack(self) -> None:
        """ 
        Abstract method for the quack behaviour. 
        
        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        pass
