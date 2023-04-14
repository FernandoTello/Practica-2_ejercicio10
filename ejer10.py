import string
def calcular_promedio(notas):
    return sum(notas)/len(notas)

def estructura_alumnos_notas(nombres,notas_1,notas_2):          #A     
    #quito todos los signos de puntuacion de la cadena nombres
    for i in string.punctuation:
        nombres=nombres.replace(i,' ')
    nombres=nombres.lower().split()
    notas= list(map(lambda x,y: [x,y],notas_1,notas_2))
    alumnos = {nombres:notas for (nombres,notas) in zip(nombres,notas)}
    return alumnos

def promedio_por_estudiante(alumnos):                             #B
    for elemento in alumnos.items():
        print(f'El estudiante {elemento[0]} tiene promedio {calcular_promedio(elemento[1])}')

def promedio_general(alumnos):                                                    #C
    promedios_estudiantes = [calcular_promedio(elemento) for elemento in alumnos.values()]
    print(f'el promedio general es de: {round(calcular_promedio(promedios_estudiantes),2)}')

def estudiante_promedio_alto(alumnos):                                  #D
    print(max(alumnos.items(), key=lambda x: calcular_promedio(x[1]))[0])

def estudiante_nota_baja(alumnos):                                         #E
    print(min(alumnos.items(), key=lambda x:x[1])[0])

nombres = ''' 
'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

alumnos = estructura_alumnos_notas(nombres,notas_1,notas_2)
option = input('''Elija la accion a realizar: 
                A: Mostrar estructura que almacena alumnos y notas.
                B: Calcular el promedio de notas de cada estudiante.
                C: Calcular el promedio general del curso.
                D: Identificar al estudiante con la nota promedio más alta.
                E: Identificar al estudiante con la nota más baja.
                ''').upper()
match option:
    case 'A':
        print(alumnos)
    case 'B':
        promedio_por_estudiante(alumnos)
    case 'C':
        promedio_general(alumnos)
    case 'D':
        estudiante_promedio_alto(alumnos)
    case 'E':
        estudiante_nota_baja(alumnos)
    case _:
        print('No se eligio ninguna opcion disponible')
