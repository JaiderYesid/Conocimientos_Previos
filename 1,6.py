
def opcion(opcion):
    if opcion == "1":
        peso = float(input("Ingrese su peso (Kilogramos): "))
        estatura = float(input("Ingrese su estatura (Metros): "))
        print("IMC: ", peso/estatura**2)
        
    elif opcion == "2":
        "masculino" == 10.8
        "femenino" == 0
        edad = int(input("Ingrese su Edad"))
        imc = float(input("Ingrese su IMC (Indice de Masa Corporal): "))
        genero = input("Ingrese su genero: ")
        print(f"Porcentage de Grasa Corporal: {1.2*imc+0.23*edad-5.4-genero}")
        