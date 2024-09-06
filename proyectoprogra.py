from selectors import SelectSelector

print("""
    ¿Qué va a querer? Le dejo nuestro menu:
     Espresso sencillo --- $31
     Espresso doble --- $38
     Americano chico --- $35
     Americano grande --- $58
     Long black --- $35
     Capuchino chico --- $49
     Capuchino grande --- $58
     Latte chico --- $49
     Latte grande --- $58
     Moka chico --- $56
     Moka grande --- $65
     Chai chico --- $63
     Chai grande --- $74
     Caramel chico --- $59
     Caramel grande --- $69
     Chocolate chico --- $56
     Chocolate grande --- $63
     Tizana --- $58
     Te caliente --- $43

    
    Por el momento nuestro sistema solo puede manejar un total de 3 productos :,(
    Favor de poner solo el precio de cada producto :)
    """)
#Esta parte del código es para que el usuario pueda ver el menú con los precios

art_1=int(input("Precio primer articulo:"))
art_2=int(input("Precio segundo articulo:"))
art_3=int(input("Precio tercer articulo:"))

#Aquí cree variables para los precios de los artículos

def total_cuenta(art_1,art_2,art_3):
    return art_1+art_2+art_3
#Aquí utilicé mi primera función para sumar los precios de todos los articulos (osea la cuenta)

pregunta=input("¿Entre cuantas personas gusta dividir su cuenta?")
# Se pregunta el numero de personas para dividir la cuenta 

def division_cuenta(pregunta):
    if pregunta == ("1"):
        return total_cuenta(art_1,art_2,art_3)/1
    elif pregunta == ("2"):
        return total_cuenta(art_1,art_2,art_3)/2
    elif pregunta == ("3"):
        return total_cuenta(art_1,art_2,art_3)/3
#Esta es la función para dividir la cuenta
    
print("Su total es:",division_cuenta(pregunta),"pesos")
#Aquí imprime la función de división de cuenta que a su vez tiene adentro la función de sumar productos

print("¡Hasta luego!:)")
# Este solo es un mensaje de despedida :)

#Ya había utilizado estructuras de decision. Quiero meterle más, pero necesito igual utilizar ciclos while y quiero seguir practicando con estos:)











    
                       











