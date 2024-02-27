import os

def addCamper(campers):
    id=int(input('Ingrese el Id: '))
    data = campers.get(id,False)
    if type(data) == dict:
        print(f'Ya existe un estudiante con id {id}, ingrese otro.')
        os.system('pause')
        addCamper(campers)
    else:
        nombre=input('Ingrese el Nombre: ')
        apellido=input('Ingrese el Apellido: ')
        direccion=input('Ingrese el Direccion: ')
        movil=int(input('Ingrese el Telefono movil: '))
        fijo=int(input('Ingrese el Telefono fijo: '))
        acudiente=input('Ingrese el nombre del acudiente: ')
        tel=int(input('Ingrese el telefono del acudiente: '))
        cc=int(input('Ingrese la cedula del acudiente: '))
        camper = {
            'id':id,
            'nombre':nombre,
            'apellido':apellido,
            'direccion':direccion,
            'movil':movil,
            'fijo':fijo,
            'acudiente':{'cc':{
                'cc':cc,
                'nombre':acudiente,
                'telefono':tel
            }},
            'estado':'inscrito',
            'ruta?':'sin ruta',
            'rendimiento':''
        }
        campers.update({id:camper})