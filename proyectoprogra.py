menu = [
    ["Espresso sencillo", 31],
    ["Espresso doble", 38],
    ["Americano chico", 35],
    ["Americano grande", 58],
    ["Long black", 35],
    ["Capuchino chico", 49],
    ["Capuchino grande", 58],
    ["Latte chico", 49],
    ["Latte grande", 58],
    ["Moka chico", 56],
    ["Moka grande", 65],
    ["Chai chico", 63],
    ["Chai grande", 74],
    ["Caramel chico", 59],
    ["Caramel grande", 69],
    ["Chocolate chico", 56],
    ["Chocolate grande", 63],
    ["Tizana", 58],
    ["Té caliente", 43]
    ]

#Cree una matriz que contiene las pequeñas listas del producto junto con su precio. Cuando se mande a llamar el número, solo tengo
#que acceder a la matriz del producto seleccionado.

print("""
    ¿Qué va a querer? Le dejo nuestro menu(ingrese el número el producto a elegir)(Ingresar 20 si se desea dejar de comprar):
     (1)Espresso sencillo --- $31
     (2)Espresso doble --- $38
     (3)Americano chico --- $35
     (4)Americano grande --- $58
     (5)Long black --- $35
     (6)Capuchino chico --- $49
     (7)Capuchino grande --- $58
     (8)Latte chico --- $49
     (9)Latte grande --- $58
     (10)Moka chico --- $56
     (11)Moka grande --- $65
     (12)Chai chico --- $63
     (13)Chai grande --- $74
     (14)Caramel chico --- $59
     (15)Caramel grande --- $69
     (16)Chocolate chico --- $56
     (17)Chocolate grande --- $63
     (18)Tizana --- $58
     (19)Te caliente --- $43
     (20)Dejar de comprar

    

    """)
#Este print lo utilicé para que el usuario pudiera ver el menú y saber que numero de producto corresponde a cada producto.

def cafeteria():
    cuenta=[]
    total=0
    opcion=""
    while opcion != 20:
        
        opcion=int(input("Elija una opcion del 1 al 20"))
        
        
        if 1 <= opcion <= 19:
            producto = menu[opcion-1][0]
            precio = menu[opcion-1][1]
            total+=precio
            cuenta.append(producto)
            print("Total Actual: $",total)
        
        elif opcion == 20:
            print("Su orden fue:", cuenta)
            print("El total es: $",total)
            print("Gracias por visitarnos, vuelva pronto :)")
            



            
            
#Esta función es la que se encarga de toda la operación. Dentro de esta, se encuentran operadores para calcular el total de la cuenta
# y estructuras de decision para las opciones de bebidas que el cliente quiera. El uso de matrices me ayudo a reducir el numero de ifs.
#Ademas añadí una lista con todos los productos elegidos por el cliente para poder imprimir esa lista junto con el total de la cuenta. 

cafeteria()

#Esto solo es para llamar a la función principal.
            
            
        
        






    
                       











