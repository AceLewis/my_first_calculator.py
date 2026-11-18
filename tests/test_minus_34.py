# test_minus_34.py
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


class TestMinus34(unittest.TestCase):

    def test_34_minus_0(self):
        self.assertEqual(run_calculator('34', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-0 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_1(self):
        self.assertEqual(run_calculator('34', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-1 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_2(self):
        self.assertEqual(run_calculator('34', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-2 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_3(self):
        self.assertEqual(run_calculator('34', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-3 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_4(self):
        self.assertEqual(run_calculator('34', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-4 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_5(self):
        self.assertEqual(run_calculator('34', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-5 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_6(self):
        self.assertEqual(run_calculator('34', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-6 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_7(self):
        self.assertEqual(run_calculator('34', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-7 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_8(self):
        self.assertEqual(run_calculator('34', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-8 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_9(self):
        self.assertEqual(run_calculator('34', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-9 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_10(self):
        self.assertEqual(run_calculator('34', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-10 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_11(self):
        self.assertEqual(run_calculator('34', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-11 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_12(self):
        self.assertEqual(run_calculator('34', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-12 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_13(self):
        self.assertEqual(run_calculator('34', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-13 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_14(self):
        self.assertEqual(run_calculator('34', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-14 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_15(self):
        self.assertEqual(run_calculator('34', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-15 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_16(self):
        self.assertEqual(run_calculator('34', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-16 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_17(self):
        self.assertEqual(run_calculator('34', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-17 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_18(self):
        self.assertEqual(run_calculator('34', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-18 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_19(self):
        self.assertEqual(run_calculator('34', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-19 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_20(self):
        self.assertEqual(run_calculator('34', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-20 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_21(self):
        self.assertEqual(run_calculator('34', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-21 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_22(self):
        self.assertEqual(run_calculator('34', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-22 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_23(self):
        self.assertEqual(run_calculator('34', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-23 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_24(self):
        self.assertEqual(run_calculator('34', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-24 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_25(self):
        self.assertEqual(run_calculator('34', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-25 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_26(self):
        self.assertEqual(run_calculator('34', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-26 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_27(self):
        self.assertEqual(run_calculator('34', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-27 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_28(self):
        self.assertEqual(run_calculator('34', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-28 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_29(self):
        self.assertEqual(run_calculator('34', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-29 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_30(self):
        self.assertEqual(run_calculator('34', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-30 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_31(self):
        self.assertEqual(run_calculator('34', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-31 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_32(self):
        self.assertEqual(run_calculator('34', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-32 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_33(self):
        self.assertEqual(run_calculator('34', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-33 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_34(self):
        self.assertEqual(run_calculator('34', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-34 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_35(self):
        self.assertEqual(run_calculator('34', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-35 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_36(self):
        self.assertEqual(run_calculator('34', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-36 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_37(self):
        self.assertEqual(run_calculator('34', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-37 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_38(self):
        self.assertEqual(run_calculator('34', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-38 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_39(self):
        self.assertEqual(run_calculator('34', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-39 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_40(self):
        self.assertEqual(run_calculator('34', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-40 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_41(self):
        self.assertEqual(run_calculator('34', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-41 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_42(self):
        self.assertEqual(run_calculator('34', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-42 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_43(self):
        self.assertEqual(run_calculator('34', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-43 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_44(self):
        self.assertEqual(run_calculator('34', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-44 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_45(self):
        self.assertEqual(run_calculator('34', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-45 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_46(self):
        self.assertEqual(run_calculator('34', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-46 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_47(self):
        self.assertEqual(run_calculator('34', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-47 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_48(self):
        self.assertEqual(run_calculator('34', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-48 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_49(self):
        self.assertEqual(run_calculator('34', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-49 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_minus_50(self):
        self.assertEqual(run_calculator('34', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34-50 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
