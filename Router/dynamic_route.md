En todos los enrutamientos dinamicos, hay que agregar las redes con as que tiene conexion directa
Los mensajes que envian constantemente los routers para su comuniccion son llamados LSA(Link State Advertisement)
Cuando hay una conexion entre OSFs, da una señal Adjancecy

RIP
Cuenta el numero de saltos hasta llegar al objetivo, automáticamente, selecciona la ruta más corta (no tiene en cuenta si las lineas están saturadas).
En versiones:
- 1: No tiene en cuenta las máscaras: /8, /16 y /24
- 2: Tiene en cuenta todas (más usado)

RIP permite hasta 15 saltos, útil en redes pequeñas.

### Tras enrutar redes

Para ver como se han enrutado de forma automática el resto de redes.
```
Router#SHOW IP ROUTE rip
```
Para ver redes conectadas
```
Router#show ip protocols
```
Ver actualizaciones en tiempo real:
```
Router#debug ip rip
```

Ospf
Protocolo de estado de enlace (detecta cual es mejor camino).
Divide todo en diferentes áreas.
Por defecto siempre hay un area 0
Las redes truncales, tienes que ir si o si conectadas a un area 0
Para crear un area `router ospf numero[1-185000]
especificacion de los que es la wildcat (restar mascara propia)
Comando: network nºred wildcard
wildcard es:
    Mascara de red - nuestra: 255.255.255.255(/32) - 255.255.255.128(/25) = 0.0.0.127 wildcard

Bgp
Enrutamiento BGP
Router(config)# Router BGP Nºidentificativo del router entre 1-65535. Cada router un número
diferente
Ejemplo: Router(config)# Router BGP 1
Ahora añadimos las redes que conoce, las que toca directamente
Router(config-router)# network red mask máscara
Ejemplo Router(config-router)# network 10.0.0.0 mask 255.0.0.0
Ahora hay que añadir los routers vecino, a través del salto, el mismo salto que cuando las rutas
estáticas y el número identificativo de BGP al que nos estamos dirigiendo
Router(config-router)#neighbor ipsalto remote-as nºBGP Al que nos dirijimos
```
Router 0
Router(config)# Router BGP 100
Router(config-router)# network 10.0.0.0 mask 255.0.0.0
Router(config-router)# network 20.0.0.0 mask 255.0.0.0
Router(config-router)# neighbor 20.0.0.2 remote-as 200
```

> Se agrega el numero de red y posteriormente el vecino con el numero de salto de conexión de la red:

[r1]-ip1-------ip2-[r2]

si estamos en el r1, usariamos la ip de r2 con ip2

Eigrp