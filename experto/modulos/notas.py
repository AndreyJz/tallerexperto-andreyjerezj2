import os

lstInscritos = []
lstAprobadosEnRuta=[]


def addNotasIniciales(campers:dict):
    addNotasIniciale=True
    while addNotasIniciale:
        idx=0
        print('Estos son los estudiantes inscritos:\n')
        for key,value in campers.items():
            if (campers[key]['estado'] == 'inscrito'):

                print(f'{idx+1}. {campers[key]["id"]} -- {campers[key]["nombre"]}')
                idx=idx+1
                lstInscritos.append(campers[key]['id'])
                
        id=int(input('Ingrese el Id del estudiante al que le ingresara las notas: '))
        if id in lstInscritos:
            Teorica=int(input('Ingrese la nota de la Prueba Teorica: '))
            Practica=int(input('Ingrese la nota de la Prueba Practica: '))
            Final=((Teorica*0.3)+(Practica*0.7))
            if Final >= 60:
                print(f'El estudiante fue aprobado con una nota Final de {Final}.')
                campers[id]['estado'] = 'aprobado'
            elif Final < 60:
                print(f'El estudiante no fue aprobado con una nota Final de {Final}.')
            addNotasIniciale=False
        else:
            print('Ese Id no esta en la lista')
            os.system('pause')

def addNotasModulo(campers:dict,matriculas:dict):
    addNotasModul=True
    while addNotasModul:
        idx=0
        print('Estos son los estudiantes aprobados que estan en una ruta:\n')
        for key,value in campers.items():
            if (campers[key]['estado'] == 'aprobado') and (campers[key]['ruta?'] == 'en ruta'):
                if (campers[key]['rendimiento'] != 'normal') or (campers[key]['rendimiento'] != 'bajo'):
                    print(f'{idx+1}. {(campers[key]["id"])} -- {campers[key]["nombre"]}')
                    idx=idx+1
                    lstAprobadosEnRuta.append(campers[key]['id'])
        
        FinalModulo=0
        Modulo=0
        id=int(input('Ingrese el Id del estudiante al que le ingresara las notas: '))
        if id in lstAprobadosEnRuta:
            Teorica=int(input('Ingrese la nota de la Prueba Teorica: '))
            Practica=int(input('Ingrese la nota de la Prueba Practica: '))
            for llave,valor in matriculas.items():
                if id in matriculas[llave]['estudiantes']:
                    for i in range(len(matriculas[llave]['ruta']['stacks'])):
                        notaModulo = int(input(f'Ingrese la nota del stack {matriculas[llave]["ruta"]["stacks"][i]} '))
                        Modulo += notaModulo
            FinalModulo = Modulo/len(matriculas[llave]['ruta']['stacks'])
            Final=((Teorica*0.3)+(Practica*0.6)+(FinalModulo*0.1))
            if Final >= 60:
                print(f'El estudiante aprobo el modulo {matriculas[llave]["ruta"]["ejetematico"]} con una nota Final de {Final}.')
                campers[id]['rendimiento'] = 'normal'
            elif Final < 60:
                print(f'El estudiante no aprobo el modulo {matriculas[llave]["ruta"]["ejetematico"]} con una nota Final de {Final}.')
                campers[id]['rendimiento'] = 'bajo'

        else:
            print('Ese Id no esta en la lista')
            os.system('pause')
        addNotasModul=bool(input('Desea agregar Notas de Modulo a otro Estudiante? S(Si) o Enter(No) '))
    