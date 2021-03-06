# Ejercicio Principios POO

Se requiere un ejemplo que utilice los principios repasados en clase.

En este Ejemplo se realizó una calculadora la cual realiza 3 operaciones:

* Operaciones Básicas
* Porcentajes
* Cambiar de Base

### Operaciones Básicas

La calculadora pide al usuario la operación a realizar en este apartado se realiza las operaciones de: Suma, Resta, Multiplicación, División. 

Si el usuario desea continuar la operación seleccionada con la respuesta obtenida debe ingresar la letra S cuando el programa se lo pida.

### Porcentajes

En esta sección la calculadora realiza tres operaciones relacionadas con los porcentajes: Suma, Resta, Calculo del porcentaje.

* Suma: el usuario digita un número y el porcentaje de ese número que desea sumar al número ingresado

* Resta: el usuario digita un número y el porcentaje de ese número que desea restar al número ingresado

* Cálculo de porcentaje: el usuario digita el número y porcentaje y el programa mostrara el porcentaje de numero ingresado.

### Cambiar Base

Aun no realizado

## Principios Utilizados

### Principio de Responsabilidad Única.

Se separa la funcionalidad de mostrar los mensajes y de capturar datos tanto de calculadora y de las demás clases que usan esta funcionalidad con el fin de que calculadora se enfoque únicamente a el control de la misma con la ejecución de sus funcionalidades.

La clase operaciones básicas y porcentaje se limitan a el cálculo que requiera el objeto calculadora.

Mensaje se enfoca a mostrar las impresiones en pantalla, y la clase capturarDatos a los diferentes momentos y formas como el sistema necesite una entrada del usuario.

### Principio de abierto y Cerrado

La clase calculadora está cerrada al cambio, pero abierta a la extensión podemos ver como esta lista la futura implementación de la opción 3 del menú sin necesidad de modificar los dos menús anteriores

Para agregarla Tendremos que agregar la opción en el elif y agregar una clase nueva que contenga la funcionalidad de cambiar de base, así mismo debemos crear una nueva clase de mensajes para la operacion cambiar base.

### DRY Dont repeat Yourself

Al crear la clase capturarDatos reutilizamos en diferentes oportunidades la funcionalidad de capturar la entrada del usuario y con la clase Mensaje mostrar mensajes repetidos en consola.

Cabe destacar que en la clase operaciones básicas se debió repetir una misma lógica para las tres primeras operaciones, en caso de no hacerlo, en caso de un fututo cambio tendremos que volver a comprender el funcionamiento de este método combinado para modificar la operación deseada, es decir, si queremos modificar la funcionalidad de la suma tendríamos que tener cuidado de no dañar la funcionalidad combinada de la resta y la multiplicacion e incluso la division.

## Diagrama UML

![image info](./pictures/Diagrama1_c.png)

## Actualizacion

Se separaron las clases de mensaje debido a que esta misma tenía conocimiento de algunas funciones de otras clases, también se simplifico la clase calculadora las opciones de los menús de cada módulo ahora está a cargo de la clase especifica es decir los submenús de las operaciones están a cargo de sus respectivas clases.

# Presentado por:

* Willmar Fabian Pelaez - 20182020123

