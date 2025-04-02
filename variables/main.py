# KOMENTARZE
x = 5 # zmienna pzrechowuje liczbę całkowintą (int)
name = "Szymon" # zmienna przechowuje ciąg zanków (string)
is_human = True # zmienna przechowuje wartość logiczną (bool)

# PRZYKLADY DEKLARACJI ZMIENNYCH
text = "to jest ciag znakow"
number = 24
float_variable = 2.4
logic_variable = True

# SPRAWDZENIE TYPOW ZMIENNYCH
print(type(text)) # str
print(type(number)) # int
print(type(float_variable)) # float
print(type(logic_variable)) # bool

# WIELOKROTNE PRZYPISANIE WARTOSCI
color, is_fruit, quantity = "red", True, 2

j = k = "jabłko"
print(j, k)

# WYSWIETLENIE ZAWARTOSCI ZMIENNYCH
print(color) # red
print(is_fruit) # True
print(quantity) # 2

# LACZENIE CIAGOW ZNAKOW
first_part = "SLI"
second_part = "MAK"

full_text = first_part + second_part # SLIMAK
print(full_text)

# ZMIANA TYPOW ZMIENNYCH
string_age = "10"
int_age = int(string_age) # konwersja string -> int

print(type(string_age))
print(type(int_age))

int_quantity = 5
float_quantity = float(int_quantity) # konwersja int -> float

print(type(int_quantity))
print(type(float_quantity))

int_height = 180
string_height = str(int_height) # konwersja int -> str

print(type(int_height))
print(type(string_height))

# USUNIECIE ZMIENNEJ Z PAMIECI
del_variable = 10
print(del_variable) # 10
del del_variable
print(del_variable) # błąd - niema zmiennej w pamięci