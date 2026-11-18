# test_minus_39.py
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


class TestMinus39(unittest.TestCase):

    def test_39_minus_0(self):
        self.assertEqual(run_calculator('39', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-0 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_1(self):
        self.assertEqual(run_calculator('39', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-1 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_2(self):
        self.assertEqual(run_calculator('39', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-2 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_3(self):
        self.assertEqual(run_calculator('39', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-3 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_4(self):
        self.assertEqual(run_calculator('39', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-4 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_5(self):
        self.assertEqual(run_calculator('39', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-5 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_6(self):
        self.assertEqual(run_calculator('39', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-6 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_7(self):
        self.assertEqual(run_calculator('39', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-7 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_8(self):
        self.assertEqual(run_calculator('39', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-8 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_9(self):
        self.assertEqual(run_calculator('39', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-9 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_10(self):
        self.assertEqual(run_calculator('39', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-10 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_11(self):
        self.assertEqual(run_calculator('39', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-11 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_12(self):
        self.assertEqual(run_calculator('39', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-12 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_13(self):
        self.assertEqual(run_calculator('39', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-13 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_14(self):
        self.assertEqual(run_calculator('39', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-14 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_15(self):
        self.assertEqual(run_calculator('39', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-15 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_16(self):
        self.assertEqual(run_calculator('39', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-16 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_17(self):
        self.assertEqual(run_calculator('39', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-17 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_18(self):
        self.assertEqual(run_calculator('39', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-18 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_19(self):
        self.assertEqual(run_calculator('39', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-19 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_20(self):
        self.assertEqual(run_calculator('39', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-20 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_21(self):
        self.assertEqual(run_calculator('39', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-21 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_22(self):
        self.assertEqual(run_calculator('39', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-22 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_23(self):
        self.assertEqual(run_calculator('39', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-23 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_24(self):
        self.assertEqual(run_calculator('39', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-24 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_25(self):
        self.assertEqual(run_calculator('39', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-25 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_26(self):
        self.assertEqual(run_calculator('39', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-26 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_27(self):
        self.assertEqual(run_calculator('39', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-27 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_28(self):
        self.assertEqual(run_calculator('39', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-28 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_29(self):
        self.assertEqual(run_calculator('39', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-29 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_30(self):
        self.assertEqual(run_calculator('39', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-30 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_31(self):
        self.assertEqual(run_calculator('39', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-31 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_32(self):
        self.assertEqual(run_calculator('39', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-32 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_33(self):
        self.assertEqual(run_calculator('39', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-33 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_34(self):
        self.assertEqual(run_calculator('39', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-34 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_35(self):
        self.assertEqual(run_calculator('39', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-35 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_36(self):
        self.assertEqual(run_calculator('39', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-36 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_37(self):
        self.assertEqual(run_calculator('39', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-37 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_38(self):
        self.assertEqual(run_calculator('39', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-38 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_39(self):
        self.assertEqual(run_calculator('39', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-39 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_40(self):
        self.assertEqual(run_calculator('39', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-40 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_41(self):
        self.assertEqual(run_calculator('39', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-41 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_42(self):
        self.assertEqual(run_calculator('39', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-42 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_43(self):
        self.assertEqual(run_calculator('39', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-43 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_44(self):
        self.assertEqual(run_calculator('39', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-44 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_45(self):
        self.assertEqual(run_calculator('39', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-45 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_46(self):
        self.assertEqual(run_calculator('39', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-46 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_47(self):
        self.assertEqual(run_calculator('39', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-47 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_48(self):
        self.assertEqual(run_calculator('39', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-48 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_49(self):
        self.assertEqual(run_calculator('39', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-49 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_minus_50(self):
        self.assertEqual(run_calculator('39', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39-50 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
