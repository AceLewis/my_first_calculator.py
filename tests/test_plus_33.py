# test_plus_33.py
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


class TestPlus33(unittest.TestCase):

    def test_33_plus_0(self):
        self.assertEqual(run_calculator('33', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+0 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_1(self):
        self.assertEqual(run_calculator('33', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+1 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_2(self):
        self.assertEqual(run_calculator('33', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+2 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_3(self):
        self.assertEqual(run_calculator('33', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+3 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_4(self):
        self.assertEqual(run_calculator('33', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+4 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_5(self):
        self.assertEqual(run_calculator('33', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+5 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_6(self):
        self.assertEqual(run_calculator('33', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+6 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_7(self):
        self.assertEqual(run_calculator('33', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+7 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_8(self):
        self.assertEqual(run_calculator('33', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+8 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_9(self):
        self.assertEqual(run_calculator('33', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+9 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_10(self):
        self.assertEqual(run_calculator('33', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+10 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_11(self):
        self.assertEqual(run_calculator('33', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+11 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_12(self):
        self.assertEqual(run_calculator('33', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+12 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_13(self):
        self.assertEqual(run_calculator('33', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+13 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_14(self):
        self.assertEqual(run_calculator('33', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+14 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_15(self):
        self.assertEqual(run_calculator('33', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+15 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_16(self):
        self.assertEqual(run_calculator('33', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+16 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_17(self):
        self.assertEqual(run_calculator('33', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+17 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_18(self):
        self.assertEqual(run_calculator('33', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+18 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_19(self):
        self.assertEqual(run_calculator('33', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+19 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_20(self):
        self.assertEqual(run_calculator('33', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+20 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_21(self):
        self.assertEqual(run_calculator('33', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+21 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_22(self):
        self.assertEqual(run_calculator('33', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+22 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_23(self):
        self.assertEqual(run_calculator('33', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+23 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_24(self):
        self.assertEqual(run_calculator('33', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+24 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_25(self):
        self.assertEqual(run_calculator('33', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+25 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_26(self):
        self.assertEqual(run_calculator('33', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+26 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_27(self):
        self.assertEqual(run_calculator('33', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+27 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_28(self):
        self.assertEqual(run_calculator('33', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+28 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_29(self):
        self.assertEqual(run_calculator('33', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+29 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_30(self):
        self.assertEqual(run_calculator('33', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+30 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_31(self):
        self.assertEqual(run_calculator('33', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+31 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_32(self):
        self.assertEqual(run_calculator('33', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+32 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_33(self):
        self.assertEqual(run_calculator('33', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+33 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_34(self):
        self.assertEqual(run_calculator('33', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+34 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_35(self):
        self.assertEqual(run_calculator('33', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+35 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_36(self):
        self.assertEqual(run_calculator('33', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+36 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_37(self):
        self.assertEqual(run_calculator('33', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+37 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_38(self):
        self.assertEqual(run_calculator('33', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+38 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_39(self):
        self.assertEqual(run_calculator('33', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+39 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_40(self):
        self.assertEqual(run_calculator('33', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+40 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_41(self):
        self.assertEqual(run_calculator('33', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+41 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_42(self):
        self.assertEqual(run_calculator('33', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+42 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_43(self):
        self.assertEqual(run_calculator('33', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+43 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_44(self):
        self.assertEqual(run_calculator('33', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+44 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_45(self):
        self.assertEqual(run_calculator('33', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+45 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_46(self):
        self.assertEqual(run_calculator('33', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+46 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_47(self):
        self.assertEqual(run_calculator('33', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+47 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_48(self):
        self.assertEqual(run_calculator('33', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+48 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_49(self):
        self.assertEqual(run_calculator('33', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+49 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_plus_50(self):
        self.assertEqual(run_calculator('33', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33+50 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
