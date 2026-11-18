# test_plus_24.py
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


class TestPlus24(unittest.TestCase):

    def test_24_plus_0(self):
        self.assertEqual(run_calculator('24', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+0 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_1(self):
        self.assertEqual(run_calculator('24', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+1 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_2(self):
        self.assertEqual(run_calculator('24', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+2 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_3(self):
        self.assertEqual(run_calculator('24', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+3 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_4(self):
        self.assertEqual(run_calculator('24', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+4 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_5(self):
        self.assertEqual(run_calculator('24', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+5 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_6(self):
        self.assertEqual(run_calculator('24', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+6 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_7(self):
        self.assertEqual(run_calculator('24', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+7 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_8(self):
        self.assertEqual(run_calculator('24', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+8 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_9(self):
        self.assertEqual(run_calculator('24', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+9 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_10(self):
        self.assertEqual(run_calculator('24', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+10 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_11(self):
        self.assertEqual(run_calculator('24', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+11 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_12(self):
        self.assertEqual(run_calculator('24', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+12 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_13(self):
        self.assertEqual(run_calculator('24', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+13 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_14(self):
        self.assertEqual(run_calculator('24', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+14 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_15(self):
        self.assertEqual(run_calculator('24', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+15 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_16(self):
        self.assertEqual(run_calculator('24', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+16 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_17(self):
        self.assertEqual(run_calculator('24', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+17 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_18(self):
        self.assertEqual(run_calculator('24', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+18 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_19(self):
        self.assertEqual(run_calculator('24', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+19 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_20(self):
        self.assertEqual(run_calculator('24', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+20 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_21(self):
        self.assertEqual(run_calculator('24', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+21 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_22(self):
        self.assertEqual(run_calculator('24', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+22 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_23(self):
        self.assertEqual(run_calculator('24', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+23 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_24(self):
        self.assertEqual(run_calculator('24', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+24 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_25(self):
        self.assertEqual(run_calculator('24', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+25 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_26(self):
        self.assertEqual(run_calculator('24', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+26 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_27(self):
        self.assertEqual(run_calculator('24', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+27 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_28(self):
        self.assertEqual(run_calculator('24', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+28 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_29(self):
        self.assertEqual(run_calculator('24', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+29 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_30(self):
        self.assertEqual(run_calculator('24', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+30 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_31(self):
        self.assertEqual(run_calculator('24', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+31 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_32(self):
        self.assertEqual(run_calculator('24', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+32 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_33(self):
        self.assertEqual(run_calculator('24', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+33 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_34(self):
        self.assertEqual(run_calculator('24', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+34 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_35(self):
        self.assertEqual(run_calculator('24', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+35 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_36(self):
        self.assertEqual(run_calculator('24', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+36 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_37(self):
        self.assertEqual(run_calculator('24', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+37 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_38(self):
        self.assertEqual(run_calculator('24', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+38 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_39(self):
        self.assertEqual(run_calculator('24', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+39 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_40(self):
        self.assertEqual(run_calculator('24', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+40 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_41(self):
        self.assertEqual(run_calculator('24', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+41 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_42(self):
        self.assertEqual(run_calculator('24', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+42 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_43(self):
        self.assertEqual(run_calculator('24', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+43 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_44(self):
        self.assertEqual(run_calculator('24', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+44 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_45(self):
        self.assertEqual(run_calculator('24', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+45 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_46(self):
        self.assertEqual(run_calculator('24', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+46 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_47(self):
        self.assertEqual(run_calculator('24', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+47 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_48(self):
        self.assertEqual(run_calculator('24', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+48 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_49(self):
        self.assertEqual(run_calculator('24', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+49 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_plus_50(self):
        self.assertEqual(run_calculator('24', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24+50 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
