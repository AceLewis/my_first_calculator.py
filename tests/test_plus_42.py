# test_plus_42.py
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


class TestPlus42(unittest.TestCase):

    def test_42_plus_0(self):
        self.assertEqual(run_calculator('42', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+0 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_1(self):
        self.assertEqual(run_calculator('42', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+1 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_2(self):
        self.assertEqual(run_calculator('42', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+2 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_3(self):
        self.assertEqual(run_calculator('42', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+3 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_4(self):
        self.assertEqual(run_calculator('42', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+4 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_5(self):
        self.assertEqual(run_calculator('42', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+5 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_6(self):
        self.assertEqual(run_calculator('42', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+6 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_7(self):
        self.assertEqual(run_calculator('42', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+7 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_8(self):
        self.assertEqual(run_calculator('42', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+8 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_9(self):
        self.assertEqual(run_calculator('42', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+9 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_10(self):
        self.assertEqual(run_calculator('42', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+10 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_11(self):
        self.assertEqual(run_calculator('42', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+11 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_12(self):
        self.assertEqual(run_calculator('42', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+12 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_13(self):
        self.assertEqual(run_calculator('42', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+13 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_14(self):
        self.assertEqual(run_calculator('42', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+14 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_15(self):
        self.assertEqual(run_calculator('42', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+15 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_16(self):
        self.assertEqual(run_calculator('42', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+16 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_17(self):
        self.assertEqual(run_calculator('42', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+17 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_18(self):
        self.assertEqual(run_calculator('42', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+18 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_19(self):
        self.assertEqual(run_calculator('42', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+19 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_20(self):
        self.assertEqual(run_calculator('42', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+20 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_21(self):
        self.assertEqual(run_calculator('42', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+21 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_22(self):
        self.assertEqual(run_calculator('42', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+22 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_23(self):
        self.assertEqual(run_calculator('42', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+23 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_24(self):
        self.assertEqual(run_calculator('42', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+24 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_25(self):
        self.assertEqual(run_calculator('42', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+25 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_26(self):
        self.assertEqual(run_calculator('42', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+26 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_27(self):
        self.assertEqual(run_calculator('42', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+27 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_28(self):
        self.assertEqual(run_calculator('42', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+28 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_29(self):
        self.assertEqual(run_calculator('42', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+29 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_30(self):
        self.assertEqual(run_calculator('42', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+30 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_31(self):
        self.assertEqual(run_calculator('42', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+31 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_32(self):
        self.assertEqual(run_calculator('42', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+32 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_33(self):
        self.assertEqual(run_calculator('42', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+33 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_34(self):
        self.assertEqual(run_calculator('42', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+34 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_35(self):
        self.assertEqual(run_calculator('42', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+35 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_36(self):
        self.assertEqual(run_calculator('42', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+36 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_37(self):
        self.assertEqual(run_calculator('42', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+37 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_38(self):
        self.assertEqual(run_calculator('42', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+38 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_39(self):
        self.assertEqual(run_calculator('42', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+39 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_40(self):
        self.assertEqual(run_calculator('42', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+40 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_41(self):
        self.assertEqual(run_calculator('42', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+41 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_42(self):
        self.assertEqual(run_calculator('42', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+42 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_43(self):
        self.assertEqual(run_calculator('42', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+43 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_44(self):
        self.assertEqual(run_calculator('42', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+44 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_45(self):
        self.assertEqual(run_calculator('42', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+45 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_46(self):
        self.assertEqual(run_calculator('42', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+46 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_47(self):
        self.assertEqual(run_calculator('42', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+47 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_48(self):
        self.assertEqual(run_calculator('42', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+48 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_49(self):
        self.assertEqual(run_calculator('42', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+49 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_plus_50(self):
        self.assertEqual(run_calculator('42', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42+50 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
