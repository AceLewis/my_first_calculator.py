# test_plus_48.py
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


class TestPlus48(unittest.TestCase):

    def test_48_plus_0(self):
        self.assertEqual(run_calculator('48', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+0 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_1(self):
        self.assertEqual(run_calculator('48', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+1 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_2(self):
        self.assertEqual(run_calculator('48', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+2 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_3(self):
        self.assertEqual(run_calculator('48', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+3 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_4(self):
        self.assertEqual(run_calculator('48', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+4 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_5(self):
        self.assertEqual(run_calculator('48', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+5 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_6(self):
        self.assertEqual(run_calculator('48', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+6 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_7(self):
        self.assertEqual(run_calculator('48', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+7 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_8(self):
        self.assertEqual(run_calculator('48', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+8 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_9(self):
        self.assertEqual(run_calculator('48', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+9 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_10(self):
        self.assertEqual(run_calculator('48', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+10 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_11(self):
        self.assertEqual(run_calculator('48', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+11 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_12(self):
        self.assertEqual(run_calculator('48', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+12 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_13(self):
        self.assertEqual(run_calculator('48', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+13 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_14(self):
        self.assertEqual(run_calculator('48', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+14 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_15(self):
        self.assertEqual(run_calculator('48', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+15 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_16(self):
        self.assertEqual(run_calculator('48', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+16 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_17(self):
        self.assertEqual(run_calculator('48', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+17 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_18(self):
        self.assertEqual(run_calculator('48', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+18 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_19(self):
        self.assertEqual(run_calculator('48', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+19 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_20(self):
        self.assertEqual(run_calculator('48', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+20 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_21(self):
        self.assertEqual(run_calculator('48', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+21 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_22(self):
        self.assertEqual(run_calculator('48', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+22 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_23(self):
        self.assertEqual(run_calculator('48', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+23 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_24(self):
        self.assertEqual(run_calculator('48', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+24 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_25(self):
        self.assertEqual(run_calculator('48', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+25 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_26(self):
        self.assertEqual(run_calculator('48', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+26 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_27(self):
        self.assertEqual(run_calculator('48', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+27 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_28(self):
        self.assertEqual(run_calculator('48', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+28 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_29(self):
        self.assertEqual(run_calculator('48', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+29 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_30(self):
        self.assertEqual(run_calculator('48', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+30 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_31(self):
        self.assertEqual(run_calculator('48', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+31 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_32(self):
        self.assertEqual(run_calculator('48', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+32 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_33(self):
        self.assertEqual(run_calculator('48', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+33 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_34(self):
        self.assertEqual(run_calculator('48', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+34 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_35(self):
        self.assertEqual(run_calculator('48', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+35 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_36(self):
        self.assertEqual(run_calculator('48', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+36 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_37(self):
        self.assertEqual(run_calculator('48', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+37 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_38(self):
        self.assertEqual(run_calculator('48', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+38 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_39(self):
        self.assertEqual(run_calculator('48', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+39 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_40(self):
        self.assertEqual(run_calculator('48', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+40 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_41(self):
        self.assertEqual(run_calculator('48', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+41 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_42(self):
        self.assertEqual(run_calculator('48', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+42 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_43(self):
        self.assertEqual(run_calculator('48', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+43 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_44(self):
        self.assertEqual(run_calculator('48', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+44 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_45(self):
        self.assertEqual(run_calculator('48', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+45 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_46(self):
        self.assertEqual(run_calculator('48', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+46 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_47(self):
        self.assertEqual(run_calculator('48', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+47 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_48(self):
        self.assertEqual(run_calculator('48', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+48 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_49(self):
        self.assertEqual(run_calculator('48', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+49 = 97',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_plus_50(self):
        self.assertEqual(run_calculator('48', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48+50 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
