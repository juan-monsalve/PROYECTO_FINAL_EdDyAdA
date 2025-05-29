# Codigo Grafo Dirigido Ponderado

import heapq

class Red_Distribucion_Alimentos:
    def __init__(self):
        self.grafo = {} 

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = {}
            print(f"Nodo '{nodo}' añadido.")
        else:
            print(f"Nodo '{nodo}' ya existe.")

    def eliminar_nodo(self, nodo):
        if nodo in self.grafo:
            for origen in self.grafo:
                if nodo in self.grafo[origen]:
                    del self.grafo[origen][nodo]
            del self.grafo[nodo]
            print(f"Nodo '{nodo}' eliminado.")
        else:
            print(f"Nodo '{nodo}' no existe.")

    def agregar_ruta(self, origen, destino, tiempo, costo=0):
        if origen in self.grafo and destino in self.grafo:
            self.grafo[origen][destino] = {"tiempo": tiempo, "costo": costo}
            print(f"Ruta {origen} → {destino} (tiempo: {tiempo} mins, costo: ${costo}).")
        else:
            print("Nodo(s) no existe(n).")

    def eliminar_ruta(self, origen, destino):
        if origen in self.grafo and destino in self.grafo[origen]:
            del self.grafo[origen][destino]
            print(f"Ruta {origen} → {destino} eliminada.")
        else:
            print("Ruta no existe.")

    def ruta_optima(self, origen, destino, criterio="tiempo"):
        if origen not in self.grafo or destino not in self.grafo:
            print("Nodo(s) no válido(s).")
            return

        metricas = {nodo: float('inf') for nodo in self.grafo}
        metricas[origen] = 0
        heap = [(0, origen)]
        previos = {}
        criterios_validos = {"tiempo", "costo"}

        if criterio not in criterios_validos:
            print("Criterio debe ser 'tiempo' o 'costo'.")
            return

        while heap:
            metrica_actual, nodo_actual = heapq.heappop(heap)

            if nodo_actual == destino:
                break

            for vecino, datos in self.grafo[nodo_actual].items():
                metrica_nueva = metrica_actual + datos[criterio]
                if metrica_nueva < metricas[vecino]:
                    metricas[vecino] = metrica_nueva
                    previos[vecino] = nodo_actual
                    heapq.heappush(heap, (metrica_nueva, vecino))

        if destino not in previos:
            print(f"No hay ruta {origen} → {destino}.")
        else:
            ruta = []
            actual = destino
            while actual != origen:
                ruta.append(actual)
                actual = previos[actual]
            ruta.append(origen)
            ruta.reverse()
            print(f"Ruta óptima ({criterio}): {' → '.join(ruta)} ({metricas[destino]} {criterio}).")

#*** EJEMPLO ***
red = Red_Distribucion_Alimentos()

print("\n--- Agregando nodos ---")
red.agregar_nodo("Almacen_Central")
red.agregar_nodo("Distribuidor_Norte")
red.agregar_nodo("Distribuidor_Sur")
red.agregar_nodo("Tienda_A")
red.agregar_nodo("Tienda_B")
red.agregar_nodo("Tienda_C")
red.agregar_nodo("Tienda_D")

red.agregar_nodo("Almacen_Central") # Agregar nodo que ya existe.

print("\n--- Agregando rutas ---")
red.agregar_ruta("Almacen_Central", "Distribuidor_Norte", 25, 40)
red.agregar_ruta("Almacen_Central", "Distribuidor_Sur", 30, 35)
red.agregar_ruta("Distribuidor_Norte", "Tienda_A", 15, 20)
red.agregar_ruta("Distribuidor_Norte", "Tienda_B", 20, 25)
red.agregar_ruta("Distribuidor_Sur", "Tienda_B", 10, 15)
red.agregar_ruta("Distribuidor_Sur", "Tienda_C", 18, 22)
red.agregar_ruta("Tienda_B", "Tienda_C", 5, 8)

red.agregar_ruta("Almacen_Central", "Tienda_X", 10, 15) # Ruta con nodo inexistente.

print("\n--- Pruebas de rutas óptimas ---")

print("\nCaso 1: Ruta más rápida Almacen_Central → Tienda_C")
red.ruta_optima("Almacen_Central", "Tienda_C", "tiempo")

print("\nCaso 2: Ruta más económica Almacen_Central → Tienda_C")
red.ruta_optima("Almacen_Central", "Tienda_C", "costo")

print("\nCaso 3: Ruta a nodo aislado Almacen_Central → Tienda_D")
red.ruta_optima("Almacen_Central", "Tienda_D", "tiempo") # Ruta a nodo aislado.

print("\nCaso 4: Ruta con criterio inválido")
red.ruta_optima("Almacen_Central", "Tienda_A", "distancia") # Ruta con criterio invalido.

print("\n--- Pruebas de eliminación ---")

red.eliminar_ruta("Distribuidor_Norte", "Tienda_A")

red.eliminar_ruta("Almacen_Central", "Tienda_D") # Ruta que no existe.

print("\nEliminando Distribuidor_Norte y verificando rutas...")
red.eliminar_nodo("Distribuidor_Norte")

print("\nIntentando ruta que pasaba por Distribuidor_Norte:")
red.ruta_optima("Almacen_Central", "Tienda_A", "tiempo")

red.eliminar_nodo("Distribuidor_Este") # Eliminar nodo que no existe.