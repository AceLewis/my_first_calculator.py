# test_minus_24.py
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


class TestMinus24(unittest.TestCase):

    def test_24_minus_0(self):
        self.assertEqual(run_calculator('24', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-0 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_1(self):
        self.assertEqual(run_calculator('24', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-1 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_2(self):
        self.assertEqual(run_calculator('24', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-2 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_3(self):
        self.assertEqual(run_calculator('24', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-3 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_4(self):
        self.assertEqual(run_calculator('24', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-4 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_5(self):
        self.assertEqual(run_calculator('24', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-5 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_6(self):
        self.assertEqual(run_calculator('24', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-6 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_7(self):
        self.assertEqual(run_calculator('24', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-7 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_8(self):
        self.assertEqual(run_calculator('24', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-8 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_9(self):
        self.assertEqual(run_calculator('24', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-9 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_10(self):
        self.assertEqual(run_calculator('24', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-10 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_11(self):
        self.assertEqual(run_calculator('24', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-11 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_12(self):
        self.assertEqual(run_calculator('24', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-12 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_13(self):
        self.assertEqual(run_calculator('24', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-13 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_14(self):
        self.assertEqual(run_calculator('24', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-14 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_15(self):
        self.assertEqual(run_calculator('24', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-15 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_16(self):
        self.assertEqual(run_calculator('24', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-16 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_17(self):
        self.assertEqual(run_calculator('24', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-17 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_18(self):
        self.assertEqual(run_calculator('24', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-18 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_19(self):
        self.assertEqual(run_calculator('24', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-19 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_20(self):
        self.assertEqual(run_calculator('24', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-20 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_21(self):
        self.assertEqual(run_calculator('24', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-21 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_22(self):
        self.assertEqual(run_calculator('24', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-22 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_23(self):
        self.assertEqual(run_calculator('24', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-23 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_24(self):
        self.assertEqual(run_calculator('24', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-24 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_25(self):
        self.assertEqual(run_calculator('24', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-25 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_26(self):
        self.assertEqual(run_calculator('24', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-26 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_27(self):
        self.assertEqual(run_calculator('24', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-27 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_28(self):
        self.assertEqual(run_calculator('24', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-28 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_29(self):
        self.assertEqual(run_calculator('24', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-29 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_30(self):
        self.assertEqual(run_calculator('24', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-30 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_31(self):
        self.assertEqual(run_calculator('24', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-31 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_32(self):
        self.assertEqual(run_calculator('24', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-32 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_33(self):
        self.assertEqual(run_calculator('24', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-33 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_34(self):
        self.assertEqual(run_calculator('24', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-34 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_35(self):
        self.assertEqual(run_calculator('24', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-35 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_36(self):
        self.assertEqual(run_calculator('24', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-36 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_37(self):
        self.assertEqual(run_calculator('24', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-37 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_38(self):
        self.assertEqual(run_calculator('24', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-38 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_39(self):
        self.assertEqual(run_calculator('24', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-39 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_40(self):
        self.assertEqual(run_calculator('24', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-40 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_41(self):
        self.assertEqual(run_calculator('24', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-41 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_42(self):
        self.assertEqual(run_calculator('24', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-42 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_43(self):
        self.assertEqual(run_calculator('24', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-43 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_44(self):
        self.assertEqual(run_calculator('24', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-44 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_45(self):
        self.assertEqual(run_calculator('24', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-45 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_46(self):
        self.assertEqual(run_calculator('24', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-46 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_47(self):
        self.assertEqual(run_calculator('24', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-47 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_48(self):
        self.assertEqual(run_calculator('24', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-48 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_49(self):
        self.assertEqual(run_calculator('24', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-49 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_minus_50(self):
        self.assertEqual(run_calculator('24', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24-50 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
