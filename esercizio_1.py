temp_soglia = int(input("Inserire la temperatura di soglia: "))
print(f"La temperatura di soglia impostata è di: {temp_soglia} °C")
def linea():
    print("-" * 25)
linea()

temperature_registrate = [82, 95, 101, 78, 110, 88, 105, 76]

def conta_sopra_soglia(x,y):
    z = 0
    for t in x:
	    if t > y:
		    z += 1
    return z

def media (x):
    return sum(x) / len(x)

n = conta_sopra_soglia(temperature_registrate,temp_soglia)
m = media(temperature_registrate)

print ("le letture sono: ", len(temperature_registrate))
print (f"la temperatura media è: {m}")
print (f"le letture oltre la soglia sono {n}")

linea()

if (n>(len(temperature_registrate)/2)):
    print("troppe registrazioni oltre la soglia")
else:
    print("tutto ok")