import io
import operator
import unittest
from contextlib import redirect_stdout
from decimal import Decimal
from pathlib import Path
from unittest import mock

SOURCE = Path(__file__).with_name('my_first_calculator.py')
CODE = compile(SOURCE.read_text(), str(SOURCE), 'exec')
NUMS = range(0, 51)
SIGNS = ['+', '-', '/', '*']
OPS = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}


def run_calculator(num1, sign, num2):
    answers = iter([str(num1), sign, str(num2)])
    out = io.StringIO()
    with mock.patch('builtins.input', lambda _prompt='': next(answers)), redirect_stdout(out):
        exec(CODE, {'__name__': '__main__'})
    return out.getvalue().splitlines()


def expected_result(num1, sign, num2):
    if sign == '/' and num2 == 0:
        return 'Undefined' if num1 == 0 else 'Inf'
    return OPS[sign](Decimal(num1), Decimal(num2))


class TestMyFirstCalculator(unittest.TestCase):
    def test_all_cases(self):
        for sign in SIGNS:
            for num1 in NUMS:
                for num2 in NUMS:
                    with self.subTest(num1=num1, sign=sign, num2=num2):
                        self.assertEqual(run_calculator(num1, sign, num2), [
                            'Welcome to this calculator!',
                            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
                            '{}{}{} = {}'.format(num1, sign, num2, expected_result(num1, sign, num2)),
                            'Thanks for using this calculator, goodbye :)',
                        ])

    def test_out_of_range_prints_no_result(self):
        self.assertEqual(run_calculator(51, '+', 1), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
