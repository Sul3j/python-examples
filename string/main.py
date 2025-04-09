text1 = "Jakis tekst"
text2 = 'j'
text3 = "   Jakis tekst Drugi tekst   "
text4 = "jeden; dwa; trzy"
text5 = "akas"


# wybieranie 1 elementu z ciągu znaków
print(text1[0])
# wybieranie elementów od 1 do 5
print(text1[0:5])
# wybranie ostaniego elementu
print(text1[-1])
# wybieranie elementów od 2 do końca
print(text1[2:])
# wybiera elementy od początku do 2
print(text1[:2])
# sprawdzenie długości tekstu
print(len(text1))
# zmiana ciągu znaków na małe litery
print(text1.lower())
# zmiana ciągu na duze litery
print(text1.upper())
# usuwanie białych znaków (spacje)
print(text3.strip())
# zamiana liter w tekście
print(text1.replace("t", "X"))
# dzielenie ciągu znaków (podajemy seperator)
print(text4.split(";"))
# łączenie ciągów znaków przez +
print(text2 + text5)
print(text2 + "akas wiadomosc")

# formatowany ciąg znaków pozwala na umieszczenie w środku wartości zmiennej
age = 36
text6 = f"Tomek ma {age} lat"
print(text6)

# w formatowanym ciągu znaków mozemy wykonywać operacje na danych
text7 = f"Kasia ma {age + 2} lat"
print(text7)