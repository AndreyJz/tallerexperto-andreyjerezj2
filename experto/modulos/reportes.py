import os

lstBajo = []
lstNormal = []

def EstInscritos(campers:dict):
    os.system('cls')
    idx=0
    print('Estos son los estudiantes inscritos:\n')
    print('-----------------------------------------')
    for key,value in campers.items():
        if (campers[key]['estado'] == 'inscrito'):

            print(f'{idx+1}. {(campers[key]["id"])} -- {campers[key]["nombre"]}')
            idx=idx+1
    print('-----------------------------------------\n')
    
def EstAprobados(campers:dict):
    os.system('cls')
    idx=0
    print('Estos son los estudiantes que aprobaron el examen inicial:\n')
    print('-----------------------------------------')
    for key,value in campers.items():
        if (campers[key]['estado'] == 'aprobado'):

            print(f'{idx+1}. {(campers[key]["id"])} -- {campers[key]["nombre"]}')
            idx=idx+1
    print('-----------------------------------------\n')

def Trainers(Trainers:dict):
    os.system('cls')
    idx=0
    print('Estos son los Trainers que trabajan en CampusLands:\n')
    print('-----------------------------------------')
    for key,value in Trainers.items():
        print(f'{idx+1}. {key}')
        idx=idx+1
    print('-----------------------------------------\n')
        
def EstRiesgo(campers:dict):
    os.system('cls')
    idx=0
    print('Estos son los estudiantes que tienen un bajo rendimiento:\n')
    print('-----------------------------------------')
    for key,value in campers.items():
        if (campers[key]['rendimiento'] == 'bajo'):

            print(f'{idx+1}. {(campers[key]["id"])} -- {campers[key]["nombre"]}')
            idx=idx+1
    print('-----------------------------------------\n')
    
def EstTrainEnRuta(campers:dict,Trainers:dict,matriculas:dict):
    os.system('cls')
    op = int(input('Si desea ver los campers digite 1 y si desea ver los trainers digite 2 '))
    if (op==1):
        idx=0
        print('Estos son los estudiantes que estan en una ruta:\n')
        print('-----------------------------------------')
        for key,value in campers.items():
            if (campers[key]['ruta?'] == 'en ruta'):
                for llave,valor in matriculas.items():
                    if campers[key]["id"] in (matriculas.get(llave).get('estudiantes')):
                        print(f'{idx+1}. {(campers[key]["id"])} y se encuentra en la matricula {llave}')
                        idx=idx+1
        print('-----------------------------------------\n')
        
    elif (op==2):
        idx=0
        print('Estos son los trainers que estan en una ruta:\n')
        print('-----------------------------------------')
        for key,value in Trainers.items():
            if (len(Trainers[key]['rutas']) != 0):

                print(f'{idx+1}. {key} y se encuentra en {len(Trainers[key]["rutas"])} rutas')
                idx=idx+1
        print('-----------------------------------------\n')
        
    else:
        print('Ese dato no es ni 1 ni 2...')
        os.system('pause')
        EstTrainEnRuta(campers,Trainers,matriculas)
        
def CampersAprovnt(campers:dict,matriculas:dict):
    os.system('cls')
    op = int(input('Si desea ver los campers en riesgo digite 1 y si desea ver los campers que van bien digite 2 '))
    if (op==1):
        idx=0
        print('Estos son los estudiantes que tienen un bajo rendimiento:')
        print('-----------------------------------------\n')
        for key,value in campers.items():
            if (campers[key]['rendimiento'] == 'bajo'):

                print(f'{idx+1}. {(campers[key]["id"])} -- {campers[key]["nombre"]}')
                idx=idx+1
                lstBajo.append(campers[key]['id'])
                
                for llave,valor in matriculas.items():
                    if campers[key]['id'] in matriculas[llave]['estudiantes']:
                        print(f'El estudiante reprobo el modulo {matriculas[llave]["ruta"]["ejetematico"]} con el Trainer {matriculas[llave]["trainer"]["trainer"]}\n')
        print('-----------------------------------------\n')
        print(f'El total de Campers en Riesgo es: {len(lstBajo)}')
    
    
    elif (op==2):
        idx=0
        print('Estos son los estudiantes que van con buen rendimiento:')
        print('-----------------------------------------\n')
        for key,value in campers.items():
            if (campers[key]['rendimiento'] == 'normal'):

                print(f'{idx+1}. {(campers[key]["id"])} -- {campers[key]["nombre"]}')
                idx=idx+1
                lstNormal.append(campers[key]['id'])
                
                for llave,valor in matriculas.items():
                    if campers[key]['id'] in matriculas[llave]['estudiantes']:
                        print(f'El estudiante aprobo el modulo {matriculas[llave]["ruta"]["ejetematico"]} con el Trainer {matriculas[llave]["trainer"]["trainer"]}\n')
        print('-----------------------------------------\n')
        print(f'El total de Campers que van bien es: {len(lstNormal)}')

    else:
        print('Ese dato no es ni 1 ni 2...')
        os.system('pause')
        CampersAprovnt(campers,matriculas)