# test_plus_23.py
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


class TestPlus23(unittest.TestCase):

    def test_23_plus_0(self):
        self.assertEqual(run_calculator('23', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+0 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_1(self):
        self.assertEqual(run_calculator('23', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+1 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_2(self):
        self.assertEqual(run_calculator('23', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+2 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_3(self):
        self.assertEqual(run_calculator('23', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+3 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_4(self):
        self.assertEqual(run_calculator('23', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+4 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_5(self):
        self.assertEqual(run_calculator('23', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+5 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_6(self):
        self.assertEqual(run_calculator('23', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+6 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_7(self):
        self.assertEqual(run_calculator('23', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+7 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_8(self):
        self.assertEqual(run_calculator('23', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+8 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_9(self):
        self.assertEqual(run_calculator('23', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+9 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_10(self):
        self.assertEqual(run_calculator('23', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+10 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_11(self):
        self.assertEqual(run_calculator('23', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+11 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_12(self):
        self.assertEqual(run_calculator('23', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+12 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_13(self):
        self.assertEqual(run_calculator('23', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+13 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_14(self):
        self.assertEqual(run_calculator('23', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+14 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_15(self):
        self.assertEqual(run_calculator('23', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+15 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_16(self):
        self.assertEqual(run_calculator('23', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+16 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_17(self):
        self.assertEqual(run_calculator('23', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+17 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_18(self):
        self.assertEqual(run_calculator('23', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+18 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_19(self):
        self.assertEqual(run_calculator('23', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+19 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_20(self):
        self.assertEqual(run_calculator('23', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+20 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_21(self):
        self.assertEqual(run_calculator('23', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+21 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_22(self):
        self.assertEqual(run_calculator('23', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+22 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_23(self):
        self.assertEqual(run_calculator('23', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+23 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_24(self):
        self.assertEqual(run_calculator('23', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+24 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_25(self):
        self.assertEqual(run_calculator('23', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+25 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_26(self):
        self.assertEqual(run_calculator('23', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+26 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_27(self):
        self.assertEqual(run_calculator('23', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+27 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_28(self):
        self.assertEqual(run_calculator('23', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+28 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_29(self):
        self.assertEqual(run_calculator('23', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+29 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_30(self):
        self.assertEqual(run_calculator('23', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+30 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_31(self):
        self.assertEqual(run_calculator('23', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+31 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_32(self):
        self.assertEqual(run_calculator('23', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+32 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_33(self):
        self.assertEqual(run_calculator('23', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+33 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_34(self):
        self.assertEqual(run_calculator('23', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+34 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_35(self):
        self.assertEqual(run_calculator('23', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+35 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_36(self):
        self.assertEqual(run_calculator('23', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+36 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_37(self):
        self.assertEqual(run_calculator('23', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+37 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_38(self):
        self.assertEqual(run_calculator('23', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+38 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_39(self):
        self.assertEqual(run_calculator('23', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+39 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_40(self):
        self.assertEqual(run_calculator('23', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+40 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_41(self):
        self.assertEqual(run_calculator('23', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+41 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_42(self):
        self.assertEqual(run_calculator('23', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+42 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_43(self):
        self.assertEqual(run_calculator('23', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+43 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_44(self):
        self.assertEqual(run_calculator('23', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+44 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_45(self):
        self.assertEqual(run_calculator('23', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+45 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_46(self):
        self.assertEqual(run_calculator('23', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+46 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_47(self):
        self.assertEqual(run_calculator('23', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+47 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_48(self):
        self.assertEqual(run_calculator('23', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+48 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_49(self):
        self.assertEqual(run_calculator('23', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+49 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_plus_50(self):
        self.assertEqual(run_calculator('23', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23+50 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
