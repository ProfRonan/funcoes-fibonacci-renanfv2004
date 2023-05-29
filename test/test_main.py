"""Test file for testing the main.py file"""

import unittest
import sys
from pathlib import Path
# add the parent directory to the path in order to run it from the run command in vscode
main_file_folder = Path(__file__).parents[1].as_posix() # pylint: disable=invalid-name
sys.path.insert(0, main_file_folder)
from main import fibonacci # pylint: disable=import-error,wrong-import-position

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def test_fibonacci_relation(self):
        """Testa se o i-ésimo número de Fibonacci é igual a soma dos dois anteriores"""
        for i in range(3, 10):
            self.assertEqual(fibonacci(i), fibonacci(i-1) + fibonacci(i-2))

    def test_fibonacci_0(self):
        """Testa se o 0-ésimo número de Fibonacci é igual a 0"""
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        """Testa se o 1-ésimo número de Fibonacci é igual a 1"""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        """Testa se o 2-ésimo número de Fibonacci é igual a 1"""
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_3(self):
        """Testa se o 3-ésimo número de Fibonacci é igual a 2"""
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_m1(self):
        """Testa so o programa lança o erro quando recebe um número negativo"""
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == "__main__":
    unittest.main()
