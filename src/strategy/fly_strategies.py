from interfaces import FlyBehaviour


class FlyWithWings(FlyBehaviour):
    def fly(self) -> None:
        print("I'm flying with Wings!")


class FlyNoWay(FlyBehaviour):
    def fly(self) -> None:
        print("I can't fly!")


class FlyRocketPowered(FlyBehaviour):
    def fly(self) -> None:
        print("I'm flying with a Rocket!")
