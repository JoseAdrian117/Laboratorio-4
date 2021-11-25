### Documentación
***Parte 4-1***

Primeramente se realiza una modulación 8-PSK, para este apartado se utiliza una simulación del sistema de comunicaciones como en la sección 3.2.
Para ralizar la modulación 8-PSK fue necesario alterar algunas de las funciones dadas, entre ellas, al modulador se le tuvo que agregar dos portadoras, ya que este al igual que la modulación IQ utiliza dos.
Se creó una variable llamada h la cual toma el valor de 0.707 y es de suma importancia en este tipo de modulación ya que esta funciona para realizar las formas de ondas y el estudio de las condiciones de los bits de este método de estudio utilizando for. Una vez terminado este proceso, se calcula la potencia promedio de la señal modulada.

Para el demodulador se crean dos prodoctos internos de funciones, uno para cada portadora del modulador, además se crea una secuencia lógica la cual funciona para los bits de 8-PSK. No fue necesario alterar la función del canal ruidoso ni los bits a RGB.
Seguidamente, utilizando la función bits_a_rgb se cuenta la cantidad de bits, se reconstruyen los canales RGB y a su vez se decodifican.

Por último se definen los parámetros de frecuencia de la portadora, muestras por periodo de la portadora y relación señal-a-ruido del canal y se grafican las señal transmitida y la recuperada.


***Parte 4.2***

Para el procedimiento de pruebas de Estacionaridad y ergodicidad de la señal modulada primero se definen los tiempos, luego de esto se realiza el proceso de inicialización aleatorio X(t).Se aplica cada valor de amplitud entre (-1, 1) para la señal, seguidamente se saca el promedio de las N realizaciones por instante.
Ahora, una vez hecho todo esto, se grafica el resultado teórico del valor esperado, se muestra las realizaciones y su promedio teórico calculado (teórico), se obtienen T valores de desplazamiento en tau.

Se da la inicialización de matriz de valores de correlación para las N funciones y se crea una nueva figura de autocorrelación. Luego se calcula la correlación para cada valor de tau, el Valor teórico de correlación y se realizan las gráficas de correlación para cada realización.


***Parte 4.3***

Para la densdad espectral de potencia se hicieron algunas modificaciones a los códigos dados, entre ellas se agregó leyendas a los ejes y se le colocó un título a cada gráfica, esto se hizo debido que nos ayuda a saber que en el eje x se encuentra la frecuencia en Hz, en el efe y está ubicada la densidad espectral de potencia.
De esta manera se grafica la densidad espectral y se obtiene que la mayor densidad espectral de potencia se encuentra entre los 2500 Hz y los 7500 Hz.
