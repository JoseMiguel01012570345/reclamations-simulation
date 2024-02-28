# Secure Company

En este proyecto estamos simulando una compañía de seguros donde llegan clientes y se van, a la vez que estos generan reclamaciones a la compañía.

## Distribución de las reclamaciones

Sabemos que la probabilidad de que exactamente un cliente se queje es $\frac{1}{n}$, la probabilidad de que exactamente 2 personas se quejen es la siguiente:
Tomemos todos los posibles subconjuntos de 2 personas de los n clientes existentes, de ellos solo uno contiene los 2 clientes que se quejaron, luego, la cantidad de subconjuntos de 2 personas de n existentes es $\frac{n!}{(n - 2)!2!}$, por lo que la probabilidad de que exactamente 2 personas se quejen es de $\frac{(n - 2)!2!}{n!}$. Siguiendo el mismo razonamiento, la probabilidad de que exactamente k personas se quejen es $\frac{(n - k)!k!}{n!}$. Aplicando la fórmula de la probabilidad total obtenemos que la probabilidad de que al menos una persona se queje es $\Sigma^{n - 1}_{k = 1} \frac{(n - k)!k!}{n!}$. Esta será la distribución de las reclamaciones. Para obtener la cantidad de reclamaciones que ocurrieron en N experimentos, iteraremos por las probabilidades de que exactamente m personas se quejen ($P_m$) y haremos el cálculo $N*P_m$ y lo aproximaremos al menor entero que no lo supere, el ultimo valor de m que arroje un resultado distinto de cero, será la cantidad de reclamaciones que ocurrieron en los N experimentos.

## Distribución de la llegada de nuevos clientes

Para esto usamos la idea planteada en el epígrafe 2.4.1 del libro "Temas de Simulación" pasado en los materiales de estudio.

## Distribución de la permanencia de un cliente

En este caso hemos modelado dos tipos de clientes. Los clientes del primer tipo siguen la siguiente distribución, la probabilidad de que permanezca en la compañía es $1 - \frac{1}{C_R}$ donde $C_R$ es la cantidad de reclamaciones que han ocurrido entre la llegada del cliente $n$ y el $n-1$. Los del segundo tipo tienen la distribución siguiente, la probabilidad de que se mantenga es $\frac{1}{N}$ donde N es la cantidad de clientes que se encuentran con la compañía.

Por último, el monto de reclamaciones por intervalo de tiempo queda implícitamente definido por las demás distribuciones.

## Limitaciones

Dado que estamos simulando la llegada de los clientes nuevos con una distribución Poisson, no podemos simular la situación de que los clientes nuevos lleguen según el éxito alcanzado por la compañía. Esto lo podríamos haber modelado con la siguiente distribución:
$P = f(C_R,N)$ donde $C_R$ es la cantidad de reclamaciones que ha tenido la compañía y N es la cantidad de clientes que permanecen en ella y además $f$ es una relación inversa entre $C_R$ y $N$.
<br>
 Considerar otra distribución para la permanencia de los clientes en dicha compañía que a su vez considere la cantidad de clientes , el numero de clientes que reclaman , cuando reclaman y con que frencuencia lo hacen.

## Conclusión

Con este modelo podemos modelar el proceso de comienzo de una compañía de seguros en el mercado acercan las condiciones reales a las que se enfrentaría una compañía real en la misma situación en cuanto a la llegada de nuevos clientes y la cantidad de reclamaciones.