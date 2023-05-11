aprobado = 0
promedio=0
for i in (0,5,1):
    for p in (0,5,1):
        nota=int(input("Ingrese la nota"))
        promedio=promedio+nota
        
    total=promedio/5
    print("---------------------------------------")

    if total>6:
        aprobado+=1

print("Lo alumnos con derecho a aprobación son", aprobado)