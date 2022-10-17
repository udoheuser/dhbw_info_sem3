"""
Unittest_ggt_euklid untersucht das Modul ggt_euklid auf zwei unterschiedliche Arten:
1. Automatische Unittests 
2. Manueller Aufruf der rekursiven oder linearen Implementierungs-Variante des ggT-Algorithmus' inkl. Zeitmessung. 
"""

# Import des zu untersuchenden Moduls (Funktionen)
import ggt_euklid 

# import unittest
import pytest # Alternative zu unittest
import timeit # Zeitmessung
# import time # Alternative zu timeit
import logging # Debugausgaben

# Basis-Einstellungen festlegen:
logging.basicConfig(level=logging.INFO)

# Logger zur aktuellen Sitzung erstellen:
logger = logging.getLogger(__name__)

"""
Aufruf aus Shell (im gleichen Verzeichnis wie unittest_ggt_euklid): 
  python -m unittest ./unittest_ggt_euklid
  python -m unittest ./unittest_ggt_euklid.TestGGTMethods
  python -m unittest ./unittest_ggt_euklid.TestGGTMethods.test_one
  Contents: https://docs.python.org/3/library/unittest.html

class TestGGTMethods(unittest.TestCase):
    # Zwei Testmethoden, erweiterbar
    def test_one(self):
        self.assertEqual(ggt_euklid.euklid(2, 6), 2)
        self.assertNotEqual(ggt_euklid.euklid(2, 6), 1)

    def test_two(self):
        self.assertEqual(ggt_euklid.euklid(3, 6), 3)
        self.assertNotEqual(ggt_euklid.euklid(3, 6), 2)

""" 

"""
Pytest (Einfachere Alternative zu Unittest)
Aufruf aus der Kommandozeile/Shell aus Repository-Verzeichnis des aktuellen VS-Projekts, 
   z.B. C:\\Users\\heuser\\source\\repos\\1_ggt_euklid
Parameter -v: verbose
   pytest -v ./unittest_ggt_euklid.py
Contents: https://docs.pytest.org/en/latest/contents.html
Usage: https://docs.pytest.org/en/latest/usage.html
"""

class TestClass:
    # Two test methods, should all be passed ok
    def test_one(self):
        ggt = ggt_euklid.euklid(3, 6)
        assert ggt == 3

    def test_two(self):
        ggt = ggt_euklid.euklid(3, 6)
        assert ggt != 2

    """
    # Test method three should yield in an AssertionError failure
    def test_three(self):
        ggt = ggt_euklid.euklid(3, 6)
        assert ggt != 3
    """

"""
Einfachste Testmethode: Doctest innerhalb Funktion selbst

def euklid(a, b):
    ''' Berechnung des ggT mit Hilfe des Eklidschen Algorithmus'
        >>> euklid(2, 4)
        2
        >>> euklid(3, 5)
        1
    ''' 
"""

if __name__ == '__main__':
    # Manuelle Aufrufe der beiden Varianten inkl. Zeitmessung
    while True:
        switch = str(input("\nAusführung der ...\n(r)ekursiven Version\n(l)inearen Variante\nE(x)it? "))

        if switch in ['L', 'l']:
            # error handling wrapping int() function
            try:
                a = int(input("Erster Wert: "))
            except:
                print("Sorry, wrong input type. Use int instead!")
                continue
            try:
                b = int(input("Zweiter Wert: "))
            except:
                print("Sorry, wrong input type. Use int instead!")
                continue

            start_time = timeit.timeit()
            # start_time = time.process_time()
            logger.info("Der ggT von {:d} und {:d} ist (linear): {:d}".format(a, b, ggt_euklid.euklid(a, b)))
            end_time = timeit.timeit()
            # end_time = time.process_time()
            logger.info("Elapsed time: {:20.18f} secs".format(end_time - start_time))
        elif switch in ['R', 'r']:
            # error handling wrapping int() function
            try:
                a = int(input("Erster Wert: "))
            except:
                print("Sorry, wrong input type. Use int instead!")
                continue
            try:
                b = int(input("Zweiter Wert: "))
            except:
                print("Sorry, wrong input type. Use int instead!")
                continue

            start_time = timeit.timeit()
            logger.info("Der ggT von {:d} und {:d} ist (rekursiv): {:d}".format(a, b, ggt_euklid.euklid_recursive(a, b)))
            end_time = timeit.timeit()
            logger.info("Elapsed time: {:20.18f} secs".format(end_time - start_time))
        else:
            break

