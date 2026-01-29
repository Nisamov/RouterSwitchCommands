> Este documento incluye:
> - OSPF, MD5 multiárea, ACL, VLANs, Redes (NAT, PAT, Dinámica), Seguridad de Puertos, BGP

## Configuración básica OSPF Multiárea

Se usará en multiarea:
- Area 0 para equipos
- Area 1 de router a router

### Paso 1: Habilitar OSPF
```
Router(config)# router ospf 1
```
`1` es el ID del proceso OSPF (local al router, no tiene que coincidir con otros).

### Paso 2: Asignar redes a áreas (Multiárea)
```
Router(config-router)#network 10.0.0.0 0.255.255.255 area 0
Router(config-router)#network 20.0.0.0 0.255.255.255 area 1
Router(config-router)#network 30.0.0.0 0.255.255.255 area 2
```
Cada red se asocia a una área.
El ABR es el router que tiene interfaces en distintas áreas.

### Paso 3: Verificación
```
Router#show ip ospf
Router#show ip ospf interface brief
Router#show ip route ospf
Router#show ip protocols
```
## Confguración ACLs

### Sintaxis General
```
> Estándar
access-list [ID] [permit|deny] [IP origen] [máscara wildcard]

> Extendida
access-list [ID] [permit|deny] [protocolo] [IP origen] [máscara wildcard] [IP destino] [máscara wildcard] [puerto opcional]
```
**Wildcard:** Es la máscara inversa (ej. 0.0.0.63 equivale a rango de 64 IPs).

### Denegar Redes
Para bloquear una red en un router de destino:
- Crear la lista con el rango de IPs a bloquear.
- Permitir el resto de redes.
- Aplicar la lista al puerto correspondiente.
```
> Crear lista de acceso estándar (1) denegando un rango de IPs
Router(config)#access-list 1 deny 192.168.1.128 0.0.0.63

> Permitir el resto de redes
Router(config)#access-list 1 permit any

> Seleccionar interfaz de salida
Router(config)#interface fa0/0

> Aplicar lista de acceso en sentido de salida
Router(config)#ip access-group 1 out
```

### Denegar Rango Redes Lista Extendida
```
> Crear lista extendida numerada
Router(config)#access-list 101 deny ip 192.168.1.128 0.0.0.63 192.168.2.0 0.0.0.255

> Denegar tráfico DHCP (server y client)
Router(config)#access-list 101 deny udp any any eq 67
Router(config)#access-list 101 deny udp any any eq 68

> Denegar FTP
Router(config)#access-list 101 deny tcp any any eq 20
Router(config)#access-list 101 deny tcp any any eq 21

> Permitir todo lo demás
Router(config)#access-list 101 permit ip any any

> Salida por la interfaz Fa0/0
Router(config)#interface fa0/0
Router(config)#ip access-group 101 out
```

### Permitir Redes
Para permitir el acceso de una red:
```
> Crear lista de acceso estándar (1) permitiendo un rango de IPs
Router(config)#access-list 1 permit 192.168.1.128 0.0.0.63

> Seleccionar interfaz de entrada
Router(config)#interface fa0/0

> Aplicar lista de acceso en sentido de entrada
Router(config)# ip access-group 1 in
```

### Eliminar Lista de Acceso u Orden
Eliminar lista de acceso:
```
Router(config)#no access-list [ID]
```
Eliminar orden de una lista de acceso:
```
Router(config)#show acces-list [ID]
Router(config)#no [número de línea de la regla]
```

## Configuración VLANs VTP
Crear VLAN 10 y VLAN 20
```
Switch(config)#vlan 10
Switch(config-vlan)#name Ventas
Switch(config-vlan)#exit

Switch(config)#vlan 20
Switch(config-vlan)#name Finanzas
Switch(config-vlan)#exit
```
Conexión de Switch a Switch y De Switch a Router
```
Switch#show running-config
Switch(config)#interface fa0/X
Switch(config-in)#switchport mode trunk 
```
Conexión de Switch a Equipo
```
Switch(config)#interface fa0/X
Switch(config-in)#switchport mode access
Switch(config-in)#switchport access vlan 10
```
Partir la interfaz del router en subinterfaces y poner en un router múltiples default gateways.
En este caso el "10", ".10" es la VLAN
(Repetir por cada VLAN necesaria a agregar)
```
Router(config)#interface fa0/0.10
Router(config-in)#encapsulation dot1q 10
Switch(config-in)#ip address 10.0.0.1 255.0.0.0
Router(config-in)#no shutdown
Router(config)#interface fa0/0.20
```
## Encapsulación

Seleccionar el puerto de conexion de  Router a Vlan

`0.10` Sería para la Vlan 10, se repite el siguiente proceso para todas las Vlans a conectar
```
Router(config)#in gi0/0.10
# El dot1Q VLAN (10,20,30...)
Router(config-subif)#encapsulation dot1Q 10
# La IP a agregar es el Gateway
Router(config-subif)#ip address 192.168.100.1 255.255.255.0
Router(config-subif)#no sh
Router(config-subif)exit
# Resto de vlans a agregar
# Conexion con la interfaz principal
Router(config)#in gi0/0
Router(config-in)#no sh
```

## Configuración Red NAT
Configuración red externa y red interna
### NAT Dinámica
- Se crea una ACL numero 1, que da acceso a la 10.0.0.0
- Convierte las IP 20.0.0.3 en 20.0.0.4
```
Router(config)#interface gi0/0
Router(config-if)#ip nat inside
Router(config-if)#exit
Router(config)#interface gi0/1
Router(config-if)#ip nat outside
Router(config-if)#exit
Router(config)#access-list 1 permit 10.0.0.0 0.0.0.255
Router(config)#ip nat pool NAT_POOL 20.0.0.3 20.0.0.4 netmask 255.255.255.0
Router(config)#ip nat inside source list 1 pool NAT_POOL
Router(config)#end
```
### NAT Overload
```
in gi0/0
ip nat inside
exit
in gi0/1
ip nat outside
exit
access-list 1 permit 10.0.0.0 0.255.255.255
ip nat inside source list 1 interface gi0/1 overload

## Telnet
Abrir conexiones de 0 a 15 por vty
```
Switch (config)# line vty 0 15
Switch (config-line)# password contraseña
Switch (config-line)# login
Switch (config-line)# exit
Switch (config)# service password-encryption 
```
Mensaje de bienvenida diario
```
Switch(config)# banner motd &mensaje&
```
Guardar configuracion permanentemente
```
Switch# copy running-config startup-config 
```
