# test_plus_40.py
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


class TestPlus40(unittest.TestCase):

    def test_40_plus_0(self):
        self.assertEqual(run_calculator('40', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+0 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_1(self):
        self.assertEqual(run_calculator('40', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+1 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_2(self):
        self.assertEqual(run_calculator('40', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+2 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_3(self):
        self.assertEqual(run_calculator('40', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+3 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_4(self):
        self.assertEqual(run_calculator('40', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+4 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_5(self):
        self.assertEqual(run_calculator('40', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+5 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_6(self):
        self.assertEqual(run_calculator('40', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+6 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_7(self):
        self.assertEqual(run_calculator('40', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+7 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_8(self):
        self.assertEqual(run_calculator('40', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+8 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_9(self):
        self.assertEqual(run_calculator('40', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+9 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_10(self):
        self.assertEqual(run_calculator('40', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+10 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_11(self):
        self.assertEqual(run_calculator('40', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+11 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_12(self):
        self.assertEqual(run_calculator('40', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+12 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_13(self):
        self.assertEqual(run_calculator('40', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+13 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_14(self):
        self.assertEqual(run_calculator('40', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+14 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_15(self):
        self.assertEqual(run_calculator('40', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+15 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_16(self):
        self.assertEqual(run_calculator('40', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+16 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_17(self):
        self.assertEqual(run_calculator('40', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+17 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_18(self):
        self.assertEqual(run_calculator('40', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+18 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_19(self):
        self.assertEqual(run_calculator('40', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+19 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_20(self):
        self.assertEqual(run_calculator('40', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+20 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_21(self):
        self.assertEqual(run_calculator('40', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+21 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_22(self):
        self.assertEqual(run_calculator('40', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+22 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_23(self):
        self.assertEqual(run_calculator('40', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+23 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_24(self):
        self.assertEqual(run_calculator('40', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+24 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_25(self):
        self.assertEqual(run_calculator('40', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+25 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_26(self):
        self.assertEqual(run_calculator('40', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+26 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_27(self):
        self.assertEqual(run_calculator('40', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+27 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_28(self):
        self.assertEqual(run_calculator('40', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+28 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_29(self):
        self.assertEqual(run_calculator('40', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+29 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_30(self):
        self.assertEqual(run_calculator('40', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+30 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_31(self):
        self.assertEqual(run_calculator('40', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+31 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_32(self):
        self.assertEqual(run_calculator('40', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+32 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_33(self):
        self.assertEqual(run_calculator('40', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+33 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_34(self):
        self.assertEqual(run_calculator('40', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+34 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_35(self):
        self.assertEqual(run_calculator('40', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+35 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_36(self):
        self.assertEqual(run_calculator('40', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+36 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_37(self):
        self.assertEqual(run_calculator('40', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+37 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_38(self):
        self.assertEqual(run_calculator('40', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+38 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_39(self):
        self.assertEqual(run_calculator('40', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+39 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_40(self):
        self.assertEqual(run_calculator('40', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+40 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_41(self):
        self.assertEqual(run_calculator('40', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+41 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_42(self):
        self.assertEqual(run_calculator('40', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+42 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_43(self):
        self.assertEqual(run_calculator('40', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+43 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_44(self):
        self.assertEqual(run_calculator('40', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+44 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_45(self):
        self.assertEqual(run_calculator('40', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+45 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_46(self):
        self.assertEqual(run_calculator('40', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+46 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_47(self):
        self.assertEqual(run_calculator('40', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+47 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_48(self):
        self.assertEqual(run_calculator('40', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+48 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_49(self):
        self.assertEqual(run_calculator('40', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+49 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_plus_50(self):
        self.assertEqual(run_calculator('40', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40+50 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
