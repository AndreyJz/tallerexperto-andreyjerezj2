import os



def addTrainer(Trainers:dict):
    nombre=input('Ingrese el Nombre del Trainer: ')
    
    trainer = {
        # 'horario':horarios,
        'horario':{
            'mañana':['6am-10am','10am-2pm'],
            'tarde':['2pm-6pm','6pm-10pm'],
            },
        'ocupado':[],
        'rutas':[]
    }
    Trainers.update({nombre:trainer})

def addTrainerRuta(Trainers:dict,matriculas:dict):
    isRunning = True
    while isRunning:
        idx = 0
        for key,value in Trainers.items():
            print(f'{idx+1}. {key}')
            idx=idx+1
        Trainer = input('\nEstos son los trainers, por favor escoja uno ingresando el nombre del mismo: ')
        print('\n')
        if Trainer in Trainers:
            idx = 0
            for key,value in Trainers[Trainer]['horario'].items():
                print(f'{idx+1}. {key}')
                idx=idx+1
            jornada= (input(f'\nEstos son las jornadas de {Trainer}, por favor escoja uno ingresando el nombre del mismo: '))
            print('\n')
            if jornada in Trainers[Trainer]['horario']:
                idx = 0
                for idx,item in enumerate(Trainers[Trainer]['horario'][jornada]):
                    if len(Trainers[Trainer]['rutas']) == 0:
                        print(f'{idx+1}. {item}')
                        idx=idx+1
                    else:
                        for llave,valor in matriculas.items():
                            if Trainers[Trainer]['horario'][jornada][idx] not in Trainers[Trainer]['ocupado']:
                                
                                print(f'{idx+1}. {item}')
                                idx=idx+1
                ub = int(input(f'\nEsos son las horas de {Trainer}, por favor escoja uno ingresando el numero del indice del mismo: '))
                if (ub != 1) and (ub != 2):
                    print('Ese numero no esta en la lista')
                    os.system('pause')
                    addTrainerRuta(Trainers,matriculas)
                else:
                    Horario = Trainers[Trainer]['horario'][jornada][ub-1]
                    if Horario in Trainers[Trainer]['horario'][jornada]:
                        TrainerALLIN = {
                            'trainer':Trainer,
                            'horario':Horario,
                        }
                        
                        return TrainerALLIN
                        isRunning=False
                    else:
                        print('Ese horario no esta en la lista')
                        os.system('pause')
            else:
                print('Esa jornada no esta en la lista')
                os.system('pause')
        else:
            print('Ese trainer no esta en la lista')
            os.system('pause')
    
    
    
    