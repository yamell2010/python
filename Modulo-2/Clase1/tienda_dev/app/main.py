from fastapi import FastAPI
from pydantic import BaseModel

# Crear la aplicación FastAPI
# Los parámetros son metadata para la documentación automática
app = FastAPI(
    title="Tienda Dev Senior",
    description="API Backend profesional - Dev Senior Code",
    version="1.0.0"
)

class ProductoCreate(BaseModel):
    nombre:str
    precio:float
    stock:int

producto_db = []

@app.get("/saludo")
def obtener_saludo():
    return {
        "mensaje": "¡Hola desde FastAPI!",
        "estado": "activo"
    }

@app.get("/")
def raiz():
    return {
        "mensaje": "Bienvenido a Tienda Dev Senior",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "aplicacion": "Tienda Dev Senior"
    }

@app.post("/productos")
def crear_producto(producto: ProductoCreate):
    producto_db.append(producto)
    return{
        "mensaje": "Producto creado exitosamente",
        "producto": producto
    }

@app.get("/productos")
def listar_productos():
    return{
        "total": len(producto_db),
        "productos": producto_db,
        "mensaje" : "esos son todos los productos"
    }