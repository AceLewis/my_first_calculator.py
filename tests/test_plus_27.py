# test_plus_27.py
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


class TestPlus27(unittest.TestCase):

    def test_27_plus_0(self):
        self.assertEqual(run_calculator('27', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+0 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_1(self):
        self.assertEqual(run_calculator('27', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+1 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_2(self):
        self.assertEqual(run_calculator('27', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+2 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_3(self):
        self.assertEqual(run_calculator('27', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+3 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_4(self):
        self.assertEqual(run_calculator('27', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+4 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_5(self):
        self.assertEqual(run_calculator('27', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+5 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_6(self):
        self.assertEqual(run_calculator('27', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+6 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_7(self):
        self.assertEqual(run_calculator('27', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+7 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_8(self):
        self.assertEqual(run_calculator('27', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+8 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_9(self):
        self.assertEqual(run_calculator('27', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+9 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_10(self):
        self.assertEqual(run_calculator('27', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+10 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_11(self):
        self.assertEqual(run_calculator('27', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+11 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_12(self):
        self.assertEqual(run_calculator('27', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+12 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_13(self):
        self.assertEqual(run_calculator('27', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+13 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_14(self):
        self.assertEqual(run_calculator('27', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+14 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_15(self):
        self.assertEqual(run_calculator('27', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+15 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_16(self):
        self.assertEqual(run_calculator('27', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+16 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_17(self):
        self.assertEqual(run_calculator('27', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+17 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_18(self):
        self.assertEqual(run_calculator('27', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+18 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_19(self):
        self.assertEqual(run_calculator('27', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+19 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_20(self):
        self.assertEqual(run_calculator('27', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+20 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_21(self):
        self.assertEqual(run_calculator('27', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+21 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_22(self):
        self.assertEqual(run_calculator('27', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+22 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_23(self):
        self.assertEqual(run_calculator('27', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+23 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_24(self):
        self.assertEqual(run_calculator('27', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+24 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_25(self):
        self.assertEqual(run_calculator('27', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+25 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_26(self):
        self.assertEqual(run_calculator('27', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+26 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_27(self):
        self.assertEqual(run_calculator('27', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+27 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_28(self):
        self.assertEqual(run_calculator('27', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+28 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_29(self):
        self.assertEqual(run_calculator('27', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+29 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_30(self):
        self.assertEqual(run_calculator('27', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+30 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_31(self):
        self.assertEqual(run_calculator('27', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+31 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_32(self):
        self.assertEqual(run_calculator('27', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+32 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_33(self):
        self.assertEqual(run_calculator('27', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+33 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_34(self):
        self.assertEqual(run_calculator('27', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+34 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_35(self):
        self.assertEqual(run_calculator('27', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+35 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_36(self):
        self.assertEqual(run_calculator('27', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+36 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_37(self):
        self.assertEqual(run_calculator('27', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+37 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_38(self):
        self.assertEqual(run_calculator('27', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+38 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_39(self):
        self.assertEqual(run_calculator('27', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+39 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_40(self):
        self.assertEqual(run_calculator('27', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+40 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_41(self):
        self.assertEqual(run_calculator('27', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+41 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_42(self):
        self.assertEqual(run_calculator('27', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+42 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_43(self):
        self.assertEqual(run_calculator('27', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+43 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_44(self):
        self.assertEqual(run_calculator('27', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+44 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_45(self):
        self.assertEqual(run_calculator('27', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+45 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_46(self):
        self.assertEqual(run_calculator('27', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+46 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_47(self):
        self.assertEqual(run_calculator('27', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+47 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_48(self):
        self.assertEqual(run_calculator('27', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+48 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_49(self):
        self.assertEqual(run_calculator('27', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+49 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_plus_50(self):
        self.assertEqual(run_calculator('27', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27+50 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
