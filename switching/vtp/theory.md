# CONFIGURACIÓN VTP - SWITCH

**VLAN Trunking Protocol (VTP)** permite la gestión centralizada de VLANs en una red con múltiples switches, sincronizando la información de VLAN entre ellos.

---

## Modos de VTP

| Modo           | Función                                                                                   |
|----------------|-------------------------------------------------------------------------------------------|
| **Servidor**   | Puede crear, modificar o borrar VLANs. Envía información a clientes.                      |
| **Cliente**    | Recibe información del servidor. No puede crear ni borrar VLANs localmente.               |
| **Transparente** | No participa en VTP. Gestiona sus propias VLANs localmente sin afectar a otros switches. |

---

## Comandos básicos para configurar VTP en Cisco Packet Tracer

### 1. Verificar el modo VTP actual y versión
```plaintext
Switch# show vtp status
```

### 2. Configurar el modo VTP
a) Configurar switch en modo servidor:
```
Switch(config)# vtp mode server
```
b) Configurar switch en modo cliente:
```
Switch(config)# vtp mode client
```
c) Configurar switch en modo transparente:
```
Switch(config)# vtp mode transparent
```

### 3. Configurar dominio VTP

El dominio debe ser el mismo para que los switches puedan compartir la información VLAN.
```
Switch(config)# vtp domain NOMBRE_DOMINIO
```
Ejemplo:
```
Switch(config)# vtp domain MI_RED
```
### 4. Configurar la contraseña VTP (opcional, para mayor seguridad)

```
Switch(config)# vtp password CONTRASEÑA_SEGURA
```
Ejemplo:
```
Switch(config)# vtp password Cisco123
```
### 5. Crear VLANs en modo servidor o transparente
```
Switch(config)# vlan 10
Switch(config-vlan)# name VENTAS
Switch(config-vlan)# exit
```

Configuración de un switch como servidor VTP en el dominio "MI_RED" con contraseña y creación de VLAN 10:
```
Switch> enable
Switch# configure terminal
Switch(config)# vtp mode server
Switch(config)# vtp domain MI_RED
Switch(config)# vtp password Cisco123
Switch(config)# vlan 10
Switch(config-vlan)# name VENTAS
Switch(config-vlan)# exit
Switch(config)# exit
Switch# show vtp status
```
## Pasos VTP:

Para que el VTP funcione, es encesario seguir los siguientes pasos:
- VTP : Modo (servidor, cliente, transparente) con seguridad md5 (para verificar la información)
- Dominio : Configurar un dominio
- Contraseña : Una contraseña, para proteger el sistema
- Trunk : Modo truncado para la conexion.

### Mostrar configuracion VTP:
Si muestra error en el estado del vtp, es posible mostrar el estado de este mismo con el siguiente comando (fuera del modo configuración):
```
Switch# show vtp status
```