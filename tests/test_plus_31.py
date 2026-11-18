# test_plus_31.py
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


class TestPlus31(unittest.TestCase):

    def test_31_plus_0(self):
        self.assertEqual(run_calculator('31', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+0 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_1(self):
        self.assertEqual(run_calculator('31', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+1 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_2(self):
        self.assertEqual(run_calculator('31', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+2 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_3(self):
        self.assertEqual(run_calculator('31', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+3 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_4(self):
        self.assertEqual(run_calculator('31', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+4 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_5(self):
        self.assertEqual(run_calculator('31', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+5 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_6(self):
        self.assertEqual(run_calculator('31', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+6 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_7(self):
        self.assertEqual(run_calculator('31', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+7 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_8(self):
        self.assertEqual(run_calculator('31', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+8 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_9(self):
        self.assertEqual(run_calculator('31', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+9 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_10(self):
        self.assertEqual(run_calculator('31', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+10 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_11(self):
        self.assertEqual(run_calculator('31', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+11 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_12(self):
        self.assertEqual(run_calculator('31', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+12 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_13(self):
        self.assertEqual(run_calculator('31', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+13 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_14(self):
        self.assertEqual(run_calculator('31', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+14 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_15(self):
        self.assertEqual(run_calculator('31', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+15 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_16(self):
        self.assertEqual(run_calculator('31', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+16 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_17(self):
        self.assertEqual(run_calculator('31', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+17 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_18(self):
        self.assertEqual(run_calculator('31', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+18 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_19(self):
        self.assertEqual(run_calculator('31', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+19 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_20(self):
        self.assertEqual(run_calculator('31', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+20 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_21(self):
        self.assertEqual(run_calculator('31', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+21 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_22(self):
        self.assertEqual(run_calculator('31', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+22 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_23(self):
        self.assertEqual(run_calculator('31', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+23 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_24(self):
        self.assertEqual(run_calculator('31', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+24 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_25(self):
        self.assertEqual(run_calculator('31', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+25 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_26(self):
        self.assertEqual(run_calculator('31', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+26 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_27(self):
        self.assertEqual(run_calculator('31', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+27 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_28(self):
        self.assertEqual(run_calculator('31', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+28 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_29(self):
        self.assertEqual(run_calculator('31', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+29 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_30(self):
        self.assertEqual(run_calculator('31', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+30 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_31(self):
        self.assertEqual(run_calculator('31', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+31 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_32(self):
        self.assertEqual(run_calculator('31', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+32 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_33(self):
        self.assertEqual(run_calculator('31', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+33 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_34(self):
        self.assertEqual(run_calculator('31', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+34 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_35(self):
        self.assertEqual(run_calculator('31', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+35 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_36(self):
        self.assertEqual(run_calculator('31', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+36 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_37(self):
        self.assertEqual(run_calculator('31', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+37 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_38(self):
        self.assertEqual(run_calculator('31', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+38 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_39(self):
        self.assertEqual(run_calculator('31', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+39 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_40(self):
        self.assertEqual(run_calculator('31', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+40 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_41(self):
        self.assertEqual(run_calculator('31', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+41 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_42(self):
        self.assertEqual(run_calculator('31', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+42 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_43(self):
        self.assertEqual(run_calculator('31', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+43 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_44(self):
        self.assertEqual(run_calculator('31', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+44 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_45(self):
        self.assertEqual(run_calculator('31', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+45 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_46(self):
        self.assertEqual(run_calculator('31', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+46 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_47(self):
        self.assertEqual(run_calculator('31', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+47 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_48(self):
        self.assertEqual(run_calculator('31', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+48 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_49(self):
        self.assertEqual(run_calculator('31', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+49 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_plus_50(self):
        self.assertEqual(run_calculator('31', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31+50 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
