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
     (20) Dejar de comprar

    

    """)
#Este print lo utilicé para que el usuario pudiera ver el menú y saber que numero de producto corresponde a cada producto.

def cafeteria():
    total=0
    opcion=""
    while opcion != 20:
        
        opcion=input("Elija una opcion del 1 al 20")
        
        if opcion == "1":
            total =  total + 31
            print("Total actual: $" ,total)
        
        elif opcion == "2":
            total += 38
            print("Total actual: $" ,total)
    
        elif opcion == "3":
            total += 35
            print("Total actual: $" ,total)
            
        elif opcion == "4":
            total += 58
            print("Total actual: $" ,total)
            
        elif opcion == "5":
            total += 35
            
        elif opcion == "6":
            total += 49
            print("Total actual: $" ,total)
            
        elif opcion == "7":
            total += 58
            print("Total actual: $" ,total)

        elif opcion == "8":
            total += 49
            print("Total actual: $" ,total)
            
        elif opcion == "9":
            total += 58
            print("Total actual: $" ,total)
            
        elif opcion == "10":
            total += 56
            print("Total actual: $" ,total)
            
        elif opcion == "11":
            total += 65
            print("Total actual: $" ,total)
            
        elif opcion == "12":
            total += 63
            print("Total actual: $" ,total)
            
        elif opcion == "13":
            total += 74
            print("Total actual: $" ,total)
            
        elif opcion == "14":
            total += 59
            print("Total actual: $" ,total)
            
        elif opcion == "15":
            total += 69
            print("Total actual: $" ,total)
            
        elif opcion == "16":
            total += 56
            print("Total actual: $" ,total)
            
        elif opcion == "17":
            total += 63
            print("Total actual: $" ,total)
            
        elif opcion == "18":
            total += 58
            print("Total actual: $" ,total)
            
        elif opcion == "19":
            total += 43
            print("Total actual: $" ,total)

        elif opcion == "20":
            print("El total es: $", total)
            print("Gracias por visitarnos. Vuelva pronto :)")
            
#Esta función es la que se encarga de toda la operación. Dentro de esta, se encuentran operadores para calcular el total de la cuenta
# y estructuras de decision para las opciones de bebidas que el cliente quiera. 

cafeteria()

#Esto solo es para llamar a la función principal.
            
            
        
        






    
                       











