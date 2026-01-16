import pickle
import os

class Pelicula:
    def __init__(self, id_peli, titulo, genero):
        self.id = id_peli
        self.titulo = titulo
        self.genero = genero
        self.activo = True 

    def __str__(self):
        estado = "[ACTIVO]" if self.activo else "[ELIMINADO]"
        return f"{estado} ID: {self.id:03d} | {self.titulo.ljust(15)} | {self.genero}"

class ManejadorBiblioteca:
    def __init__(self, nombre_archivo):
        self.archivo = nombre_archivo

    def agregar_registro(self):
        print("\n--- Alta de Registro (Escritura) ---")
        try:
            with open(self.archivo, "ab") as f:
                idx = int(input("ID: "))
                nom = input("Título: ")
                gen = input("Género: ")
                p = Pelicula(idx, nom, gen)
                pickle.dump(p, f)
                print(">>> Registro guardado.")
        except ValueError:
            print(">>> Error: Datos inválidos.")

    def listar_activos(self):
        """Lectura Secuencial filtrando borrados lógicos"""
        print("\n--- Películas Disponibles (Filtro Lógico) ---")
        if not os.path.exists(self.archivo): return

        with open(self.archivo, "rb") as f:
            while True:
                try:
                    p = pickle.load(f)
                    if p.activo: # Solo mostramos si no está borrado lógicamente
                        print(p)
                except EOFError:
                    break

    def eliminar_logico(self):
        """Busca un registro y cambia su estado sin borrarlo físicamente"""
        print("\n--- Borrado Lógico ---")
        id_borrar = int(input("Ingrese el ID de la película a eliminar: "))
        registros_actualizados = []
        encontrado = False

        if not os.path.exists(self.archivo): return

        # 1. Leemos todo a memoria o usamos un temporal
        with open(self.archivo, "rb") as f:
            while True:
                try:
                    p = pickle.load(f)
                    if p.id == id_borrar:
                        p.activo = False # Marcamos como eliminado
                        encontrado = True
                    registros_actualizados.append(p)
                except EOFError:
                    break
        
        # 2. Reescribimos el archivo con la bandera cambiada
        if encontrado:
            with open(self.archivo, "wb") as f:
                for r in registros_actualizados:
                    pickle.dump(r, f)
            print(">>> Registro eliminado lógicamente.")
        else:
            print(">>> ID no encontrado.")

# --- Interfaz ---
def main():
    sistema = ManejadorBiblioteca("biblioteca_v2.dat")
    while True:
        print("\n1. Agregar  2. Listar  3. Borrar Lógico  4. Salir")
        op = input("Seleccione: ")
        if op == "1": sistema.agregar_registro()
        elif op == "2": sistema.listar_activos()
        elif op == "3": sistema.eliminar_logico()
        elif op == "4": break

if __name__ == "__main__":
    main()
