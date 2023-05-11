candi1 = 0
candi2 = 0
candi3 = 0
for x in range(0, 5, 1):
    voto = int(input(
        "Elija el numero del candidato por el cual va a votar 1. Valery 2. Pily 3. Karla"))
    if voto == 1:
        candi1 += 1
    elif voto == 2:
        candi2 += 1
    elif voto == 3:
        candi3 += 1

if candi1 > candi2 and candi1 > candi3:
    print("el candidato 1 ha ganado con la cantidad de votos", candi1)
elif candi2 > candi1 and candi2 > candi3:
    print("el candidato 2 ha ganado con la cantidad de votos", candi2)
elif candi3 > candi1 and candi3 > candi2:
    print("el candidato 3 ha ganado con la cantidad de votos", candi3)
