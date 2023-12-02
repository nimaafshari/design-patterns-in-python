from abstract_classes import Duck
from fly_strategies import FlyWithWings, FlyNoWay, FlyRocketPowered
from quack_strategies import Quack, Squeak, MuteQuack


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behaviour=FlyWithWings(), quack_behaviour=Quack())

    def display(self) -> None:
        print("I'm a real Mallard Duck!")


class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behaviour=FlyNoWay(), quack_behaviour=Quack())

    def display(self) -> None:
        print("I'm a Model Duck!")


class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behaviour=FlyNoWay(), quack_behaviour=Squeak())

    def display(self) -> None:
        print("I'm a Rubber Duckie!")


class ReadHeadDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behaviour=FlyWithWings(), quack_behaviour=Quack())

    def display(self) -> None:
        print("I'm a Red Headed Duck!")


class DecoyDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behaviour=FlyNoWay(), quack_behaviour=MuteQuack())

    def display(self) -> None:
        print("I'm a Duck Decoy!")


if __name__ == "__main__":
    mallard_duck = MallardDuck()
    rubber_duck = RubberDuck()
    decoy_duck = DecoyDuck()
    model_duck = ModelDuck()

    mallard_duck.perform_fly()
    rubber_duck.perform_quack()
    decoy_duck.perform_fly()

    model_duck.perform_fly()
    model_duck.fly_behaviour = FlyRocketPowered()
    model_duck.perform_fly()
