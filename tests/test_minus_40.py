# test_minus_40.py
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


class TestMinus40(unittest.TestCase):

    def test_40_minus_0(self):
        self.assertEqual(run_calculator('40', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-0 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_1(self):
        self.assertEqual(run_calculator('40', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-1 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_2(self):
        self.assertEqual(run_calculator('40', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-2 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_3(self):
        self.assertEqual(run_calculator('40', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-3 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_4(self):
        self.assertEqual(run_calculator('40', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-4 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_5(self):
        self.assertEqual(run_calculator('40', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-5 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_6(self):
        self.assertEqual(run_calculator('40', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-6 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_7(self):
        self.assertEqual(run_calculator('40', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-7 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_8(self):
        self.assertEqual(run_calculator('40', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-8 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_9(self):
        self.assertEqual(run_calculator('40', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-9 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_10(self):
        self.assertEqual(run_calculator('40', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-10 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_11(self):
        self.assertEqual(run_calculator('40', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-11 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_12(self):
        self.assertEqual(run_calculator('40', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-12 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_13(self):
        self.assertEqual(run_calculator('40', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-13 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_14(self):
        self.assertEqual(run_calculator('40', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-14 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_15(self):
        self.assertEqual(run_calculator('40', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-15 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_16(self):
        self.assertEqual(run_calculator('40', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-16 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_17(self):
        self.assertEqual(run_calculator('40', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-17 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_18(self):
        self.assertEqual(run_calculator('40', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-18 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_19(self):
        self.assertEqual(run_calculator('40', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-19 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_20(self):
        self.assertEqual(run_calculator('40', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-20 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_21(self):
        self.assertEqual(run_calculator('40', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-21 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_22(self):
        self.assertEqual(run_calculator('40', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-22 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_23(self):
        self.assertEqual(run_calculator('40', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-23 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_24(self):
        self.assertEqual(run_calculator('40', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-24 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_25(self):
        self.assertEqual(run_calculator('40', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-25 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_26(self):
        self.assertEqual(run_calculator('40', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-26 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_27(self):
        self.assertEqual(run_calculator('40', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-27 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_28(self):
        self.assertEqual(run_calculator('40', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-28 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_29(self):
        self.assertEqual(run_calculator('40', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-29 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_30(self):
        self.assertEqual(run_calculator('40', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-30 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_31(self):
        self.assertEqual(run_calculator('40', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-31 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_32(self):
        self.assertEqual(run_calculator('40', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-32 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_33(self):
        self.assertEqual(run_calculator('40', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-33 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_34(self):
        self.assertEqual(run_calculator('40', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-34 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_35(self):
        self.assertEqual(run_calculator('40', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-35 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_36(self):
        self.assertEqual(run_calculator('40', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-36 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_37(self):
        self.assertEqual(run_calculator('40', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-37 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_38(self):
        self.assertEqual(run_calculator('40', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-38 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_39(self):
        self.assertEqual(run_calculator('40', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-39 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_40(self):
        self.assertEqual(run_calculator('40', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-40 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_41(self):
        self.assertEqual(run_calculator('40', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-41 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_42(self):
        self.assertEqual(run_calculator('40', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-42 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_43(self):
        self.assertEqual(run_calculator('40', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-43 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_44(self):
        self.assertEqual(run_calculator('40', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-44 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_45(self):
        self.assertEqual(run_calculator('40', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-45 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_46(self):
        self.assertEqual(run_calculator('40', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-46 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_47(self):
        self.assertEqual(run_calculator('40', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-47 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_48(self):
        self.assertEqual(run_calculator('40', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-48 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_49(self):
        self.assertEqual(run_calculator('40', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-49 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_minus_50(self):
        self.assertEqual(run_calculator('40', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40-50 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
