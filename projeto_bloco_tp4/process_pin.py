import os
import platform
import psutil

#devolve o sistema operacional
plataforma = platform.system()
print("Sistema Operacional: ",plataforma)
#Achar PID
pid = os.getpid()
print("Nome do processo ",psutil.Process(pid).name(),"PID", pid)

#Memoria
#rss ou [0] usado para encontrar a memoria dentro da lista Sistema Operacional Windows
processo = psutil.Process(os.getpid())
#processo que esta acontecendo no momento
#for proc in psutil.process_iter():
    #print(proc.name)

# conversao em MB
memoria = processo.memory_info()[0] >> 20
print("Memoria usada processamento: ", memoria, "MB")

memoria_porcentagem = processo.memory_percent("rss")
print("Memoria em porcentagem: ",memoria_porcentagem*100,"%")
#conversao bytes para MB
memoria_virtual = psutil.virtual_memory()
print("Memoria Usada Windows :", memoria_virtual[3]>> 20, "MB")


