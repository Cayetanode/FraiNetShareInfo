# By Fraile - 2024
# FraiNetShareInfo
# Cyber Attack - CBA
# Cayetano De Juan.

Ver recursos compartidos en SMB.

¿Qué es Smbclient?
smbclient: herramienta para todo, mostrar recursos de un equipo, conectarse a uno de forma temporal, etc... Los comandos mount. cifs y smbmount sirven para montar, como clientes, un recurso compartido de la red de Windows.

Lo que aporta esta pequeña herramienta es que visualiza la unidad logica del recurso (Linux). Esta información muchas veces puede destapar, nombres de usuario, empresa.... Que podria ser utilizada para futuros ataques.

La version de python es la 3.10.4
Necesitas los módulos instalados: 
- win32net (pip install pywin32) En Windows puede instalarlo (py -3.x -m pip install pywin32)
- colorama (pip install colorama) En Windows puede instalarlo (py -3.x -m pip install colorama).

Uso:
python frainetshareinfo.py -ip <ip>



