Router#configure terminal
Router(config)#router ospf 1
Router(config-router)#network 10.0.0.0 0.255.255.255 area 0
Router(config-router)#network 20.0.0.0 0.255.255.255 area 0

§;Establecer conexion con la red 20.0.0.0 y 20.0.0.0 con un area 0 + mascara invertida
