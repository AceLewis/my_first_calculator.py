# test_minus_27.py
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


class TestMinus27(unittest.TestCase):

    def test_27_minus_0(self):
        self.assertEqual(run_calculator('27', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-0 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_1(self):
        self.assertEqual(run_calculator('27', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-1 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_2(self):
        self.assertEqual(run_calculator('27', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-2 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_3(self):
        self.assertEqual(run_calculator('27', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-3 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_4(self):
        self.assertEqual(run_calculator('27', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-4 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_5(self):
        self.assertEqual(run_calculator('27', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-5 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_6(self):
        self.assertEqual(run_calculator('27', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-6 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_7(self):
        self.assertEqual(run_calculator('27', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-7 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_8(self):
        self.assertEqual(run_calculator('27', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-8 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_9(self):
        self.assertEqual(run_calculator('27', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-9 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_10(self):
        self.assertEqual(run_calculator('27', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-10 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_11(self):
        self.assertEqual(run_calculator('27', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-11 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_12(self):
        self.assertEqual(run_calculator('27', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-12 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_13(self):
        self.assertEqual(run_calculator('27', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-13 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_14(self):
        self.assertEqual(run_calculator('27', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-14 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_15(self):
        self.assertEqual(run_calculator('27', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-15 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_16(self):
        self.assertEqual(run_calculator('27', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-16 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_17(self):
        self.assertEqual(run_calculator('27', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-17 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_18(self):
        self.assertEqual(run_calculator('27', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-18 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_19(self):
        self.assertEqual(run_calculator('27', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-19 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_20(self):
        self.assertEqual(run_calculator('27', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-20 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_21(self):
        self.assertEqual(run_calculator('27', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-21 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_22(self):
        self.assertEqual(run_calculator('27', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-22 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_23(self):
        self.assertEqual(run_calculator('27', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-23 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_24(self):
        self.assertEqual(run_calculator('27', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-24 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_25(self):
        self.assertEqual(run_calculator('27', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-25 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_26(self):
        self.assertEqual(run_calculator('27', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-26 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_27(self):
        self.assertEqual(run_calculator('27', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-27 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_28(self):
        self.assertEqual(run_calculator('27', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-28 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_29(self):
        self.assertEqual(run_calculator('27', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-29 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_30(self):
        self.assertEqual(run_calculator('27', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-30 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_31(self):
        self.assertEqual(run_calculator('27', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-31 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_32(self):
        self.assertEqual(run_calculator('27', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-32 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_33(self):
        self.assertEqual(run_calculator('27', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-33 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_34(self):
        self.assertEqual(run_calculator('27', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-34 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_35(self):
        self.assertEqual(run_calculator('27', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-35 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_36(self):
        self.assertEqual(run_calculator('27', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-36 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_37(self):
        self.assertEqual(run_calculator('27', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-37 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_38(self):
        self.assertEqual(run_calculator('27', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-38 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_39(self):
        self.assertEqual(run_calculator('27', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-39 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_40(self):
        self.assertEqual(run_calculator('27', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-40 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_41(self):
        self.assertEqual(run_calculator('27', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-41 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_42(self):
        self.assertEqual(run_calculator('27', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-42 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_43(self):
        self.assertEqual(run_calculator('27', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-43 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_44(self):
        self.assertEqual(run_calculator('27', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-44 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_45(self):
        self.assertEqual(run_calculator('27', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-45 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_46(self):
        self.assertEqual(run_calculator('27', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-46 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_47(self):
        self.assertEqual(run_calculator('27', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-47 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_48(self):
        self.assertEqual(run_calculator('27', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-48 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_49(self):
        self.assertEqual(run_calculator('27', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-49 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_minus_50(self):
        self.assertEqual(run_calculator('27', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27-50 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
