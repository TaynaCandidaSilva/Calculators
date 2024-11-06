import numpy
from typing import List
from .interfaces.driver_handler_inteface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
