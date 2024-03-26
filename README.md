# Secure Company

## Introducción

Simular un escenario dentro de una compañía de seguros. En este modelo, los clientes generan reclamaciones de acuerdo con una distribución común M, y cada monto de reclamación sigue una distribución F. Los nuevos clientes se registran de acuerdo con una distribución ν, y cada cliente existente permanece en la compañía durante un tiempo distribuido por μ. Además, cada cliente paga a la compañía de seguros una tasa fija c por unidad de tiempo. La simulación comienza con n0 clientes y un capital inicial a0≥0. 

- ### Objetivos y metas

El objetivo es observar y analizar el comportamiento del sistema, incluyendo la llegada de clientes, la generación de reclamaciones y la salud financiera de la compañía, para entender la dinámica de una compañía de seguros bajo diversas condiciones.Asi como evaluar las limitaciones y similitudes que presenta con respecto a la situación real que se desea simular.

- ### Variables que describen el problema

- Cantidad inicial de clientes: $N_0$
- Capital inicial de la compañía: $a_0$
- Cantidad de dinero que da el cliente : $M_0$
- Total de reclamaciones : $R_T$
- Tiempo de arrivo de un cliente : $C_t$
- Numero de cliente que abandonan la compania: $N_f$
- Dinero de la compania : $M_T$
- Número total de clientes atendidos : $n_{in}$

## Detalles de Implementación

Para implementar el escenario de seguros, se pueden seguir los siguientes pasos:

1) Definir las distribuciones de probabilidad:

 * Distribución de llegada de clientes: Se utiliza para determinar el tiempo entre la llegada de un nuevo cliente.
 * Distribución de reclamaciones: Se utiliza para determinar el número de reclamaciones que un cliente genera.
 * Distribución de tiempo de permanencia: Se utiliza para determinar cuánto tiempo un cliente permanece en la compañía antes de abandonarla.
 * Distribución de tiempo de reparación: Se utiliza para determinar cuánto tiempo se necesita para reparar una máquina.

 2) Inicializar las variables del sistema:

 * $N_0$: Número inicial de clientes.
 * $a_0$: Capital inicial de la compañía.
 * $n_{in}$: Número total de clientes atendidos.
 * $reclamation_number$: Número total de reclamaciones.
 * capital : monto a pagar por cliente ( $M_0$ )

3) Simular el tiempo de llegada de los clientes:

 * Utilizar la función `time_client_arrive` para calcular el tiempo de llegada de los clientes basado en el número total de reclamaciones.

4) Simular la generación de reclamaciones:

 * Utilizar la función `amount_reclamation_distribution` para calcular el número de reclamaciones generadas por los clientes.

5) Actualizar el capital de la compañía:

 * Incrementar el capital inicial con el número de clientes multiplicado por el capital ( $M_0$ ).
 * Decrementar el capital con el número de reclamaciones multiplicado por un porcentaje (por ejemplo, 25%).

6) Simular el tiempo de salida de los clientes:

 * Utilizar la función `number_client_time` para calcular el número de clientes que dejan la compañía basado en el número de reclamaciones y el tiempo transcurrido.

7) Actualizar el número de clientes:

 * Decrementar el número de clientes con el número de clientes que dejan la compañía.
 
8) Repetir los pasos 3 a 7 hasta que el sistema falle:

El sistema falla cuando no hay más clientes disponibles y no hay reparaciones pendientes.

## Resultados y experimentos

### Parámetros iniciales de la simulación

- cantidad inicial de clientes: $N_0$
- capital inicial de la compañía: $a_0$
- cantidad de dinero que da el cliente : $M_0$

Estos fueron los resultados observados para los siguientes casos iniciales:

> ( $N_0$ : 1000, $a_0$ : 500 , $M_0$ : 0.1 )

Al comienzo, el comportamiento del capital de la compañía y el número de reclamaciones en cada intervalo se comportan de manera errática, luego de unas iteraciones, ambas variables estabilizan su comportamiento. El capital de la compañía tiende a disminuir con el tiempo llegando a caer por debajo del capital inicial y alcanzando valores negativos; mientras que el número de reclamaciones aumenta constantemente. También se observa como el número de clientes de la compañía aumenta y ninguno la abandona, a la vez que el tiempo en que se espera llegue un nuevo cliente aumenta hasta estabilizarse en un valor de 15.

