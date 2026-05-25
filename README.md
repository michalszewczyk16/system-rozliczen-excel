Automatyzacja obsługi plików Excel - System Rozliczeń HR

1. Opis Projektu

Projekt to zautomatyzowane narzędzie napisane w języku Python, służące do agregacji, walidacji i przeliczania danych kadrowo-płacowych rozproszonych w wielu plikach Excel. Skrypt eliminuje konieczność ręcznego przepisywania danych, minimalizując ryzyko błędu ludzkiego.

Główne funkcjonalności:

Wczytywanie danych: Automatyczne pobieranie danych z pliku bazowego (dane pracowników) oraz plików szczegółowych (raporty godzinowe z poszczególnych tygodni).

Walidacja: Sprawdzanie kompletności danych (brakujące wartości, ujemne godziny, niepoprawne typy danych).

Scalanie (Merge): Łączenie danych z wielu plików na podstawie unikalnego klucza (ID_Pracownika).

Obliczenia: Agregacja przepracowanych godzin i wyliczanie całkowitego wynagrodzenia (Godziny * Stawka).

Raportowanie: Generowanie wieloarkuszowego pliku raport_koncowy.xlsx zawierającego szczegółowe zestawienie oraz ogólne podsumowanie finansowe dla firmy.

2. Wymagania Techniczne i Instalacja

Aby uruchomić projekt, upewnij się, że posiadasz zainstalowanego Pythona (wersja 3.8+) oraz niezbędne biblioteki zewnętrzne.

pip install pandas openpyxl


3. Struktura Danych Wejściowych

Projekt wymaga przygotowania plików w następującym formacie:

Plik bazowy: pracownicy.xlsx

ID_Pracownika (np. 1, 2, 3...)

Imie (Tekst)

Nazwisko (Tekst)

Dzial (Tekst, np. IT, HR, Sprzedaż)

Stawka_Godzinowa (Liczba, np. 50.0, 120.0)

Pliki szczegółowe (np. godziny_tydzien1.xlsx, godziny_tydzien2.xlsx):

ID_Pracownika (Klucz obcy)

Przepracowane_Godziny (Liczba)

4. Oczekiwany Wynik (Raport Końcowy)

Skrypt wygeneruje plik raport_koncowy.xlsx składający się z dwóch arkuszy:

Szczegóły_Rozliczen: Tabela zawierająca połączone dane każdego pracownika wraz ze zsumowanymi godzinami i wyliczonym wynagrodzeniem całkowitym.

Podsumowanie_Dzialow: Zgrupowane dane prezentujące całkowity koszt wynagrodzeń i sumę godzin w rozbiciu na poszczególne działy w firmie.