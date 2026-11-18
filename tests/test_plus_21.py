# test_plus_21.py
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


class TestPlus21(unittest.TestCase):

    def test_21_plus_0(self):
        self.assertEqual(run_calculator('21', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+0 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_1(self):
        self.assertEqual(run_calculator('21', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+1 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_2(self):
        self.assertEqual(run_calculator('21', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+2 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_3(self):
        self.assertEqual(run_calculator('21', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+3 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_4(self):
        self.assertEqual(run_calculator('21', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+4 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_5(self):
        self.assertEqual(run_calculator('21', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+5 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_6(self):
        self.assertEqual(run_calculator('21', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+6 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_7(self):
        self.assertEqual(run_calculator('21', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+7 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_8(self):
        self.assertEqual(run_calculator('21', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+8 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_9(self):
        self.assertEqual(run_calculator('21', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+9 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_10(self):
        self.assertEqual(run_calculator('21', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+10 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_11(self):
        self.assertEqual(run_calculator('21', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+11 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_12(self):
        self.assertEqual(run_calculator('21', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+12 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_13(self):
        self.assertEqual(run_calculator('21', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+13 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_14(self):
        self.assertEqual(run_calculator('21', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+14 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_15(self):
        self.assertEqual(run_calculator('21', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+15 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_16(self):
        self.assertEqual(run_calculator('21', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+16 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_17(self):
        self.assertEqual(run_calculator('21', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+17 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_18(self):
        self.assertEqual(run_calculator('21', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+18 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_19(self):
        self.assertEqual(run_calculator('21', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+19 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_20(self):
        self.assertEqual(run_calculator('21', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+20 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_21(self):
        self.assertEqual(run_calculator('21', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+21 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_22(self):
        self.assertEqual(run_calculator('21', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+22 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_23(self):
        self.assertEqual(run_calculator('21', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+23 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_24(self):
        self.assertEqual(run_calculator('21', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+24 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_25(self):
        self.assertEqual(run_calculator('21', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+25 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_26(self):
        self.assertEqual(run_calculator('21', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+26 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_27(self):
        self.assertEqual(run_calculator('21', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+27 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_28(self):
        self.assertEqual(run_calculator('21', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+28 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_29(self):
        self.assertEqual(run_calculator('21', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+29 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_30(self):
        self.assertEqual(run_calculator('21', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+30 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_31(self):
        self.assertEqual(run_calculator('21', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+31 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_32(self):
        self.assertEqual(run_calculator('21', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+32 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_33(self):
        self.assertEqual(run_calculator('21', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+33 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_34(self):
        self.assertEqual(run_calculator('21', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+34 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_35(self):
        self.assertEqual(run_calculator('21', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+35 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_36(self):
        self.assertEqual(run_calculator('21', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+36 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_37(self):
        self.assertEqual(run_calculator('21', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+37 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_38(self):
        self.assertEqual(run_calculator('21', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+38 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_39(self):
        self.assertEqual(run_calculator('21', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+39 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_40(self):
        self.assertEqual(run_calculator('21', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+40 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_41(self):
        self.assertEqual(run_calculator('21', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+41 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_42(self):
        self.assertEqual(run_calculator('21', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+42 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_43(self):
        self.assertEqual(run_calculator('21', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+43 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_44(self):
        self.assertEqual(run_calculator('21', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+44 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_45(self):
        self.assertEqual(run_calculator('21', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+45 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_46(self):
        self.assertEqual(run_calculator('21', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+46 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_47(self):
        self.assertEqual(run_calculator('21', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+47 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_48(self):
        self.assertEqual(run_calculator('21', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+48 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_49(self):
        self.assertEqual(run_calculator('21', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+49 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_plus_50(self):
        self.assertEqual(run_calculator('21', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21+50 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
