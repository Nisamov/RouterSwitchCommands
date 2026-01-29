CONFIGURACIÓN BÁSICA DE BGP

1) Activar BGP en el router

Para iniciar el proceso BGP se usa el comando:

Router(config)# router bgp <numero_AS>

- El número AS (Autonomous System) identifica al router o conjunto de routers.
- Rango válido: 1 – 65535.
- Cada sistema autónomo debe tener un número AS distinto.

Ejemplo:
Router(config)# router bgp 1

2) Anunciar redes en BGP

Se anuncian las redes que el router conoce directamente.
Estas redes deben existir previamente en la tabla de enrutamiento.

Comando:
Router(config-router)# network <red> mask <mascara>

Ejemplo:
Router(config-router)# network 10.0.0.0 mask 255.0.0.0

3) Configurar routers vecinos (BGP neighbors)

Para intercambiar rutas BGP es necesario definir los routers vecinos.

Comando:
Router(config-router)# neighbor <ip_vecino> remote-as <AS_vecino>

- <ip_vecino>: dirección IP del router vecino (siguiente salto).
- <AS_vecino>: número AS del router vecino.
- Normalmente el salto es el mismo que se usaría en rutas estáticas.

EJEMPLO COMPLETO
```
Router0
Router(config)# router bgp 100
Router(config-router)# network 10.0.0.0 mask 255.0.0.0
Router(config-router)# network 20.0.0.0 mask 255.0.0.0
Router(config-router)# neighbor 20.0.0.2 remote-as 200
```
Explicación:
- El router pertenece al AS 100.
- Anuncia las redes 10.0.0.0/8 y 20.0.0.0/8.
- Se establece una relación BGP con el vecino 20.0.0.2 del AS 200.