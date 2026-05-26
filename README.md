# Taller SOLID

Este repositorio contiene ejemplos refactorizados para aplicar los cinco principios SOLID.

Cada carpeta tiene el sufijo `_sol` porque contiene la solucion aplicada para un principio especifico.

## SRP - Single Responsibility Principle

Carpeta: `srp_sol`

Archivo principal: `srp_sol/file_manager.py`

Antes, la clase `FileManager` tenia mas de una responsabilidad:

- Leer archivos.
- Escribir archivos.
- Comprimir archivos.
- Descomprimir archivos.

Eso rompia el principio de responsabilidad unica, porque una misma clase podia cambiar por razones diferentes.

La solucion fue separar las responsabilidades:

- `FileManager`: se encarga solamente de leer y escribir archivos.
- `ZipFileManager`: se encarga solamente de comprimir y descomprimir archivos ZIP.

De esta forma, cada clase tiene una sola razon para cambiar.

## OCP - Open/Closed Principle

Carpeta: `ocp_sol`

Archivo principal: `ocp_sol/shapes.py`

Antes, la clase `Shape` dependia de un valor `shape_type` y usaba condicionales para calcular el area de cada figura.

El problema era que, si se queria agregar una nueva figura, habia que modificar la clase existente.

La solucion fue crear una abstraccion:

- `Shape`: clase base abstracta.
- `Rectangle`: calcula el area de un rectangulo.
- `Circle`: calcula el area de un circulo.

Ahora el codigo esta cerrado para modificacion y abierto para extension. Si se necesita una nueva figura, se crea una nueva clase sin modificar las clases existentes.

## LSP - Liskov Substitution Principle

Carpeta: `lsp_sol`

Archivo principal: `lsp_sol/shapes.py`

La solucion define un contrato comun para las figuras:

- `Shape`: clase base abstracta con el metodo `calculate_area`.
- `Rectangle`: implementa el calculo de area de un rectangulo.
- `Square`: implementa el calculo de area de un cuadrado.
- `total_area`: recibe una coleccion de figuras y suma sus areas.

La idea es que cualquier clase que herede de `Shape` pueda usarse donde se espera una figura, sin romper el comportamiento del programa.

## ISP - Interface Segregation Principle

Carpeta: `isp_sol`

Archivo principal: `isp_sol/printers.py`

Antes existia una interfaz grande llamada `Printer` con metodos para imprimir, escanear y enviar fax.

El problema era que una impresora antigua estaba obligada a implementar metodos que no soportaba, como `fax` y `scan`.

La solucion fue dividir la interfaz en capacidades pequenas:

- `Printable`: define solamente la accion de imprimir.
- `Faxable`: define solamente la accion de enviar fax.
- `Scannable`: define solamente la accion de escanear.

Ahora:

- `OldPrinter` implementa solamente `Printable`.
- `ModernPrinter` implementa `Printable`, `Faxable` y `Scannable`.

Asi ninguna clase queda obligada a depender de metodos que no necesita.

## DIP - Dependency Inversion Principle

Carpeta: `dip_sol`

Archivo principal: `dip_sol/app.py`

Antes, `FrontEnd` dependia directamente de la clase concreta `BackEnd` y de un metodo especifico llamado `get_data_from_database`.

La solucion fue introducir una abstraccion:

- `DataSource`: define el contrato para obtener datos.
- `FrontEnd`: depende de `DataSource`, no de una clase concreta.
- `BackEnd`: implementa `DataSource`.

Con este cambio, el frontend puede trabajar con cualquier fuente de datos que cumpla el contrato, no solamente con una base de datos concreta.

## Carpetas finales

- `srp_sol`
- `ocp_sol`
- `lsp_sol`
- `isp_sol`
- `dip_sol`

## Commits realizados

Se dejaron commits locales separados para cada principio SOLID:

- `Aplicar SRP separando compresion de archivos`
- `Aplicar OCP con figuras extensibles`
- `Aplicar LSP con figuras sustituibles`
- `Aplicar ISP dividiendo capacidades de impresora`
- `Aplicar DIP usando fuente de datos abstracta`

Tambien se creo un commit local para renombrar las carpetas con el sufijo `_sol`.

No se hizo `push` al repositorio remoto.
