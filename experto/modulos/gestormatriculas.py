import os


lstAprobadosSinRuta=[]
def gestarMatricula(campus:dict,RutaALLIN:dict,TrainerALLIN:dict,Salon):
    ismatricula=True
    while ismatricula:
    
        NombreGrupo= (input('Ingrese el nombre del grupo para la matricula: '))
        
        data = campus['matriculas'].get(NombreGrupo,False)
        if type(data) == dict:
            print(f'Ya existe un grupo con el nombre {NombreGrupo}.')
            os.system('pause')
        elif (type(data) == bool) and (data == False):
                    
            FechaIn=input('ingrese la fecha de inicio para la matricula (mes y año): ')
            FechaFin=input('ingrese la fecha de Final para la matricula (mes y año): ')
            
            idx=0
            print('Estos son los estudiantes aprobados que aun no se les ha asignado una ruta:\n')
            for key,value in campus['camper'].items():
                if (campus['camper'][key]['estado'] == 'aprobado') and (campus['camper'][key]['ruta?'] == 'sin ruta'):

                    print(f'{idx+1}. {(campus["camper"][key]["id"])} -- {campus["camper"][key]["nombre"]}')
                    idx=idx+1
                    lstAprobadosSinRuta.append(campus['camper'][key]['id'])
            
            matricula = {
                'trainer':TrainerALLIN,
                'ruta':RutaALLIN,
                'salon':Salon,
                'capacidad':33,
                'estudiantes':[],
                'FechaIn':FechaIn,
                'FechaFin':FechaFin
            }
            
            addId=True
            i=0
            while addId:
                if len(matricula['estudiantes']) <= matricula['capacidad']:
                    id=int(input(f'\nIngrese el Id del estudiante al que quiere asignarle esta ruta (Solo pueden haber 33 estudiantes por ruta) {i+1}/33: '))
                    if id in lstAprobadosSinRuta:
                        matricula['estudiantes'].append(id)
                        campus['camper'][id]['ruta?'] = 'en ruta'
                        i+=1
                        if len(matricula['estudiantes']) != matricula['capacidad']:
                            addId = bool(input('Desea seguir agregando Estudiantes a la ruta? S(si) o Enter(no) '))
                        else:
                            break
                        if addId == False:
                            break
                    else:
                        print('Ese id no esta en la lista de aprobados...')
                        os.system('pause')

                else:
                    print('Limite de 33 personas por ruta alcanzado...')
                    os.system('pause')
                    break
                

            campus['matriculas'].update({NombreGrupo:matricula})
            Horario = campus['matriculas'][NombreGrupo]['trainer']['horario']
            Salon = campus['matriculas'][NombreGrupo]['salon']
            Trainer = campus['matriculas'][NombreGrupo]["trainer"]["trainer"]
            campus['trainer'][Trainer]['rutas'].append(NombreGrupo)
            campus['trainer'][Trainer]['ocupado'].append(Horario)
            campus['Areas'][Salon]['rutas'].append(NombreGrupo)
            campus['Areas'][Salon]['horario'].append(Horario)

            ismatricula=False