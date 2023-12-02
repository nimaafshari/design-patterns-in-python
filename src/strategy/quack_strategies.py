from behaviour_interfaces import QuackBehaviour


class Quack(QuackBehaviour):
    """
    Concrete implementation of Quack.
    """
    def quack(self) -> None:
        """
        Concrete implementation of the interface quack method.

        Parameters:
            self: The instance of the object.
        
        Returns:
            None
        """
        print("Quack!")


class Squeak(QuackBehaviour):
    """
    Concrete implementation of Squeak.
    """
    def quack(self) -> None:
        """
        Concrete implementation of the interface quack method.

        Parameters:
            self: The instance of the object.
        
        Returns:
            None
        """
        print("Squeak!")


class MuteQuack(QuackBehaviour):
    """
    Concrete implementation of MuteQuack.
    """
    def quack(self) -> None:
        """
        Concrete implementation of the interface quack method.

        Parameters:
            self: The instance of the object.
        
        Returns:
            None
        """
        print("<< Silence >>")


class FakeQuack(QuackBehaviour):
    """
    Concrete implementation of FakeQuack.
    """
    def quack(self) -> None:
        """
        Concrete implementation of the interface quack method.

        Parameters:
            self: The instance of the object.
        
        Returns:
            None
        """
        print("Qwak!")
