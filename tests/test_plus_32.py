# test_plus_32.py
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


class TestPlus32(unittest.TestCase):

    def test_32_plus_0(self):
        self.assertEqual(run_calculator('32', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+0 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_1(self):
        self.assertEqual(run_calculator('32', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+1 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_2(self):
        self.assertEqual(run_calculator('32', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+2 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_3(self):
        self.assertEqual(run_calculator('32', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+3 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_4(self):
        self.assertEqual(run_calculator('32', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+4 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_5(self):
        self.assertEqual(run_calculator('32', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+5 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_6(self):
        self.assertEqual(run_calculator('32', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+6 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_7(self):
        self.assertEqual(run_calculator('32', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+7 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_8(self):
        self.assertEqual(run_calculator('32', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+8 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_9(self):
        self.assertEqual(run_calculator('32', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+9 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_10(self):
        self.assertEqual(run_calculator('32', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+10 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_11(self):
        self.assertEqual(run_calculator('32', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+11 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_12(self):
        self.assertEqual(run_calculator('32', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+12 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_13(self):
        self.assertEqual(run_calculator('32', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+13 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_14(self):
        self.assertEqual(run_calculator('32', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+14 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_15(self):
        self.assertEqual(run_calculator('32', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+15 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_16(self):
        self.assertEqual(run_calculator('32', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+16 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_17(self):
        self.assertEqual(run_calculator('32', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+17 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_18(self):
        self.assertEqual(run_calculator('32', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+18 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_19(self):
        self.assertEqual(run_calculator('32', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+19 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_20(self):
        self.assertEqual(run_calculator('32', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+20 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_21(self):
        self.assertEqual(run_calculator('32', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+21 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_22(self):
        self.assertEqual(run_calculator('32', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+22 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_23(self):
        self.assertEqual(run_calculator('32', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+23 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_24(self):
        self.assertEqual(run_calculator('32', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+24 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_25(self):
        self.assertEqual(run_calculator('32', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+25 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_26(self):
        self.assertEqual(run_calculator('32', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+26 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_27(self):
        self.assertEqual(run_calculator('32', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+27 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_28(self):
        self.assertEqual(run_calculator('32', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+28 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_29(self):
        self.assertEqual(run_calculator('32', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+29 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_30(self):
        self.assertEqual(run_calculator('32', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+30 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_31(self):
        self.assertEqual(run_calculator('32', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+31 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_32(self):
        self.assertEqual(run_calculator('32', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+32 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_33(self):
        self.assertEqual(run_calculator('32', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+33 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_34(self):
        self.assertEqual(run_calculator('32', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+34 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_35(self):
        self.assertEqual(run_calculator('32', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+35 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_36(self):
        self.assertEqual(run_calculator('32', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+36 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_37(self):
        self.assertEqual(run_calculator('32', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+37 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_38(self):
        self.assertEqual(run_calculator('32', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+38 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_39(self):
        self.assertEqual(run_calculator('32', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+39 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_40(self):
        self.assertEqual(run_calculator('32', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+40 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_41(self):
        self.assertEqual(run_calculator('32', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+41 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_42(self):
        self.assertEqual(run_calculator('32', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+42 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_43(self):
        self.assertEqual(run_calculator('32', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+43 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_44(self):
        self.assertEqual(run_calculator('32', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+44 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_45(self):
        self.assertEqual(run_calculator('32', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+45 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_46(self):
        self.assertEqual(run_calculator('32', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+46 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_47(self):
        self.assertEqual(run_calculator('32', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+47 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_48(self):
        self.assertEqual(run_calculator('32', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+48 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_49(self):
        self.assertEqual(run_calculator('32', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+49 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_plus_50(self):
        self.assertEqual(run_calculator('32', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32+50 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
