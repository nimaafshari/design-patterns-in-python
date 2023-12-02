from interfaces import QuackBehaviour


class Quack(QuackBehaviour):
    def quack(self) -> None:
        print("Quack!")


class Squeak(QuackBehaviour):
    def quack(self) -> None:
        print("Squeak!")


class MuteQuack(QuackBehaviour):
    def quack(self) -> None:
        print("<< Silence >>")


class FakeQuack(QuackBehaviour):
    def quack(self) -> None:
        print("Qwak!")
