import random

# Baza haseł do zgadnięcia
BANK_HASEL = ["CMAZ", "Nigdy", "nie", "zatankuje", "na", "Orlenie", "Taylor", "Swift", "Mariusz", "Pudzian", "papieżak"]

# Funkcja do losowania hasła z bazy haseł
def losuj_haslo():
    return random.choice(BANK_HASEL)

# Funkcja do inicjalizacji planszy gry
def inicjalizuj_plansze(haslo):
    return ["*" for _ in range(len(haslo))]

# Funkcja do wyświetlania planszy
def wyswietl_plansze(plansza):
    print("Hasło do zgadnięcia: " + " ".join(plansza))

# Funkcja do aktualizacji planszy po podaniu litery przez użytkownika
def aktualizuj_plansze(haslo, plansza, litera):
    for i in range(len(haslo)):
        if haslo[i] == litera:
            plansza[i] = litera

# Funkcja do sprawdzenia, czy podana litera już została użyta
def czy_juz_uzyta(litera, uzyte_litery):
    return litera in uzyte_litery

# Funkcja do wyświetlania użycia liter przez użytkownika
def wyswietl_uzyte_litery(uzyte_litery):
    print("Użyte litery: " + ", ".join(uzyte_litery))

# Funkcja do wyświetlania liczby popełnionych błędów
def wyswietl_bledy(bledy):
    print("Liczba popełnionych błędów: " + str(bledy))

# Funkcja do sprawdzenia, czy użytkownik zgadł hasło
def czy_wygral(haslo, plansza):
    return "".join(plansza) == haslo

# Funkcja do wczytywania haseł z pliku
def wczytaj_hasele_z_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r") as plik:
            return plik.read().splitlines()
    except FileNotFoundError:
        print("Nie udało się wczytać haseł z pliku.")
        return []

# Główna funkcja gry w wisielca
def graj_w_wisielca():
    print("Witaj w grze w wisielca!")
    while True:
        print("1 - Rozpocznij nową grę")
        print("2 - Wyjdź z programu")
        wybor = input("Twój wybór: ")
        if wybor == "1":
            haslo = losuj_haslo()
            plansza = inicjalizuj_plansze(haslo)
            uzyte_litery = []
            bledy = 0
            while True:
                wyswietl_plansze(plansza)
                litera = input("Podaj literę: ").lower()
                if len(litera) != 1 or not litera.isalpha():
                    print("Podaj jedną literę!")
                    continue
                if czy_juz_uzyta(litera, uzyte_litery):
                    print