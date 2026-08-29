import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """
    Servicio encargado de la persistencia de productos, usuarios y ventas en formato JSON.
    """

    def __init__(self) -> None:
        self.dir_datos = "datos"
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        """
        Crea el directorio 'datos' si no existe previamente.
        """
        if not os.path.exists(self.dir_datos):
            try:
                os.makedirs(self.dir_datos)
            except PermissionError:
                print("❌ Error: No tiene permisos para crear el directorio de datos.")

    def cargar_productos(self, ruta: str = "datos/productos.json") -> List[Producto]:
        productos = []
        if not os.path.exists(ruta):
            return productos
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        codigo = item["codigo"]
                        nombre = item["nombre"]
                        categoria = item["categoria"]
                        precio = float(item["precio"])
                        stock = int(item["stock"])
                        if precio < 0 or stock < 0:
                            continue
                        productos.append(Producto(codigo, nombre, categoria, precio, stock))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return productos

    def guardar_productos(self, productos: List[Producto], ruta: str = "datos/productos.json") -> None:
        try:
            data = [p.a_diccionario() for p in productos]
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("❌ Error: Sin permisos para guardar productos.")

    def cargar_usuarios(self, ruta: str = "datos/usuarios.json") -> List[Usuario]:
        usuarios = []
        if not os.path.exists(ruta):
            return usuarios
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        identificacion = item["identificacion"]
                        nombre = item["nombre"]
                        correo = item["correo"]
                        usuarios.append(Usuario(identificacion, nombre, correo))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return usuarios

    def guardar_usuarios(self, usuarios: List[Usuario], ruta: str = "datos/usuarios.json") -> None:
        try:
            data = [u.a_diccionario() for u in usuarios]
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("❌ Error: Sin permisos para guardar usuarios.")

    def cargar_ventas(self, ruta: str = "datos/ventas.json") -> List[Venta]:
        ventas = []
        if not os.path.exists(ruta):
            return ventas
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                if not isinstance(data, list):
                    return []
                for item in data:
                    try:
                        usuario_id = item["usuario_id"]
                        producto_codigo = item["producto_codigo"]
                        cantidad = int(item["cantidad"])
                        if cantidad <= 0:
                            continue
                        ventas.append(Venta(usuario_id, producto_codigo, cantidad))
                    except (KeyError, ValueError, TypeError):
                        continue
        except (json.JSONDecodeError, PermissionError):
            pass
        return ventas

    def guardar_ventas(self, ventas: List[Venta], ruta: str = "datos/ventas.json") -> None:
        try:
            data = [v.a_diccionario() for v in ventas]
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("❌ Error: Sin permisos para guardar ventas.")