#Desarrollar un sistema avanzado de gestión de inventarios para una tienda, que incorpore las colecciones en POO
# para un manejo eficiente de los ítems del inventario y almacene la información del inventario en archivos.

import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto.to_dict())
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({id_p: p.to_dict() for id_p, p in self.productos.items()}, f)
        print("Inventario guardado con éxito.")

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {id_p: Producto.from_dict(p) for id_p, p in data.items()}
            print("Inventario cargado con éxito.")
        except FileNotFoundError:
            print("No se encontró un archivo de inventario. Iniciando desde cero.")


# Menú interactivo
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n MENÚ DE INVENTARIO ")
        print("1 Añadir producto")
        print("2 Eliminar producto")
        print("3 Actualizar producto")
        print("4 Buscar producto por nombre")
        print("5 Mostrar todos los productos")
        print("6 Guardar inventario")
        print("7 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_en_archivo()

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
