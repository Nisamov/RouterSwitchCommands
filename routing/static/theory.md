OSPF: Open Shortest Path First (Protocolo)

Este protocolo cuenta con varios modos de protección NAT por ocultamiento:

NAT estática - Hay que hacerla de manera manual
NAT dinámica - Es automática, se le peude agregar un rango de ip
NAT PAT overload - Otorga una misma ip diferenciada por puertos

Ejemplo gráfico:
```
pc0 = usuario1
pc1 = usuario2

         -> 10.0.0.1   -> 20.0.0.2   -> 30.0.0.2
         |             |             | 
[pc0] --- [router0] --- [router1] --- [pc1]
  |                |             | 
  -> 10.0.0.2      -> 20.0.0.1   -> 30.0.0.1 

```
En este ejemplo, es posible comprender la estructura red, siendo así, más sencillo de comprender.
En este caso tenemos dos usuarios: `usuario1` y `usuario2`.
Estos son los datos de cada equipo/conexión:
```
IP(PC0): 10.0.0.2
IP(PC1): 30.0.0.2

Pueto gig0/0/1: 10.0.0.1
Puerto gig0/0/0: 20.0.0.1
Puerto gig0/0/0: 20.0.0.2
Puerto gig0/0/1: 30.0.0.1
```
Para poder ocultarlos, será necesario elegir el método con el cual trataremos su privacidad desde el router.

Ejemplo práctico `NAT Estática`:
```
Entrada:
    IP(PC0): 10.0.0.2
    IP(PC0): 20.0.0.3
```
En el ejemplo anterior se puede apreciar la entrada de datos por la ip `10.0.0.2` de un solo equipo, en este caso se le asigna a esa dirección IP, una IP de salida de forma manual, en este caso se indica que la salida de la ip `10.0.0.2` es la IP `20.0.0.3`.

Ejemplo práctico `NAT Dinámica`:
```
    IP(Rango): 20.0.0.3 20.0.0.240
```
En el ejemplo anterior se puede apreciar un rango de IP con el cual, el router trabajará para ir otorgando de manera automática, en todo momento es necesario establecer un rango con el cual se va a trabajar.
En este caso puede haber X IPs ocupadas, no obstante, mientras aún quede espacio para una, se nos otorgará la siguiente a la última IP usada.


Ejemplo práctico `NAT PAT Overload`:
```
Entrada:
    IP(PC0): 20.0.3.4    IP(PC1): 20.0.3.4
Salida:
    IP(PC0): 30.0.8.1:1 IP(PC1): 30.0.8.1:2
```
En el ejemplo anterior se puede apreciar la entrada de datos por la IP `20.0.3.4` de dos equipos (de diferente red), como resultado, el router les ha asignado una misma IP con un puerto como método de distinción.
