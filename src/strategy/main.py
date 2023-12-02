from ducks import MallardDuck, RubberDuck, DecoyDuck, ModelDuck
from fly_strategies import FlyWithWings, FlyNoWay, FlyRocketPowered

if __name__ == "__main__":
    mallard_duck = MallardDuck()
    rubber_duck = RubberDuck()
    decoy_duck = DecoyDuck()
    model_duck = ModelDuck()

    mallard_duck.perform_fly()
    rubber_duck.perform_quack()
    decoy_duck.perform_fly()

    model_duck.perform_fly()
    ## Changing the fly behaviour of the model duck at runtime
    model_duck.fly_behaviour = FlyRocketPowered()
    model_duck.perform_fly()
