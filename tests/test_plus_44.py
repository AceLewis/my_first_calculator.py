# test_plus_44.py
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


class TestPlus44(unittest.TestCase):

    def test_44_plus_0(self):
        self.assertEqual(run_calculator('44', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+0 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_1(self):
        self.assertEqual(run_calculator('44', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+1 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_2(self):
        self.assertEqual(run_calculator('44', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+2 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_3(self):
        self.assertEqual(run_calculator('44', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+3 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_4(self):
        self.assertEqual(run_calculator('44', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+4 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_5(self):
        self.assertEqual(run_calculator('44', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+5 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_6(self):
        self.assertEqual(run_calculator('44', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+6 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_7(self):
        self.assertEqual(run_calculator('44', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+7 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_8(self):
        self.assertEqual(run_calculator('44', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+8 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_9(self):
        self.assertEqual(run_calculator('44', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+9 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_10(self):
        self.assertEqual(run_calculator('44', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+10 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_11(self):
        self.assertEqual(run_calculator('44', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+11 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_12(self):
        self.assertEqual(run_calculator('44', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+12 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_13(self):
        self.assertEqual(run_calculator('44', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+13 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_14(self):
        self.assertEqual(run_calculator('44', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+14 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_15(self):
        self.assertEqual(run_calculator('44', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+15 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_16(self):
        self.assertEqual(run_calculator('44', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+16 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_17(self):
        self.assertEqual(run_calculator('44', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+17 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_18(self):
        self.assertEqual(run_calculator('44', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+18 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_19(self):
        self.assertEqual(run_calculator('44', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+19 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_20(self):
        self.assertEqual(run_calculator('44', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+20 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_21(self):
        self.assertEqual(run_calculator('44', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+21 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_22(self):
        self.assertEqual(run_calculator('44', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+22 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_23(self):
        self.assertEqual(run_calculator('44', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+23 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_24(self):
        self.assertEqual(run_calculator('44', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+24 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_25(self):
        self.assertEqual(run_calculator('44', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+25 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_26(self):
        self.assertEqual(run_calculator('44', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+26 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_27(self):
        self.assertEqual(run_calculator('44', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+27 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_28(self):
        self.assertEqual(run_calculator('44', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+28 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_29(self):
        self.assertEqual(run_calculator('44', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+29 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_30(self):
        self.assertEqual(run_calculator('44', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+30 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_31(self):
        self.assertEqual(run_calculator('44', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+31 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_32(self):
        self.assertEqual(run_calculator('44', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+32 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_33(self):
        self.assertEqual(run_calculator('44', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+33 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_34(self):
        self.assertEqual(run_calculator('44', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+34 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_35(self):
        self.assertEqual(run_calculator('44', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+35 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_36(self):
        self.assertEqual(run_calculator('44', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+36 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_37(self):
        self.assertEqual(run_calculator('44', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+37 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_38(self):
        self.assertEqual(run_calculator('44', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+38 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_39(self):
        self.assertEqual(run_calculator('44', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+39 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_40(self):
        self.assertEqual(run_calculator('44', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+40 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_41(self):
        self.assertEqual(run_calculator('44', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+41 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_42(self):
        self.assertEqual(run_calculator('44', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+42 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_43(self):
        self.assertEqual(run_calculator('44', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+43 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_44(self):
        self.assertEqual(run_calculator('44', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+44 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_45(self):
        self.assertEqual(run_calculator('44', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+45 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_46(self):
        self.assertEqual(run_calculator('44', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+46 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_47(self):
        self.assertEqual(run_calculator('44', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+47 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_48(self):
        self.assertEqual(run_calculator('44', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+48 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_49(self):
        self.assertEqual(run_calculator('44', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+49 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_plus_50(self):
        self.assertEqual(run_calculator('44', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44+50 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
