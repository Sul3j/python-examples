# definicja funkcji wyświetlającej komunikat
def message():
    print("Nasz komunikat")

message()

# definicja funkcji z argumentem
def newUser(name):
    print(f"Twoje imie to: {name}")

newUser("Szymon")

# definicja funkcji z dwoma argumentami
def newCustomer(firstname, lastname):
    print(f"Witaj {firstname} {lastname}")

newCustomer("Jan", "Kowalski")

# definicja funkcji z listą argumentów
def childrenList(*childs):
    print(f"Dziecko 1: {childs[0]}, Dziecko 2: {childs[1]}, Dziecko 3: {childs[2]}, Dziecko 4: {childs[3]}")

childrenList("Janek", "Tomek", "Malgosia", "Szymon")

# przypisywanie argumentów do konkretnych argumentów funkcji
def fruitsList(fruit1, fruit2, fruit3):
    print(fruit1, fruit2, fruit3)

fruitsList(fruit2="Jabłko", fruit3="Pomarańcza", fruit1="Kiwi")

# przekazywanie wartości słownikowych jako argumenty funkcji
def lastNames(**lastnames):
    print(f"nazwisko1 to: {lastnames["nazwisko2"]}")

lastNames(nazwisko1="Nowak", nazwisko2="Kowalski")

# ustawienie domyślnej wartości w argumencie
def country(name="Polska"):
    print(f"Nazwa kraju to {name}")

country("Niemcy")
country()

# funkcja zwracająca wartość
def sum(num1, num2):
    return num1 + num2

print(sum(2, 6))
result = sum(4, 5)
print(result)


# algorym minimalna i makszymalna liczba
def minAndMax(*numbers):
    min = 1000
    max = -1000
    for num in numbers:
        if num > max:
            max = num
        elif num < min:
            min = num
    return f"Minimalna: {min}, Maksymalna: {max}"


print(minAndMax(8, 3, 5, 1, 0, 2))

# algorym liczący średnią
def avgNumbers(*numbers):
    sum = 0
    i = 0
    for num in numbers:
        i = i + 1
        sum = sum + num
    return sum / i


print(avgNumbers(4, 6, 2, 1, 5, 2))

# deklaracja pustej funkcji
def function():
    pass
