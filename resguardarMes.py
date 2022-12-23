from calendar import monthrange
import variables
import loggingRudi
import os

isilon = variables.ISILON
standar = variables.STANDAR

def cantidad_dias_por_mes(yyyy, mm):
    return monthrange(yyyy, mm)[1] 

def resguardarMes(yyyy,mm,tramite):
    loggingRudi.logInfo("loggeo desde resguardarMes.py: parametros de entrada: yyyy: " + str(yyyy) + " mm: " + str(mm) + " tramite: " + tramite)
    #primeros diez dias del mes
    for i in range(1,10):
        if len(str(mm)) == 1:
            fecha =str(yyyy)+"-0"+str(mm)+"-0"+str(i)
            origen = standar.format(fecha, tramite)
            destino = isilon.format(tramite, fecha, tramite)
            moveDirectorio(origen,destino)
        else:          
            fecha = str(yyyy)+"-"+str(mm)+"-0"+str(i)
            origen = standar.format(fecha, tramite)
            destino = isilon.format(tramite, fecha, tramite)
            moveDirectorio(origen,destino)
    #ultimos dias del mes
    for i in range(10,cantidad_dias_por_mes(yyyy,mm)+1): 
            if len(str(mm)) == 1:
                fecha =str(yyyy)+"-0"+str(mm)+"-"+str(i)
                origen = standar.format(fecha, tramite)
                destino = isilon.format(tramite, fecha, tramite)
                moveDirectorio(origen,destino)
            else:          
                fecha = str(yyyy)+"-"+str(mm)+"-"+str(i)
                origen = standar.format(fecha, tramite)
                destino = isilon.format(tramite, fecha, tramite)
                moveDirectorio(origen,destino)

def moveDirectorio(origen, destino):
    print("origen: "+origen)
    print(os.path.exists(origen))
    if os.path.exists(origen):
        print("destino = "+ destino)
        #create directory if not exists
        if not os.path.exists(destino):
            os.makedirs(destino)
            print("se creo el directorio "+destino)
            loggingRudi.logInfo("se creo el directorio "+destino)
            moveFiles(origen,destino)
        else:
            print("el directorio "+destino+" ya existe")
            loggingRudi.logWarning("el directorio "+destino+" ya existe")
            moveFiles(origen,destino)
    else:
        loggingRudi.logWarning("no existe el directorio "+origen+" no se pueden mover archivos desde un directorio inexistente")

def moveFiles(origen,destino):
        for filename in os.listdir(origen):
            try:                
                os.rename(origen+filename,destino+filename)
                loggingRudi.logInfo("se movio el archivo "+filename+" de "+origen+" a "+destino )
            except Exception as error:
                loggingRudi.logError("no se pudo mover el archivo "+filename)
                loggingRudi.logError(error)
