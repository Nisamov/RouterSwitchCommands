# NAT Dinámica

<!--Pendiente de revisar apuntes-->

- La NAT siempre se hace de cara al exterior.
- Se habilita el router.
- Indicación de puerto de entrada y puerto de salida.
```prolog
Router>enable
Router#configure terminal
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
Router#
Ver traducciones NAT
prolog
Copiar código
Router#show ip nat translations
Limpiar traducciones activas
prolog
Copiar código
Router#clear ip nat translation *
Eliminar NAT Dinámica
prolog
Copiar código
Router#configure terminal
Router(config)#no ip nat inside source list 1 pool NAT_POOL
Router(config)#no ip nat pool NAT_POOL
Router(config)#no access-list 1
Router(config)#end
Router#
```