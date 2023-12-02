from behaviour_interfaces import FlyBehaviour


class FlyWithWings(FlyBehaviour):
    """
    Concrete implementation of FlyWithWings.
    """
    def fly(self) -> None:
        """
        Concrete implementation of the interface fly method.
        Parameters:
            self: The instance of the object.
        
        Returns:
            None
        """
        print("I'm flying with Wings!")


class FlyNoWay(FlyBehaviour):
    """
    Concrete implementation of FlyNoWay.
    """
    def fly(self) -> None:
        """
        Concrete implementation of the interface fly method.
        
        Parameters:
            self: The instance of the object.
        
        Returns:
            None
        """
        print("I can't fly!")


class FlyRocketPowered(FlyBehaviour):
    """
    Concrete implementation of FlyRocketPowered.
    """
    def fly(self) -> None:
        """
        Concrete implementation of the interface fly method.

        Parameters:
            self: The instance of the object.

        Returns:
            None
        """
        print("I'm flying with a Rocket!")
