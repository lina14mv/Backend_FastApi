from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid
from data import productos

app = FastAPI(
    title="CRUD con FastApi",
    description='Crud completo realizado con FastApi y Pydantic \n\n'
                'Realizado por: \n\n'
                'Diego Fernando Moreno - 2159838 \n\n' 
                'Lina Maria Muñoz - 2159849',
    contact={
        "name": "Diego Fernando Moreno - 2159838",
        "name": "Lina Maria Muñoz - 2159849",
    },
)

#Productos Model
class Productos(BaseModel):
    id: Optional[str] = None
    name: str
    precio: str
    stock: Text
    created_at: datetime = datetime.now()

@app.get('/')
def read_root():
    return {
        "Bienvenido": "A nuestro backend con FastAPI"
                      "Realizado por:"
                      "Diego Fernando Moreno - 2159838"
                      "Lina Maria Muñoz - 2159849"
                      "Prueba nuestro CRUD en:"
    }

@app.get('/productos')
def get_productos():
    return productos

@app.post('/productos')
def save_productos(producto: Productos): 
    producto.id = str(uuid())
    productos.append(producto.dict()) 
    if len(productos) > 0:
        return productos[-1]
    else:
        return productos[0]

@app.get('/productos/{producto_id}')
def get_producto(producto_id: str):
    for producto in productos:
        if producto['id'] == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete('/productos/{producto_id}')
def delete_producto(producto_id: str):
    for index, producto in enumerate(productos):
        if producto["id"] == producto_id:
            productos.pop(index)
            return {"message": "Producto eliminado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.put('/put/{producto_id}')
def update_producto(producto_id: str, updateProducto: Productos):
    for index, producto in enumerate(productos):
        if producto["id"] == producto_id:
            productos[index]["name"] = updateProducto.name
            productos[index]["precio"] = updateProducto.precio
            productos[index]["stock"] = updateProducto.stock
            return {"message": "Producto actualizado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")


