"""
Proyecto de programación.
Simulador de cafetería.
El programa da un menú de opciones al usuario y le pide al cliente que introduzca el producto que quiera.
El programa va agregando los productos a la cuenta y los precios al total.
Al final, te imprime todos los producos seleccionados y el total de la cuenta.
"""




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

"""
================== función auxiliar  =======================================
"""

def imprimir_menu():
        """
        (funciones)
          como tal esta funcion no recibe ningun dato, solo sirve para dar la orden de imprimir el menú
        """

        print("""¿Qué va a querer? Le dejo nuestro menu(ingrese el número el producto a elegir)(Ingresar 20 si se desea dejar de comprar):
         
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





def cafeteria(menu):
    """
    (operadores,funciones, condicionales, ciclos, listas, listas anidadas,)
    Recibe la matriz con productos y precios.
    El resto de variables se crean dentro de la misma función.
     Imprime el menu llamando la función auxiliar. Pide al usuario un número de producto entre las opciones.
     Va sumando los precios de los productos y agregando el nombre de los productos a la cuenta extrayendo estos de la matriz.
     Cuando el cliente pide el total, se para el ciclo y se muestran todos los productos consumidos junto con el total de la cuenta.
     Tampoco devuelve algun valor o variable ya que todo se imprime dentro de la misma función.
    """
    cuenta=[]
    #Cree una lista para ir agregando los productos a la cuenta
    total = 0
    #Crea variable para ir guardando el total de la cuenta
    opcion = ""
    #Crea variable vacía para que el cliente ingrese el número de producto
    
    imprimir_menu()
    
    while opcion != 20:
        #Ciclo para mantener habilitada la opción de comandar hasta que el cliente solicite el total
        
        try:
            opcion=int(input("Elija una opcion del 1 al 20"))
        #Se pide al usuario el número de producto delm menú de opciones
        
            if 1 <= opcion <= 19:
            #Condicional para verificar si entra en el rango del menú
                producto = menu[opcion-1][0]
            #Extrae el producto de la matriz del menú 
                precio = menu[opcion-1][1]
            #Extrae el precio del producto de la matriz
                total += precio
            #Suma el precio del producto elegido al total
                cuenta.append(producto)
            #Agrega el producto a la lista de la cuenta
                print("Total Actual: $",total)
            #Va imprimiendo el total hasta ese punto
        
            elif opcion == 20:
            #Condicional para verificar si entra en el rango del menú
                print("Su orden fue:", cuenta)
            #Imprime todos los productos que se consumieron
                print("El total es: $",total)
            #Imprime el total de la cuenta
                print("Gracias por visitarnos, vuelva pronto :)")
            #Un mensaje de despedida
            
            else:
                print("Favor de ingresar un número valido")
            #Le informa al cliente que ponga un valor válido de producto en el caso que haya ingresado un valor que no se encuentra
            

        except ValueError:
            print("Favor de ingresar un valor numérico")
            """
            Esta es una funcion nueva que funciona junto con el try que se encuentra más arriba.
            Esta función sirve para verificar si el tipo de dato es válido, de no ser así, imprime un mensaje para
            que el usuario sepa que tiene que ingresar un tipo de dato válido.
            """
            

            
            

cafeteria(menu)

#Esto solo es para llamar a la función principal.
            
            
        
        






    
                       











