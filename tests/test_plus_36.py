# test_plus_36.py
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


class TestPlus36(unittest.TestCase):

    def test_36_plus_0(self):
        self.assertEqual(run_calculator('36', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+0 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_1(self):
        self.assertEqual(run_calculator('36', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+1 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_2(self):
        self.assertEqual(run_calculator('36', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+2 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_3(self):
        self.assertEqual(run_calculator('36', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+3 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_4(self):
        self.assertEqual(run_calculator('36', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+4 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_5(self):
        self.assertEqual(run_calculator('36', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+5 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_6(self):
        self.assertEqual(run_calculator('36', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+6 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_7(self):
        self.assertEqual(run_calculator('36', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+7 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_8(self):
        self.assertEqual(run_calculator('36', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+8 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_9(self):
        self.assertEqual(run_calculator('36', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+9 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_10(self):
        self.assertEqual(run_calculator('36', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+10 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_11(self):
        self.assertEqual(run_calculator('36', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+11 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_12(self):
        self.assertEqual(run_calculator('36', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+12 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_13(self):
        self.assertEqual(run_calculator('36', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+13 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_14(self):
        self.assertEqual(run_calculator('36', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+14 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_15(self):
        self.assertEqual(run_calculator('36', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+15 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_16(self):
        self.assertEqual(run_calculator('36', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+16 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_17(self):
        self.assertEqual(run_calculator('36', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+17 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_18(self):
        self.assertEqual(run_calculator('36', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+18 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_19(self):
        self.assertEqual(run_calculator('36', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+19 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_20(self):
        self.assertEqual(run_calculator('36', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+20 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_21(self):
        self.assertEqual(run_calculator('36', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+21 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_22(self):
        self.assertEqual(run_calculator('36', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+22 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_23(self):
        self.assertEqual(run_calculator('36', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+23 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_24(self):
        self.assertEqual(run_calculator('36', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+24 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_25(self):
        self.assertEqual(run_calculator('36', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+25 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_26(self):
        self.assertEqual(run_calculator('36', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+26 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_27(self):
        self.assertEqual(run_calculator('36', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+27 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_28(self):
        self.assertEqual(run_calculator('36', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+28 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_29(self):
        self.assertEqual(run_calculator('36', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+29 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_30(self):
        self.assertEqual(run_calculator('36', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+30 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_31(self):
        self.assertEqual(run_calculator('36', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+31 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_32(self):
        self.assertEqual(run_calculator('36', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+32 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_33(self):
        self.assertEqual(run_calculator('36', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+33 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_34(self):
        self.assertEqual(run_calculator('36', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+34 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_35(self):
        self.assertEqual(run_calculator('36', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+35 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_36(self):
        self.assertEqual(run_calculator('36', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+36 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_37(self):
        self.assertEqual(run_calculator('36', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+37 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_38(self):
        self.assertEqual(run_calculator('36', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+38 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_39(self):
        self.assertEqual(run_calculator('36', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+39 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_40(self):
        self.assertEqual(run_calculator('36', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+40 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_41(self):
        self.assertEqual(run_calculator('36', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+41 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_42(self):
        self.assertEqual(run_calculator('36', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+42 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_43(self):
        self.assertEqual(run_calculator('36', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+43 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_44(self):
        self.assertEqual(run_calculator('36', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+44 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_45(self):
        self.assertEqual(run_calculator('36', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+45 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_46(self):
        self.assertEqual(run_calculator('36', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+46 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_47(self):
        self.assertEqual(run_calculator('36', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+47 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_48(self):
        self.assertEqual(run_calculator('36', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+48 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_49(self):
        self.assertEqual(run_calculator('36', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+49 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_plus_50(self):
        self.assertEqual(run_calculator('36', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36+50 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
