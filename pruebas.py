from calendar import monthrange
import os
import variables

standar = variables.STANDAR
isilon = variables.ISILON

mm=10
yyyy=2021
tramite = "PADM"

def cantidad_dias_por_mes(yyyy, mm):
    return monthrange(yyyy, mm)[1] 

for i in range(1,10):
    if len(str(mm)) == 1:
        fecha =str(yyyy)+"-0"+str(mm)+"-0"+str(i)
        origen = standar.format(fecha, tramite)
        destino = isilon.format(tramite, fecha)
        print("origen: "+origen)
        print(os.path.exists(origen))
        print("destino = "+ destino)
        print(os.path.exists(destino))
    else:          
        fecha = str(yyyy)+"-"+str(mm)+"-0"+str(i)
        origen = standar.format(fecha, tramite)
        destino = isilon.format(tramite, fecha)
        print("origen: "+origen)
        print(os.path.exists(origen))
        print("destino = "+ destino)
        print(os.path.exists(destino))
#ultimos dias del mes
for i in range(10,cantidad_dias_por_mes(yyyy,mm)+1): 
        if len(str(mm)) == 1:
            fecha =str(yyyy)+"-0"+str(mm)+"-"+str(i)
            origen = standar.format(fecha, tramite)
            destino = isilon.format(tramite, fecha)
            print("origen: "+origen)
            print(os.path.exists(origen))
            print("destino = "+ destino)
            print(os.path.exists(destino))
        else:          
            fecha = str(yyyy)+"-"+str(mm)+"-"+str(i)
            origen = standar.format(fecha, tramite)
            destino = isilon.format(tramite, fecha)
            print("origen: "+origen)
            print(os.path.exists(origen))
            print("destino = "+ destino)
            print(os.path.exists(destino))