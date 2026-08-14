from fastapi import FastAPI
from pydantic import BaseModel 


app = FastAPI(
    title = "tienda dev senior",
    description="Api1",
    version ="1.0.0"
)


class ProductoCreate(BaseModel):
    nombre:str
    precio:float
    stock:int

producto_db=[]


@app.get("/saludo")
def obtener_saludo():
    return{
        "mensaje": "hola",
        "estado": "activo"
    }
