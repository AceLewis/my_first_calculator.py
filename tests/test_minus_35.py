# test_minus_35.py
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


class TestMinus35(unittest.TestCase):

    def test_35_minus_0(self):
        self.assertEqual(run_calculator('35', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-0 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_1(self):
        self.assertEqual(run_calculator('35', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-1 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_2(self):
        self.assertEqual(run_calculator('35', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-2 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_3(self):
        self.assertEqual(run_calculator('35', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-3 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_4(self):
        self.assertEqual(run_calculator('35', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-4 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_5(self):
        self.assertEqual(run_calculator('35', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-5 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_6(self):
        self.assertEqual(run_calculator('35', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-6 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_7(self):
        self.assertEqual(run_calculator('35', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-7 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_8(self):
        self.assertEqual(run_calculator('35', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-8 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_9(self):
        self.assertEqual(run_calculator('35', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-9 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_10(self):
        self.assertEqual(run_calculator('35', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-10 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_11(self):
        self.assertEqual(run_calculator('35', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-11 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_12(self):
        self.assertEqual(run_calculator('35', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-12 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_13(self):
        self.assertEqual(run_calculator('35', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-13 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_14(self):
        self.assertEqual(run_calculator('35', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-14 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_15(self):
        self.assertEqual(run_calculator('35', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-15 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_16(self):
        self.assertEqual(run_calculator('35', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-16 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_17(self):
        self.assertEqual(run_calculator('35', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-17 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_18(self):
        self.assertEqual(run_calculator('35', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-18 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_19(self):
        self.assertEqual(run_calculator('35', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-19 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_20(self):
        self.assertEqual(run_calculator('35', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-20 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_21(self):
        self.assertEqual(run_calculator('35', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-21 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_22(self):
        self.assertEqual(run_calculator('35', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-22 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_23(self):
        self.assertEqual(run_calculator('35', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-23 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_24(self):
        self.assertEqual(run_calculator('35', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-24 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_25(self):
        self.assertEqual(run_calculator('35', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-25 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_26(self):
        self.assertEqual(run_calculator('35', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-26 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_27(self):
        self.assertEqual(run_calculator('35', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-27 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_28(self):
        self.assertEqual(run_calculator('35', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-28 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_29(self):
        self.assertEqual(run_calculator('35', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-29 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_30(self):
        self.assertEqual(run_calculator('35', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-30 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_31(self):
        self.assertEqual(run_calculator('35', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-31 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_32(self):
        self.assertEqual(run_calculator('35', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-32 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_33(self):
        self.assertEqual(run_calculator('35', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-33 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_34(self):
        self.assertEqual(run_calculator('35', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-34 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_35(self):
        self.assertEqual(run_calculator('35', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-35 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_36(self):
        self.assertEqual(run_calculator('35', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-36 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_37(self):
        self.assertEqual(run_calculator('35', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-37 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_38(self):
        self.assertEqual(run_calculator('35', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-38 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_39(self):
        self.assertEqual(run_calculator('35', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-39 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_40(self):
        self.assertEqual(run_calculator('35', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-40 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_41(self):
        self.assertEqual(run_calculator('35', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-41 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_42(self):
        self.assertEqual(run_calculator('35', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-42 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_43(self):
        self.assertEqual(run_calculator('35', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-43 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_44(self):
        self.assertEqual(run_calculator('35', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-44 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_45(self):
        self.assertEqual(run_calculator('35', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-45 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_46(self):
        self.assertEqual(run_calculator('35', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-46 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_47(self):
        self.assertEqual(run_calculator('35', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-47 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_48(self):
        self.assertEqual(run_calculator('35', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-48 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_49(self):
        self.assertEqual(run_calculator('35', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-49 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_minus_50(self):
        self.assertEqual(run_calculator('35', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35-50 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
