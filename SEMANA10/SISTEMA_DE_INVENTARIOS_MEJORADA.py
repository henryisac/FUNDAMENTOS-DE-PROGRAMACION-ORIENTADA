import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            return {}
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo de inventario.")
            return {}

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                json.dump(self.productos, file, indent=4)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Añade un producto al inventario."""
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto existente."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            if precio is not None:
                self.productos[nombre]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado correctamente.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for nombre, datos in self.productos.items():
                print(f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

# Prueba del sistema
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")