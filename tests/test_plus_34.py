# test_plus_34.py
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


class TestPlus34(unittest.TestCase):

    def test_34_plus_0(self):
        self.assertEqual(run_calculator('34', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+0 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_1(self):
        self.assertEqual(run_calculator('34', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+1 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_2(self):
        self.assertEqual(run_calculator('34', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+2 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_3(self):
        self.assertEqual(run_calculator('34', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+3 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_4(self):
        self.assertEqual(run_calculator('34', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+4 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_5(self):
        self.assertEqual(run_calculator('34', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+5 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_6(self):
        self.assertEqual(run_calculator('34', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+6 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_7(self):
        self.assertEqual(run_calculator('34', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+7 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_8(self):
        self.assertEqual(run_calculator('34', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+8 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_9(self):
        self.assertEqual(run_calculator('34', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+9 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_10(self):
        self.assertEqual(run_calculator('34', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+10 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_11(self):
        self.assertEqual(run_calculator('34', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+11 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_12(self):
        self.assertEqual(run_calculator('34', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+12 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_13(self):
        self.assertEqual(run_calculator('34', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+13 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_14(self):
        self.assertEqual(run_calculator('34', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+14 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_15(self):
        self.assertEqual(run_calculator('34', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+15 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_16(self):
        self.assertEqual(run_calculator('34', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+16 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_17(self):
        self.assertEqual(run_calculator('34', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+17 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_18(self):
        self.assertEqual(run_calculator('34', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+18 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_19(self):
        self.assertEqual(run_calculator('34', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+19 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_20(self):
        self.assertEqual(run_calculator('34', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+20 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_21(self):
        self.assertEqual(run_calculator('34', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+21 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_22(self):
        self.assertEqual(run_calculator('34', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+22 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_23(self):
        self.assertEqual(run_calculator('34', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+23 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_24(self):
        self.assertEqual(run_calculator('34', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+24 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_25(self):
        self.assertEqual(run_calculator('34', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+25 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_26(self):
        self.assertEqual(run_calculator('34', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+26 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_27(self):
        self.assertEqual(run_calculator('34', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+27 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_28(self):
        self.assertEqual(run_calculator('34', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+28 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_29(self):
        self.assertEqual(run_calculator('34', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+29 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_30(self):
        self.assertEqual(run_calculator('34', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+30 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_31(self):
        self.assertEqual(run_calculator('34', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+31 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_32(self):
        self.assertEqual(run_calculator('34', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+32 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_33(self):
        self.assertEqual(run_calculator('34', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+33 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_34(self):
        self.assertEqual(run_calculator('34', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+34 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_35(self):
        self.assertEqual(run_calculator('34', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+35 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_36(self):
        self.assertEqual(run_calculator('34', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+36 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_37(self):
        self.assertEqual(run_calculator('34', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+37 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_38(self):
        self.assertEqual(run_calculator('34', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+38 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_39(self):
        self.assertEqual(run_calculator('34', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+39 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_40(self):
        self.assertEqual(run_calculator('34', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+40 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_41(self):
        self.assertEqual(run_calculator('34', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+41 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_42(self):
        self.assertEqual(run_calculator('34', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+42 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_43(self):
        self.assertEqual(run_calculator('34', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+43 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_44(self):
        self.assertEqual(run_calculator('34', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+44 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_45(self):
        self.assertEqual(run_calculator('34', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+45 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_46(self):
        self.assertEqual(run_calculator('34', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+46 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_47(self):
        self.assertEqual(run_calculator('34', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+47 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_48(self):
        self.assertEqual(run_calculator('34', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+48 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_49(self):
        self.assertEqual(run_calculator('34', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+49 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_plus_50(self):
        self.assertEqual(run_calculator('34', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34+50 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
