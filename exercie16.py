limite = int(input("Tu veux aller jusqu'à quelle table ? "))

for nombre in range(1, limite + 1):  
    print("Table de", nombre)
    for multiple in range(1, 11):    
        print(nombre, "x", multiple, "=", nombre * multiple)
    print("-------")  
