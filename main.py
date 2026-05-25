import pandas as pd
import glob
import os


class HRReportGenerator:
    def __init__(self, pracownicy_file='pracownicy.xlsx', godziny_pattern='godziny_tydzien*.xlsx'):
        self.pracownicy_file = pracownicy_file
        self.godziny_pattern = godziny_pattern

    def generuj(self, wyjscie='raport_koncowy.xlsx'):
        if not os.path.exists(self.pracownicy_file):
            raise FileNotFoundError(f"Nie znaleziono pliku: {self.pracownicy_file}")

        df_prac = pd.read_excel(self.pracownicy_file)
        pliki = glob.glob(self.godziny_pattern)

        if not pliki:
            df_godziny = pd.DataFrame(columns=['ID_Pracownika', 'Przepracowane_Godziny'])
        else:
            df_godziny = pd.concat([pd.read_excel(f) for f in pliki])

        # Walidacja danych
        df_godziny = df_godziny[df_godziny['Przepracowane_Godziny'] >= 0]

        df_suma = df_godziny.groupby('ID_Pracownika')['Przepracowane_Godziny'].sum().reset_index()
        df_raport = pd.merge(df_prac, df_suma, on='ID_Pracownika', how='left').fillna(0)
        df_raport['Wynagrodzenie_Calkowite'] = df_raport['Przepracowane_Godziny'] * df_raport['Stawka_Godzinowa']

        df_raport.to_excel(wyjscie, index=False)
        print(f"[SUKCES] Raport został wygenerowany: {wyjscie}")


if __name__ == "__main__":
    generator = HRReportGenerator()
    generator.generuj()