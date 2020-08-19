import pymysql


def get_data_BD():
    archivo = open("valuesBD.txt","r")
    lineas = archivo.readlines()
    host,username,password,nombreBD = None,None,None,None
    for lin in lineas:
        val = lin.split(" ")
        val[2] = val[2][:len(val[2])-1]
        if val[0] == "HOSTNAME":
            host = val[2]
        elif val[0] == "USERNAME":
            username = val[2]
        elif val[0] == "PASSWORD":
            password = val[2]
        else:
            nombreBD = val[2]
    archivo.close()
    return host,username,password,nombreBD

# Función para abrir una conexion con la base de datos
def conexion_DB(host,username,password,nombreBD):
    db = None
    try:
        db = pymysql.connect(host,username,password,nombreBD)
    except:
        print("Fallo conexion con la BD")
    return db


def autenticate(username,password):

    a,b,c,d = get_data_BD()
    conexion = conexion_DB(a,b,c,d)
    if conexion == None:
        return False
    else:
        #Preparando un curso para la consulta
        cursor = conexion.cursor()
        estado = 0
        cursor.execute("SELECT count(*) FROM General_usuario where username = \""+username+"\" and password = \""+password+"\"")
        results = cursor.fetchone()
        if str(results) == "(1,)":
            estado = 1
         # desconecta del servidor
        conexion.close()
        if estado:
            return True
        else:
            return False