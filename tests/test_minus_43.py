# test_minus_43.py
# Every single case gets its own test, to be true to the story

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

SOURCE = Path(__file__).parent.parent / 'my_first_calculator.py'
CODE = compile(SOURCE.read_text(), str(SOURCE), 'exec')


def run_calculator(num1, sign, num2):
    answers = iter([num1, sign, num2])
    out = io.StringIO()
    with mock.patch('builtins.input', lambda prompt='': next(answers)), redirect_stdout(out):
        exec(CODE, {'__name__': '__main__'})
    return out.getvalue().splitlines()


class TestMinus43(unittest.TestCase):

    def test_43_minus_0(self):
        self.assertEqual(run_calculator('43', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-0 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_1(self):
        self.assertEqual(run_calculator('43', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-1 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_2(self):
        self.assertEqual(run_calculator('43', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-2 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_3(self):
        self.assertEqual(run_calculator('43', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-3 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_4(self):
        self.assertEqual(run_calculator('43', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-4 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_5(self):
        self.assertEqual(run_calculator('43', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-5 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_6(self):
        self.assertEqual(run_calculator('43', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-6 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_7(self):
        self.assertEqual(run_calculator('43', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-7 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_8(self):
        self.assertEqual(run_calculator('43', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-8 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_9(self):
        self.assertEqual(run_calculator('43', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-9 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_10(self):
        self.assertEqual(run_calculator('43', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-10 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_11(self):
        self.assertEqual(run_calculator('43', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-11 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_12(self):
        self.assertEqual(run_calculator('43', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-12 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_13(self):
        self.assertEqual(run_calculator('43', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-13 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_14(self):
        self.assertEqual(run_calculator('43', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-14 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_15(self):
        self.assertEqual(run_calculator('43', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-15 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_16(self):
        self.assertEqual(run_calculator('43', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-16 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_17(self):
        self.assertEqual(run_calculator('43', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-17 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_18(self):
        self.assertEqual(run_calculator('43', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-18 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_19(self):
        self.assertEqual(run_calculator('43', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-19 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_20(self):
        self.assertEqual(run_calculator('43', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-20 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_21(self):
        self.assertEqual(run_calculator('43', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-21 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_22(self):
        self.assertEqual(run_calculator('43', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-22 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_23(self):
        self.assertEqual(run_calculator('43', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-23 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_24(self):
        self.assertEqual(run_calculator('43', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-24 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_25(self):
        self.assertEqual(run_calculator('43', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-25 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_26(self):
        self.assertEqual(run_calculator('43', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-26 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_27(self):
        self.assertEqual(run_calculator('43', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-27 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_28(self):
        self.assertEqual(run_calculator('43', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-28 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_29(self):
        self.assertEqual(run_calculator('43', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-29 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_30(self):
        self.assertEqual(run_calculator('43', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-30 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_31(self):
        self.assertEqual(run_calculator('43', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-31 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_32(self):
        self.assertEqual(run_calculator('43', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-32 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_33(self):
        self.assertEqual(run_calculator('43', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-33 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_34(self):
        self.assertEqual(run_calculator('43', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-34 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_35(self):
        self.assertEqual(run_calculator('43', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-35 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_36(self):
        self.assertEqual(run_calculator('43', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-36 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_37(self):
        self.assertEqual(run_calculator('43', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-37 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_38(self):
        self.assertEqual(run_calculator('43', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-38 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_39(self):
        self.assertEqual(run_calculator('43', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-39 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_40(self):
        self.assertEqual(run_calculator('43', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-40 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_41(self):
        self.assertEqual(run_calculator('43', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-41 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_42(self):
        self.assertEqual(run_calculator('43', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-42 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_43(self):
        self.assertEqual(run_calculator('43', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-43 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_44(self):
        self.assertEqual(run_calculator('43', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-44 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_45(self):
        self.assertEqual(run_calculator('43', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-45 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_46(self):
        self.assertEqual(run_calculator('43', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-46 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_47(self):
        self.assertEqual(run_calculator('43', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-47 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_48(self):
        self.assertEqual(run_calculator('43', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-48 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_49(self):
        self.assertEqual(run_calculator('43', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-49 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_minus_50(self):
        self.assertEqual(run_calculator('43', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43-50 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
