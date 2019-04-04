# Exercise: Unit converter
print("Tai konverteris, kuris kilometrus pavercia myliomis")

while True:
    print("Iveskite skaiciu kilometrais kuri noretumete konvertuoti i mylias. Iveskite tik viena skaiciu!")

    km = input("Kilometrai: ")
    km = float(km.replace(",", "."))
    miles = km * 0.621371

    print("{0} kilometrai yra {1} mylios.".format(km, miles))

    choice = input("Ar noretumete atlikti dar viena konverta (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print("Darbas baigtas.")
        break