import os


def addSalonRuta(salones:dict,matriculas:dict,TrainerALLIN:dict):
    while True:
        idx=0
        for key,value in salones.items():
            if len(salones[key]['rutas']) == 0:
                print(f'{idx+1}. {key}')
                idx=idx+1
            else:
                for llave,valor in matriculas.items():
                    if TrainerALLIN['horario'] not in salones[key]['horario']:
                        
                        print(f'{idx+1}. {key}')
                        idx=idx+1
        
        Salon = input('\nEstos son los salones, por favor escoja uno ingresando el nombre del mismo: ')
        
        if Salon in salones:
            return Salon
        else:
            print('Ese salon no esta en la lista')
            os.system('pause')
        
    