import pandas as pd
import os

def generuj_raport():
    print("[1/5] Rozpoczynam wczytywanie danych...")

    wymagane_pliki = ['pracownicy.xlsx', 'godziny_tydzien1.xlsx', 'godziny_tydzien2.xlsx']
    for plik in wymagane_pliki:
        if not os.path.exists(plik):
            print(f"[BŁĄD KRYTYCZNY] Brak pliku wejściowego: {plik}")
            return

    df_pracownicy = pd.read_excel('pracownicy.xlsx')
    df_t1 = pd.read_excel('godziny_tydzien1.xlsx')
    df_t2 = pd.read_excel('godziny_tydzien2.xlsx')

    print("[2/5] Agregacja i WALIDACJA danych z raportów godzinowych...")
    df_godziny_wszystkie = pd.concat([df_t1, df_t2], ignore_index=True)

    bledne_rekordy = df_godziny_wszystkie[df_godziny_wszystkie['Przepracowane_Godziny'] < 0]
    if not bledne_rekordy.empty:
        print(f" -> [UWAGA] Wykryto niepoprawne wpisy (ujemne godziny). Rekordy odrzucone:\n{bledne_rekordy}")

    df_godziny_poprawne = df_godziny_wszystkie[df_godziny_wszystkie['Przepracowane_Godziny'] >= 0]

    df_godziny_suma = df_godziny_poprawne.groupby('ID_Pracownika', as_index=False)['Przepracowane_Godziny'].sum()

    print("[3/5] Scalanie danych (Merge)...")
    df_raport = pd.merge(df_pracownicy, df_godziny_suma, on='ID_Pracownika', how='left')

    df_raport['Przepracowane_Godziny'] = df_raport['Przepracowane_Godziny'].fillna(0)

    print("[4/5] Przeliczanie wynagrodzeń...")
    df_raport['Wynagrodzenie_Calkowite'] = df_raport['Przepracowane_Godziny'] * df_raport['Stawka_Godzinowa']

    print("[5/5] Generowanie podsumowań i zapis do pliku Excel...")
    df_podsumowanie_dzialow = df_raport.groupby('Dzial', as_index=False).agg({
        'Przepracowane_Godziny': 'sum',
        'Wynagrodzenie_Calkowite': 'sum'
    })

    nazwa_raportu = 'raport_koncowy.xlsx'
    with pd.ExcelWriter(nazwa_raportu, engine='openpyxl') as writer:
        df_raport.to_excel(writer, sheet_name='Szczegóły_Rozliczeń', index=False)
        df_podsumowanie_dzialow.to_excel(writer, sheet_name='Podsumowanie_Działów', index=False)

    print(f"\n[SUKCES] Projekt zakończony! Plik '{nazwa_raportu}' jest gotowy.")


if __name__ == "__main__":
    generuj_raport()