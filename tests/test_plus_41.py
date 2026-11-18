# test_plus_41.py
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


class TestPlus41(unittest.TestCase):

    def test_41_plus_0(self):
        self.assertEqual(run_calculator('41', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+0 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_1(self):
        self.assertEqual(run_calculator('41', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+1 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_2(self):
        self.assertEqual(run_calculator('41', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+2 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_3(self):
        self.assertEqual(run_calculator('41', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+3 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_4(self):
        self.assertEqual(run_calculator('41', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+4 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_5(self):
        self.assertEqual(run_calculator('41', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+5 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_6(self):
        self.assertEqual(run_calculator('41', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+6 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_7(self):
        self.assertEqual(run_calculator('41', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+7 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_8(self):
        self.assertEqual(run_calculator('41', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+8 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_9(self):
        self.assertEqual(run_calculator('41', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+9 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_10(self):
        self.assertEqual(run_calculator('41', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+10 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_11(self):
        self.assertEqual(run_calculator('41', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+11 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_12(self):
        self.assertEqual(run_calculator('41', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+12 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_13(self):
        self.assertEqual(run_calculator('41', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+13 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_14(self):
        self.assertEqual(run_calculator('41', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+14 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_15(self):
        self.assertEqual(run_calculator('41', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+15 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_16(self):
        self.assertEqual(run_calculator('41', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+16 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_17(self):
        self.assertEqual(run_calculator('41', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+17 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_18(self):
        self.assertEqual(run_calculator('41', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+18 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_19(self):
        self.assertEqual(run_calculator('41', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+19 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_20(self):
        self.assertEqual(run_calculator('41', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+20 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_21(self):
        self.assertEqual(run_calculator('41', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+21 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_22(self):
        self.assertEqual(run_calculator('41', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+22 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_23(self):
        self.assertEqual(run_calculator('41', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+23 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_24(self):
        self.assertEqual(run_calculator('41', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+24 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_25(self):
        self.assertEqual(run_calculator('41', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+25 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_26(self):
        self.assertEqual(run_calculator('41', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+26 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_27(self):
        self.assertEqual(run_calculator('41', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+27 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_28(self):
        self.assertEqual(run_calculator('41', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+28 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_29(self):
        self.assertEqual(run_calculator('41', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+29 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_30(self):
        self.assertEqual(run_calculator('41', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+30 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_31(self):
        self.assertEqual(run_calculator('41', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+31 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_32(self):
        self.assertEqual(run_calculator('41', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+32 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_33(self):
        self.assertEqual(run_calculator('41', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+33 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_34(self):
        self.assertEqual(run_calculator('41', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+34 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_35(self):
        self.assertEqual(run_calculator('41', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+35 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_36(self):
        self.assertEqual(run_calculator('41', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+36 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_37(self):
        self.assertEqual(run_calculator('41', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+37 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_38(self):
        self.assertEqual(run_calculator('41', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+38 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_39(self):
        self.assertEqual(run_calculator('41', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+39 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_40(self):
        self.assertEqual(run_calculator('41', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+40 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_41(self):
        self.assertEqual(run_calculator('41', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+41 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_42(self):
        self.assertEqual(run_calculator('41', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+42 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_43(self):
        self.assertEqual(run_calculator('41', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+43 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_44(self):
        self.assertEqual(run_calculator('41', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+44 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_45(self):
        self.assertEqual(run_calculator('41', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+45 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_46(self):
        self.assertEqual(run_calculator('41', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+46 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_47(self):
        self.assertEqual(run_calculator('41', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+47 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_48(self):
        self.assertEqual(run_calculator('41', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+48 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_49(self):
        self.assertEqual(run_calculator('41', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+49 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_plus_50(self):
        self.assertEqual(run_calculator('41', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41+50 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
