class Persona:
    mayoria_edad = 18 # Atributo de Clase
    
    def __init__(self, nombre, apellido, edad, dni): 
        """ Metodo Constructor """

        """
            Atributo de Instancia
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.saldo = 0

    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}")

    def caminar(self):
        print("Estoy caminando")

    def __toString(self):
        return f"{self.nombre} {self.apellido} DNI: {self.dni}"
    
    def __repr__(self):
        return self.__toString()
    
    def __str__(self):
        return self.__toString()
    
    def transaccion(self, monto):
        self.saldo += monto


class Instituto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []

    def registrar_persona(self, persona):
        if persona.edad < Persona.mayoria_edad: # Early return
            raise ValueError("La persona a registrar debe ser mayor de edad")
        
        self.personas.append(persona)

    def contar_personas(self):
        return len(self.personas)

    def calcular_saldo_total(self):
        total = 0
        
        for persona in self.personas:
            total += persona.saldo

        return total
            

# Creando dos instancias de la clase Persona
persona1 = Persona("Carlos", "Lopez", 25, 1234)
persona2 = Persona("Maria", "Del Cerro", 30, 5678)
persona3 = Persona("Roberto", "Perez", 52, 6651)

print("primeros ejemplos")
persona1.presentar()
persona2.presentar()
persona1.caminar()
print(persona1)

#-----------

persona1.transaccion(1000)
persona2.transaccion(1520)
persona3.transaccion(5080) # Ingreso de plata
persona3.transaccion(-1000) # Egreso


instituto = Instituto("El Banco de Codo a Codo")

instituto.registrar_persona(persona1)
instituto.registrar_persona(persona2)
instituto.registrar_persona(persona3)

print(instituto.contar_personas())

print(instituto.calcular_saldo_total())

print(instituto.personas)

#------

print(persona1.__toString())