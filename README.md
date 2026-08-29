# Sistema de Restaurante (restaurante_app) - Semana 11

## **Autor**
* **Elkin Esteban Tovar Caicedo**

## **Descripción del Sistema**
Sistema modular en Python basado en Programación Orientada a Objetos (POO). En esta undécima semana se implementan relaciones y operaciones reales entre objetos, añadiendo el control de stock, la entidad `Venta` para relacionar usuarios con productos, consultas de compras por usuario y persistencia JSON completa para productos, usuarios y ventas.

## **Estructura del Proyecto**
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
Responsabilidad de los Componentes
modelos/producto.py: Define la clase Producto con control estricto de stock y serialización a diccionario.

modelos/usuario.py: Define la clase Usuario con sus datos personales y soporte para serialización.

modelos/venta.py: Representa la relación comercial vinculando la identificación del usuario, el código del producto y la cantidad adquirida.

servicios/archivo_servicio.py: Centraliza la persistencia de los archivos productos.json, usuarios.json y ventas.json utilizando codificación UTF-8.

servicios/restaurante.py: Administra las tres colecciones del sistema, validando reglas de negocio, existencias de stock y ejecutando el filtrado de ventas por usuario.

main.py: Coordina el menú interactivo por consola y dirige la interacción con el usuario.

Relación Usuario-Producto mediante Venta y Stock
Atributo Stock: Cada producto posee una cantidad disponible que se actualiza y valida para impedir números negativos o ventas que excedan las existencias.

Operación de Venta: Se verifica la existencia del usuario y producto, que la cantidad solicitada sea mayor a cero y que haya stock disponible. De cumplirse, se instancia una Venta, se añade a la colección, se reduce el stock y se actualizan de forma sincronizada los archivos productos.json y ventas.json.

Persistencia y Excepciones Controladas
Persistencia Integral: Las colecciones se cargan al iniciar mediante json.load() y se guardan de forma automatizada mediante json.dump() cada vez que se modifican.

Excepciones Controladas: Se manejan de forma específica FileNotFoundError (iniciando colecciones vacías si los archivos no existen), json.JSONDecodeError (archivos corruptos), PermissionError y validaciones internas con ValueError para evitar cierres inesperados.

Instrucciones para Ejecutar
Abre una terminal en la raíz del proyecto.

Ejecuta el comando:

Bash
python main.py
Utiliza las opciones del menú interactivo.

Comprobación de Pruebas y Persistencia
Para verificar el funcionamiento correcto:

Se ejecutó el programa y se registró un usuario y un producto con stock limitado.

Se realizó una venta válida, verificando que el stock disminuyó correctamente y que los cambios se reflejaron en ventas.json y productos.json.

Se intentó realizar una venta superando el stock disponible, siendo rechazada sin alterar los datos.

Se cerró por completo el programa y se reinició, confirmando que las tres colecciones (productos, usuarios y ventas) se recuperaron exitosamente desde los archivos JSON.
