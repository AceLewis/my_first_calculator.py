# test_minus_31.py
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


class TestMinus31(unittest.TestCase):

    def test_31_minus_0(self):
        self.assertEqual(run_calculator('31', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-0 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_1(self):
        self.assertEqual(run_calculator('31', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-1 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_2(self):
        self.assertEqual(run_calculator('31', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-2 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_3(self):
        self.assertEqual(run_calculator('31', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-3 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_4(self):
        self.assertEqual(run_calculator('31', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-4 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_5(self):
        self.assertEqual(run_calculator('31', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-5 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_6(self):
        self.assertEqual(run_calculator('31', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-6 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_7(self):
        self.assertEqual(run_calculator('31', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-7 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_8(self):
        self.assertEqual(run_calculator('31', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-8 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_9(self):
        self.assertEqual(run_calculator('31', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-9 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_10(self):
        self.assertEqual(run_calculator('31', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-10 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_11(self):
        self.assertEqual(run_calculator('31', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-11 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_12(self):
        self.assertEqual(run_calculator('31', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-12 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_13(self):
        self.assertEqual(run_calculator('31', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-13 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_14(self):
        self.assertEqual(run_calculator('31', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-14 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_15(self):
        self.assertEqual(run_calculator('31', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-15 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_16(self):
        self.assertEqual(run_calculator('31', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-16 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_17(self):
        self.assertEqual(run_calculator('31', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-17 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_18(self):
        self.assertEqual(run_calculator('31', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-18 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_19(self):
        self.assertEqual(run_calculator('31', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-19 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_20(self):
        self.assertEqual(run_calculator('31', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-20 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_21(self):
        self.assertEqual(run_calculator('31', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-21 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_22(self):
        self.assertEqual(run_calculator('31', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-22 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_23(self):
        self.assertEqual(run_calculator('31', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-23 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_24(self):
        self.assertEqual(run_calculator('31', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-24 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_25(self):
        self.assertEqual(run_calculator('31', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-25 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_26(self):
        self.assertEqual(run_calculator('31', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-26 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_27(self):
        self.assertEqual(run_calculator('31', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-27 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_28(self):
        self.assertEqual(run_calculator('31', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-28 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_29(self):
        self.assertEqual(run_calculator('31', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-29 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_30(self):
        self.assertEqual(run_calculator('31', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-30 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_31(self):
        self.assertEqual(run_calculator('31', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-31 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_32(self):
        self.assertEqual(run_calculator('31', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-32 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_33(self):
        self.assertEqual(run_calculator('31', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-33 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_34(self):
        self.assertEqual(run_calculator('31', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-34 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_35(self):
        self.assertEqual(run_calculator('31', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-35 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_36(self):
        self.assertEqual(run_calculator('31', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-36 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_37(self):
        self.assertEqual(run_calculator('31', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-37 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_38(self):
        self.assertEqual(run_calculator('31', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-38 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_39(self):
        self.assertEqual(run_calculator('31', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-39 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_40(self):
        self.assertEqual(run_calculator('31', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-40 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_41(self):
        self.assertEqual(run_calculator('31', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-41 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_42(self):
        self.assertEqual(run_calculator('31', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-42 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_43(self):
        self.assertEqual(run_calculator('31', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-43 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_44(self):
        self.assertEqual(run_calculator('31', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-44 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_45(self):
        self.assertEqual(run_calculator('31', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-45 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_46(self):
        self.assertEqual(run_calculator('31', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-46 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_47(self):
        self.assertEqual(run_calculator('31', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-47 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_48(self):
        self.assertEqual(run_calculator('31', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-48 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_49(self):
        self.assertEqual(run_calculator('31', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-49 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_minus_50(self):
        self.assertEqual(run_calculator('31', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31-50 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
