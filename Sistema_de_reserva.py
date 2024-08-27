Usuario = []
Reserva = []
Mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre" , "Noviembre", "Diciembre"]
Lugares = ["Paris", "Quito", "Rido de janerio", "Buenos Aires"]

def Lugar():
    print("")
    print("*" * 15, "Destinos", "*" * 15)
    for l in Lugares:
        print(l)
    print("*" * 40)


def Menu_reserva():
    while True:
        print("")
        print("-" * 31, "Menu", "-" * 31)
        print("1. Registrar usuario")
        print("2. Realizar reserva")
        print("3. Mostrar reserva")
        print("4. Actualizar reserva")
        print("5. Cancelar reserva")
        print("6. Salir del sistema")
        print("")
        opcion = input("Eliga una opcion: ")
        print("-" * 68)
        print("")
        if opcion == "6":
            print("Cerrando el sistema...")
            print("")
            break
        elif opcion == "1":
            Registrar_usuario()
        elif opcion == "2":
            Realizar_reserva()
        elif opcion == "3":
            Mostrar_reserva()
        elif opcion == "4":
            Actualizar()
        elif opcion == "5":
            Cancelar()
        else:
            print("Opcion no valida")

def Registrar_usuario():
    print("¿Ha nombre de quien estara la reservar?")
    Name = input()
    if Name in Usuario:
        print("El nombra ya ha sido registrado antes")
    else:
        Usuario.append(Name)
        print("Nombre registrado")

def Realizar_reserva():
    nombre = input("Escriba su nombre y apellido: ")
    if any(nombre.lower() == User.lower() for User in Usuario):
        Lugar()
        print("")
        Destino = input("Elija su destino: ")
        if any(Destino.lower() == lug.lower() for lug in Lugares):
            print("Destino registrado")
            print("")
            fecha_n = int(input("Ingrese el día: "))
            fecha_m = input("Ingrese el mes: ").lower()  
            
            if fecha_n >= 1 and any(fecha_m == m.lower() for m in Mes):
                if fecha_m == "febrero" and fecha_n <= 28:  
                    print("Fecha registrada")
                    registro = {"nombre": nombre, "destino": Destino.capitalize(), "dia": fecha_n, "mes": fecha_m.capitalize()}
                    Reserva.append(registro)
                    print("")
                    print("¡Viaje reservado con éxito!")
                    return
                elif fecha_m in ["abril", "junio", "septiembre", "noviembre"] and fecha_n <= 30:
                    print("Fecha registrada")
                    registro = {"nombre": nombre, "destino": Destino.capitalize(), "dia": fecha_n, "mes": fecha_m.capitalize()}
                    Reserva.append(registro)
                    print("")
                    print("¡Viaje reservado con éxito!")
                    return
                elif fecha_m in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"] and fecha_n <= 31:
                    print("Fecha registrada") 
                    registro = {"nombre": nombre, "destino": Destino.capitalize(), "dia": fecha_n, "mes": fecha_m.capitalize()}
                    Reserva.append(registro)
                    print("")
                    print("¡Viaje reservado con éxito!")
                    return
                else:
                    print(f"Día no válido dentro de {fecha_m.capitalize()}")
            else:
                print("Fecha no válida")
        else:
            print("Destino no presente")
    else:
        print("Debe registrar su nombre y apellido primero")

def Mostrar_reserva():
    if len(Reserva) == 0:
        print("No hay reservas")
    else:
        print("=" * 29, "Reservas", "=" * 29) 
        for reserva in Reserva:
            print(f"Nombre: {reserva['nombre']} / Destino: {reserva['destino']} / Fecha: {reserva['dia']} de {reserva['mes']} del 2024")
        print("=" * 68)

def Actualizar():
    if len(Reserva) == 0:
        print("Aun no hay reservas")
    else:
        nombre = input("Escriba su nombre y apellido: ")
        if any(nombre.lower() == user.lower() for user in Usuario):
            for reserva in Reserva:
                if reserva['nombre'].lower() == nombre.lower():
                        while True:
                            print("")
                            print("1. Destino")
                            print("2. Fecha")
                            print("3. Salir")
                            print("")
                            print("¿Qué actualizara? Si no desea actualizar presione \"Enter\"")
                            option = input()
                            if option == '1':
                                Lugar()
                                print("")
                                Destino_Nuevo = input("Elija su destino: ")
                                if any(Destino_Nuevo.lower() == lug.lower() for lug in Lugares):
                                    reserva['destino'] = Destino_Nuevo.capitalize()
                                    print("Destino actualizado")
                                    print("")
                                else:
                                    print("Destino no encontrado")
                                    print("")
                            elif option == '2':
                                print("")
                                dia = int(input("Ingrese el nuevo día: "))
                                mes = input("Ingrese el nuevo mes: ").lower()
                                if dia >= 1 and any(mes == m.lower() for m in Mes):
                                    if mes == "febrero" and dia < 28:
                                        reserva['dia'] = dia
                                        reserva['mes'] = mes.capitalize()
                                        print("Fecha de viaje actualizada")
                                    elif mes in ["abril", "junio", "septiembre", "noviembre"] and dia <= 30:
                                        reserva['dia'] = dia
                                        reserva['mes'] = mes.capitalize()
                                        print("Fecha de viaje actualizada")
                                    elif mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"] and dia <= 31:
                                        reserva['dia'] = dia
                                        reserva['mes'] = mes.capitalize()
                                        print("Fecha de viaje actualizada")
                                    else: 
                                        print(f"Día no valido dentro de {mes.capitalize()}")
                                        print("")
                                else:
                                    print("Fecha no valida")
                                    print("")
                            elif option == '3':
                                print("Terminando actualizacion..")
                                break
                            elif option == "":
                                print("Actualizacion no realizada")
                                break
                            else:
                                print("Opcion no valida")
                else:
                    print(f"No hay reservas a nombre de {nombre}")
        else:
            print("Nombre no registrado")

def Cancelar():
    if len(Reserva) == 0:
        print("No hay reservas aun")
    else:
        nombre = input("Escriba su nombre y apellido: ")
        if any(nombre.lower() == user.lower() for user in Usuario):
                for reserva in Reserva:
                    if reserva['nombre'].lower() == nombre.lower():
                        print("")
                        print("¿Seguro de querer cancelar la reserva?")
                        decision = input().lower()
                        if decision in ["si", "sí", "yes"]:
                            Reserva.remove(reserva)
                            print("Reserva cancelada")
                            return
                        elif decision in ["no", "not", ""]:
                            print("Reserva no cancelada")
                            return
                        else: 
                            print("Decisión no valida")
                    else:
                        print(f"No hay reservas a nombre de {nombre}")
        else:
            print("Nombre no registrado")

Menu_reserva()