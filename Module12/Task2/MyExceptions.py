class MyException(Exception):
    def __str__(self):
        return self.__class__.__name__


class KillError(MyException):
    pass


class DrunkError(MyException):
    pass


class CarCrashError(MyException):
    pass


class GluttonyError(MyException):
    pass


class DepressionError(MyException):
    pass
