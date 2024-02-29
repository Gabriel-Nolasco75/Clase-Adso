edad = int(input('Ingrese su edad: '))
if edad >= 0 and edad<= 5:
    print ("Aun eres un bebe")
elif edad >=6 and edad <= 11:
    print ("Eres un niño")
elif edad >=12 and edad <=18:
    print("Eres un adolecente")
else:
    print ("Ya estas grande")