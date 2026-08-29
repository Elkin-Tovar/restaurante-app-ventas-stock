class Producto:
    """
    Clase base que representa un producto del restaurante con su respectivo stock.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.stock = stock

    def mostrar_informacion(self) -> str:
        """
        Retorna la información detallada del producto.
        """
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def vender(self, cantidad: int) -> None:
        """
        Disminuye el stock del producto según la cantidad vendida.
        """
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")
        self.stock -= cantidad

    def a_diccionario(self) -> dict:
        """
        Convierte el objeto Producto en un diccionario para su almacenamiento en JSON.
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }