# test_minus_25.py
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


class TestMinus25(unittest.TestCase):

    def test_25_minus_0(self):
        self.assertEqual(run_calculator('25', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-0 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_1(self):
        self.assertEqual(run_calculator('25', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-1 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_2(self):
        self.assertEqual(run_calculator('25', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-2 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_3(self):
        self.assertEqual(run_calculator('25', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-3 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_4(self):
        self.assertEqual(run_calculator('25', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-4 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_5(self):
        self.assertEqual(run_calculator('25', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-5 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_6(self):
        self.assertEqual(run_calculator('25', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-6 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_7(self):
        self.assertEqual(run_calculator('25', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-7 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_8(self):
        self.assertEqual(run_calculator('25', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-8 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_9(self):
        self.assertEqual(run_calculator('25', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-9 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_10(self):
        self.assertEqual(run_calculator('25', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-10 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_11(self):
        self.assertEqual(run_calculator('25', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-11 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_12(self):
        self.assertEqual(run_calculator('25', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-12 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_13(self):
        self.assertEqual(run_calculator('25', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-13 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_14(self):
        self.assertEqual(run_calculator('25', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-14 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_15(self):
        self.assertEqual(run_calculator('25', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-15 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_16(self):
        self.assertEqual(run_calculator('25', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-16 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_17(self):
        self.assertEqual(run_calculator('25', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-17 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_18(self):
        self.assertEqual(run_calculator('25', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-18 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_19(self):
        self.assertEqual(run_calculator('25', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-19 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_20(self):
        self.assertEqual(run_calculator('25', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-20 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_21(self):
        self.assertEqual(run_calculator('25', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-21 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_22(self):
        self.assertEqual(run_calculator('25', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-22 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_23(self):
        self.assertEqual(run_calculator('25', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-23 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_24(self):
        self.assertEqual(run_calculator('25', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-24 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_25(self):
        self.assertEqual(run_calculator('25', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-25 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_26(self):
        self.assertEqual(run_calculator('25', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-26 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_27(self):
        self.assertEqual(run_calculator('25', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-27 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_28(self):
        self.assertEqual(run_calculator('25', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-28 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_29(self):
        self.assertEqual(run_calculator('25', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-29 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_30(self):
        self.assertEqual(run_calculator('25', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-30 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_31(self):
        self.assertEqual(run_calculator('25', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-31 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_32(self):
        self.assertEqual(run_calculator('25', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-32 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_33(self):
        self.assertEqual(run_calculator('25', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-33 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_34(self):
        self.assertEqual(run_calculator('25', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-34 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_35(self):
        self.assertEqual(run_calculator('25', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-35 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_36(self):
        self.assertEqual(run_calculator('25', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-36 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_37(self):
        self.assertEqual(run_calculator('25', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-37 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_38(self):
        self.assertEqual(run_calculator('25', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-38 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_39(self):
        self.assertEqual(run_calculator('25', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-39 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_40(self):
        self.assertEqual(run_calculator('25', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-40 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_41(self):
        self.assertEqual(run_calculator('25', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-41 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_42(self):
        self.assertEqual(run_calculator('25', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-42 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_43(self):
        self.assertEqual(run_calculator('25', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-43 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_44(self):
        self.assertEqual(run_calculator('25', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-44 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_45(self):
        self.assertEqual(run_calculator('25', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-45 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_46(self):
        self.assertEqual(run_calculator('25', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-46 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_47(self):
        self.assertEqual(run_calculator('25', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-47 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_48(self):
        self.assertEqual(run_calculator('25', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-48 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_49(self):
        self.assertEqual(run_calculator('25', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-49 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_minus_50(self):
        self.assertEqual(run_calculator('25', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25-50 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
