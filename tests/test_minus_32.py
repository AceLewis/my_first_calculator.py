# test_minus_32.py
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


class TestMinus32(unittest.TestCase):

    def test_32_minus_0(self):
        self.assertEqual(run_calculator('32', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-0 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_1(self):
        self.assertEqual(run_calculator('32', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-1 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_2(self):
        self.assertEqual(run_calculator('32', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-2 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_3(self):
        self.assertEqual(run_calculator('32', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-3 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_4(self):
        self.assertEqual(run_calculator('32', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-4 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_5(self):
        self.assertEqual(run_calculator('32', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-5 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_6(self):
        self.assertEqual(run_calculator('32', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-6 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_7(self):
        self.assertEqual(run_calculator('32', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-7 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_8(self):
        self.assertEqual(run_calculator('32', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-8 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_9(self):
        self.assertEqual(run_calculator('32', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-9 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_10(self):
        self.assertEqual(run_calculator('32', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-10 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_11(self):
        self.assertEqual(run_calculator('32', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-11 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_12(self):
        self.assertEqual(run_calculator('32', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-12 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_13(self):
        self.assertEqual(run_calculator('32', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-13 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_14(self):
        self.assertEqual(run_calculator('32', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-14 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_15(self):
        self.assertEqual(run_calculator('32', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-15 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_16(self):
        self.assertEqual(run_calculator('32', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-16 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_17(self):
        self.assertEqual(run_calculator('32', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-17 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_18(self):
        self.assertEqual(run_calculator('32', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-18 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_19(self):
        self.assertEqual(run_calculator('32', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-19 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_20(self):
        self.assertEqual(run_calculator('32', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-20 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_21(self):
        self.assertEqual(run_calculator('32', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-21 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_22(self):
        self.assertEqual(run_calculator('32', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-22 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_23(self):
        self.assertEqual(run_calculator('32', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-23 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_24(self):
        self.assertEqual(run_calculator('32', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-24 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_25(self):
        self.assertEqual(run_calculator('32', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-25 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_26(self):
        self.assertEqual(run_calculator('32', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-26 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_27(self):
        self.assertEqual(run_calculator('32', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-27 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_28(self):
        self.assertEqual(run_calculator('32', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-28 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_29(self):
        self.assertEqual(run_calculator('32', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-29 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_30(self):
        self.assertEqual(run_calculator('32', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-30 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_31(self):
        self.assertEqual(run_calculator('32', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-31 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_32(self):
        self.assertEqual(run_calculator('32', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-32 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_33(self):
        self.assertEqual(run_calculator('32', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-33 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_34(self):
        self.assertEqual(run_calculator('32', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-34 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_35(self):
        self.assertEqual(run_calculator('32', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-35 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_36(self):
        self.assertEqual(run_calculator('32', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-36 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_37(self):
        self.assertEqual(run_calculator('32', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-37 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_38(self):
        self.assertEqual(run_calculator('32', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-38 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_39(self):
        self.assertEqual(run_calculator('32', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-39 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_40(self):
        self.assertEqual(run_calculator('32', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-40 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_41(self):
        self.assertEqual(run_calculator('32', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-41 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_42(self):
        self.assertEqual(run_calculator('32', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-42 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_43(self):
        self.assertEqual(run_calculator('32', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-43 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_44(self):
        self.assertEqual(run_calculator('32', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-44 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_45(self):
        self.assertEqual(run_calculator('32', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-45 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_46(self):
        self.assertEqual(run_calculator('32', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-46 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_47(self):
        self.assertEqual(run_calculator('32', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-47 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_48(self):
        self.assertEqual(run_calculator('32', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-48 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_49(self):
        self.assertEqual(run_calculator('32', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-49 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_minus_50(self):
        self.assertEqual(run_calculator('32', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32-50 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
