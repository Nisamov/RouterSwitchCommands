# Configuración DHCP Router IPs y Rangos
- Acceso al modo configuración.
```
Router>en
Router#confi t
```
- Creción de un POOL con nombre `salmon`.
- Se indica la red en la que trabaja `20.0.0.0`.
- Se le asigna IP al router `20.0.0.1`.
- Se agrega un DNS `8.8.8.8` (Salida a internet por servidor de GOOGLE)
```
Router(config)#ip dhcp pool salmon 
Router(dhcp-config)#network 20.0.0.0 255.0.0.0
Router(dhcp-config)#default-router 20.0.0.1
Router(dhcp-config)#dns-server 8.8.8.8
Router(dhcp-config)#exit
```
- Exclusión de IP de servidor `20.0.0.1`.
- Exclusión en rango de la IP `20.0.0.2` a la `20.0.0.99`.
- Exclusión en rango de la IP `20.0.0.200` a la `20.255.255.255`.
```
Router(config)#ip dhcp excluded-address 20.0.0.1
Router(config)#ip dhcp excluded-address 20.0.0.2 20.0.0.99
Router(config)#ip dhcp excluded-address 20.0.0.200 20.255.255.255
```
> Si otorga una IP, semejante a: `169.254.XXX.XXX`, es el error APIPA.
> Este error informa de un problema en el proceso de conexión.

Finalmente se entra al equipo y se habilita la conexión por DHCP.
