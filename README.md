# Práctica 10. Archivos

### 1. Objetivos
* Implementar las operaciones básicas de un **TDA Archivo** (Creación, Lectura, Escritura y Cierre).
* Comprender y manipular el **apuntador de archivo** mediante desplazamientos lógicos.
* Aplicar la **serialización de objetos** para el empaquetamiento de registros lógicos en archivos binarios.

### 2. Introducción Teórica
Un archivo es una colección de información relacionada que se guarda en memoria secundaria. Para el Sistema Operativo, representa una secuencia de bytes. En esta práctica, utilizaremos el módulo `pickle` de Python, el cual permite convertir objetos complejos (diccionarios, listas, objetos) en un flujo de bytes (byte stream) para su almacenamiento persistente.



---

### 3. Actividad: "Sistema de Control de Inventario (Videoclub)"

La empresa **"RetroMovies"** requiere un sistema que permita gestionar su catálogo de películas sin perder la información al cerrar el programa. Cada película se considera un **registro lógico**.

#### Especificaciones del Registro:
Cada registro debe ser un diccionario con los siguientes atributos:
* `id`: Entero (identificador único).
* `titulo`: Cadena de texto.
* `genero`: Cadena de texto.

#### Tareas a realizar:
1.  **Alta de registros:** Implementar una función que permita agregar películas al final del archivo `peliculas.dat` sin borrar los registros anteriores (Modo `ab`).
2.  **Lectura secuencial:** Implementar una función que recorra todo el archivo y despliegue los datos de forma tabulada.
3.  **Acceso Aleatorio (Simulado):** Implementar una función que permita buscar un registro por su "índice" (posición 0, 1, 2...). El programa debe saltar los registros necesarios y mostrar el contenido del registro solicitado junto con la posición del puntero en bytes (`tell()`).
