CARGOS = ['ceo', 'desarrollador', 'analista de datos']


def registrar_trabajador(trabajadores):
    nombre = input("ingrese nombre y apellido del trabajador: ")
    cargo = input(
        "Ingrese el cargo del trabajador (CEO/DESAROLLADOR/ANALISTA DE DATOS):").lower()
    while cargo not in CARGOS:
        print("cargo no existe, intente nuevamente")
        cargo = input(
            "Ingrese el cargo del trabajador (CEO/DESAROLLADOR/ANALISTA DE DATOS):").lower()
    sueldoBruto = int(input("ingrese sueldo bruto del trabajador: "))

    # calcular los descuentos
    descSalud = sueldoBruto * 0.07
    descAFP = sueldoBruto * 0.12
    liquidoPagar = sueldoBruto-descSalud-descAFP

    trabajadores.append({
        'nombre': nombre,
        'Cargo': cargo,
        'SueldoBruto': sueldoBruto,
        'DescSalud': descSalud,
        'DescAfp': descAFP,
        'LiquidoPagar': liquidoPagar,
    })


def listar_trabajadores(trabajadores):
    print('Lista de Trabajdores')
    for trabajador in trabajadores:
        print(trabajador)


def imprimir_plantillas(trabajadores):
    cargoSeleccionado = input(
        "Ingrese cargo para imprimir planilla o bien presione ENTER para seleccionar todos: ").lower()
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = "plantilla_todos.txt"
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador["Cargo"] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print("Cargo no valido")
        return

    with open(nombreArchivo, 'w')as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f'nombre y apellido:{trabajador["nombre"]}\n')
            archivo.write(f'cargo:{trabajador['Cargo']}\n')
            archivo.write(f'sueldo Burto: {trabajador["SueldoBruto"]}\n')
            archivo.write(f'desc De Salud : {trabajador["DescSalud"]}\n')
            archivo.write(f'Desc Afp: {trabajador["DescAfp"]}\n')
            archivo.write(f'liquido a Pagar: {trabajador["LiquidoPagar"]}\n\n')
