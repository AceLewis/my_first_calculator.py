# test_plus_28.py
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


class TestPlus28(unittest.TestCase):

    def test_28_plus_0(self):
        self.assertEqual(run_calculator('28', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+0 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_1(self):
        self.assertEqual(run_calculator('28', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+1 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_2(self):
        self.assertEqual(run_calculator('28', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+2 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_3(self):
        self.assertEqual(run_calculator('28', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+3 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_4(self):
        self.assertEqual(run_calculator('28', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+4 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_5(self):
        self.assertEqual(run_calculator('28', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+5 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_6(self):
        self.assertEqual(run_calculator('28', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+6 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_7(self):
        self.assertEqual(run_calculator('28', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+7 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_8(self):
        self.assertEqual(run_calculator('28', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+8 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_9(self):
        self.assertEqual(run_calculator('28', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+9 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_10(self):
        self.assertEqual(run_calculator('28', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+10 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_11(self):
        self.assertEqual(run_calculator('28', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+11 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_12(self):
        self.assertEqual(run_calculator('28', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+12 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_13(self):
        self.assertEqual(run_calculator('28', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+13 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_14(self):
        self.assertEqual(run_calculator('28', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+14 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_15(self):
        self.assertEqual(run_calculator('28', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+15 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_16(self):
        self.assertEqual(run_calculator('28', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+16 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_17(self):
        self.assertEqual(run_calculator('28', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+17 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_18(self):
        self.assertEqual(run_calculator('28', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+18 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_19(self):
        self.assertEqual(run_calculator('28', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+19 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_20(self):
        self.assertEqual(run_calculator('28', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+20 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_21(self):
        self.assertEqual(run_calculator('28', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+21 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_22(self):
        self.assertEqual(run_calculator('28', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+22 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_23(self):
        self.assertEqual(run_calculator('28', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+23 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_24(self):
        self.assertEqual(run_calculator('28', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+24 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_25(self):
        self.assertEqual(run_calculator('28', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+25 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_26(self):
        self.assertEqual(run_calculator('28', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+26 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_27(self):
        self.assertEqual(run_calculator('28', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+27 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_28(self):
        self.assertEqual(run_calculator('28', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+28 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_29(self):
        self.assertEqual(run_calculator('28', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+29 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_30(self):
        self.assertEqual(run_calculator('28', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+30 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_31(self):
        self.assertEqual(run_calculator('28', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+31 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_32(self):
        self.assertEqual(run_calculator('28', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+32 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_33(self):
        self.assertEqual(run_calculator('28', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+33 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_34(self):
        self.assertEqual(run_calculator('28', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+34 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_35(self):
        self.assertEqual(run_calculator('28', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+35 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_36(self):
        self.assertEqual(run_calculator('28', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+36 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_37(self):
        self.assertEqual(run_calculator('28', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+37 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_38(self):
        self.assertEqual(run_calculator('28', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+38 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_39(self):
        self.assertEqual(run_calculator('28', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+39 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_40(self):
        self.assertEqual(run_calculator('28', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+40 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_41(self):
        self.assertEqual(run_calculator('28', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+41 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_42(self):
        self.assertEqual(run_calculator('28', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+42 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_43(self):
        self.assertEqual(run_calculator('28', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+43 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_44(self):
        self.assertEqual(run_calculator('28', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+44 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_45(self):
        self.assertEqual(run_calculator('28', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+45 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_46(self):
        self.assertEqual(run_calculator('28', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+46 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_47(self):
        self.assertEqual(run_calculator('28', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+47 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_48(self):
        self.assertEqual(run_calculator('28', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+48 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_49(self):
        self.assertEqual(run_calculator('28', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+49 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_plus_50(self):
        self.assertEqual(run_calculator('28', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28+50 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
