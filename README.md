Entrega #3 - Implementación de Grafos

Juan Esteban Monsalve Hernández - ( 2240056 )

Descripción del problema:
-

  Este proyecto implementa un sistema para optimizar rutas de distribución de alimentos utilizando teoría de grafos. El programa permite modelar una red de distribución como un grafo dirigido ponderado, donde los nodos representan puntos de distribución (almacenes, mercados, tiendas) y las aristas representan rutas con sus respectivos tiempos de viaje y costos asociados. 
  
  El objetivo principal es determinar las rutas más eficientes entre dos puntos de la red, considerando diferentes criterios de optimización (tiempo mínimo o costo mínimo), lo que resulta esencial para la logística en la distribución de alimentos perecederos.

Características: 
-
  .) Modelado de la red de distribución como un grafo dirigido ponderado.
  
  .) Gestión completa de nodos (agregar/eliminar puntos de distribución).
  
  .) Gestión de rutas con parámetros expecíficos (tiempo, costo).
  
  .) Algoritmo de Dijkstra para encontrar rutas óptimas.
  

Estructura: 
-
  .) La implementación consta de una clase principal `Red_Distribucion_Alimentos` que contiene:
  
  .) Métodos para gestión de nodos (agregar/eliminar)
  
  .) Métodos para gestión de rutas (agregar/eliminar)
  
  .) Algoritmo de búsqueda de ruta óptima (`ruta_optima`)
  
  .) Representación interna mediante diccionarios de diccionarios 
  

Ejmplo para el uso del código: 
-
( Cabe recalcar que en el codígo ya se encuentra un ejemplo un poco más extenso )

-Creación de red

red = Red_Distribucion_Alimentos()

red.agregar_nodo("Almacén")

red.agregar_nodo("Supermercado")

red.agregar_ruta("Almacén", "Supermercado", 30, 50)


-Consulta de ruta óptima

red.ruta_optima("Almacén", "Supermercado", "tiempo")

red.ruta_optima("Almacén", "Supermercado", "costo")

  

