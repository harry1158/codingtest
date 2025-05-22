from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import HTTPException
from typing import Union

app = FastAPI()


class SplitRequest(BaseModel):
    count    : int
    amount   : int
    delimiter: str


class SplitResponse(BaseModel):
    perPerson: Union[list[int],str]

def perPerson_calculator(count:int,amount:int):
    if count == 0:
        raise ValueError("Invalid count: must be at least 1")
    quotient = amount // count
    remainder = amount % count
    perPerson = [quotient] * count
    perPerson[-1] += remainder
    return perPerson


@app.post("/api/v1/split", response_model=SplitResponse)
def split_text(request: SplitRequest):
    try:
        per_person_list = perPerson_calculator(request.count, request.amount)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    return SplitResponse(perPerson=per_person_list)