for i in range(0, 5):
    compra = int(input("Ingrese el total de la compra, por favor"))
    bolita = int(input(
        "Ingrese el numero de la bolita que ha sacado 1.Roja, 2.Amarilla, 3.Blanca"))

    if bolita == 1:
        descuento = compra*40/100
        totalcom = compra-descuento
        print("El total de su compra es: ", totalcom)
        print("El descuento es de: ", descuento)
    elif bolita == 2:
        descuento1 = compra*25/100
        totalcomp = compra-descuento
        print("El total de su compra es: ", totalcomp)
        print("El descuento es de: ", descuento1)
    elif bolita == 3:
        print("El total de su compra es: ", compra)
        print("No tiene descuento")
