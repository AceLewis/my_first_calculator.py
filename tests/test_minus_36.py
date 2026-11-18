# test_minus_36.py
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


class TestMinus36(unittest.TestCase):

    def test_36_minus_0(self):
        self.assertEqual(run_calculator('36', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-0 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_1(self):
        self.assertEqual(run_calculator('36', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-1 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_2(self):
        self.assertEqual(run_calculator('36', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-2 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_3(self):
        self.assertEqual(run_calculator('36', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-3 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_4(self):
        self.assertEqual(run_calculator('36', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-4 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_5(self):
        self.assertEqual(run_calculator('36', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-5 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_6(self):
        self.assertEqual(run_calculator('36', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-6 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_7(self):
        self.assertEqual(run_calculator('36', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-7 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_8(self):
        self.assertEqual(run_calculator('36', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-8 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_9(self):
        self.assertEqual(run_calculator('36', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-9 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_10(self):
        self.assertEqual(run_calculator('36', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-10 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_11(self):
        self.assertEqual(run_calculator('36', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-11 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_12(self):
        self.assertEqual(run_calculator('36', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-12 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_13(self):
        self.assertEqual(run_calculator('36', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-13 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_14(self):
        self.assertEqual(run_calculator('36', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-14 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_15(self):
        self.assertEqual(run_calculator('36', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-15 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_16(self):
        self.assertEqual(run_calculator('36', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-16 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_17(self):
        self.assertEqual(run_calculator('36', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-17 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_18(self):
        self.assertEqual(run_calculator('36', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-18 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_19(self):
        self.assertEqual(run_calculator('36', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-19 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_20(self):
        self.assertEqual(run_calculator('36', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-20 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_21(self):
        self.assertEqual(run_calculator('36', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-21 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_22(self):
        self.assertEqual(run_calculator('36', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-22 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_23(self):
        self.assertEqual(run_calculator('36', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-23 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_24(self):
        self.assertEqual(run_calculator('36', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-24 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_25(self):
        self.assertEqual(run_calculator('36', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-25 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_26(self):
        self.assertEqual(run_calculator('36', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-26 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_27(self):
        self.assertEqual(run_calculator('36', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-27 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_28(self):
        self.assertEqual(run_calculator('36', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-28 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_29(self):
        self.assertEqual(run_calculator('36', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-29 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_30(self):
        self.assertEqual(run_calculator('36', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-30 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_31(self):
        self.assertEqual(run_calculator('36', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-31 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_32(self):
        self.assertEqual(run_calculator('36', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-32 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_33(self):
        self.assertEqual(run_calculator('36', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-33 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_34(self):
        self.assertEqual(run_calculator('36', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-34 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_35(self):
        self.assertEqual(run_calculator('36', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-35 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_36(self):
        self.assertEqual(run_calculator('36', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-36 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_37(self):
        self.assertEqual(run_calculator('36', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-37 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_38(self):
        self.assertEqual(run_calculator('36', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-38 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_39(self):
        self.assertEqual(run_calculator('36', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-39 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_40(self):
        self.assertEqual(run_calculator('36', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-40 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_41(self):
        self.assertEqual(run_calculator('36', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-41 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_42(self):
        self.assertEqual(run_calculator('36', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-42 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_43(self):
        self.assertEqual(run_calculator('36', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-43 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_44(self):
        self.assertEqual(run_calculator('36', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-44 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_45(self):
        self.assertEqual(run_calculator('36', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-45 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_46(self):
        self.assertEqual(run_calculator('36', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-46 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_47(self):
        self.assertEqual(run_calculator('36', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-47 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_48(self):
        self.assertEqual(run_calculator('36', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-48 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_49(self):
        self.assertEqual(run_calculator('36', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-49 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_minus_50(self):
        self.assertEqual(run_calculator('36', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36-50 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
