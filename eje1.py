vendedores = int(input("Ingrese el numero de vendedores"))
for i in range(0, vendedores):

    venta1 = int(input("Ingrese la venta 1"))
    venta2 = int(input("Ingrese la venta 2"))
    venta3 = int(input("Ingrese la venta 3"))

    sueldob = int(input("Ingrese su sueldo base"))
    comisiones = (venta1+venta2+venta3*10)/100
    sueltot = comisiones+sueldob
    print("Su sueldo base es de", sueldo, "y su comision es", comisiones)
