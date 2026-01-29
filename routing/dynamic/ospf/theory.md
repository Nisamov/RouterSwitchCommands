# CONFIGURACIÓN VLANS - SWITCH

Las VLAN van por numero, la 1 y la 0 no se deben modificar.

## Configuración básica de VLANs en Switch
Paso 1: Entrar al modo privilegiado y modo configuración global
```
Switch> enable
Switch# configure terminal
Switch(config)#
```

## Paso 2: Crear VLANs
Ejemplo: Crear VLAN 10 y VLAN 20
```
Switch(config)# vlan 10
Switch(config-vlan)# name Ventas
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name Finanzas
Switch(config-vlan)# exit
```

## Paso 3: Asignar puertos a VLANs (modo access)
Todo lo que vaya de un switch a un cliente (ordenador), es modo acceso

Ejemplo: Asignar puerto FastEthernet 0/1 a VLAN 10 y FastEthernet 0/2 a VLAN 20
```
Switch(config)# interface FastEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit

Switch(config)# interface FastEthernet0/2
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20
Switch(config-if)# exit
```

## Paso 4: Configurar puerto trunk (si es necesario)
Todo lo que vaya de un switch a un switch o de un switch a un router, es modo truncado.

Puerto FastEthernet 0/24 será trunk para transportar múltiples VLANs
```
Switch(config)# interface FastEthernet0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20
Switch(config-if)# exit
```
En caso de ser un rango, sería usando `in range`:
```
Switch> enable
Switch# configure terminal
Switch(config)# interface range FastEthernet0/1 - 3
Switch(config-if-range)# switchport mode trunk
Switch(config-if-range)# exit
Switch(config)#
```

## Paso 5: Mostrar Vlans en el servidor
```
Switch#show vlan
```

## VTP (VLAN Trunking Protocol)
- VTP (VLAN Trunking Protocol) es un protocolo de Cisco que permite la administración centralizada de VLANs en una red de switches.
- Facilita la creación, eliminación y propagación automática de VLANs entre switches dentro de un mismo dominio VTP.
- Evita la configuración manual VLAN por VLAN en cada switch.

## Paso 1: Configurar el modo VTP, dominio y contraseña
Nota: El dominio VTP distingue mayúsculas y minúsculas.

Modo servidor (puede crear y propagar VLANs)
```
Switch> enable
Switch# configure terminal
Switch(config)# vtp mode server
Switch(config)# vtp domain smr2
Switch(config)# vtp password smr2
```

Modo transparente (pasa mensajes pero no actualiza VLANs)
```
Switch> enable
Switch# configure terminal
Switch(config)# vtp mode transparent
Switch(config)# vtp domain smr2
Switch(config)# vtp password smr2
```

Modo cliente (solo recibe actualizaciones, no modifica VLANs)
```
Switch> enable
Switch# configure terminal
Switch(config)# vtp mode client
Switch(config)# vtp domain smr2
Switch(config)# vtp password smr2
```

## Paso 2: Configurar puertos trunk para comunicación VTP

El protocolo VTP usa enlaces trunk para propagar información entre switches.
```
Switch(config)# interface <puerto>
Switch(config-if)# switchport mode trunk
Switch(config-if)# exit
```

Ejemplo para un rango de puertos FastEthernet 0/1 a 0/3:
```
Switch(config)# interface range FastEthernet0/1 - 3
Switch(config-if-range)# switchport mode trunk
Switch(config-if-range)# exit
```

## Paso 3: Configurar puertos en modo access para dispositivos finales

Los puertos conectados a PCs u otros dispositivos deben estar en modo access y asignados a una VLAN específica.
```
Switch(config)# interface <puerto>
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan <número_vlan>
Switch(config-if)# exit
```