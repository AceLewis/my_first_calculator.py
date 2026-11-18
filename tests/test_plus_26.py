# test_plus_26.py
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


class TestPlus26(unittest.TestCase):

    def test_26_plus_0(self):
        self.assertEqual(run_calculator('26', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+0 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_1(self):
        self.assertEqual(run_calculator('26', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+1 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_2(self):
        self.assertEqual(run_calculator('26', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+2 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_3(self):
        self.assertEqual(run_calculator('26', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+3 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_4(self):
        self.assertEqual(run_calculator('26', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+4 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_5(self):
        self.assertEqual(run_calculator('26', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+5 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_6(self):
        self.assertEqual(run_calculator('26', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+6 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_7(self):
        self.assertEqual(run_calculator('26', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+7 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_8(self):
        self.assertEqual(run_calculator('26', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+8 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_9(self):
        self.assertEqual(run_calculator('26', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+9 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_10(self):
        self.assertEqual(run_calculator('26', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+10 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_11(self):
        self.assertEqual(run_calculator('26', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+11 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_12(self):
        self.assertEqual(run_calculator('26', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+12 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_13(self):
        self.assertEqual(run_calculator('26', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+13 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_14(self):
        self.assertEqual(run_calculator('26', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+14 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_15(self):
        self.assertEqual(run_calculator('26', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+15 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_16(self):
        self.assertEqual(run_calculator('26', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+16 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_17(self):
        self.assertEqual(run_calculator('26', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+17 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_18(self):
        self.assertEqual(run_calculator('26', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+18 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_19(self):
        self.assertEqual(run_calculator('26', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+19 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_20(self):
        self.assertEqual(run_calculator('26', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+20 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_21(self):
        self.assertEqual(run_calculator('26', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+21 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_22(self):
        self.assertEqual(run_calculator('26', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+22 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_23(self):
        self.assertEqual(run_calculator('26', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+23 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_24(self):
        self.assertEqual(run_calculator('26', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+24 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_25(self):
        self.assertEqual(run_calculator('26', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+25 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_26(self):
        self.assertEqual(run_calculator('26', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+26 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_27(self):
        self.assertEqual(run_calculator('26', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+27 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_28(self):
        self.assertEqual(run_calculator('26', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+28 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_29(self):
        self.assertEqual(run_calculator('26', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+29 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_30(self):
        self.assertEqual(run_calculator('26', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+30 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_31(self):
        self.assertEqual(run_calculator('26', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+31 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_32(self):
        self.assertEqual(run_calculator('26', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+32 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_33(self):
        self.assertEqual(run_calculator('26', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+33 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_34(self):
        self.assertEqual(run_calculator('26', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+34 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_35(self):
        self.assertEqual(run_calculator('26', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+35 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_36(self):
        self.assertEqual(run_calculator('26', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+36 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_37(self):
        self.assertEqual(run_calculator('26', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+37 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_38(self):
        self.assertEqual(run_calculator('26', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+38 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_39(self):
        self.assertEqual(run_calculator('26', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+39 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_40(self):
        self.assertEqual(run_calculator('26', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+40 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_41(self):
        self.assertEqual(run_calculator('26', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+41 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_42(self):
        self.assertEqual(run_calculator('26', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+42 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_43(self):
        self.assertEqual(run_calculator('26', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+43 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_44(self):
        self.assertEqual(run_calculator('26', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+44 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_45(self):
        self.assertEqual(run_calculator('26', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+45 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_46(self):
        self.assertEqual(run_calculator('26', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+46 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_47(self):
        self.assertEqual(run_calculator('26', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+47 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_48(self):
        self.assertEqual(run_calculator('26', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+48 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_49(self):
        self.assertEqual(run_calculator('26', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+49 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_plus_50(self):
        self.assertEqual(run_calculator('26', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26+50 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
