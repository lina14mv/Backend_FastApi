from datetime import datetime
from uuid import uuid4 as uuid

productos = [
    {
        "id": str(uuid()),
        "name": "Laptop",
        "precio": "1200.00",
        "stock": "15 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Smartphone",
        "precio": "800.00",
        "stock": "30 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Teclado Mecánico",
        "precio": "150.00",
        "stock": "50 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Mouse Gamer",
        "precio": "75.00",
        "stock": "40 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Monitor 4K",
        "precio": "400.00",
        "stock": "20 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Impresora",
        "precio": "250.00",
        "stock": "10 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Tablet",
        "precio": "300.00",
        "stock": "25 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Auriculares Bluetooth",
        "precio": "100.00",
        "stock": "60 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Cámara Digital",
        "precio": "500.00",
        "stock": "8 unidades",
        "created_at": datetime.now(),
    },
    {
        "id": str(uuid()),
        "name": "Disco Duro Externo",
        "precio": "120.00",
        "stock": "35 unidades",
        "created_at": datetime.now(),
    },
]