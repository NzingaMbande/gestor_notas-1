import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

lista_alumnos = [
    {'nombre': 'pepe', 'nota': 10.0},
    {'nombre': 'paolo', 'nota': 4.0},
    {'nombre': 'aria', 'nota': 3.5},
    {'nombre': 'ana', 'nota': 8.0},
    {'nombre': 'carlos', 'nota': 7.0},
    {'nombre': 'teresa', 'nota': 6.0}

    ]

def mostrar_nota_media(notas):
    return sum(notas) / len(notas)


def main():

    continuar = True

    # * El menú debe repetirse hasta que el usuario elija la opción  Salir.
    while True:
        # El programa debe incluir un menú interactivo con las siguientes opciones:
        print(''' Gestor de tareas interactivo
            1.- Mostrar todos los alumnos
            2.- Nota media del grupo de alumnos
            3.- Mostrar alumnos aprobados
            4.- Mostrar estadísticas de la clase
            5.- Buscar alumno por nombre
            6.- Salir
            ''')
        opcion = input('Elige una opcion')
        op = int(opcion)

        if op >= 1 and op<=6:

            match opcion:
                case '1': 
                    #    * Imprimir la lista completa de alumnos con todos sus datos.
                    if not lista_alumnos:
                        print('No tiene alumnos')
                    else:
                        for a in lista_alumnos:
                            print(a)

                    # nota_c = True

                    # nombre = input('Introducir Nombre del Alumno')
                    
                    # # while not nombre.isalpha():  #while True
                    # #     print("Error: El nombre no puede contener numeros o simbolos")
                    # #     nombre = input('Introducir Nombre del Alumno')

                    # while True:
                    #     nombre = input('Introducir Nombre del Alumno')
                    #     if nombre:
                    #         break
                    #     else:
                    #         print("La entrada no puede estar vacia")

                    # # edad = int(input("Introducir Edad del Alumno: "))

                    # # while not (edad > 0 and edad <= 65):
                    # #     print("Error: La edad debe estar entre 1 y 65")
                    # #     edad = int(input("Introducir Edad del Alumno: "))
                    
                    # #isdigit() valores numericos
                    
                    # #sus validaciones no me funcionan desde mi proyecto
                    # while True:
                    #     try:
                    #         edad = int(input("Introducir Edad del Alumno: "))
                    #         break
                    #     except ValueError:
                    #         print("La entrada debe ser numerico")

            
                    # # Si la nota no es valida, te la seguira pidiendo hasta que sea correcta
                    # # while nota_c == True:
                    # #     nota = int(input('Introducir Nota Final'))
                    # #     if (nota >=0 and nota<=10):
                    # #         ficha = (nombre,edad,nota)
                    # #         # Guardar los datos como una tupla (nombre, edad, nota) dentro de una  lista de alumnos .
                    # #         lista_alumnos.append(ficha)
                    # #         nota_c = False
                    # #     else: nota_c = True
                    # # print(lista_alumnos)

                    # while True:
                    #     try:
                    #         nota = int(input('Introducir Nota Final'))
                    #         if not (nota >= 0 and nota <= 10):
                    #             break
                    #         else:
                    #             print("La nota debe ser comprendida entre 0 y 10")
                    #     except ValueError:
                    #         print("La nota debe ser numerico")


                case '2': 
                    nota = mostrar_nota_media(notas)
                    print(f'La nota media es: {float(nota)}')
                case '3':
                    #    * Mostrar solo los alumnos cuya nota final sea mayor o igual a 5.
                    if not lista_alumnos:
                        print('No tiene alumnos')
                    else:
                        # for alumno in lista_alumnos:
                        #         nombre, edad, nota = alumno
                        #         if nota >= 5:
                        #             print("Alumno aprobado:")
                        #             print(f"Nombre: {nombre}")
                        #             print(f"Edad: {edad}")
                        #             print(f"Nota: {nota}")
                        #             print('-----------------')                    

                        for a in lista_alumnos:
                            if a[2] >= 5:
                                print(a[0])

                case '4':
                    # Se calcula la Media, la Nota Mayor y la Nota Menor de la Clase
                    # suma = mayor = 0
                    # menor = 10
                    if not lista_alumnos:
                        print('No tiene alumnos')
                    else:
                        notas = [a[2] for a in lista_alumnos]
                        media = sum(notas) / len(lista_alumnos)

                        # x = len(lista_alumnos)
                        # for alumno in lista_alumnos:
                        #         _, _, nota = alumno
                        #         suma += nota 
                        #         if (nota > mayor): mayor = nota
                        #         if (nota < menor): menor = nota

                        
                        print(f'La media es {media:.2f}')
                        print(f'La nota mas alta de la clase es {max(notas)}')
                        print(f'La nota mas baja de la clase es {min(notas)}')


                case '5':
                    # if not lista_alumnos:
                    #     print('No tiene alumnos')
                    # else:
                    #     nom = input('Introducir nombre a buscar')
                    #     for alumno in lista_alumnos:
                    #             nombre, edad, nota = alumno
                    #             if ((nom.lower() == nombre) or (nom.upper() == nombre)): 
                    #                 print("Alumno:")
                    #                 print(f"Nombre: {nombre}")
                    #                 print(f"Edad: {edad}")
                    #                 print(f"Nota: {nota}")
                    #                 print('-----------------')                                                
                    #                 existe = True
                    #             else: existe = False

                    # if existe == False:
                    #     print('El nombre no se ha encontrado')

                    busqueda = input('Introducir nombre a buscar')
                    encontrados = [a for a in lista_alumnos if a[0].lower() == busqueda.lower()]            

                    if encontrados:
                        for e in encontrados:
                            print(e)
                    else:
                        print('No hay coincidencia para un estudiante')

                case '6':
                    # 6. Salir
                    #    * Finalizar la ejecución del programa.

                    print('Adios salir')
                    time.sleep(2)
                    continuar = False
                case _: 
                    if not ('1','2','3','4','5','6'):
                        print('opcion no contemplada')


        if opcion in ('1','2','3','4','5','6'):
            os.system('cls' if os.name == 'nt' else 'clear')

#llamamos al main
if __name__ == '__main__':
    main()


