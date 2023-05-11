menor50 = 0
de50a70 = 0
de70a80 = 0
mayor80 = 0

cantidad_estudiantes = int(input("¿Cuál es la cantidad de estudiantes? "))

for i in range(cantidad_estudiantes):
    califi = int(input("¿Cuál fue la calificación del estudiante? "))

    if califi < 50:
        menor50 += 1
    elif califi >= 50 and califi < 70:
        de50a70 += 1
    elif califi >= 70 and califi < 80:
        de70a80 += 1
    else:
        mayor80 += 1

print("Estudiantes con una calificación menor a 50:", menor50)
print("Estudiantes con una calificación entre 50 y 70:", de50a70)
print("Estudiantes con una calificación entre 70 y 80:", de70a80)
print("Estudiantes con una calificación mayor o igual a 80:", mayor80)
