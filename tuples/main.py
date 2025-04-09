# tupla zawierająca wartości tekstowe
fruits = ("jablko", "pomarancza", "sliwka")
# tupla zawierająca liczby
numbers = (5,8,2,6,9)
# tupla zawierająca wartości logiczne 
logic = (True, False, True)
# tupla zawirająca wrtości mieszane
mixed = (True, "jablko", 5)
# tworzenie tupli za pomocą konstruktora
tuple_constructor = tuple(("krzeslo", "stolik", "monitor"))

# sprawdzenie typu zmiennej tuple_constructor
print(type(tuple_constructor))

# dostęp do danych tupli za pomocą indexów i do przedziału danych
print(fruits[0])
print(fruits[-1])
print(fruits[2:4])
print(fruits[:3])
print(fruits[2:])

# zamiana wrtości tupli za pomocą konwersji do listy poniewa tupla nie jest modyfikowalna
x = list(fruits)
print(type(fruits))
print(type(x))
x[0] = "kiwi"
fruits = tuple(x)
print(fruits)
print(type(fruits))

# dodawanie danej do tupli za pomocą konwersji do listy poniewa tupla nie jset modyfikowalna
y = list(fruits)
y.append("jablko")
fruits = tuple(y)
print(fruits)

# usuwanie danej do tupli za pomocą konwersji do listy poniewa tupla nie jset modyfikowalna
z = list(tuple_constructor)
z.remove("monitor")
tuple_constructor = tuple(z)
print(tuple_constructor)

# usuwanie tupli mieszane z pamięci
del mixed
print(mixed)