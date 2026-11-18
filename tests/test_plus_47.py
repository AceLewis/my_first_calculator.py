# test_plus_47.py
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


class TestPlus47(unittest.TestCase):

    def test_47_plus_0(self):
        self.assertEqual(run_calculator('47', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+0 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_1(self):
        self.assertEqual(run_calculator('47', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+1 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_2(self):
        self.assertEqual(run_calculator('47', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+2 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_3(self):
        self.assertEqual(run_calculator('47', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+3 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_4(self):
        self.assertEqual(run_calculator('47', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+4 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_5(self):
        self.assertEqual(run_calculator('47', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+5 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_6(self):
        self.assertEqual(run_calculator('47', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+6 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_7(self):
        self.assertEqual(run_calculator('47', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+7 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_8(self):
        self.assertEqual(run_calculator('47', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+8 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_9(self):
        self.assertEqual(run_calculator('47', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+9 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_10(self):
        self.assertEqual(run_calculator('47', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+10 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_11(self):
        self.assertEqual(run_calculator('47', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+11 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_12(self):
        self.assertEqual(run_calculator('47', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+12 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_13(self):
        self.assertEqual(run_calculator('47', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+13 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_14(self):
        self.assertEqual(run_calculator('47', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+14 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_15(self):
        self.assertEqual(run_calculator('47', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+15 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_16(self):
        self.assertEqual(run_calculator('47', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+16 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_17(self):
        self.assertEqual(run_calculator('47', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+17 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_18(self):
        self.assertEqual(run_calculator('47', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+18 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_19(self):
        self.assertEqual(run_calculator('47', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+19 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_20(self):
        self.assertEqual(run_calculator('47', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+20 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_21(self):
        self.assertEqual(run_calculator('47', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+21 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_22(self):
        self.assertEqual(run_calculator('47', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+22 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_23(self):
        self.assertEqual(run_calculator('47', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+23 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_24(self):
        self.assertEqual(run_calculator('47', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+24 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_25(self):
        self.assertEqual(run_calculator('47', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+25 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_26(self):
        self.assertEqual(run_calculator('47', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+26 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_27(self):
        self.assertEqual(run_calculator('47', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+27 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_28(self):
        self.assertEqual(run_calculator('47', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+28 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_29(self):
        self.assertEqual(run_calculator('47', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+29 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_30(self):
        self.assertEqual(run_calculator('47', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+30 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_31(self):
        self.assertEqual(run_calculator('47', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+31 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_32(self):
        self.assertEqual(run_calculator('47', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+32 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_33(self):
        self.assertEqual(run_calculator('47', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+33 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_34(self):
        self.assertEqual(run_calculator('47', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+34 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_35(self):
        self.assertEqual(run_calculator('47', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+35 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_36(self):
        self.assertEqual(run_calculator('47', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+36 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_37(self):
        self.assertEqual(run_calculator('47', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+37 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_38(self):
        self.assertEqual(run_calculator('47', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+38 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_39(self):
        self.assertEqual(run_calculator('47', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+39 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_40(self):
        self.assertEqual(run_calculator('47', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+40 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_41(self):
        self.assertEqual(run_calculator('47', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+41 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_42(self):
        self.assertEqual(run_calculator('47', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+42 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_43(self):
        self.assertEqual(run_calculator('47', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+43 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_44(self):
        self.assertEqual(run_calculator('47', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+44 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_45(self):
        self.assertEqual(run_calculator('47', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+45 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_46(self):
        self.assertEqual(run_calculator('47', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+46 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_47(self):
        self.assertEqual(run_calculator('47', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+47 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_48(self):
        self.assertEqual(run_calculator('47', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+48 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_49(self):
        self.assertEqual(run_calculator('47', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+49 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_plus_50(self):
        self.assertEqual(run_calculator('47', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47+50 = 97',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
