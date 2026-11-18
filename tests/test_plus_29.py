# test_plus_29.py
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


class TestPlus29(unittest.TestCase):

    def test_29_plus_0(self):
        self.assertEqual(run_calculator('29', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+0 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_1(self):
        self.assertEqual(run_calculator('29', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+1 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_2(self):
        self.assertEqual(run_calculator('29', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+2 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_3(self):
        self.assertEqual(run_calculator('29', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+3 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_4(self):
        self.assertEqual(run_calculator('29', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+4 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_5(self):
        self.assertEqual(run_calculator('29', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+5 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_6(self):
        self.assertEqual(run_calculator('29', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+6 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_7(self):
        self.assertEqual(run_calculator('29', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+7 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_8(self):
        self.assertEqual(run_calculator('29', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+8 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_9(self):
        self.assertEqual(run_calculator('29', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+9 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_10(self):
        self.assertEqual(run_calculator('29', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+10 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_11(self):
        self.assertEqual(run_calculator('29', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+11 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_12(self):
        self.assertEqual(run_calculator('29', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+12 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_13(self):
        self.assertEqual(run_calculator('29', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+13 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_14(self):
        self.assertEqual(run_calculator('29', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+14 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_15(self):
        self.assertEqual(run_calculator('29', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+15 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_16(self):
        self.assertEqual(run_calculator('29', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+16 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_17(self):
        self.assertEqual(run_calculator('29', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+17 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_18(self):
        self.assertEqual(run_calculator('29', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+18 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_19(self):
        self.assertEqual(run_calculator('29', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+19 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_20(self):
        self.assertEqual(run_calculator('29', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+20 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_21(self):
        self.assertEqual(run_calculator('29', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+21 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_22(self):
        self.assertEqual(run_calculator('29', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+22 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_23(self):
        self.assertEqual(run_calculator('29', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+23 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_24(self):
        self.assertEqual(run_calculator('29', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+24 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_25(self):
        self.assertEqual(run_calculator('29', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+25 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_26(self):
        self.assertEqual(run_calculator('29', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+26 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_27(self):
        self.assertEqual(run_calculator('29', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+27 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_28(self):
        self.assertEqual(run_calculator('29', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+28 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_29(self):
        self.assertEqual(run_calculator('29', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+29 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_30(self):
        self.assertEqual(run_calculator('29', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+30 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_31(self):
        self.assertEqual(run_calculator('29', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+31 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_32(self):
        self.assertEqual(run_calculator('29', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+32 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_33(self):
        self.assertEqual(run_calculator('29', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+33 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_34(self):
        self.assertEqual(run_calculator('29', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+34 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_35(self):
        self.assertEqual(run_calculator('29', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+35 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_36(self):
        self.assertEqual(run_calculator('29', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+36 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_37(self):
        self.assertEqual(run_calculator('29', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+37 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_38(self):
        self.assertEqual(run_calculator('29', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+38 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_39(self):
        self.assertEqual(run_calculator('29', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+39 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_40(self):
        self.assertEqual(run_calculator('29', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+40 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_41(self):
        self.assertEqual(run_calculator('29', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+41 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_42(self):
        self.assertEqual(run_calculator('29', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+42 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_43(self):
        self.assertEqual(run_calculator('29', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+43 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_44(self):
        self.assertEqual(run_calculator('29', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+44 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_45(self):
        self.assertEqual(run_calculator('29', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+45 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_46(self):
        self.assertEqual(run_calculator('29', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+46 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_47(self):
        self.assertEqual(run_calculator('29', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+47 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_48(self):
        self.assertEqual(run_calculator('29', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+48 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_49(self):
        self.assertEqual(run_calculator('29', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+49 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_plus_50(self):
        self.assertEqual(run_calculator('29', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29+50 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
