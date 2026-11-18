# test_plus_9.py
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


class TestPlus9(unittest.TestCase):

    def test_9_plus_0(self):
        self.assertEqual(run_calculator('9', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+0 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_1(self):
        self.assertEqual(run_calculator('9', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+1 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_2(self):
        self.assertEqual(run_calculator('9', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+2 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_3(self):
        self.assertEqual(run_calculator('9', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+3 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_4(self):
        self.assertEqual(run_calculator('9', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+4 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_5(self):
        self.assertEqual(run_calculator('9', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+5 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_6(self):
        self.assertEqual(run_calculator('9', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+6 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_7(self):
        self.assertEqual(run_calculator('9', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+7 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_8(self):
        self.assertEqual(run_calculator('9', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+8 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_9(self):
        self.assertEqual(run_calculator('9', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+9 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_10(self):
        self.assertEqual(run_calculator('9', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+10 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_11(self):
        self.assertEqual(run_calculator('9', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+11 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_12(self):
        self.assertEqual(run_calculator('9', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+12 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_13(self):
        self.assertEqual(run_calculator('9', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+13 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_14(self):
        self.assertEqual(run_calculator('9', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+14 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_15(self):
        self.assertEqual(run_calculator('9', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+15 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_16(self):
        self.assertEqual(run_calculator('9', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+16 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_17(self):
        self.assertEqual(run_calculator('9', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+17 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_18(self):
        self.assertEqual(run_calculator('9', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+18 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_19(self):
        self.assertEqual(run_calculator('9', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+19 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_20(self):
        self.assertEqual(run_calculator('9', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+20 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_21(self):
        self.assertEqual(run_calculator('9', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+21 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_22(self):
        self.assertEqual(run_calculator('9', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+22 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_23(self):
        self.assertEqual(run_calculator('9', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+23 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_24(self):
        self.assertEqual(run_calculator('9', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+24 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_25(self):
        self.assertEqual(run_calculator('9', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+25 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_26(self):
        self.assertEqual(run_calculator('9', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+26 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_27(self):
        self.assertEqual(run_calculator('9', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+27 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_28(self):
        self.assertEqual(run_calculator('9', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+28 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_29(self):
        self.assertEqual(run_calculator('9', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+29 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_30(self):
        self.assertEqual(run_calculator('9', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+30 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_31(self):
        self.assertEqual(run_calculator('9', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+31 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_32(self):
        self.assertEqual(run_calculator('9', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+32 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_33(self):
        self.assertEqual(run_calculator('9', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+33 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_34(self):
        self.assertEqual(run_calculator('9', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+34 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_35(self):
        self.assertEqual(run_calculator('9', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+35 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_36(self):
        self.assertEqual(run_calculator('9', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+36 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_37(self):
        self.assertEqual(run_calculator('9', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+37 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_38(self):
        self.assertEqual(run_calculator('9', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+38 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_39(self):
        self.assertEqual(run_calculator('9', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+39 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_40(self):
        self.assertEqual(run_calculator('9', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+40 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_41(self):
        self.assertEqual(run_calculator('9', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+41 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_42(self):
        self.assertEqual(run_calculator('9', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+42 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_43(self):
        self.assertEqual(run_calculator('9', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+43 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_44(self):
        self.assertEqual(run_calculator('9', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+44 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_45(self):
        self.assertEqual(run_calculator('9', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+45 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_46(self):
        self.assertEqual(run_calculator('9', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+46 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_47(self):
        self.assertEqual(run_calculator('9', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+47 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_48(self):
        self.assertEqual(run_calculator('9', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+48 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_49(self):
        self.assertEqual(run_calculator('9', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+49 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_plus_50(self):
        self.assertEqual(run_calculator('9', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9+50 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
