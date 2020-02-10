# 01 - Variabelen

naam = "Chris"
leeftijd = 22
print("\n" + naam + " is " + leeftijd + "jaar oud")


# 02 - Als dan

isAanHetWerk = true

if (isAanHetWerk) {
    print(naam + " is aan het werk")
} else {
    print(naam + " is niet aan het werk")
}


# 03 - Lijsten

lijstMetGetallen = [20, 40, 60, 140, 300]

print("\n" + lijstMetGetallen)


# 04 - Lussen

leerlingen = ["Jan", "Bo"]

for leerling in leerlingen:
    print("\n" + leerling)


# 05 - Functies

def herbruikbaarStukjeCode(a, b):
    product = a * b
    print("\nHet product van " + a + " en " + b " is " product")

herbruikbaarStukjeCode(3, 4)
herbruikbaarStukjeCode(5, 5)


# 06 - Gecombineerd

lijst2MetGetallen = [2, 1, 30, 50, 1, 7, 90, 1] # 3 eenen

def telDeEenen(lijst):
    aantalEenen = 0

    for getal in lijst:
        if (getal == 1):
            aantalEenen++

print("\nAantal eenen: " + telDeEenen(lijst2MetGetallen))
