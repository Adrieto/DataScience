Un consultorio médico necesita un programa para gestionar los datos de sus
pacientes. Por cada paciente, se deben almacenar los siguientes elementos: número de
historia clínica (un número entero), nombre del paciente, fecha de la última visita (en días –
otro número entero) y código de la enfermedad o problema registrado (un valor entre 0 y 9
incluidos). Los datos deben cargarse y almacenarse inicialmente en un arreglo de
registros/objetos, a razón de un objeto por paciente, el cual debe mantenerse en todo
momento ordenado de menor a mayor de acuerdo al valor del número de historia clínica de
los pacientes. El programa debe incluir un menú con las opciones siguientes:
1. Cargar el arreglo con los objetos pedidos (recuerde: el arreglo debe mantenerse
ordenado por historia clínica: cada objeto debe insertarse en el lugar correcto cuando
se agrega al arreglo).
2. Cargar por teclado un número entero d, y mostrar por pantalla los datos de todos los
pacientes del arreglo que hayan asistido al consultorio por última vez en un período
de d días o más.
3. Determinar si en el arreglo existe un paciente con número de historia clínica igual a x.
Si existe, mostrar todos sus datos. Si no, dar un mensaje de error.
4. Mostrar todos los datos del arreglo.
5. Grabe todos los datos del arreglo en un archivo (para favorecer el desarrollo de los
puntos que siguen, asegúrese de hacerlo de forma que cada objeto se grabe por
separado, uno por uno). El archivo debe ser creado si no existía, y todo dato que
hubiese contenido debe ser eliminado si ya existía.
6. Mostrar el archivo generado en el punto anterior.
7. Usando el archivo creado en el punto 5, crear en memoria otro arreglo que contenga
los objetos de los pacientes cuyo código de enfermedad sea 8 o 9. Recuerde: debe
crear otro arreglo de objetos, y no eliminar ni modificar el original que se creó en el
punto 1.
8. Mostrar el arreglo creado en el punto 7.