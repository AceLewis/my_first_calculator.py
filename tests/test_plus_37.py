# test_plus_37.py
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


class TestPlus37(unittest.TestCase):

    def test_37_plus_0(self):
        self.assertEqual(run_calculator('37', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+0 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_1(self):
        self.assertEqual(run_calculator('37', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+1 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_2(self):
        self.assertEqual(run_calculator('37', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+2 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_3(self):
        self.assertEqual(run_calculator('37', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+3 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_4(self):
        self.assertEqual(run_calculator('37', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+4 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_5(self):
        self.assertEqual(run_calculator('37', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+5 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_6(self):
        self.assertEqual(run_calculator('37', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+6 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_7(self):
        self.assertEqual(run_calculator('37', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+7 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_8(self):
        self.assertEqual(run_calculator('37', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+8 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_9(self):
        self.assertEqual(run_calculator('37', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+9 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_10(self):
        self.assertEqual(run_calculator('37', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+10 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_11(self):
        self.assertEqual(run_calculator('37', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+11 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_12(self):
        self.assertEqual(run_calculator('37', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+12 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_13(self):
        self.assertEqual(run_calculator('37', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+13 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_14(self):
        self.assertEqual(run_calculator('37', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+14 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_15(self):
        self.assertEqual(run_calculator('37', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+15 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_16(self):
        self.assertEqual(run_calculator('37', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+16 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_17(self):
        self.assertEqual(run_calculator('37', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+17 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_18(self):
        self.assertEqual(run_calculator('37', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+18 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_19(self):
        self.assertEqual(run_calculator('37', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+19 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_20(self):
        self.assertEqual(run_calculator('37', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+20 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_21(self):
        self.assertEqual(run_calculator('37', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+21 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_22(self):
        self.assertEqual(run_calculator('37', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+22 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_23(self):
        self.assertEqual(run_calculator('37', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+23 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_24(self):
        self.assertEqual(run_calculator('37', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+24 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_25(self):
        self.assertEqual(run_calculator('37', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+25 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_26(self):
        self.assertEqual(run_calculator('37', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+26 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_27(self):
        self.assertEqual(run_calculator('37', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+27 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_28(self):
        self.assertEqual(run_calculator('37', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+28 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_29(self):
        self.assertEqual(run_calculator('37', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+29 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_30(self):
        self.assertEqual(run_calculator('37', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+30 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_31(self):
        self.assertEqual(run_calculator('37', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+31 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_32(self):
        self.assertEqual(run_calculator('37', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+32 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_33(self):
        self.assertEqual(run_calculator('37', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+33 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_34(self):
        self.assertEqual(run_calculator('37', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+34 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_35(self):
        self.assertEqual(run_calculator('37', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+35 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_36(self):
        self.assertEqual(run_calculator('37', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+36 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_37(self):
        self.assertEqual(run_calculator('37', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+37 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_38(self):
        self.assertEqual(run_calculator('37', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+38 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_39(self):
        self.assertEqual(run_calculator('37', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+39 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_40(self):
        self.assertEqual(run_calculator('37', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+40 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_41(self):
        self.assertEqual(run_calculator('37', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+41 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_42(self):
        self.assertEqual(run_calculator('37', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+42 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_43(self):
        self.assertEqual(run_calculator('37', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+43 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_44(self):
        self.assertEqual(run_calculator('37', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+44 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_45(self):
        self.assertEqual(run_calculator('37', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+45 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_46(self):
        self.assertEqual(run_calculator('37', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+46 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_47(self):
        self.assertEqual(run_calculator('37', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+47 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_48(self):
        self.assertEqual(run_calculator('37', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+48 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_49(self):
        self.assertEqual(run_calculator('37', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+49 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_plus_50(self):
        self.assertEqual(run_calculator('37', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37+50 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
