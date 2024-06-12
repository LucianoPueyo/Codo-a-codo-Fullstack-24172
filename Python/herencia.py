from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    @abstractmethod
    def metodo_abstracto(self):
        pass

    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}")
    
    def __toString(self):
        return f"{self.nombre} {self.apellido} DNI: {self.dni}"
    
    def __repr__(self):
        return self.__toString()
    
    def __str__(self):
        return self.__toString()


class Empleado(Persona):
    def __init__(self, nombre, apellido, dni, CUIT):
        super().__init__(nombre, apellido, dni)

        self.CUIT = CUIT
    
    def metodo_abstracto(self):
        return 0
    
    def vender(self):
        print("Se realizó una venta")

class Cliente(Persona):
    def __init__(self, nombre, apellido, dni, codigo_cliente):
        super().__init__(nombre, apellido, dni)

        self.codigo_cliente = codigo_cliente

    def metodo_abstracto(self):
        return 0
    
    def comprar(self):
        print("Se realizó una compra")

# persona1 = Persona("Roberto", "Perez", 12379)
# persona1.presentar()

empleado1 = Empleado("Carlos", "Lopez", 1234, 1234000)
empleado1.presentar()
empleado1.vender()

cliente1 = Cliente("Maria", "Del Cerro", 5678, "A5678")
cliente1.presentar()
cliente1.comprar()