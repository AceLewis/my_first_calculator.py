# test_plus_25.py
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


class TestPlus25(unittest.TestCase):

    def test_25_plus_0(self):
        self.assertEqual(run_calculator('25', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+0 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_1(self):
        self.assertEqual(run_calculator('25', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+1 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_2(self):
        self.assertEqual(run_calculator('25', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+2 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_3(self):
        self.assertEqual(run_calculator('25', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+3 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_4(self):
        self.assertEqual(run_calculator('25', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+4 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_5(self):
        self.assertEqual(run_calculator('25', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+5 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_6(self):
        self.assertEqual(run_calculator('25', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+6 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_7(self):
        self.assertEqual(run_calculator('25', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+7 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_8(self):
        self.assertEqual(run_calculator('25', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+8 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_9(self):
        self.assertEqual(run_calculator('25', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+9 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_10(self):
        self.assertEqual(run_calculator('25', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+10 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_11(self):
        self.assertEqual(run_calculator('25', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+11 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_12(self):
        self.assertEqual(run_calculator('25', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+12 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_13(self):
        self.assertEqual(run_calculator('25', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+13 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_14(self):
        self.assertEqual(run_calculator('25', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+14 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_15(self):
        self.assertEqual(run_calculator('25', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+15 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_16(self):
        self.assertEqual(run_calculator('25', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+16 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_17(self):
        self.assertEqual(run_calculator('25', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+17 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_18(self):
        self.assertEqual(run_calculator('25', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+18 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_19(self):
        self.assertEqual(run_calculator('25', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+19 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_20(self):
        self.assertEqual(run_calculator('25', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+20 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_21(self):
        self.assertEqual(run_calculator('25', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+21 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_22(self):
        self.assertEqual(run_calculator('25', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+22 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_23(self):
        self.assertEqual(run_calculator('25', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+23 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_24(self):
        self.assertEqual(run_calculator('25', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+24 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_25(self):
        self.assertEqual(run_calculator('25', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+25 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_26(self):
        self.assertEqual(run_calculator('25', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+26 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_27(self):
        self.assertEqual(run_calculator('25', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+27 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_28(self):
        self.assertEqual(run_calculator('25', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+28 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_29(self):
        self.assertEqual(run_calculator('25', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+29 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_30(self):
        self.assertEqual(run_calculator('25', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+30 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_31(self):
        self.assertEqual(run_calculator('25', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+31 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_32(self):
        self.assertEqual(run_calculator('25', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+32 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_33(self):
        self.assertEqual(run_calculator('25', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+33 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_34(self):
        self.assertEqual(run_calculator('25', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+34 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_35(self):
        self.assertEqual(run_calculator('25', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+35 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_36(self):
        self.assertEqual(run_calculator('25', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+36 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_37(self):
        self.assertEqual(run_calculator('25', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+37 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_38(self):
        self.assertEqual(run_calculator('25', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+38 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_39(self):
        self.assertEqual(run_calculator('25', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+39 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_40(self):
        self.assertEqual(run_calculator('25', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+40 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_41(self):
        self.assertEqual(run_calculator('25', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+41 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_42(self):
        self.assertEqual(run_calculator('25', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+42 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_43(self):
        self.assertEqual(run_calculator('25', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+43 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_44(self):
        self.assertEqual(run_calculator('25', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+44 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_45(self):
        self.assertEqual(run_calculator('25', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+45 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_46(self):
        self.assertEqual(run_calculator('25', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+46 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_47(self):
        self.assertEqual(run_calculator('25', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+47 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_48(self):
        self.assertEqual(run_calculator('25', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+48 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_49(self):
        self.assertEqual(run_calculator('25', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+49 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_plus_50(self):
        self.assertEqual(run_calculator('25', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25+50 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
