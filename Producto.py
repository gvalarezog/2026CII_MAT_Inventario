

class Producto:

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

if __name__ == "__main__":
    producto1 = Producto('A001', 'Arroz 2 Kg', 2.10, 50)
    producto2 = Producto('L010', 'Leche 1 L', 0.95, 40)

