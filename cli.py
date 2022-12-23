import sys
import recuperarDia
import resguardarMes
import loggingRudi

fecha = sys.argv[1]
tramite = sys.argv[2].upper()
loggingRudi.logInfo("parametros de entrada: fecha: " + fecha + " tramite: " + tramite)


#si el parametro es de 10 caracteres es una fecha yyyy-mm-dd
#si el parametro es de 7 caracteres es un mes yyyy-mm
#si el parametro es de 6 caracteres es un año yyyy-m pasarlo a yyyy-0m
#el tramite debe tener 4 caracteres
def main():
    if len(fecha) == 10 and len(tramite) == 4:
        yyyy = fecha[0:4]
        mm = fecha[5:7]
        dd = fecha[8:10]
        recuperarDia.recuperarDia(int(yyyy),int(mm),int(dd),tramite)
    elif len(fecha) == 7 and len(tramite) == 4:
        yyyy = fecha[0:4]
        mm = fecha[5:7]
        resguardarMes.resguardarMes(int(yyyy),int(mm),tramite)
    elif len(fecha) == 6 and len(tramite) == 4:
        yyyy = fecha[0:4]
        mm = fecha[5:6]
        resguardarMes.resguardarMes(int(yyyy),int(mm),tramite)
    else:
        loggingRudi.logError("la fecha o el tramite no son validos")
        loggingRudi.logInfo("el formato de la fecha debe ser yyy-mm-dd para recuperar un dia")
        loggingRudi.logInfo("el formato para resguardar un mes debe ser yyyy-mm o yyyy-m ")
        loggingRudi.logInfo("los tramites deben contar con 4 caracteres ")
        print("la fecha o el tramite no son validos")

main()