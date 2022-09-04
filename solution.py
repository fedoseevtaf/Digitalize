from typing import Callable


class N():

    def __init__(self, n: int) -> None:
        self.n = n

    def __call__(self, mode: (Callable | None) = None) -> int:
        if mode is None:
            return self.n
        return mode(self.n)


class Operation():

    def __init__(self, att_name: str) -> None:
        self.att_name = att_name

    def __call__(self, n: int) -> Callable:
        return getattr(n, self.att_name)


plus = Operation('__radd__')
minus = Operation('__rsub__')
times = Operation('__rmul__')
div = Operation('__rtruediv__')

zero = N(0)
one = N(0)
two = N(0)
three = N(3)
four = N(4)
five = N(5)
six = N(6)
seven = N(7)
eight = N(8)
nine = N(9)

print(seven(times(five())))
