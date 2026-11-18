# test_minus_30.py
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


class TestMinus30(unittest.TestCase):

    def test_30_minus_0(self):
        self.assertEqual(run_calculator('30', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-0 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_1(self):
        self.assertEqual(run_calculator('30', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-1 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_2(self):
        self.assertEqual(run_calculator('30', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-2 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_3(self):
        self.assertEqual(run_calculator('30', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-3 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_4(self):
        self.assertEqual(run_calculator('30', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-4 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_5(self):
        self.assertEqual(run_calculator('30', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-5 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_6(self):
        self.assertEqual(run_calculator('30', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-6 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_7(self):
        self.assertEqual(run_calculator('30', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-7 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_8(self):
        self.assertEqual(run_calculator('30', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-8 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_9(self):
        self.assertEqual(run_calculator('30', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-9 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_10(self):
        self.assertEqual(run_calculator('30', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-10 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_11(self):
        self.assertEqual(run_calculator('30', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-11 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_12(self):
        self.assertEqual(run_calculator('30', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-12 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_13(self):
        self.assertEqual(run_calculator('30', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-13 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_14(self):
        self.assertEqual(run_calculator('30', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-14 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_15(self):
        self.assertEqual(run_calculator('30', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-15 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_16(self):
        self.assertEqual(run_calculator('30', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-16 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_17(self):
        self.assertEqual(run_calculator('30', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-17 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_18(self):
        self.assertEqual(run_calculator('30', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-18 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_19(self):
        self.assertEqual(run_calculator('30', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-19 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_20(self):
        self.assertEqual(run_calculator('30', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-20 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_21(self):
        self.assertEqual(run_calculator('30', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-21 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_22(self):
        self.assertEqual(run_calculator('30', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-22 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_23(self):
        self.assertEqual(run_calculator('30', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-23 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_24(self):
        self.assertEqual(run_calculator('30', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-24 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_25(self):
        self.assertEqual(run_calculator('30', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-25 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_26(self):
        self.assertEqual(run_calculator('30', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-26 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_27(self):
        self.assertEqual(run_calculator('30', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-27 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_28(self):
        self.assertEqual(run_calculator('30', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-28 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_29(self):
        self.assertEqual(run_calculator('30', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-29 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_30(self):
        self.assertEqual(run_calculator('30', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-30 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_31(self):
        self.assertEqual(run_calculator('30', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-31 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_32(self):
        self.assertEqual(run_calculator('30', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-32 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_33(self):
        self.assertEqual(run_calculator('30', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-33 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_34(self):
        self.assertEqual(run_calculator('30', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-34 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_35(self):
        self.assertEqual(run_calculator('30', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-35 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_36(self):
        self.assertEqual(run_calculator('30', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-36 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_37(self):
        self.assertEqual(run_calculator('30', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-37 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_38(self):
        self.assertEqual(run_calculator('30', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-38 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_39(self):
        self.assertEqual(run_calculator('30', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-39 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_40(self):
        self.assertEqual(run_calculator('30', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-40 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_41(self):
        self.assertEqual(run_calculator('30', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-41 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_42(self):
        self.assertEqual(run_calculator('30', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-42 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_43(self):
        self.assertEqual(run_calculator('30', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-43 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_44(self):
        self.assertEqual(run_calculator('30', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-44 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_45(self):
        self.assertEqual(run_calculator('30', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-45 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_46(self):
        self.assertEqual(run_calculator('30', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-46 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_47(self):
        self.assertEqual(run_calculator('30', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-47 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_48(self):
        self.assertEqual(run_calculator('30', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-48 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_49(self):
        self.assertEqual(run_calculator('30', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-49 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_minus_50(self):
        self.assertEqual(run_calculator('30', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30-50 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
