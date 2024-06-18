import funciones as fn


trabajadores = []
print(trabajadores)

while True:
    print("Bienvenidos al super sistema de pago de sueldo")
    print("1.Registrar trabajador:")
    print("2.Listar los Trabajadores:")
    print("3.Imprimir Planilla De Sueldo")
    print("4.Salir")

    opcion = int(input("ingrese su opcion: "))

    if opcion == 1:
        fn.registrar_trabajador(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)
        print(trabajadores)
    elif opcion == 3:
        fn.imprimir_plantillas(trabajadores)
    elif opcion == 4:
        break
    else:
        print("opcion no valida,seleccione nuevamente")
