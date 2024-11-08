from typing import Dict
from flask import request as FlaskRequest
from src.drives.interfaces.driver_handler_inteface import DriverHandlerInterface


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calcalate(self, request: FlaskRequest) -> Dict:  # type: ignore
        pass
