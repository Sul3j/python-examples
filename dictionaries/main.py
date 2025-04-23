# tworzenie słownika
car = {
    "producent": "Toyota",
    "model": "Corolla",
    "rocznik": 2003,
    "bite": False
}

# sprawdzenie ilości elementów słownika
print(len(car))

# sprawdzenie typu zmiennej car
print(type(car))

# tworzenie słownika za pomocą konstuktora
dictConstructor = dict(producent = "BMW", model = "e36", rocznik = 1998, bite = True)

# wyciąganie ze słownika wartości o kluczu model
print(car["model"])

# wyciąganie ze słownika wartości o kluczu producent
print(car.get("producent"))

# wyswietlanie nazw kluczy słownika
print(car.keys())

# przypisanie do klucza model wartosci e46
dictConstructor["model"] = "e46"
print(dictConstructor)

# sprawdzanie wartości słownika
print(car.values())

# wyświetlenie zbiorów wartości klucz : wartość w słowniku
print(car.items())

# dodanie nowej danej do słownika
car.update({"kolor": "srebrny"})
print(car)
car["przebieg"] = 140000
print(car)

# usunięcie elementu o kluczu kolor
car.pop("kolor")
print(car)

# usunięcie ostanio dodanego elementu
car.popitem()
print(car)

# wyczyszczenie słownika
dictConstructor.clear()
print(dictConstructor)