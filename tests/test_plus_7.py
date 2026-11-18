# test_plus_7.py
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


class TestPlus7(unittest.TestCase):

    def test_7_plus_0(self):
        self.assertEqual(run_calculator('7', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+0 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_1(self):
        self.assertEqual(run_calculator('7', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+1 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_2(self):
        self.assertEqual(run_calculator('7', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+2 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_3(self):
        self.assertEqual(run_calculator('7', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+3 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_4(self):
        self.assertEqual(run_calculator('7', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+4 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_5(self):
        self.assertEqual(run_calculator('7', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+5 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_6(self):
        self.assertEqual(run_calculator('7', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+6 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_7(self):
        self.assertEqual(run_calculator('7', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+7 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_8(self):
        self.assertEqual(run_calculator('7', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+8 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_9(self):
        self.assertEqual(run_calculator('7', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+9 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_10(self):
        self.assertEqual(run_calculator('7', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+10 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_11(self):
        self.assertEqual(run_calculator('7', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+11 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_12(self):
        self.assertEqual(run_calculator('7', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+12 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_13(self):
        self.assertEqual(run_calculator('7', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+13 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_14(self):
        self.assertEqual(run_calculator('7', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+14 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_15(self):
        self.assertEqual(run_calculator('7', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+15 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_16(self):
        self.assertEqual(run_calculator('7', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+16 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_17(self):
        self.assertEqual(run_calculator('7', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+17 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_18(self):
        self.assertEqual(run_calculator('7', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+18 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_19(self):
        self.assertEqual(run_calculator('7', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+19 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_20(self):
        self.assertEqual(run_calculator('7', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+20 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_21(self):
        self.assertEqual(run_calculator('7', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+21 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_22(self):
        self.assertEqual(run_calculator('7', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+22 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_23(self):
        self.assertEqual(run_calculator('7', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+23 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_24(self):
        self.assertEqual(run_calculator('7', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+24 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_25(self):
        self.assertEqual(run_calculator('7', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+25 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_26(self):
        self.assertEqual(run_calculator('7', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+26 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_27(self):
        self.assertEqual(run_calculator('7', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+27 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_28(self):
        self.assertEqual(run_calculator('7', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+28 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_29(self):
        self.assertEqual(run_calculator('7', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+29 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_30(self):
        self.assertEqual(run_calculator('7', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+30 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_31(self):
        self.assertEqual(run_calculator('7', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+31 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_32(self):
        self.assertEqual(run_calculator('7', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+32 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_33(self):
        self.assertEqual(run_calculator('7', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+33 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_34(self):
        self.assertEqual(run_calculator('7', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+34 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_35(self):
        self.assertEqual(run_calculator('7', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+35 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_36(self):
        self.assertEqual(run_calculator('7', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+36 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_37(self):
        self.assertEqual(run_calculator('7', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+37 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_38(self):
        self.assertEqual(run_calculator('7', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+38 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_39(self):
        self.assertEqual(run_calculator('7', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+39 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_40(self):
        self.assertEqual(run_calculator('7', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+40 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_41(self):
        self.assertEqual(run_calculator('7', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+41 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_42(self):
        self.assertEqual(run_calculator('7', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+42 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_43(self):
        self.assertEqual(run_calculator('7', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+43 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_44(self):
        self.assertEqual(run_calculator('7', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+44 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_45(self):
        self.assertEqual(run_calculator('7', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+45 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_46(self):
        self.assertEqual(run_calculator('7', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+46 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_47(self):
        self.assertEqual(run_calculator('7', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+47 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_48(self):
        self.assertEqual(run_calculator('7', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+48 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_49(self):
        self.assertEqual(run_calculator('7', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+49 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_plus_50(self):
        self.assertEqual(run_calculator('7', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7+50 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
