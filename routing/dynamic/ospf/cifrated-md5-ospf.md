<!--
md5 = tipo de encriptación
cabra = contraseña que usarán los routers para comunicarse de forma cifrada
-->
```prolog
#---------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------#
|   COMANDO                                                                 |       DESCRIPCION                                                                                 |
#---------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------#
Router (config) #router ospf 1                                              §;
Router (config-router) #area 0 authentication message-digest                §;
Router (config-router) #exit                                                §;
Router (config) #in gi0/0                                                   §;
Router (config-if) #ip ospf message-digest-key 1 md5 cabra                  §;
Router (config-if) #ip ospf authentication message-digest                   §;
Router (config-if) #in gi0/1                                                §;
Router (config-if) #ip ospf message-digest-key 1 md5 cabra                  §;
Router (config-if) #ip ospf authentication message-digest                   §;
```

Mostrar estado de conexions
show ip osfp interface {interfaz}
show ip ospf interface gi0/0