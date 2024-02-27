import os

lstAprobados=[]

def addRuta(campus:dict):
    
    while True:
        idx = 0
        for key,value in campus['rutas'].items():
            print(f'{idx+1}. {key}')
            idx=idx+1
        ruta = input('\nEstas son las rutas, por favor escoja una ingresando el nombre de la misma: ')
        print('\n')
        data = campus['rutas'].get(ruta,False)    
        if ruta in campus['rutas']:
            idx = 0
            for key,value in campus['rutas'][ruta].items():
                print(f'{idx+1}. {key}')
                idx=idx+1
            ejetematico = input('\nEstos son los Ejes Tematicos, por favor escoja uno ingresando el nombre del mismo: ')
            print('\n')
            if ejetematico in campus['rutas'][ruta]:
                idx=0
                myStack = []
                PickStack=True
                while PickStack:
                    print('\nEstos son los stacks:\n')
                    for idx,item in enumerate(campus['rutas'][ruta][ejetematico]):
                        if len(myStack) == 0:
                            print(f'{idx+1}. {item}')
                            idx=idx+1
                        else:
                                if campus['rutas'][ruta][ejetematico][idx] not in myStack:
                                    print(f'{idx+1}. {item}')
                                    idx=idx+1
                    PickStack=True
                    stacks = input('\nPor favor escoja los stacks que desee ingresando el nombre del mismo: ')
                    
                    if stacks in campus['rutas'][ruta][ejetematico]:
                        myStack.append(stacks)
                    else:
                        print('Ese stack no esta en la lista')
                        os.system('pause')
                        
                    if len(myStack) != len(campus['rutas'][ruta][ejetematico]):
                        PickStack = bool(input('Desea seguir agregando Stacks? S(si) o Enter(no) '))
                        if PickStack == False:
                            if len(myStack) == 0:
                                print('No puedes pasar a la sieguiente seccion hasta que no pongas al menos un stack..')
                                os.system('pause')

                            RutaALLIN = {
                                'ruta':ruta,
                                'ejetematico':ejetematico,
                                'stacks':myStack,
                                }
                            
                            return RutaALLIN
                        
                    
                    
                   
                    
                    
            else:
                print('Ese Eje Tematico no esta en la lista')
                os.system('pause')
                
        else:
            print('Esa ruta no esta en la lista')
            os.system('pause')
        
