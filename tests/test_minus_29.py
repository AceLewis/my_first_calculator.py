# test_minus_29.py
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


class TestMinus29(unittest.TestCase):

    def test_29_minus_0(self):
        self.assertEqual(run_calculator('29', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-0 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_1(self):
        self.assertEqual(run_calculator('29', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-1 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_2(self):
        self.assertEqual(run_calculator('29', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-2 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_3(self):
        self.assertEqual(run_calculator('29', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-3 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_4(self):
        self.assertEqual(run_calculator('29', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-4 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_5(self):
        self.assertEqual(run_calculator('29', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-5 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_6(self):
        self.assertEqual(run_calculator('29', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-6 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_7(self):
        self.assertEqual(run_calculator('29', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-7 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_8(self):
        self.assertEqual(run_calculator('29', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-8 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_9(self):
        self.assertEqual(run_calculator('29', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-9 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_10(self):
        self.assertEqual(run_calculator('29', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-10 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_11(self):
        self.assertEqual(run_calculator('29', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-11 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_12(self):
        self.assertEqual(run_calculator('29', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-12 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_13(self):
        self.assertEqual(run_calculator('29', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-13 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_14(self):
        self.assertEqual(run_calculator('29', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-14 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_15(self):
        self.assertEqual(run_calculator('29', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-15 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_16(self):
        self.assertEqual(run_calculator('29', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-16 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_17(self):
        self.assertEqual(run_calculator('29', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-17 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_18(self):
        self.assertEqual(run_calculator('29', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-18 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_19(self):
        self.assertEqual(run_calculator('29', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-19 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_20(self):
        self.assertEqual(run_calculator('29', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-20 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_21(self):
        self.assertEqual(run_calculator('29', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-21 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_22(self):
        self.assertEqual(run_calculator('29', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-22 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_23(self):
        self.assertEqual(run_calculator('29', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-23 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_24(self):
        self.assertEqual(run_calculator('29', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-24 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_25(self):
        self.assertEqual(run_calculator('29', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-25 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_26(self):
        self.assertEqual(run_calculator('29', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-26 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_27(self):
        self.assertEqual(run_calculator('29', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-27 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_28(self):
        self.assertEqual(run_calculator('29', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-28 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_29(self):
        self.assertEqual(run_calculator('29', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-29 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_30(self):
        self.assertEqual(run_calculator('29', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-30 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_31(self):
        self.assertEqual(run_calculator('29', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-31 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_32(self):
        self.assertEqual(run_calculator('29', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-32 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_33(self):
        self.assertEqual(run_calculator('29', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-33 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_34(self):
        self.assertEqual(run_calculator('29', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-34 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_35(self):
        self.assertEqual(run_calculator('29', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-35 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_36(self):
        self.assertEqual(run_calculator('29', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-36 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_37(self):
        self.assertEqual(run_calculator('29', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-37 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_38(self):
        self.assertEqual(run_calculator('29', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-38 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_39(self):
        self.assertEqual(run_calculator('29', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-39 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_40(self):
        self.assertEqual(run_calculator('29', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-40 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_41(self):
        self.assertEqual(run_calculator('29', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-41 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_42(self):
        self.assertEqual(run_calculator('29', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-42 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_43(self):
        self.assertEqual(run_calculator('29', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-43 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_44(self):
        self.assertEqual(run_calculator('29', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-44 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_45(self):
        self.assertEqual(run_calculator('29', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-45 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_46(self):
        self.assertEqual(run_calculator('29', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-46 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_47(self):
        self.assertEqual(run_calculator('29', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-47 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_48(self):
        self.assertEqual(run_calculator('29', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-48 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_49(self):
        self.assertEqual(run_calculator('29', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-49 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_minus_50(self):
        self.assertEqual(run_calculator('29', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29-50 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
