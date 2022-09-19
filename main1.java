
from fastapi

import FastAPI

from enum
import Enum

app=FastAPI()

class Foods(str,Enum):indian="indian"american="american"chinese="chinese"

food_items={
    'indian':['samosa','dosa','idli','vada'],
    'american': ['burger','fries','pizza','hotdog'],
    'chinese': ['noodles','fried rice','spring rolls','chowmein']   
}

@app.get("/get_Item/{name}")
async def

    get_Item(name:Foods):
    return food_items.get(name)


coupan_code={
    1234: '10%',
    1111: '20%',
    1235: '30%',    
}


@app.get("/get_coupan/{code}")
async def get_coupan(code:int):
    return coupan_code.get(code)


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
