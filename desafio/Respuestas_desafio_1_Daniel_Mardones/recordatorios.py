recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output

#print(recordatorios)
# Removemos los errores y lo que no se necesita
recordatorios.remove(['2021-07-15', "13:00", "No hacer nada es feriado"])
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])
recordatorios.remove(['2021-12-25', "00:00", "Navidad"])

# Creamos variables para las nuevas listas a insertar
feriado = ['2021-07-16', "13:00", "No hacer nada es feriado"]
cena = ['2021-12-24','22:00','Cena de Navidad']
año_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo']
empieza = ['2021-01-02', '06:00', 'Empezar el año']
navidad = ['2021-12-25', '00:00', 'Navidad']

# Insertamos las nuevas listas a nuestra lista
recordatorios.insert(1, empieza)
recordatorios.insert(2, feriado)
recordatorios.insert(4, cena)
recordatorios.insert(5, navidad)
recordatorios.insert(6,año_nuevo)

#Salida
for listas in recordatorios:
    print(listas)
