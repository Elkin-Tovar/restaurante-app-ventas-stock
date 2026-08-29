class Usuario:
    """
    Clase que representa un usuario general del restaurante.
    """

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del usuario.
        """
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def a_diccionario(self) -> dict:
        """
        Convierte el objeto Usuario en un diccionario para su almacenamiento en JSON.
        """
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }