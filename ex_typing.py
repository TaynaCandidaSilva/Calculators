from typing import Dict


def add(elem1: int, elem2: float) -> dict:
    response = elem1 + elem2
    return {"sum": response}


val = add(5, 2.5)
print(val)
