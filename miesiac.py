# Wczytanie daty

Mc = int(input("Podaj miesiąc: "))
Rok = int(input("Podaj rok: "))

# Zmiana miesiąca na kolejny

Mc = Mc + 1

if Mc == 13:
     Mc = 1
     Rok = Rok + 1

# Wyświetlanie nowej daty

print("Miesiąc:",Mc)
print("Rok:", Rok)
