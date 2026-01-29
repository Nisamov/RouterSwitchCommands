En todos los enrutamientos dinamicos, hay que agregar las redes con as que tiene conexion directa
Los mensajes que envian constantemente los routers para su comuniccion son llamados LSA(Link State Advertisement)
Cuando hay una conexion entre OSFs, da una señal Adjancecy

RIP
Cuenta el numero de saltos hasta llegar al objetivo, automáticamente, selecciona la ruta más corta (no tiene en cuenta si las lineas están saturadas).
En versiones:
- 1: No tiene en cuenta las máscaras: /8, /16 y /24
- 2: Tiene en cuenta todas (más usado)

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


Eigrp