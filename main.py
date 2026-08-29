from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR PRODUCTO =====")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        if precio < 0 or stock < 0:
            print("\n❌ El precio y el stock no pueden ser negativos.")
            return
    except ValueError:
        print("\n❌ Ingrese valores numéricos válidos para precio y stock.")
        return

    try:
        producto = Producto(codigo, nombre, categoria, precio, stock)
        if restaurante.registrar_producto(producto):
            print("\n✅ Producto registrado y guardado correctamente en JSON.")
        else:
            print("\n❌ Ya existe un producto con ese código.")
    except ValueError as e:
        print(f"\n❌ Error de validación: {e}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n===== BUSCAR PRODUCTO =====")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto:
        print(f"\n✅ Producto encontrado:\n{producto.mostrar_informacion()}")
    else:
        print("\n❌ No se encontró ningún producto con ese código.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n===== ACTUALIZAR PRODUCTO =====")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    producto_existente = restaurante.buscar_producto(codigo)
    if not producto_existente:
        print("\n❌ No se encontró ningún producto con ese código.")
        return

    print(f"Actual: {producto_existente.mostrar_informacion()}")
    nuevo_nombre = input("Nuevo nombre: ").strip()
    nueva_categoria = input("Nueva categoría: ").strip()
    try:
        nuevo_precio = float(input("Nuevo precio: "))
        nuevo_stock = int(input("Nuevo stock: "))
        if nuevo_precio < 0 or nuevo_stock < 0:
            print("\n❌ El precio y el stock no pueden ser negativos.")
            return
    except ValueError:
        print("\n❌ Ingrese valores numéricos válidos.")
        return

    if restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio, nuevo_stock):
        print("\n✅ Producto actualizado y guardado correctamente en JSON.")
    else:
        print("\n❌ No se pudo actualizar el producto.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n===== ELIMINAR PRODUCTO =====")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("\n✅ Producto eliminado y archivo JSON actualizado.")
    else:
        print("\n❌ No se encontró un producto con ese código.")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("\nNo existen productos registrados.")
        return

    print("\n========== PRODUCTOS ==========\n")
    for producto in productos:
        print(producto.mostrar_informacion())


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR USUARIO =====")
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo electrónico: ").strip()

    usuario = Usuario(identificacion, nombre, correo)

    if restaurante.registrar_usuario(usuario):
        print("\n✅ Usuario registrado y guardado correctamente.")
    else:
        print("\n❌ Ya existe un usuario con esa identificación.")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("\nNo existen usuarios registrados.")
        return

    print("\n========== USUARIOS ==========\n")
    for usuario in usuarios:
        print(usuario.mostrar_informacion())


def realizar_venta(restaurante: Restaurante) -> None:
    print("\n===== REALIZAR VENTA =====")
    identificacion_usuario = input("Identificación del usuario: ").strip()
    codigo_producto = input("Código del producto: ").strip()
    try:
        cantidad = int(input("Cantidad a comprar: "))
    except ValueError:
        print("\n❌ Ingrese un valor entero válido para la cantidad.")
        return

    if restaurante.vender_producto(codigo_producto, identificacion_usuario, cantidad):
        print("\n✅ Venta realizada con éxito. Stock actualizado y guardada en JSON.")
    else:
        print("\n❌ No se pudo realizar la venta. Verifique que el usuario y producto existan, que la cantidad sea mayor a cero y que haya stock suficiente.")


def consultar_ventas_usuario(restaurante: Restaurante) -> None:
    print("\n===== CONSULTAR VENTAS POR USUARIO =====")
    identificacion_usuario = input("Ingrese la identificación del usuario: ").strip()
    usuario = restaurante.buscar_usuario(identificacion_usuario)
    if not usuario:
        print("\n❌ Usuario no encontrado.")
        return

    ventas = restaurante.consultar_ventas_usuario(identificacion_usuario)
    if not ventas:
        print(f"\nEl usuario {usuario.nombre} no registra compras.")
        return

    print(f"\n========== VENTAS DE {usuario.nombre.upper()} ==========\n")
    for venta in ventas:
        prod = restaurante.buscar_producto(venta.producto_codigo)
        nombre_prod = prod.nombre if prod else "Producto desconocido"
        print(f"- Producto: {nombre_prod} (Código: {venta.producto_codigo}) | Cantidad adquirida: {venta.cantidad}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n===== CATEGORÍAS ÚNICAS (CONJUNTO) =====")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
    else:
        for categoria in categorias:
            print(f"- {categoria}")


def main() -> None:
    restaurante = Restaurante()

    opciones_menu: tuple = (
        "1. Registrar producto",
        "2. Buscar producto",
        "3. Actualizar producto",
        "4. Eliminar producto",
        "5. Listar productos",
        "6. Registrar usuario",
        "7. Listar usuarios",
        "8. Realizar venta",
        "9. Consultar ventas por usuario",
        "10. Mostrar categorías",
        "11. Salir"
    )

    acciones_menu = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante),
        "4": lambda: eliminar_producto(restaurante),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: realizar_venta(restaurante),
        "9": lambda: consultar_ventas_usuario(restaurante),
        "10": lambda: mostrar_categorias(restaurante)
    }

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        for opcion in opciones_menu:
            print(opcion)
        print("----------------------------------------")

        eleccion = input("\nSeleccione una opción: ").strip()

        if eleccion == "11":
            print("\n¡Gracias por utilizar el sistema!")
            break
        elif eleccion in acciones_menu:
            acciones_menu[eleccion]()
        else:
            print("\n❌ Opción no válida.")


if __name__ == "__main__":
    main()