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
        return JSONResponse(status_code=400, content={"error": "Invalid count: must be at least 1"})
    quotient :int = amount//count   #商について
    remainder:int = amount % count  #余りについて
    perPerson: list[int] = [quotient] * count 
    perPerson[-1] += remainder
    return JSONResponse(status_code=200, content={"perPerson": perPerson})

@app.post("/api/v1/split", response_model=SplitResponse)
def split_text(request: SplitRequest):
    response = perPerson_calculator(request.count,request.amount)  
    return response