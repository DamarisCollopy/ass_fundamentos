import subprocess
import os
import platform


#devolve o sistema operacional
plataforma = platform.system()
print(plataforma)
#Achar PID
pid = os.getpid()
print(pid)

#Memoria
processo =