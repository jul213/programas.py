import hashlib

class HASH:
    def generalHash(n):
        digest=n.hexdigest()
        return digest

x=0
while x<1:
    print("escoge el hash que quieres utilizar")
    print("SHA256")
    print("SHA512")
    print("ACABA EL PROGRAMA")

    eleccion=int(input())
    
    print("INTRODUCE LOS DATOS A HASHEAR")
    datos = input()

    algoritmo = ""
    if eleccion != 3:

        if eleccion == 1:
            algoritmo = "SHA256"
        elif eleccion == 2:
            algoritmo = "SHA512"

        bdatos = bytes(datos, "utf-8")
        n = hashlib.new(algoritmo, bdatos)
        hash1 = HASH.generalHash(n)
        print()
        print(hash1)
        print()
        x=0
    else:
        x=1

print("ESTO SE ACABO!!!!")


