importeP = float(input("introduce el importe del prestamo"))
ingresosA = float(input("ingresos anuales"))
costeP = float(input("coste tasado del piso"))
terminiP = float(input("termini de pagament en años"))
importeMR = importeP*2/(terminiP*12)
if importeP <= costeP*0.8 and importeMR < ingresosA/12 * 0.5:
        print("hipoteca concedida")
  
else:print("hipoteca no concedida")
# HACIENDO PRUEBAS