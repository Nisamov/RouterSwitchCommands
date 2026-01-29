ENtrar en interfaz

Activar port security:

switchport mode access
switchport port-security

Desactivar port security:
no switchport port-security
switchport access vlan 1

Indicar cuantas macs pueden conectarse como maximo
switchport port-security maximum 1

Extablecer conexiones automaticas:
switchport port-security mac-address sticky

Establecer mac manualmente
switchport port-security mac-address 0000.0000.0000
