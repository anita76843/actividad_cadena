#1.
name = "Ana"
age = 21
favouriteFood = "la Lasaña con Pollo"
print(f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi"
      f" comida favorita es {favouriteFood}")

#2.
nombre= input("introduzca su nombre completo:")
nombre_completo= nombre.replace(" ","")
numero_de_letras = len(nombre_completo)
print(f"Hola, {nombre}! Tu nombre tienes {numero_de_letras} letras, excluyendo los espacios.")

nombre2= input("introduzca su nombre completo:")
nombre_completo2= nombre2.replace(" ","")
numero_de_letras2 = len(nombre_completo2)
print(f"Hola, {nombre2}! Tu nombre tienes {numero_de_letras2} letras, excluyendo los espacios.")

#3.
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
print(f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% "
      f"y los ingresos crecieron un {revenueGrowthPercent:.2f}%")

#4.
secretMessage = ("aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!")
result1= secretMessage [3::2]
print(result1)


#5.
text = "El nombre Python viene dado por la afición de Van Rossum al grupo Monty Python."
text1= text.split()
text2= len(text1)
print(f"Numero de palabras en la frase:{text2}")


#6.
word= "Camila"
print(word)
word2= word.replace( "a", "e")
print(word2)

#7
sentence = "La historia del lenguaje de programación Python"
text1=  sentence.split()
text2= ' '.join(reversed(text1))
print(text2)