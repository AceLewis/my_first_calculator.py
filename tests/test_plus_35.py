# test_plus_35.py
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


class TestPlus35(unittest.TestCase):

    def test_35_plus_0(self):
        self.assertEqual(run_calculator('35', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+0 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_1(self):
        self.assertEqual(run_calculator('35', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+1 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_2(self):
        self.assertEqual(run_calculator('35', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+2 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_3(self):
        self.assertEqual(run_calculator('35', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+3 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_4(self):
        self.assertEqual(run_calculator('35', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+4 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_5(self):
        self.assertEqual(run_calculator('35', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+5 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_6(self):
        self.assertEqual(run_calculator('35', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+6 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_7(self):
        self.assertEqual(run_calculator('35', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+7 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_8(self):
        self.assertEqual(run_calculator('35', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+8 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_9(self):
        self.assertEqual(run_calculator('35', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+9 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_10(self):
        self.assertEqual(run_calculator('35', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+10 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_11(self):
        self.assertEqual(run_calculator('35', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+11 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_12(self):
        self.assertEqual(run_calculator('35', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+12 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_13(self):
        self.assertEqual(run_calculator('35', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+13 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_14(self):
        self.assertEqual(run_calculator('35', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+14 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_15(self):
        self.assertEqual(run_calculator('35', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+15 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_16(self):
        self.assertEqual(run_calculator('35', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+16 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_17(self):
        self.assertEqual(run_calculator('35', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+17 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_18(self):
        self.assertEqual(run_calculator('35', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+18 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_19(self):
        self.assertEqual(run_calculator('35', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+19 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_20(self):
        self.assertEqual(run_calculator('35', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+20 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_21(self):
        self.assertEqual(run_calculator('35', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+21 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_22(self):
        self.assertEqual(run_calculator('35', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+22 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_23(self):
        self.assertEqual(run_calculator('35', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+23 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_24(self):
        self.assertEqual(run_calculator('35', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+24 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_25(self):
        self.assertEqual(run_calculator('35', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+25 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_26(self):
        self.assertEqual(run_calculator('35', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+26 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_27(self):
        self.assertEqual(run_calculator('35', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+27 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_28(self):
        self.assertEqual(run_calculator('35', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+28 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_29(self):
        self.assertEqual(run_calculator('35', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+29 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_30(self):
        self.assertEqual(run_calculator('35', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+30 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_31(self):
        self.assertEqual(run_calculator('35', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+31 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_32(self):
        self.assertEqual(run_calculator('35', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+32 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_33(self):
        self.assertEqual(run_calculator('35', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+33 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_34(self):
        self.assertEqual(run_calculator('35', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+34 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_35(self):
        self.assertEqual(run_calculator('35', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+35 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_36(self):
        self.assertEqual(run_calculator('35', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+36 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_37(self):
        self.assertEqual(run_calculator('35', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+37 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_38(self):
        self.assertEqual(run_calculator('35', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+38 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_39(self):
        self.assertEqual(run_calculator('35', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+39 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_40(self):
        self.assertEqual(run_calculator('35', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+40 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_41(self):
        self.assertEqual(run_calculator('35', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+41 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_42(self):
        self.assertEqual(run_calculator('35', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+42 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_43(self):
        self.assertEqual(run_calculator('35', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+43 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_44(self):
        self.assertEqual(run_calculator('35', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+44 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_45(self):
        self.assertEqual(run_calculator('35', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+45 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_46(self):
        self.assertEqual(run_calculator('35', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+46 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_47(self):
        self.assertEqual(run_calculator('35', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+47 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_48(self):
        self.assertEqual(run_calculator('35', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+48 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_49(self):
        self.assertEqual(run_calculator('35', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+49 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_plus_50(self):
        self.assertEqual(run_calculator('35', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35+50 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
