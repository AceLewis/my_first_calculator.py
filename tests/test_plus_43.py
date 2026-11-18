# test_plus_43.py
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


class TestPlus43(unittest.TestCase):

    def test_43_plus_0(self):
        self.assertEqual(run_calculator('43', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+0 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_1(self):
        self.assertEqual(run_calculator('43', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+1 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_2(self):
        self.assertEqual(run_calculator('43', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+2 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_3(self):
        self.assertEqual(run_calculator('43', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+3 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_4(self):
        self.assertEqual(run_calculator('43', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+4 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_5(self):
        self.assertEqual(run_calculator('43', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+5 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_6(self):
        self.assertEqual(run_calculator('43', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+6 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_7(self):
        self.assertEqual(run_calculator('43', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+7 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_8(self):
        self.assertEqual(run_calculator('43', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+8 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_9(self):
        self.assertEqual(run_calculator('43', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+9 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_10(self):
        self.assertEqual(run_calculator('43', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+10 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_11(self):
        self.assertEqual(run_calculator('43', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+11 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_12(self):
        self.assertEqual(run_calculator('43', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+12 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_13(self):
        self.assertEqual(run_calculator('43', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+13 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_14(self):
        self.assertEqual(run_calculator('43', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+14 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_15(self):
        self.assertEqual(run_calculator('43', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+15 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_16(self):
        self.assertEqual(run_calculator('43', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+16 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_17(self):
        self.assertEqual(run_calculator('43', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+17 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_18(self):
        self.assertEqual(run_calculator('43', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+18 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_19(self):
        self.assertEqual(run_calculator('43', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+19 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_20(self):
        self.assertEqual(run_calculator('43', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+20 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_21(self):
        self.assertEqual(run_calculator('43', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+21 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_22(self):
        self.assertEqual(run_calculator('43', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+22 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_23(self):
        self.assertEqual(run_calculator('43', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+23 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_24(self):
        self.assertEqual(run_calculator('43', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+24 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_25(self):
        self.assertEqual(run_calculator('43', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+25 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_26(self):
        self.assertEqual(run_calculator('43', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+26 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_27(self):
        self.assertEqual(run_calculator('43', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+27 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_28(self):
        self.assertEqual(run_calculator('43', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+28 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_29(self):
        self.assertEqual(run_calculator('43', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+29 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_30(self):
        self.assertEqual(run_calculator('43', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+30 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_31(self):
        self.assertEqual(run_calculator('43', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+31 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_32(self):
        self.assertEqual(run_calculator('43', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+32 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_33(self):
        self.assertEqual(run_calculator('43', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+33 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_34(self):
        self.assertEqual(run_calculator('43', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+34 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_35(self):
        self.assertEqual(run_calculator('43', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+35 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_36(self):
        self.assertEqual(run_calculator('43', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+36 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_37(self):
        self.assertEqual(run_calculator('43', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+37 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_38(self):
        self.assertEqual(run_calculator('43', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+38 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_39(self):
        self.assertEqual(run_calculator('43', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+39 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_40(self):
        self.assertEqual(run_calculator('43', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+40 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_41(self):
        self.assertEqual(run_calculator('43', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+41 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_42(self):
        self.assertEqual(run_calculator('43', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+42 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_43(self):
        self.assertEqual(run_calculator('43', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+43 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_44(self):
        self.assertEqual(run_calculator('43', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+44 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_45(self):
        self.assertEqual(run_calculator('43', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+45 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_46(self):
        self.assertEqual(run_calculator('43', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+46 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_47(self):
        self.assertEqual(run_calculator('43', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+47 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_48(self):
        self.assertEqual(run_calculator('43', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+48 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_49(self):
        self.assertEqual(run_calculator('43', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+49 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_plus_50(self):
        self.assertEqual(run_calculator('43', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43+50 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
