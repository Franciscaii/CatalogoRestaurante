from django.shortcuts import render

# Definimos los productos en una lista
productos = [
    {
        "id": 1,
        "nombre": "Hamburguesa",
        "precio": 8.499,
        "descripcion": """Una hamburguesa jugosa y sabrosa, hecha con carne de res de primera calidad, 
        perfectamente asada a la parrilla para lograr un exterior ligeramente crujiente y un interior tierno 
        y jugoso. Se sirve en un pan suave y esponjoso, ligeramente tostado, que equilibra a la perfección cada 
        bocado. Esta delicia está acompañada de queso derretido, fresco y cremoso, que se funde sobre la carne, 
        junto a una generosa porción de lechuga crujiente, tomate fresco y rodajas de cebolla morada que aportan 
        un toque de frescura y textura. Para rematar, una combinación de salsas especiales, 
        ligeramente dulces y picantes, intensifican los sabores y brindan una explosión de gusto en cada mordida.""",
        "stock": 20,
        "imagen": "img/comida1.jpg"
    },
    {
        "id": 2,
        "nombre": "Tacos mexicanos",
        "precio": 16.999,
        "descripcion": """Auténticos tacos mexicanos hechos con tortillas de maíz recién hechas, calientes y suaves, 
        que envuelven un relleno de carne jugosa, ya sea carne asada, al pastor, carnitas o pollo marinado. 
        La carne, cocinada a la perfección, está condimentada con especias tradicionales que le aportan un sabor 
        profundo y lleno de autenticidad. Se acompañan con cebolla picada y cilantro fresco, que le dan un toque 
        de frescura y equilibrio a cada bocado. Unas gotas de limón realzan el sabor, mientras que una variedad de 
        salsas —desde la suave y cremosa hasta la picante y ardiente— permiten ajustar el nivel de picor al gusto. 
        Estos tacos son una explosión de sabores y texturas, y una auténtica delicia de la gastronomía mexicana """,
        "stock": 15,
        "imagen": "img/comida2.jpg"
    },
]

# Vista para listar los productos
def listar_productos(request):
    return render(request, 'listarproductos.html', {'productos': productos})

# Vista para ver el detalle de un producto
def ver_detalle(request, producto_id):
    # Buscamos el producto en la lista por su id
    producto = next((p for p in productos if p["id"] == producto_id), None)
    return render(request, 'verdetalle.html', {'producto': producto})