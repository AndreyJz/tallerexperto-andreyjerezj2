import os

def CrearMenu():
    lstOpciones = [1,2,3,4,5,6,7]
    titulo = """
        ++++++++++++++++++++++++++++++++++++++++
        +   RECOLECTOR DE ALMAS (CAMPUSLANDS)  +
        ++++++++++++++++++++++++++++++++++++++++
    """
    os.system('cls')
    print(titulo)
    try:
        opciones = "1. Registrar Camper\n2. Registrar Notas Examen Inicial\n3. Registrar Trainer\n4. Asignar Matricula\n5. Registrar Notas Modulo\n6. Reportes\n7. Salir\n"
        print(opciones)
        op =int(input(':) '))
        if (op not in lstOpciones):
            print('Ese dato no esta en las opciones')
            os.system('pause')
            CrearMenu()
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        CrearMenu()
    else:
        return op

def MenuRep():
    lstOpciones =  ['a','b','c','d','e','f','g']
    titulo = """
        ++++++++++++++++++++++++++++
        +   REPORTES CAMPUSLANDS   +
        ++++++++++++++++++++++++++++
    """
    os.system('cls')
    print(titulo)
    try:
        opciones = 'a. Campers en estado de inscrito.\nb. Campers que aprobaron el examen inicial.\nc. Entrenadores que se encuentran trabajando con campuslands.\nd. Estudiantes que cuentan con bajo rendimiento.\ne. Campers y entrenador que se encuentran asociados a una ruta de entrenamiento.\nf. Campers que perdieron y aprobaron cada uno de los modulos\ng. Salir\n'
        print(opciones)
        opr =str(input('Ingrese la letra en minuscula del apartado al que desea ingresar ')).lower()
        if (opr not in lstOpciones):
            print('Ese dato no esta en las opciones')
            os.system('pause')
            CrearMenu()
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        CrearMenu()
    else:
        return opr
    