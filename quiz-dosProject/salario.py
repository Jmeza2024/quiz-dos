
nombre = "Luis Vejarano"
 input("ingrese el numero de dias ")
 input("ingrese el salario del empleado")

print("nombre: "+ nombre)

def calcularsalario(nombre,dias,salario):
prima = salario * dias / 360
Cesantías = salario * días  / 360
Intereses_cesantías = cesantías * 0.12 / días_laborados
Vacaciones = salario * días_laborados / 720

liquidacionTotal = prima + cesantias + intereses_cesantias + vacaciones
return prima, cesantías, intereses_cesantias, vacaciones

if __name__ "main__":
nombre = ("Luis Vejarano")
dias = int(7)
salario = float(785000)

prima, cesantias, intereses_cesantias, vacaciones, liquidacion_total = calcularsalario(nombre, dias, salario)

print(f"señor {nombre} para los {dias} dias laborados y salario ${salario}, su liquidacion se compone ")
print(f"prima:"prima: .2f)