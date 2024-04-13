from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, email:str, tarjeta:str) -> None:
        self._email = email
        self._tarjeta = tarjeta

    @property
    def email(self:str) -> str:
        return self._email

    @property
    def tarjeta(self:str) -> str:
        return self._tarjeta

    @abstractmethod
    def cambiar_membresia(self, nuevo_tipo:int):
        pass

    @abstractmethod
    def cancelar_suscripcion(self):
        pass

    def _crear_nueva_membresia(self, nuevo_tipo:int):
        if nuevo_tipo == 1:
            return Basica(self.email, self.tarjeta)
        elif nuevo_tipo == 2:
            return Familiar(self.email, self.tarjeta)
        elif nuevo_tipo == 3:
            return SinConexion(self.email, self.tarjeta)
        elif nuevo_tipo == 4:
            return Pro(self.email, self.tarjeta)
        raise ValueError(f"No existe el tipo de membresía {nuevo_tipo}")

class Gratis(Membresia):
    def cambiar_membresia(self, nuevo_tipo:int):
        if 1 <= nuevo_tipo <= 4:
            return self._crear_nueva_membresia(nuevo_tipo)
        raise ValueError("El tipo de membresía debe ser 1, 2, 3 o 4")

    def cancelar_suscripcion(self):
        # La membresía ya es gratis, no hay cambio.
        pass

class Basica(Membresia):
    def __init__(self, email, tarjeta):
        super().__init__(email, tarjeta)
        self.costo = 3000
        self.dispositivos_maximos = 2

    def cambiar_membresia(self, nuevo_tipo: int):
        if 2 <= nuevo_tipo <= 4:
            return self._crear_nueva_membresia(nuevo_tipo)
        raise ValueError("El tipo de membresía debe ser 2, 3 o 4")

    def cancelar_suscripcion(self):
        return Gratis(self.email, self.tarjeta)

class Familiar(Membresia):
    def __init__(self, email, tarjeta):
        super().__init__(email, tarjeta)
        self.costo = 5000
        self.dispositivos_maximos = 5
        self.dias_regalo = 7

    def cambiar_membresia(self, nuevo_tipo:str):
        if nuevo_tipo in [1, 3, 4]:
            return self._crear_nueva_membresia(nuevo_tipo)
        raise ValueError("El tipo de membresía debe ser 1, 3 o 4")

    def cancelar_suscripcion(self):
        return Gratis(self.email, self.tarjeta)

    def modificar_control_parental(self):
        # Lógica para modificar el control parental (sin implementar)
        pass

class SinConexion(Membresia):
    def __init__(self, email:str, tarjeta:str):
        super().__init__(email, tarjeta)
        self.costo = 3500
        self.dispositivos_maximos = 2
        self.dias_regalo = 7

    def cambiar_membresia(self, nuevo_tipo:str):
        if nuevo_tipo in [1, 2, 4]:
            return self._crear_nueva_membresia(nuevo_tipo)
        raise ValueError("El tipo de membresía debe ser 1, 2 o 4")

    def cancelar_suscripcion(self):
        return Gratis(self.email, self.tarjeta)

    def incrementar_contenido_sin_conexion(self):
        # Lógica para incrementar contenido disponible sin conexión (sin implementar)
        pass

class Pro(Membresia):
    def __init__(self, email:str, tarjeta:str):
        super().__init__(email, tarjeta)
        self.costo = 7000
        self.dispositivos_maximos = 6
        self.dias_regalo = 15

    def cambiar_membresia(self, nuevo_tipo: int):
        if nuevo_tipo in [1, 2, 3]:
            return self._crear_nueva_membresia(nuevo_tipo)
        raise ValueError("El tipo de membresía debe ser 1, 2 o 3")

    def cancelar_suscripcion(self):
        return Gratis(self.email, self.tarjeta)

# Ejemplo de uso
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_membresia(1)
print(type(b))
f = b.cambiar_membresia(2)
print(type(f))
sc = f.cambiar_membresia(3)
print(type(sc))
pro = sc.cambiar_membresia(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
