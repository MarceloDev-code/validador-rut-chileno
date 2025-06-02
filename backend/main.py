from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class ValidationInput(BaseModel):
    rut: str

def validate_rut(rut: str) -> bool:
    rut = rut.upper().replace("-", "").replace(".", "")
    if not re.match(r'^\d{7,8}[0-9K]$', rut):
        return False

    body = rut[:-1]
    check_digit = rut[-1]
    suma = 0
    multiplo = 2

    for d in reversed(body):
        suma += int(d) * multiplo
        multiplo = 9 if multiplo == 7 else multiplo + 1

    expected = 11 - (suma % 11)
    if expected == 11:
        expected_digit = '0'
    elif expected == 10:
        expected_digit = 'K'
    else:
        expected_digit = str(expected)

    return check_digit == expected_digit

@app.post("/validate_rut/")
def validate(data: ValidationInput):
    result = validate_rut(data.rut)
    return {"valid": result}
