Agregar IP a los routers:
```
Router> enable
Router# configure terminal
Router(config)# interface <tipo> <número>
Router(config-if)# ip address <IP> <MASCARA>
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# end
```

Ejemplo práctico:
```
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shut
```
