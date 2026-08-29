from typing import List, Set, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    """
    Clase encargada de administrar las colecciones, operaciones de negocio
    y persistencia del restaurante.
    """

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: List[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: List[Usuario] = self.archivo_servicio.cargar_usuarios()
        self.ventas: List[Venta] = self.archivo_servicio.cargar_ventas()

    def _sincronizar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(self.productos)

    def _sincronizar_usuarios(self) -> None:
        self.archivo_servicio.guardar_usuarios(self.usuarios)

    def _sincronizar_ventas(self) -> None:
        self.archivo_servicio.guardar_ventas(self.ventas)

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self.productos.append(producto)
        self._sincronizar_productos()
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio
            producto.stock = stock
            self._sincronizar_productos()
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            self._sincronizar_productos()
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        return self.productos

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self.usuarios.append(usuario)
        self._sincronizar_usuarios()
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """
        Valida stock, usuario y producto, registra la venta y descuenta stock.
        """
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        try:
            venta = Venta(usuario.identificacion, producto.codigo, cantidad)
            self.ventas.append(venta)
            producto.vender(cantidad)
            self._sincronizar_ventas()
            self._sincronizar_productos()
            return True
        except ValueError:
            return False

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> List[Venta]:
        """
        Filtra y retorna las ventas asociadas a un usuario específico.
        """
        ventas_usuario: List[Venta] = []
        for venta in self.ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def obtener_categorias_unicas(self) -> Set[str]:
        return {producto.categoria for producto in self.productos}