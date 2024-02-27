import modulos.campermodule as camp
import modulos.rutas as rut
import modulos.notas as notas
import modulos.gestormatriculas as gm
import modulos.menus as m
import modulos.trainers as t
import modulos.salones as s
import modulos.reportes as r

campus = {
    'camper':{},
    'rutas':{
        'Java':{
            'Fundamentos':['IntroducciónAlgoritmia', 'PSeInt', 'Python'],
            'web':['HTML', 'CSS', 'Bootstrap'],
            'formal':['Java', 'JavaScript', 'C#'],
            'BaseDatos':['Mysql', 'MongoDb', 'Postgresql'],
            'backend':['NetCore', 'SpringBoot', 'NodeJS', 'Express']
        },
        'NodeJS':{
            'Fundamentos':['IntroducciónAlgoritmia', 'PSeInt', 'Python'],
            'web':['HTML', 'CSS', 'Bootstrap'],
            'formal':['Java', 'JavaScript', 'C#'],
            'BaseDatos':['Mysql', 'MongoDb', 'Postgresql'],
            'backend':['NetCore', 'SpringBoot', 'NodeJS', 'Express']
        },
        'NetCore':{
            'Fundamentos':['IntroducciónAlgoritmia', 'PSeInt', 'Python'],
            'web':['HTML', 'CSS', 'Bootstrap'],
            'formal':['Java', 'JavaScript', 'C#'],
            'BaseDatos':['Mysql', 'MongoDb', 'Postgresql'],
            'backend':['NetCore', 'SpringBoot', 'NodeJS', 'Express']
        }
    },
    'trainer':{},
    'Areas':{
        'apolo':{
            'rutas':[],
            'horario':[]
            },
        'artemis':{
            'rutas':[],
            'horario':[]
            },
        'sputnik':{
            'rutas':[],
            'horario':[]
        }
    },
    'matriculas':{}
}



if __name__ == '__main__':
    isAppRunning = True
    while isAppRunning:
        op=m.CrearMenu()
        if (op == 1):
            isAddAlma = True
            while isAddAlma:
                rut.os.system('cls')
                camp.addCamper(campus.get('camper'))
                isAddAlma = bool(input('Desea agregar otro Estudiante? S(Si) o Enter(No) '))
        elif (op == 2):
            isAddNota = True
            while isAddNota:
                rut.os.system('cls')
                notas.addNotasIniciales(campus.get('camper'))
                isAddNota = bool(input('Desea agregar Notas del examen Inicial a otro Estudiante? S(Si) o Enter(No) '))
        elif (op == 3):
            isAddTrainer = True
            while isAddTrainer:
                rut.os.system('cls')
                t.addTrainer(campus.get('trainer'))
                isAddTrainer = bool(input('Desea agregar otro Trainer? S(Si) o Enter(No) '))
        elif (op == 4):
            isAddMatricula = True
            while isAddMatricula:
                rut.os.system('cls')
                RutaALLIN = rut.addRuta(campus)
                rut.os.system('cls')
                TrainerALLIN = t.addTrainerRuta(campus.get('trainer'),campus.get('matriculas'))
                rut.os.system('cls')
                Salon = s.addSalonRuta(campus.get('Areas'),campus.get('matriculas'),TrainerALLIN)
                rut.os.system('cls')
                gm.gestarMatricula(campus,RutaALLIN,TrainerALLIN,Salon)
                isAddMatricula = bool(input('Desea agregar otra Matricula? S(Si) o Enter(No) '))
        elif (op == 5):
            isAddNotaModulo = True
            while isAddNotaModulo:
                rut.os.system('cls')
                notas.addNotasModulo(campus.get('camper'),campus.get('matriculas'))
                isAddNotaModulo = bool(input('Desea agregar Notas de Modulo a otro Estudiante? S(Si) o Enter(No) '))
        elif (op == 6):
            viewReports=True
            while viewReports:
                rut.os.system('cls')
                opr=m.MenuRep()
                if (opr == 'a'):
                    viewA=True
                    while viewA:
                        r.EstInscritos(campus.get('camper'))
                        viewA = bool(input('\nDesea seguir mirando este apartado de reportes? S(si) o Enter(no) '))
                elif (opr == 'b'):
                    viewB=True
                    while viewB:
                        r.EstAprobados(campus.get('camper'))
                        viewB = bool(input('\nDesea seguir mirando este apartado de reportes? S(si) o Enter(no) '))
                elif (opr == 'c'):
                    viewC=True
                    while viewC:
                        r.Trainers(campus.get('trainer'))
                        viewC = bool(input('\nDesea seguir mirando este apartado de reportes? S(si) o Enter(no) '))
                elif (opr == 'd'):
                    viewD=True
                    while viewD:
                        r.EstRiesgo(campus.get('camper'))
                        viewD = bool(input('\nDesea seguir mirando este apartado de reportes? S(si) o Enter(no) '))
                elif (opr == 'e'):
                    viewE=True
                    while viewE:
                        r.EstTrainEnRuta(campus.get('camper'),campus.get('trainer'),campus.get('matriculas'))
                        viewE = bool(input('\nDesea seguir mirando este apartado de reportes? S(si) o Enter(no) '))
                elif (opr == 'f'):
                    viewF=True
                    while viewF:
                        r.CampersAprovnt(campus.get('camper'),campus.get('matriculas'))
                        viewF = bool(input('\nDesea seguir mirando este apartado de reportes? S(si) o Enter(no) '))
                elif (opr == 'g'):
                    viewReports = False
        elif (op == 7):
            print('-----Gracias por Usar La Base de Datos de CAMPUSLANDS-----')
            print('No disfruto de tiempo de sueño desde mas de dos semanas!! :D')
            print('*Vuelva pronto (no tan pronto...)*')
            isAppRunning=False
    