> ( $N_0$ : 10, $a_0$ : 500 , $M_0$ : 0.1 )

El comportamiento observado es similar al anterior, con la pequeña diferencia de que se estabiliza mucho más rápido y el tiempo de espera para el próximo cliente se estabiliza en 17. Se observa también que el capital de la compañía disminuye más rápidamente mientras que la cantidad de clientes de esta aumenta mucho más rápido. Este comportamiento nos lleva a pensar que existe una relación entre la cantidad de clientes inicial y la velocidad en que se estabiliza el tiempo de espera para el próximo cliente, a la vez que afecta el grado de descenso del capital de la compañía y el grado de aumento de las reclamaciones en cada intervalo de tiempo.

> ( $N_0$ : 10, $a_0$ : 500 , $M_0$ : 0.23 )

A medida que aumentamos el cobro de la compañía por cada cliente, la velocidad de disminución del capital de la compañía disminuye, y cuando se alcanza el valor de 0.23, se observa como el capital aumenta de forma alternada, superando el capital inicial con un descenso espontáneo cada cierto tiempo. De manera similar se comporta la cantidad de reclamaciones por intervalo. Esto sigue así hasta que el número de reclamaciones por intervalo de tiempo supera el valor de 1250, en este momento el capital comienza a disminuir gradualmente y de forma alternada con un muy pequeño crecimiento. Es interesante el hecho de que el número de clientes no deja de aumentar. A partir de valores mayores de cobro, el comportamiento del sistema es similar, con el único cambio de que las caídas del capital son menores que antes. Estas observaciones evidencian la relación existente entre el capital de la compañía y la cantidad que se le cobra a cada cliente, junto con la cantidad de reclamaciones que se hacen.

> ( $N_0$ : 1000, $a_0$ : 500 , $M_0$ : 0.235 )

Para estos valores, al comienzo el capital asciende rápidamente, después de cierto tiempo se observa un decrecimiento casi constante en el capital de la compañía y un aumento casi constante de la cantidad de reclamaciones por intervalo de tiempo, llegando a tener un capital por debajo del inicial. Esto demuestra también la existencia de una relación entre el cobro por cliente y la cantidad de clientes iniciales de la compañía.

> ($N_0$ : 1000 , $a_0$ : 50 , $M_0$ : 0.235)

En este caso se observa un comportamiento similar, solo que después de cierto tiempo el capital comienza a descender hasta que llega a un puento en el que comienza a oscilar con una amplitud muy pronunciada, pasando de valores negativos a valores positivos sin exceder al capital inicial de la compañía.

En los últimos casos se observó que el capital aumentaba de forma intermitente, alternando con cortos momentos de caída. Por lo general estos momentos coincidieron con esos en los que no hubo reclamaciones. Esto es lógico debido a que el capital de la compañía esta directamente relacionada con la cantidad de reclamaciones que recibe.

### Análisis estadístico de la simulación (Variables de interés)

#### Analisis sobre el monto a pagar por cliente :

Como se puedo apreciar en los ejemplos anteriores existe un punto muerto en el que la cantidad de ingreso de la compañía no aumenta ni disminuye y este se adquiere para los valores iniciales 0.25 a pagar por cliente en cada intervalo de tiempo . 

#### Como se comporta el flujo de clientes ?

Existe una tendencia al aumento del tiempo en que cada cliente llega al sistema , aunque el numero de clientes que se van es proporcionar al tiempo que pasa y al numero de reclamaciones

#### Lealtad del cliente :

Para el tiempo simulado , ningun cliente se va ( 1500 clientes ), aunque generan reclamaciones y por cada tiempo se generan tantas reclamaciones como clientes hay.

#### Rentabilidad de la empresa : 

Nuevamente, si la empresa pide un pago al cliente de 0.25 o superior , entonces se considera rentable






## Analisis de la parada de la simulacion

La simulacion no se detiene a menos que el usuario lo detenga , aunque resulta importante destacar que para valores muy grandes de clientes iniciales , el tiempo de simulacion para cada iteracion es considerablemente grande

