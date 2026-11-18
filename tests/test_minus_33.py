# test_minus_33.py
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


class TestMinus33(unittest.TestCase):

    def test_33_minus_0(self):
        self.assertEqual(run_calculator('33', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-0 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_1(self):
        self.assertEqual(run_calculator('33', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-1 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_2(self):
        self.assertEqual(run_calculator('33', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-2 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_3(self):
        self.assertEqual(run_calculator('33', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-3 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_4(self):
        self.assertEqual(run_calculator('33', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-4 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_5(self):
        self.assertEqual(run_calculator('33', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-5 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_6(self):
        self.assertEqual(run_calculator('33', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-6 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_7(self):
        self.assertEqual(run_calculator('33', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-7 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_8(self):
        self.assertEqual(run_calculator('33', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-8 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_9(self):
        self.assertEqual(run_calculator('33', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-9 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_10(self):
        self.assertEqual(run_calculator('33', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-10 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_11(self):
        self.assertEqual(run_calculator('33', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-11 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_12(self):
        self.assertEqual(run_calculator('33', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-12 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_13(self):
        self.assertEqual(run_calculator('33', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-13 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_14(self):
        self.assertEqual(run_calculator('33', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-14 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_15(self):
        self.assertEqual(run_calculator('33', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-15 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_16(self):
        self.assertEqual(run_calculator('33', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-16 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_17(self):
        self.assertEqual(run_calculator('33', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-17 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_18(self):
        self.assertEqual(run_calculator('33', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-18 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_19(self):
        self.assertEqual(run_calculator('33', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-19 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_20(self):
        self.assertEqual(run_calculator('33', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-20 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_21(self):
        self.assertEqual(run_calculator('33', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-21 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_22(self):
        self.assertEqual(run_calculator('33', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-22 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_23(self):
        self.assertEqual(run_calculator('33', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-23 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_24(self):
        self.assertEqual(run_calculator('33', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-24 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_25(self):
        self.assertEqual(run_calculator('33', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-25 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_26(self):
        self.assertEqual(run_calculator('33', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-26 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_27(self):
        self.assertEqual(run_calculator('33', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-27 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_28(self):
        self.assertEqual(run_calculator('33', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-28 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_29(self):
        self.assertEqual(run_calculator('33', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-29 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_30(self):
        self.assertEqual(run_calculator('33', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-30 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_31(self):
        self.assertEqual(run_calculator('33', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-31 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_32(self):
        self.assertEqual(run_calculator('33', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-32 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_33(self):
        self.assertEqual(run_calculator('33', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-33 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_34(self):
        self.assertEqual(run_calculator('33', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-34 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_35(self):
        self.assertEqual(run_calculator('33', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-35 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_36(self):
        self.assertEqual(run_calculator('33', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-36 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_37(self):
        self.assertEqual(run_calculator('33', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-37 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_38(self):
        self.assertEqual(run_calculator('33', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-38 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_39(self):
        self.assertEqual(run_calculator('33', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-39 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_40(self):
        self.assertEqual(run_calculator('33', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-40 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_41(self):
        self.assertEqual(run_calculator('33', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-41 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_42(self):
        self.assertEqual(run_calculator('33', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-42 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_43(self):
        self.assertEqual(run_calculator('33', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-43 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_44(self):
        self.assertEqual(run_calculator('33', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-44 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_45(self):
        self.assertEqual(run_calculator('33', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-45 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_46(self):
        self.assertEqual(run_calculator('33', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-46 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_47(self):
        self.assertEqual(run_calculator('33', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-47 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_48(self):
        self.assertEqual(run_calculator('33', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-48 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_49(self):
        self.assertEqual(run_calculator('33', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-49 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_minus_50(self):
        self.assertEqual(run_calculator('33', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33-50 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
