en
confi t
in gi0/0.10
#Dot1Q protocolo VLANs, permite que las vlans se comuniquen entre si, permite que todas las vlans sean compatibles entre si idnependientemente del tamaño de paquetes enviados entre si
encapsulation Dot1Q 10
ip address 10.0.0.1 255.0.0.0
no sh

<!--
Router>en
Router#confi t
Router(config)#in gi0/0.10
Router(config-subif)#encapsulation dot1Q 10
Router(config-subif)#ip address 192.168.100.1 255.255.255.0
Router(config-subif)#no sh
Router(config-subif)#in gi0/0.20
Router(config-subif)#encapsulation dot1Q 20
Router(config-subif)#ip address 192.168.101.1 255.255.255.0
Router(config-subif)#no sh
Router(config-subif)#in gi0/0.30
Router(config-subif)#encapsulation dot1Q 30
Router(config-subif)#ip address 192.168.102.1 255.255.255.0
Router(config-subif)#no sh
Router(config-subif)#in gi0/0
Router(config-if)#no sh
-->