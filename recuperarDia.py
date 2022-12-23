import variables
import loggingRudi
import os

isilon = variables.ISILON
standar = variables.STANDAR

def recuperarDia(yyyy,mm,dd,tramite):
    loggingRudi.logInfo("loggeo desde recuperarDia.py: parametros de entrada: yyyy: " + str(yyyy) + " mm: " + str(mm) + " tramite: " + tramite)

    if dd < 10:
        fecha =str(yyyy) + "-" + str(mm) + "-0" + str(dd)
        origen = isilon.format(tramite,fecha,tramite)
        destino = standar.format(fecha,tramite)
        recuperarArchivos(origen,destino)
    else:
        fecha =str(yyyy)+"-" + str(mm)+"-" + str(dd)
        origen = isilon.format(tramite,fecha,tramite)
        destino =standar.format(fecha,tramite)
        recuperarArchivos(origen,destino)

def recuperarArchivos(origen,destino):
    if os.path.exists(origen):
        for filename in os.listdir(origen):
            try:
                os.rename(origen+filename,destino+filename)
                loggingRudi.logInfo("se movio el archivo "+filename+" de "+origen+" a "+destino )
            except Exception as error:
                loggingRudi.logError("no se pudo recuperar "+filename)
                loggingRudi.logError(error)
    else:
        os.mkdir(destino)
        loggingRudi.logInfo("se creo la carpeta "+destino)
        for filename in os.listdir(origen):
            try:
                os.rename(origen+filename,destino+filename)
                loggingRudi.logInfo("se movio el archivo "+filename+" de "+origen+" a "+destino )
            except Exception as error:
                loggingRudi.logError("no se pudo recuperar "+filename)
                loggingRudi.logError(error)