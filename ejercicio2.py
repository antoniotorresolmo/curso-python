string = "dabale arroz a la zorra el abad"
string2 = "esto no es valido"

def comprobar(sparametro):
    exito = True
    sparametro = sparametro.replace(" ", "")

    for contador in range(len(sparametro)):
        if sparametro[contador] != sparametro[-(contador + 1)]:
            exito = False
            break

    return exito

print(comprobar("lola"))

# Tests
assert comprobar("lol")
assert comprobar("dabale arroz a la zorra el abad")
assert not comprobar("awdasd")