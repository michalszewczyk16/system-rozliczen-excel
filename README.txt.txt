Automatyzacja obsługi plików Excel - System Rozliczeń HR

1. Opis Projektu

Projekt to zautomatyzowane narzędzie w języku Python, służące do agregacji, walidacji i przeliczania danych kadrowo-płacowych rozproszonych w wielu plikach Excel. Skrypt automatyzuje proces, minimalizując ryzyko błędu ludzkiego przy ręcznym wprowadzaniu danych.

Główne funkcjonalności:

Wczytywanie danych: Pobieranie danych z pliku bazowego (pracownicy) oraz plików tygodniowych (godziny pracy).

Walidacja: Weryfikacja kompletności danych oraz odrzucanie rekordów z ujemnymi wartościami godzin.

Scalanie (Merge): Łączenie danych z wielu źródeł na podstawie unikalnego klucza ID_Pracownika.

Obliczenia: Agregacja godzin pracy oraz wyliczanie wynagrodzenia (Godziny * Stawka).

Raportowanie: Generowanie czytelnego pliku raport_koncowy.xlsx z podziałem na szczegóły i podsumowania.

2. Wymagania Techniczne i Instalacja

Do uruchomienia projektu wymagany jest Python w wersji 3.8 lub wyższej oraz biblioteki pandas i openpyxl.

Instalacja bibliotek:

Otwórz terminal w folderze projektu i wykonaj:

pip install pandas openpyxl


3. Struktura Danych Wejściowych

Projekt wymaga plików Excel w następującym formacie:

Plik bazowy: pracownicy.xlsx

ID_Pracownika: Unikalny numer pracownika (np. 1, 2, 3).

Imie: Imię pracownika (tekst).

Nazwisko: Nazwisko pracownika (tekst).

Dzial: Dział firmy (np. IT, HR, Sprzedaż).

Stawka_Godzinowa: Stawka za godzinę (liczba zmiennoprzecinkowa).

Pliki szczegółowe: godziny_tydzienX.xlsx

ID_Pracownika: Identyfikator dopasowany do bazy pracowników.

Przepracowane_Godziny: Liczba przepracowanych godzin (liczba dodatnia).

4. Uruchomienie

Przygotuj pliki wejściowe w katalogu projektu.

Uruchom skrypt generujący raport:

python main.py


Oczekiwany wynik: W katalogu pojawi się plik raport_koncowy.xlsx zawierający arkusz ze szczegółami rozliczeń oraz zestawienie zbiorcze.

5. Testowanie

W projekcie znajduje się skrypt test_main.py umożliwiający weryfikację logiki obliczeń. Uruchom go komendą:

python test_main.py