## Modelo Matemático

#### Descripción del modelo de simulación

El modelo se basa en tomar un conjunto de comportamientos posibles que se pueden dar en clientes de alguna empresa, y permutarlos para generar una situacion no determinista , pero posible. 

 * Se modelo una distribucion comun M para el numero de reclamaciones por unidad de tiempo de un cliente
 * El monto de reclamacion por unidad de tiempo tiene distribucion F
 * Los nuevos clientes se registran de acuerdo con una distribución ν
 * Ademas cada asegurado existente permanece con la compañía durante un tiempo distribuido μ.
 * Cada asegurado paga a la compañía de seguros a una tasa fija c por unidad de tiempo
 * Comenzamos con n0​ clientes y un capital inicial a0​≥0

#### Supuestos y restricciones

 * Distribución de las reclamaciones

Sabemos que la probabilidad de que exactamente un cliente se queje es $\frac{1}{n}$, la probabilidad de que exactamente 2 personas se quejen es la siguiente:
Tomemos todos los posibles subconjuntos de 2 personas de los n clientes existentes, de ellos solo uno contiene los 2 clientes que se quejaron, luego, la cantidad de subconjuntos de 2 personas de n existentes es $\frac{n!}{(n - 2)!2!}$, por lo que la probabilidad de que exactamente 2 personas se quejen es de $\frac{(n - 2)!2!}{n!}$. Siguiendo el mismo razonamiento, la probabilidad de que exactamente k personas se quejen es $\frac{(n - k)!k!}{n!}$. Aplicando la fórmula de la probabilidad total obtenemos que la probabilidad de que al menos una persona se queje es $\Sigma^{n - 1}_{k = 1} \frac{(n - k)!k!}{n!}$. Esta será la distribución de las reclamaciones. Para obtener la cantidad de reclamaciones que ocurrieron en N experimentos, iteraremos por las probabilidades de que exactamente m personas se quejen ($P_m$) y haremos el cálculo $N*P_m$ y lo aproximaremos al menor entero que no lo supere, el ultimo valor de m que arroje un resultado distinto de cero, será la cantidad de reclamaciones que ocurrieron en los N experimentos.

 * Distribución de la llegada de nuevos clientes

Para esto usamos la idea planteada en el epígrafe 2.4.1 del libro "Temas de Simulación" pasado en los materiales de estudio.

 * Distribución de la permanencia de un cliente

En este caso hemos modelado dos tipos de clientes. Los clientes del primer tipo siguen la siguiente distribución, la probabilidad de que permanezca en la compañía es $1 - \frac{1}{C_R}$ donde $C_R$ es la cantidad de reclamaciones que han ocurrido entre la llegada del cliente $n$ y el $n-1$. Los del segundo tipo tienen la distribución siguiente, la probabilidad de que se mantenga es $\frac{1}{N}$ donde N es la cantidad de clientes que se encuentran con la compañía.

Por último, el monto de reclamaciones por intervalo de tiempo queda implícitamente definido por las demás distribuciones.



## Limitaciones

Dado que estamos simulando la llegada de los clientes nuevos con una distribución Poisson, no podemos simular la situación de que los clientes nuevos lleguen según el éxito alcanzado por la compañía. Esto lo podríamos haber modelado con la siguiente distribución:
$P = f(C_R,N)$ donde $C_R$ es la cantidad de reclamaciones que ha tenido la compañía y N es la cantidad de clientes que permanecen en ella y además $f$ es una relación inversa entre $C_R$ y $N$.
<br>
 Considerar otra distribución para la permanencia de los clientes en dicha compañía que a su vez considere la cantidad de clientes , el numero de clientes que reclaman , cuando reclaman y con que frencuencia lo hacen.

## Conclusión

Con este modelo podemos modelar el proceso de comienzo de una compañía de seguros en el mercado acercan las condiciones reales a las que se enfrentaría una compañía real en la misma situación en cuanto a la llegada de nuevos clientes y la cantidad de reclamaciones.


## Correr el proyecto

Para correr la simulación solo debe correr el script de python  **secure-company.py**