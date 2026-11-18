# test_plus_30.py
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


class TestPlus30(unittest.TestCase):

    def test_30_plus_0(self):
        self.assertEqual(run_calculator('30', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+0 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_1(self):
        self.assertEqual(run_calculator('30', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+1 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_2(self):
        self.assertEqual(run_calculator('30', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+2 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_3(self):
        self.assertEqual(run_calculator('30', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+3 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_4(self):
        self.assertEqual(run_calculator('30', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+4 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_5(self):
        self.assertEqual(run_calculator('30', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+5 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_6(self):
        self.assertEqual(run_calculator('30', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+6 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_7(self):
        self.assertEqual(run_calculator('30', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+7 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_8(self):
        self.assertEqual(run_calculator('30', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+8 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_9(self):
        self.assertEqual(run_calculator('30', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+9 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_10(self):
        self.assertEqual(run_calculator('30', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+10 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_11(self):
        self.assertEqual(run_calculator('30', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+11 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_12(self):
        self.assertEqual(run_calculator('30', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+12 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_13(self):
        self.assertEqual(run_calculator('30', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+13 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_14(self):
        self.assertEqual(run_calculator('30', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+14 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_15(self):
        self.assertEqual(run_calculator('30', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+15 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_16(self):
        self.assertEqual(run_calculator('30', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+16 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_17(self):
        self.assertEqual(run_calculator('30', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+17 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_18(self):
        self.assertEqual(run_calculator('30', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+18 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_19(self):
        self.assertEqual(run_calculator('30', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+19 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_20(self):
        self.assertEqual(run_calculator('30', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+20 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_21(self):
        self.assertEqual(run_calculator('30', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+21 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_22(self):
        self.assertEqual(run_calculator('30', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+22 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_23(self):
        self.assertEqual(run_calculator('30', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+23 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_24(self):
        self.assertEqual(run_calculator('30', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+24 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_25(self):
        self.assertEqual(run_calculator('30', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+25 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_26(self):
        self.assertEqual(run_calculator('30', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+26 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_27(self):
        self.assertEqual(run_calculator('30', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+27 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_28(self):
        self.assertEqual(run_calculator('30', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+28 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_29(self):
        self.assertEqual(run_calculator('30', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+29 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_30(self):
        self.assertEqual(run_calculator('30', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+30 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_31(self):
        self.assertEqual(run_calculator('30', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+31 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_32(self):
        self.assertEqual(run_calculator('30', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+32 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_33(self):
        self.assertEqual(run_calculator('30', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+33 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_34(self):
        self.assertEqual(run_calculator('30', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+34 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_35(self):
        self.assertEqual(run_calculator('30', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+35 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_36(self):
        self.assertEqual(run_calculator('30', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+36 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_37(self):
        self.assertEqual(run_calculator('30', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+37 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_38(self):
        self.assertEqual(run_calculator('30', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+38 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_39(self):
        self.assertEqual(run_calculator('30', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+39 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_40(self):
        self.assertEqual(run_calculator('30', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+40 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_41(self):
        self.assertEqual(run_calculator('30', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+41 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_42(self):
        self.assertEqual(run_calculator('30', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+42 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_43(self):
        self.assertEqual(run_calculator('30', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+43 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_44(self):
        self.assertEqual(run_calculator('30', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+44 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_45(self):
        self.assertEqual(run_calculator('30', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+45 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_46(self):
        self.assertEqual(run_calculator('30', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+46 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_47(self):
        self.assertEqual(run_calculator('30', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+47 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_48(self):
        self.assertEqual(run_calculator('30', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+48 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_49(self):
        self.assertEqual(run_calculator('30', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+49 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_plus_50(self):
        self.assertEqual(run_calculator('30', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30+50 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
