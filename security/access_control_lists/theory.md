## Listas de Acceso (Access Lists) en Routers

Las listas de acceso se utilizan para permitir o denegar tráfico en redes. Pueden ser numeradas o con nombre.

> Por defecto, al crear una lista de acceso, se deniega todo el tráfico. Por eso es necesario especificar permisos para las redes deseadas.

### Tipos de Redes y Listas de Acceso

Existen dos tipos de listas de acceso:
| Tipo          | Rango / Nombre   | Uso                                                                                               |
| ------------- | ---------------- | ------------------------------------------------------------------------------------------------- |
| **Estándar**  | 1-99 / Nombre    | Permite o deniega todo el tráfico de IPs.                                                         |
| **Extendida** | 100-199 / Nombre | Permite o deniega tráfico por protocolo (HTTP, HTTPS, SSH, Telnet, etc.) y por IP origen/destino. Usan puertos por los que permitir o bloquear el acceso. |

> Las listas se leen de arriba hacia abajo. Si colocas permit all al inicio, todas las reglas siguientes se ignoran.

Sintaxis General
```
# Estándar
access-list [ID] [permit|deny] [IP origen] [máscara wildcard]
# Extendida
access-list [ID] [permit|deny] [protocolo] [IP origen] [máscara wildcard] [IP destino] [máscara wildcard] [puerto opcional]
```
**Wildcard:** Es la máscara inversa (ej. 0.0.0.63 equivale a rango de 64 IPs).

### Denegar Redes
Para bloquear una red en un router de destino:
- Crear la lista con el rango de IPs a bloquear.
- Permitir el resto de redes.
- Aplicar la lista al puerto correspondiente.
```
# Habilitar router
enable
# Modo configuración
configure terminal
# Crear lista de acceso estándar (1) denegando un rango de IPs
access-list 1 deny 192.168.1.128 0.0.0.63
# Permitir el resto de redes
access-list 1 permit any
# Seleccionar interfaz de salida
interface fa0/0
# Aplicar lista de acceso en sentido de salida
ip access-group 1 out
```

### Denegar Rango Redes Lista Extendida
```
# Habilitar router
enable
# Modo configuración
configure terminal
# Creamos lista extendida numerada
access-list 101 deny ip 192.168.1.128 0.0.0.63 192.168.2.0 0.0.0.255
# Denegar tráfico DHCP (server y client)
access-list 101 deny udp any any eq 67
access-list 101 deny udp any any eq 68
# Denegar FTP
access-list 101 deny tcp any any eq 20
access-list 101 deny tcp any any eq 21
# Permitir todo lo demás
access-list 101 permit ip any any
# Salida por la interfaz Fa0/0
interface fa0/0
ip access-group 101 out
```

### Permitir Redes
Para permitir el acceso de una red:
```
# Habilitar router
enable
# Modo configuración
configure terminal
# Crear lista de acceso estándar (1) permitiendo un rango de IPs
access-list 1 permit 192.168.1.128 0.0.0.63
# Seleccionar interfaz de entrada
interface fa0/0
# Aplicar lista de acceso en sentido de entrada
ip access-group 1 in
```

### Eliminar Lista de Acceso u Orden
Eliminar lista de acceso:
```
configure terminal
no access-list [ID]
```
Eliminar orden de una lista de acceso:
```
show acces-list [ID]
no [número de línea de la regla]
```

### Mostrar Listas de Acceso
| Comando                 | Descripción                                      |
| ----------------------- | ------------------------------------------------ |
| `show access-list [ID]` | Muestra la lista de acceso específica.           |
| `show access-lists`     | Muestra todas las listas de acceso creadas.      |
| `ip access-list ?`      | Muestra los tipos de listas que se pueden crear. |

### Acceso por Protocolos (Listas Extendidas)
- Sintaxis:
```
access-list [101-199] [permit|deny] [protocolo] [IP origen] [máscara wildcard] [IP destino] [máscara wildcard] [puerto opcional]
```
- Ejemplo:

Denegar el protocolo SSH (puerto 22) desde 192.168.1.128 hasta 192.168.1.208:
```
access-list 101 deny tcp 192.168.1.128 0.0.0.69 192.168.1.208 0.0.0.15 eq 22
```

### Resumen Visual
| Acción         | Lista Estándar                         | Lista Extendida                                                                      |
| -------------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| Permitir IPs   | `access-list 1 permit [IP] [wildcard]` | `access-list 101 permit tcp [IP origen] [wildcard] [IP destino] [wildcard] [puerto]` |
| Denegar IPs    | `access-list 1 deny [IP] [wildcard]`   | `access-list 101 deny tcp [IP origen] [wildcard] [IP destino] [wildcard] [puerto]`   |
| Aplicar lista  | `ip access-group [ID] in/out`          | Igual que estándar                                                                   |
| Eliminar lista | `no access-list [ID]`                  | Igual que estándar                                                                   |
| Mostrar lista  | `show access-list [ID]`                | Igual que estándar                                                                   |
