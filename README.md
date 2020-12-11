![Centralita](assets/centralita.jpg)


## Campanas al Sur

Estamos en 1989, la empresa “Campanas al Sur” llega al país para iniciar el mercado de telefonía celular.

La empresa nos contrata para crear el primer sistema de cobro de llamadas celulares.

Como el servicio todavía es muy caro y solo algunos pocos afortunados pueden pagarlo la cantidad de suscriptores iniciales es de 10 personas, pero puede crecer más adelante.

Un detalle a tener en cuenta, como estamos en 1989 y las bases de datos transaccionales todavía no están en auge, vamos a tener que utilizar otro método para almacenar los consumos y recargas de los abonados, un archivo, arrays, variables, etc.


## Requerimientos

1. Simular el paso de los días, donde los abonados por un lado consumen saldo de las líneas al realizar llamadas ($2 el minuto) y por otro, un operador realiza recargas diarias a todos los abonados ($3 por dia).

2. Tener en cuenta que:

- Los abonados cuentan con un saldo inicial de $3.

- Mientras haya una llamada en curso, no se pueden realizar recargas y si se esta haciendo una recarga, no se pueden realizar llamadas.

- Cuando el abonado no tenga saldo suficiente para realizar una llamada, tendrá que esperar a que el operador le asigne la recarga diaria y le "avise" que la misma esta hecha.

3. La empresa tuvo éxito y ahora suma el servicio de mensajes de texto (SMS) con un costo de $1 cada uno. Permitir que los abonados envíen mensajes de texto teniendo en cuenta que estos terminales no son multitareas.
