import pandas as pd

def utworz_pliki_testowe():
    print("[INFO] Rozpoczynam generowanie plików Excel...")

    # 1. Baza pracowników
    pracownicy_dane = {
        'ID_Pracownika': [1, 2, 3, 4, 5],
        'Imie': ['Jan', 'Anna', 'Piotr', 'Katarzyna', 'Michał'],
        'Nazwisko': ['Kowalski', 'Nowak', 'Zieliński', 'Wójcik', 'Szewczyk'],
        'Dzial': ['IT', 'HR', 'Sprzedaż', 'IT', 'Zarząd'],
        'Stawka_Godzinowa': [120.0, 70.0, 85.0, 110.0, 200.0]
    }
    df_pracownicy = pd.DataFrame(pracownicy_dane)
    df_pracownicy.to_excel('pracownicy.xlsx', index=False)
    print(" -> Utworzono: pracownicy.xlsx")

    tydzien1_dane = {
        'ID_Pracownika': [1, 2, 3, 4, 5],
        'Przepracowane_Godziny': [40, 35, 42, -5, 40]
    }
    df_tydzien1 = pd.DataFrame(tydzien1_dane)
    df_tydzien1.to_excel('godziny_tydzien1.xlsx', index=False)
    print(" -> Utworzono: godziny_tydzien1.xlsx")

    # 3. Raport godzin - Tydzień 2
    tydzien2_dane = {
        'ID_Pracownika': [1, 2, 3, 4, 5],
        'Przepracowane_Godziny': [45, 40, 38, 40, 42]
    }
    df_tydzien2 = pd.DataFrame(tydzien2_dane)
    df_tydzien2.to_excel('godziny_tydzien2.xlsx', index=False)
    print(" -> Utworzono: godziny_tydzien2.xlsx")

    print("[SUKCES] Wszystkie pliki testowe zostały wygenerowane.")

if __name__ == "__main__":
    utworz_pliki_testowe()