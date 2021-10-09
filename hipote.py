importeP = float(input("introduce el importe del prestamo"))
ingresosA = float(input("ingresos anuales"))
costeP = float(input("coste tasado del piso"))
terminiP = float(input("termini de pagament en años"))
importeMR = importeP*2/(terminiP*12)
if importeP <= costeP*0.8 and importeMR < ingresosA/12 * 0.5:
        print("hipoteca concedida")
  
else:print("hipoteca no concedida")
# HACIENDO PRUEBAS

# importeP = 80000
# ingresosA = 35000
# costeP = 100000
# terminiP = 35 años
# importeMR = 80000*2/(35*12)
# if 80000 <= 100000 * 0.8 and importeMR < 35000/12 * 0.5:
#         print hipotreca concedida