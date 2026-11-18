# test_plus_45.py
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


class TestPlus45(unittest.TestCase):

    def test_45_plus_0(self):
        self.assertEqual(run_calculator('45', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+0 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_1(self):
        self.assertEqual(run_calculator('45', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+1 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_2(self):
        self.assertEqual(run_calculator('45', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+2 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_3(self):
        self.assertEqual(run_calculator('45', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+3 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_4(self):
        self.assertEqual(run_calculator('45', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+4 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_5(self):
        self.assertEqual(run_calculator('45', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+5 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_6(self):
        self.assertEqual(run_calculator('45', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+6 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_7(self):
        self.assertEqual(run_calculator('45', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+7 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_8(self):
        self.assertEqual(run_calculator('45', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+8 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_9(self):
        self.assertEqual(run_calculator('45', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+9 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_10(self):
        self.assertEqual(run_calculator('45', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+10 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_11(self):
        self.assertEqual(run_calculator('45', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+11 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_12(self):
        self.assertEqual(run_calculator('45', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+12 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_13(self):
        self.assertEqual(run_calculator('45', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+13 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_14(self):
        self.assertEqual(run_calculator('45', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+14 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_15(self):
        self.assertEqual(run_calculator('45', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+15 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_16(self):
        self.assertEqual(run_calculator('45', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+16 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_17(self):
        self.assertEqual(run_calculator('45', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+17 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_18(self):
        self.assertEqual(run_calculator('45', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+18 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_19(self):
        self.assertEqual(run_calculator('45', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+19 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_20(self):
        self.assertEqual(run_calculator('45', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+20 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_21(self):
        self.assertEqual(run_calculator('45', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+21 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_22(self):
        self.assertEqual(run_calculator('45', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+22 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_23(self):
        self.assertEqual(run_calculator('45', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+23 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_24(self):
        self.assertEqual(run_calculator('45', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+24 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_25(self):
        self.assertEqual(run_calculator('45', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+25 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_26(self):
        self.assertEqual(run_calculator('45', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+26 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_27(self):
        self.assertEqual(run_calculator('45', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+27 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_28(self):
        self.assertEqual(run_calculator('45', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+28 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_29(self):
        self.assertEqual(run_calculator('45', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+29 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_30(self):
        self.assertEqual(run_calculator('45', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+30 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_31(self):
        self.assertEqual(run_calculator('45', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+31 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_32(self):
        self.assertEqual(run_calculator('45', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+32 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_33(self):
        self.assertEqual(run_calculator('45', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+33 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_34(self):
        self.assertEqual(run_calculator('45', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+34 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_35(self):
        self.assertEqual(run_calculator('45', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+35 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_36(self):
        self.assertEqual(run_calculator('45', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+36 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_37(self):
        self.assertEqual(run_calculator('45', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+37 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_38(self):
        self.assertEqual(run_calculator('45', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+38 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_39(self):
        self.assertEqual(run_calculator('45', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+39 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_40(self):
        self.assertEqual(run_calculator('45', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+40 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_41(self):
        self.assertEqual(run_calculator('45', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+41 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_42(self):
        self.assertEqual(run_calculator('45', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+42 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_43(self):
        self.assertEqual(run_calculator('45', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+43 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_44(self):
        self.assertEqual(run_calculator('45', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+44 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_45(self):
        self.assertEqual(run_calculator('45', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+45 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_46(self):
        self.assertEqual(run_calculator('45', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+46 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_47(self):
        self.assertEqual(run_calculator('45', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+47 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_48(self):
        self.assertEqual(run_calculator('45', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+48 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_49(self):
        self.assertEqual(run_calculator('45', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+49 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_plus_50(self):
        self.assertEqual(run_calculator('45', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45+50 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
