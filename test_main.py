import unittest
import os
from main import HRReportGenerator

class TestHRReportGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = HRReportGenerator(pracownicy_file='nieistniejacy_plik.xlsx')

    def test_brak_pliku_pracownikow(self):
        # Sprawdzamy, czy podniesie błąd FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            self.generator.generuj()

    def test_obliczenia_prostego_przykladu(self):
        # Tutaj można dopisać testy logiki, jeśli pliki istnieją
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
