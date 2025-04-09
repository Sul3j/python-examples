list1 = ["jablko", "banan", "pomarancza"]
list2 = list((1,2,3))
list3 = [6, 2, 8, 4, 2, 1, 9, 2]
list4 = ["jeden", "dwa", "trzy", "cztery", "piec"]
# wybieranie 2 elementu listy
print(list1[1])
# wybieranie ostatniego elementu
print(list1[-1])
# wybieranie elementów od 2 do 4
print(list2[1:3])
# wybieranie elementów do 3
print(list1[:2])
# wybieranie elementów od 3
print(list1[2:])
# zamiana pierwszego elementu listy na arbuz
list1[0] = "arbuz"
print(list1)
# zamiana elementu pierwszego i drugiego na 8 i 9
list2[0:2] = [8,9]
print(list2)
# dodanie elementu na koniec listy
list1.append("mandarynka")
print(list1)
# dodanie śliwki na 2 pozycję
list1.insert(1, "sliwka")
print(list1)
# roszerzenie listy1 o liste2
list1.extend(list2)
print(list1)
# usuniecie 1 elementu listy
list1.pop(0)
print(list1)
# usuniecie ostatniego elementu
list1.pop()
print(list1)
# usunięcie drugiego elementu listy za pomocą del
del list1[1]
print(list1)
# wyczyszcznie całej listy
list2.clear()
print(list2)
# sortowanie listy z cyframi
list3.sort()
print(list3)
# sortowanie ciągów znaków
list4.sort()
print(list4)
# sortowanie listy z cyframi w odwrotnej kolejności
list3.sort(reverse = True)
print(list3)
# kopiowanie listy do nowej zmiennej
list5 = list4.copy()
print(list5)
# zliczenie ile jest wratości 2 w liście
print(list3.count(2))