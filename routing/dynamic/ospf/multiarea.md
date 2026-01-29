- **OSPF (Open Shortest Path First)** es un protocolo de enrutamiento de estado de enlace (Link-State).  
- Divide la red en **áreas** para mejorar el rendimiento y la escalabilidad.  
- El **área 0 (backbone)** es obligatoria y todas las demás áreas deben conectarse a ella directa o indirectamente.  
- Los routers que conectan varias áreas se denominan **ABR (Area Border Routers)**.  

---

## Tipos de routers OSPF

| Tipo de router | Descripción |
|-----------------|--------------|
| **Internal Router** | Todas sus interfaces están en la misma área. |
| **Area Border Router (ABR)** | Conecta dos o más áreas diferentes. |
| **Backbone Router** | Tiene al menos una interfaz en el área 0. |
| **AS Boundary Router (ASBR)** | Redistribuye rutas desde otros protocolos (EIGRP, RIP, etc.) hacia OSPF. |

---

## Configuración básica OSPF Multiárea

### Paso 1: Habilitar OSPF
```bash
Router(config)# router ospf 1
```
`1` es el ID del proceso OSPF (local al router, no tiene que coincidir con otros).

### Paso 2: Asignar redes a áreas
```bash
Router(config-router)# network 10.0.0.0 0.255.255.255 area 0
Router(config-router)# network 20.0.0.0 0.255.255.255 area 1
Router(config-router)# network 30.0.0.0 0.255.255.255 area 2
```
Cada red se asocia a una área.
El ABR es el router que tiene interfaces en distintas áreas.

### Paso 3: Verificación
```bash
Router# show ip ospf
Router# show ip ospf interface brief
Router# show ip route ospf
Router# show ip protocols
```
