# test_minus_37.py
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


class TestMinus37(unittest.TestCase):

    def test_37_minus_0(self):
        self.assertEqual(run_calculator('37', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-0 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_1(self):
        self.assertEqual(run_calculator('37', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-1 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_2(self):
        self.assertEqual(run_calculator('37', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-2 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_3(self):
        self.assertEqual(run_calculator('37', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-3 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_4(self):
        self.assertEqual(run_calculator('37', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-4 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_5(self):
        self.assertEqual(run_calculator('37', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-5 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_6(self):
        self.assertEqual(run_calculator('37', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-6 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_7(self):
        self.assertEqual(run_calculator('37', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-7 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_8(self):
        self.assertEqual(run_calculator('37', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-8 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_9(self):
        self.assertEqual(run_calculator('37', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-9 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_10(self):
        self.assertEqual(run_calculator('37', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-10 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_11(self):
        self.assertEqual(run_calculator('37', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-11 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_12(self):
        self.assertEqual(run_calculator('37', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-12 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_13(self):
        self.assertEqual(run_calculator('37', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-13 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_14(self):
        self.assertEqual(run_calculator('37', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-14 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_15(self):
        self.assertEqual(run_calculator('37', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-15 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_16(self):
        self.assertEqual(run_calculator('37', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-16 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_17(self):
        self.assertEqual(run_calculator('37', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-17 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_18(self):
        self.assertEqual(run_calculator('37', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-18 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_19(self):
        self.assertEqual(run_calculator('37', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-19 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_20(self):
        self.assertEqual(run_calculator('37', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-20 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_21(self):
        self.assertEqual(run_calculator('37', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-21 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_22(self):
        self.assertEqual(run_calculator('37', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-22 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_23(self):
        self.assertEqual(run_calculator('37', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-23 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_24(self):
        self.assertEqual(run_calculator('37', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-24 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_25(self):
        self.assertEqual(run_calculator('37', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-25 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_26(self):
        self.assertEqual(run_calculator('37', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-26 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_27(self):
        self.assertEqual(run_calculator('37', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-27 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_28(self):
        self.assertEqual(run_calculator('37', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-28 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_29(self):
        self.assertEqual(run_calculator('37', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-29 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_30(self):
        self.assertEqual(run_calculator('37', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-30 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_31(self):
        self.assertEqual(run_calculator('37', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-31 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_32(self):
        self.assertEqual(run_calculator('37', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-32 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_33(self):
        self.assertEqual(run_calculator('37', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-33 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_34(self):
        self.assertEqual(run_calculator('37', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-34 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_35(self):
        self.assertEqual(run_calculator('37', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-35 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_36(self):
        self.assertEqual(run_calculator('37', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-36 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_37(self):
        self.assertEqual(run_calculator('37', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-37 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_38(self):
        self.assertEqual(run_calculator('37', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-38 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_39(self):
        self.assertEqual(run_calculator('37', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-39 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_40(self):
        self.assertEqual(run_calculator('37', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-40 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_41(self):
        self.assertEqual(run_calculator('37', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-41 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_42(self):
        self.assertEqual(run_calculator('37', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-42 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_43(self):
        self.assertEqual(run_calculator('37', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-43 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_44(self):
        self.assertEqual(run_calculator('37', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-44 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_45(self):
        self.assertEqual(run_calculator('37', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-45 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_46(self):
        self.assertEqual(run_calculator('37', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-46 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_47(self):
        self.assertEqual(run_calculator('37', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-47 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_48(self):
        self.assertEqual(run_calculator('37', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-48 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_49(self):
        self.assertEqual(run_calculator('37', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-49 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_minus_50(self):
        self.assertEqual(run_calculator('37', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37-50 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
