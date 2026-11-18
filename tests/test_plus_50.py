# test_plus_50.py
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


class TestPlus50(unittest.TestCase):

    def test_50_plus_0(self):
        self.assertEqual(run_calculator('50', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+0 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_1(self):
        self.assertEqual(run_calculator('50', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+1 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_2(self):
        self.assertEqual(run_calculator('50', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+2 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_3(self):
        self.assertEqual(run_calculator('50', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+3 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_4(self):
        self.assertEqual(run_calculator('50', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+4 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_5(self):
        self.assertEqual(run_calculator('50', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+5 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_6(self):
        self.assertEqual(run_calculator('50', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+6 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_7(self):
        self.assertEqual(run_calculator('50', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+7 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_8(self):
        self.assertEqual(run_calculator('50', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+8 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_9(self):
        self.assertEqual(run_calculator('50', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+9 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_10(self):
        self.assertEqual(run_calculator('50', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+10 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_11(self):
        self.assertEqual(run_calculator('50', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+11 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_12(self):
        self.assertEqual(run_calculator('50', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+12 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_13(self):
        self.assertEqual(run_calculator('50', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+13 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_14(self):
        self.assertEqual(run_calculator('50', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+14 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_15(self):
        self.assertEqual(run_calculator('50', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+15 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_16(self):
        self.assertEqual(run_calculator('50', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+16 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_17(self):
        self.assertEqual(run_calculator('50', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+17 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_18(self):
        self.assertEqual(run_calculator('50', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+18 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_19(self):
        self.assertEqual(run_calculator('50', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+19 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_20(self):
        self.assertEqual(run_calculator('50', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+20 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_21(self):
        self.assertEqual(run_calculator('50', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+21 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_22(self):
        self.assertEqual(run_calculator('50', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+22 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_23(self):
        self.assertEqual(run_calculator('50', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+23 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_24(self):
        self.assertEqual(run_calculator('50', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+24 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_25(self):
        self.assertEqual(run_calculator('50', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+25 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_26(self):
        self.assertEqual(run_calculator('50', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+26 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_27(self):
        self.assertEqual(run_calculator('50', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+27 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_28(self):
        self.assertEqual(run_calculator('50', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+28 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_29(self):
        self.assertEqual(run_calculator('50', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+29 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_30(self):
        self.assertEqual(run_calculator('50', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+30 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_31(self):
        self.assertEqual(run_calculator('50', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+31 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_32(self):
        self.assertEqual(run_calculator('50', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+32 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_33(self):
        self.assertEqual(run_calculator('50', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+33 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_34(self):
        self.assertEqual(run_calculator('50', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+34 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_35(self):
        self.assertEqual(run_calculator('50', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+35 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_36(self):
        self.assertEqual(run_calculator('50', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+36 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_37(self):
        self.assertEqual(run_calculator('50', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+37 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_38(self):
        self.assertEqual(run_calculator('50', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+38 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_39(self):
        self.assertEqual(run_calculator('50', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+39 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_40(self):
        self.assertEqual(run_calculator('50', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+40 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_41(self):
        self.assertEqual(run_calculator('50', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+41 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_42(self):
        self.assertEqual(run_calculator('50', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+42 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_43(self):
        self.assertEqual(run_calculator('50', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+43 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_44(self):
        self.assertEqual(run_calculator('50', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+44 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_45(self):
        self.assertEqual(run_calculator('50', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+45 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_46(self):
        self.assertEqual(run_calculator('50', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+46 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_47(self):
        self.assertEqual(run_calculator('50', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+47 = 97',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_48(self):
        self.assertEqual(run_calculator('50', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+48 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_49(self):
        self.assertEqual(run_calculator('50', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+49 = 99',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_plus_50(self):
        self.assertEqual(run_calculator('50', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50+50 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
