"""Tests task 9, error: В начале или конце строки-результата лишние символы (пробелы, ...)"""
from unittest import TestCase
import task_9


class Task9Test(TestCase):
    """Тесты для задания 9."""

    def test_length(self):
        """Проверка что после расшифровки длина строки равна длине строки в зашифрованном виде."""
        initial_data: str = 'омоюу толл дюиа акчп йрьк'
        result: str = task_9.TheRabbitsFoot(initial_data, False)
        self.assertEqual(len(initial_data), len(result))

    def test_first_and_last_symbols_for_space(self):
        """Проверка что после расшифровки первый и последний символ не являются пробелами."""
        initial_data: str = 'омоюу толл дюиа акчп йрьк'
        result: str = task_9.TheRabbitsFoot(initial_data, False)
        self.assertFalse(result[0] == " ")
        self.assertFalse(result[len(result) - 1] == " ")
