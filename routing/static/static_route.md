# Default Router / Ruta Estática Predeterminada

Una ruta estática es cuando tú manualmente indicas a un router por dónde enviar paquetes hacia una red destino específica.

Una ruta predeterminada (default route) es una ruta especial que se usa cuando no hay ninguna ruta más específica en la tabla de enrutamiento.
Su sintaxis es algo como:
```
ip route 0.0.0.0 0.0.0.0 [next-hop o interfaz]
```
`0.0.0.0 0.0.0.0` significa “cualquier red que no esté en la tabla”.

### Posibles Escenarios

> `[PC1] --- [Router1] --- [Router2] --- [Internet/Red externa]`
- Router1: está conectado a la LAN (PC1) y a Router2
- Router2: está conectado a Router1 y hacia “Internet”

--- 

**Interfaz y Conexión de Routers - Router 1**
| Interfaz | IP          | Máscara         | Conexión      |
| -------- | ----------- | --------------- | ------------- |
| g0/0     | 192.168.1.1 | 255.255.255.0   | LAN (PC1)     |
| g0/1     | 10.0.0.1    | 255.255.255.252 | Hacia Router2 |

--- 

**Interfaz y Conexión de Routers - Router 2**
| Interfaz | IP        | Máscara         | Conexión                 |
| -------- | --------- | --------------- | ------------------------ |
| g0/0     | 10.0.0.2  | 255.255.255.252 | Hacia Router1            |
| g0/1     | 200.1.1.1 | 255.255.255.0   | “Internet” / red externa |

--- 
Se desea que Router1 envíe todo el tráfico que no conozca hacia Router2.


## Asignar IPs a interfaces
`Router1:`
```
Router> enable
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# interface g0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface g0/1
Router(config-if)# ip address 10.0.0.1 255.255.255.252
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)#
```
`Router2:`
```
Router> enable
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# interface g0/0
Router(config-if)# ip address 10.0.0.2 255.255.255.252
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface g0/1
Router(config-if)# ip address 200.1.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)#
```
## Configurar la ruta predeterminada en Router1
Indicamos que cualquier paquete que no tenga destino conocido vaya hacia la interfaz de Router2 `(10.0.0.2)`
`Router1:`
```
ip route 0.0.0.0 0.0.0.0 10.0.0.2
```
Si Router1 recibe un paquete hacia cualquier red que no esté en su tabla, lo enviará a Router2.

## Configurar la ruta en Router2 hacia la LAN
Si queremos que el tráfico de regreso funcione, Router2 necesita saber dónde está la LAN de Router1.
`Router2:`
```
ip route 192.168.1.0 255.255.255.0 10.0.0.1
```
Así Router2 sabe que para llegar a la red `192.168.1.0/24` debe enviar los paquetes hacia Router1.

## Comprobación
Ejecutamos el siguiente comando desde una terminal de equipo (ordenador), para saber información sobre la conectividad realizada.
```
show ip route
```
La ruta predeterminada aparecerá como:
```
S*    0.0.0.0/0 [1/0] via 10.0.0.2
```
- **`S*`** indica que es estática y predeterminada.