# test_minus_21.py
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


class TestMinus21(unittest.TestCase):

    def test_21_minus_0(self):
        self.assertEqual(run_calculator('21', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-0 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_1(self):
        self.assertEqual(run_calculator('21', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-1 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_2(self):
        self.assertEqual(run_calculator('21', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-2 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_3(self):
        self.assertEqual(run_calculator('21', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-3 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_4(self):
        self.assertEqual(run_calculator('21', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-4 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_5(self):
        self.assertEqual(run_calculator('21', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-5 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_6(self):
        self.assertEqual(run_calculator('21', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-6 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_7(self):
        self.assertEqual(run_calculator('21', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-7 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_8(self):
        self.assertEqual(run_calculator('21', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-8 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_9(self):
        self.assertEqual(run_calculator('21', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-9 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_10(self):
        self.assertEqual(run_calculator('21', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-10 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_11(self):
        self.assertEqual(run_calculator('21', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-11 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_12(self):
        self.assertEqual(run_calculator('21', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-12 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_13(self):
        self.assertEqual(run_calculator('21', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-13 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_14(self):
        self.assertEqual(run_calculator('21', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-14 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_15(self):
        self.assertEqual(run_calculator('21', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-15 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_16(self):
        self.assertEqual(run_calculator('21', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-16 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_17(self):
        self.assertEqual(run_calculator('21', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-17 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_18(self):
        self.assertEqual(run_calculator('21', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-18 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_19(self):
        self.assertEqual(run_calculator('21', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-19 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_20(self):
        self.assertEqual(run_calculator('21', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-20 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_21(self):
        self.assertEqual(run_calculator('21', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-21 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_22(self):
        self.assertEqual(run_calculator('21', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-22 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_23(self):
        self.assertEqual(run_calculator('21', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-23 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_24(self):
        self.assertEqual(run_calculator('21', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-24 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_25(self):
        self.assertEqual(run_calculator('21', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-25 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_26(self):
        self.assertEqual(run_calculator('21', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-26 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_27(self):
        self.assertEqual(run_calculator('21', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-27 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_28(self):
        self.assertEqual(run_calculator('21', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-28 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_29(self):
        self.assertEqual(run_calculator('21', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-29 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_30(self):
        self.assertEqual(run_calculator('21', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-30 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_31(self):
        self.assertEqual(run_calculator('21', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-31 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_32(self):
        self.assertEqual(run_calculator('21', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-32 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_33(self):
        self.assertEqual(run_calculator('21', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-33 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_34(self):
        self.assertEqual(run_calculator('21', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-34 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_35(self):
        self.assertEqual(run_calculator('21', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-35 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_36(self):
        self.assertEqual(run_calculator('21', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-36 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_37(self):
        self.assertEqual(run_calculator('21', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-37 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_38(self):
        self.assertEqual(run_calculator('21', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-38 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_39(self):
        self.assertEqual(run_calculator('21', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-39 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_40(self):
        self.assertEqual(run_calculator('21', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-40 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_41(self):
        self.assertEqual(run_calculator('21', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-41 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_42(self):
        self.assertEqual(run_calculator('21', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-42 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_43(self):
        self.assertEqual(run_calculator('21', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-43 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_44(self):
        self.assertEqual(run_calculator('21', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-44 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_45(self):
        self.assertEqual(run_calculator('21', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-45 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_46(self):
        self.assertEqual(run_calculator('21', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-46 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_47(self):
        self.assertEqual(run_calculator('21', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-47 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_48(self):
        self.assertEqual(run_calculator('21', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-48 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_49(self):
        self.assertEqual(run_calculator('21', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-49 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_minus_50(self):
        self.assertEqual(run_calculator('21', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21-50 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
