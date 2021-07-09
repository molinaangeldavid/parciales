def caminito_baldosas(baldosas : str)->None:
    lista = baldosas.split(",")
    for baldosa in range(len(lista)):
        if baldosa == 0:
            if lista[baldosa] == "R":
                lista[baldosa] = "B"
        elif baldosa > 0 and baldosa < (len(lista) - baldosa):
            if lista[baldosa] == "R":
                if lista[baldosa] != lista[baldosa-1] and lista[baldosa-1] != "G" and lista[baldosa+1] != "G":
                    lista[baldosa] = "G"
                elif lista[baldosa] != lista[baldosa-1] and lista[baldosa-1] != "N" and lista[baldosa+1] != "N":
                    lista[baldosa] = "N"
                elif lista[baldosa] != lista[baldosa-1] and lista[baldosa-1] != "B" and lista[baldosa+1] != "B":
                    lista[baldosa] = "B"
            elif lista[baldosa] != "R":
                if lista[baldosa] != lista[baldosa-1] and lista[baldosa-1] != "G" and lista[baldosa+1] != "G":
                    lista[baldosa] = "G"
                elif lista[baldosa] != lista[baldosa-1] and lista[baldosa-1] != "N" and lista[baldosa+1] != "N":
                    lista[baldosa] = "N"
                elif lista[baldosa] != lista[baldosa-1] and lista[baldosa-1] != "B" and lista[baldosa+1] != "B":
                    lista[baldosa] = "B"
        elif baldosa == (len(lista) - baldosa):
            if lista[baldosa] == "R":
                if lista[baldosa] != "G" and lista[baldosa-1] != "G":
                    lista[baldosa] = "G"
                elif lista[baldosa] != "N" and lista[baldosa-1] != "N":
                    lista[baldosa] = "N"
                elif lista[baldosa] != "B" and lista[baldosa-1] != "B":
                    lista[baldosa] = "B"
    print("".join(lista))
caminito_baldosas("R,G,N,R,R,N,R,R,R,B,R,N")