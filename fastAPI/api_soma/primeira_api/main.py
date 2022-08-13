from typing import Union, Optional
from fastapi import FastAPI, Header
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    quantidade: int
    valor: float
    
app = FastAPI()

banco= []

@app.post("/item") 
def add_item(novo_item: Item): 
    banco.append(novo_item)
    return novo_item

@app.get("/item")
def read_item():
	return banco

@app.get("/item/valor_total")
def get_valor_total(): 
	valor_total = 0.0
	for item in banco:
		valor_total+=item.valor*item.quantidade
	return valor_total
