# test_plus_38.py
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


class TestPlus38(unittest.TestCase):

    def test_38_plus_0(self):
        self.assertEqual(run_calculator('38', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+0 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_1(self):
        self.assertEqual(run_calculator('38', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+1 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_2(self):
        self.assertEqual(run_calculator('38', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+2 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_3(self):
        self.assertEqual(run_calculator('38', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+3 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_4(self):
        self.assertEqual(run_calculator('38', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+4 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_5(self):
        self.assertEqual(run_calculator('38', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+5 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_6(self):
        self.assertEqual(run_calculator('38', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+6 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_7(self):
        self.assertEqual(run_calculator('38', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+7 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_8(self):
        self.assertEqual(run_calculator('38', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+8 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_9(self):
        self.assertEqual(run_calculator('38', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+9 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_10(self):
        self.assertEqual(run_calculator('38', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+10 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_11(self):
        self.assertEqual(run_calculator('38', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+11 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_12(self):
        self.assertEqual(run_calculator('38', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+12 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_13(self):
        self.assertEqual(run_calculator('38', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+13 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_14(self):
        self.assertEqual(run_calculator('38', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+14 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_15(self):
        self.assertEqual(run_calculator('38', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+15 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_16(self):
        self.assertEqual(run_calculator('38', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+16 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_17(self):
        self.assertEqual(run_calculator('38', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+17 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_18(self):
        self.assertEqual(run_calculator('38', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+18 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_19(self):
        self.assertEqual(run_calculator('38', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+19 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_20(self):
        self.assertEqual(run_calculator('38', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+20 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_21(self):
        self.assertEqual(run_calculator('38', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+21 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_22(self):
        self.assertEqual(run_calculator('38', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+22 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_23(self):
        self.assertEqual(run_calculator('38', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+23 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_24(self):
        self.assertEqual(run_calculator('38', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+24 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_25(self):
        self.assertEqual(run_calculator('38', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+25 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_26(self):
        self.assertEqual(run_calculator('38', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+26 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_27(self):
        self.assertEqual(run_calculator('38', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+27 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_28(self):
        self.assertEqual(run_calculator('38', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+28 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_29(self):
        self.assertEqual(run_calculator('38', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+29 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_30(self):
        self.assertEqual(run_calculator('38', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+30 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_31(self):
        self.assertEqual(run_calculator('38', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+31 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_32(self):
        self.assertEqual(run_calculator('38', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+32 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_33(self):
        self.assertEqual(run_calculator('38', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+33 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_34(self):
        self.assertEqual(run_calculator('38', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+34 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_35(self):
        self.assertEqual(run_calculator('38', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+35 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_36(self):
        self.assertEqual(run_calculator('38', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+36 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_37(self):
        self.assertEqual(run_calculator('38', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+37 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_38(self):
        self.assertEqual(run_calculator('38', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+38 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_39(self):
        self.assertEqual(run_calculator('38', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+39 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_40(self):
        self.assertEqual(run_calculator('38', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+40 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_41(self):
        self.assertEqual(run_calculator('38', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+41 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_42(self):
        self.assertEqual(run_calculator('38', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+42 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_43(self):
        self.assertEqual(run_calculator('38', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+43 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_44(self):
        self.assertEqual(run_calculator('38', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+44 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_45(self):
        self.assertEqual(run_calculator('38', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+45 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_46(self):
        self.assertEqual(run_calculator('38', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+46 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_47(self):
        self.assertEqual(run_calculator('38', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+47 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_48(self):
        self.assertEqual(run_calculator('38', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+48 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_49(self):
        self.assertEqual(run_calculator('38', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+49 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_plus_50(self):
        self.assertEqual(run_calculator('38', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38+50 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
