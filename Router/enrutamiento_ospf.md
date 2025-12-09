<!--Configuracion enrutamiento por router-->
```prolog
#---------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------#
|   COMANDO                                                                 |       DESCRIPCION                                                                                 |
#---------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------#
Router>enable                                                               §;Inicio del router
Router#configure terminal                                                   §;Acceso al modo configuracion
Router(config)#router ospf 1                                                §;Entrar al modo de configuracion ospf con identificador 1
Router(config-router)#network 10.0.0.0 0.255.255.255 area 0                 §;Establecer conexion con la red 10.0.0.0 y 20.0.0.0 con un area 0 + mascara invertida
Router(config-router)#network 20.0.0.0 0.255.255.255 area 0                 §;Establecer conexion con la red 20.0.0.0 y 20.0.0.0 con un area 0 + mascara invertida
```