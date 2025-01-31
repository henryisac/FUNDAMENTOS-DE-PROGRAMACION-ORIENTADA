#Desarrollar un programa que permita gestionar información sobre personas y empleados.

class Persona:
    def __init__(self, nombre, edad):
        """Constructor de la clase Persona"""
        self.nombre = nombre
        self.edad = edad
        print(f"Persona {self.nombre} ha sido creada.")

    def mostrar_info(self):
        """Muestra la información de la persona"""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def __del__(self):
        """Destructor de la clase Persona"""
        print(f"Persona {self.nombre} ha sido eliminada.")

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        """Constructor de la clase Empleado que hereda de Persona"""
        super().__init__(nombre, edad)
        self.salario = salario
        print(f"Empleado {self.nombre} con salario {self.salario} ha sido creado.")

    def mostrar_info(self):
        """Muestra la información del empleado"""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}")

    def __del__(self):
        """Destructor de la clase Empleado"""
        print(f"Empleado {self.nombre} ha sido eliminado.")
        super().__del__()  # Llama al destructor de la clase base

# Creación de objetos
persona1 = Persona("HENRY", 28)
persona1.mostrar_info()

empleado1 = Empleado("ISAAC", 30, 800)
empleado1.mostrar_info()
