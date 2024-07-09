Notas_ingles=[]

for i in range(1, 6):
    notas=float(input(f"Ingrese la nota {i}: "))
    Notas_ingles.append(notas)
    
suma = sum(Notas_ingles)

print(f"Promedio: {suma/5}")

