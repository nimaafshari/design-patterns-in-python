from duck import Duck
from fly_strategies import FlyWithWings, FlyNoWay, FlyRocketPowered
from quack_strategies import Quack, Squeak, MuteQuack

class MallardDuck(Duck):
    """
    Concrete implementation of MallardDuck. MallardDuck is a real-world duck.
    """
    def __init__(self) -> None:
        """
        Initializes the object with the proper fly behaviour and quack behaviour.

        Parameters:
            self: The instance of the object being initialized.

        Returns:
            None
        """
        super().__init__(fly_behaviour = FlyWithWings(), quack_behaviour = Quack())

    def display(self) -> None:
        """
        Concrete implementation of the interface display method.

        Parameters:
            self: The instance of the object being displayed.

        Returns:
            None
        """
        print("I'm a real Mallard Duck!")


class ModelDuck(Duck):
    """
    Concrete implementation of ModelDuck. ModelDuck is not a real-world duck.
    """
    def __init__(self) -> None:
        """
        Initializes the object with the proper fly behaviour and quack behaviour.

        Parameters:
            self: The instance of the object being initialized.

        Returns:
            None
        """
        super().__init__(fly_behaviour=FlyNoWay(), quack_behaviour=Quack())

    def display(self) -> None:
        """
        Concrete implementation of the interface display method.

        Parameters:
            self: The instance of the object being displayed.

        Returns:
            None
        """
        print("I'm a Model Duck!")


class RubberDuck(Duck):
    """
    Concrete implementation of RubberDuck. RubberDuck is not a real-world duck.
    """
    def __init__(self) -> None:
        """
        Initializes the object with the proper fly behaviour and quack behaviour.

        Parameters:
            self: The instance of the object being initialized.

        Returns:
            None
        """
        super().__init__(fly_behaviour=FlyNoWay(), quack_behaviour=Squeak())

    def display(self) -> None:
        """
        Concrete implementation of the interface display method.

        Parameters:
            self: The instance of the object being displayed.

        Returns:
            None
        """
        print("I'm a Rubber Duckie!")


class ReadHeadDuck(Duck):
    """
    Concrete implementation of ReadHeadDuck. ReadHeadDuck is a real-world duck.
    """
    def __init__(self) -> None:
        """
        Initializes the object with the proper fly behaviour and quack behaviour.

        Parameters:
            self: The instance of the object being initialized.

        Returns:
            None
        """
        super().__init__(fly_behaviour=FlyWithWings(), quack_behaviour=Quack())

    def display(self) -> None:
        """
        Concrete implementation of the interface display method.

        Parameters:
            self: The instance of the object being displayed.

        Returns:
            None
        """
        print("I'm a Red Headed Duck!")


class DecoyDuck(Duck):
    """
    Concrete implementation of DecoyDuck. DecoyDuck is not a real-world duck.
    """
    def __init__(self) -> None:
        """
        Initializes the object with the proper fly behaviour and quack behaviour.

        Parameters:
            self: The instance of the object being initialized.

        Returns:
            None
        """
        super().__init__(fly_behaviour=FlyNoWay(), quack_behaviour=MuteQuack())

    def display(self) -> None:
        """
        Concrete implementation of the interface display method.

        Parameters:
            self: The instance of the object being displayed.

        Returns:
            None
        """
        print("I'm a Duck Decoy!")
