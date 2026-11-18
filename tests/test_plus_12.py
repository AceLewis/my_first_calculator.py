# test_plus_12.py
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


class TestPlus12(unittest.TestCase):

    def test_12_plus_0(self):
        self.assertEqual(run_calculator('12', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+0 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_1(self):
        self.assertEqual(run_calculator('12', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+1 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_2(self):
        self.assertEqual(run_calculator('12', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+2 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_3(self):
        self.assertEqual(run_calculator('12', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+3 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_4(self):
        self.assertEqual(run_calculator('12', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+4 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_5(self):
        self.assertEqual(run_calculator('12', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+5 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_6(self):
        self.assertEqual(run_calculator('12', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+6 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_7(self):
        self.assertEqual(run_calculator('12', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+7 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_8(self):
        self.assertEqual(run_calculator('12', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+8 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_9(self):
        self.assertEqual(run_calculator('12', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+9 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_10(self):
        self.assertEqual(run_calculator('12', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+10 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_11(self):
        self.assertEqual(run_calculator('12', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+11 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_12(self):
        self.assertEqual(run_calculator('12', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+12 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_13(self):
        self.assertEqual(run_calculator('12', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+13 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_14(self):
        self.assertEqual(run_calculator('12', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+14 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_15(self):
        self.assertEqual(run_calculator('12', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+15 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_16(self):
        self.assertEqual(run_calculator('12', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+16 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_17(self):
        self.assertEqual(run_calculator('12', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+17 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_18(self):
        self.assertEqual(run_calculator('12', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+18 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_19(self):
        self.assertEqual(run_calculator('12', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+19 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_20(self):
        self.assertEqual(run_calculator('12', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+20 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_21(self):
        self.assertEqual(run_calculator('12', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+21 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_22(self):
        self.assertEqual(run_calculator('12', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+22 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_23(self):
        self.assertEqual(run_calculator('12', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+23 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_24(self):
        self.assertEqual(run_calculator('12', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+24 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_25(self):
        self.assertEqual(run_calculator('12', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+25 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_26(self):
        self.assertEqual(run_calculator('12', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+26 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_27(self):
        self.assertEqual(run_calculator('12', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+27 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_28(self):
        self.assertEqual(run_calculator('12', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+28 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_29(self):
        self.assertEqual(run_calculator('12', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+29 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_30(self):
        self.assertEqual(run_calculator('12', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+30 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_31(self):
        self.assertEqual(run_calculator('12', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+31 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_32(self):
        self.assertEqual(run_calculator('12', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+32 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_33(self):
        self.assertEqual(run_calculator('12', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+33 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_34(self):
        self.assertEqual(run_calculator('12', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+34 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_35(self):
        self.assertEqual(run_calculator('12', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+35 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_36(self):
        self.assertEqual(run_calculator('12', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+36 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_37(self):
        self.assertEqual(run_calculator('12', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+37 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_38(self):
        self.assertEqual(run_calculator('12', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+38 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_39(self):
        self.assertEqual(run_calculator('12', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+39 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_40(self):
        self.assertEqual(run_calculator('12', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+40 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_41(self):
        self.assertEqual(run_calculator('12', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+41 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_42(self):
        self.assertEqual(run_calculator('12', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+42 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_43(self):
        self.assertEqual(run_calculator('12', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+43 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_44(self):
        self.assertEqual(run_calculator('12', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+44 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_45(self):
        self.assertEqual(run_calculator('12', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+45 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_46(self):
        self.assertEqual(run_calculator('12', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+46 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_47(self):
        self.assertEqual(run_calculator('12', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+47 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_48(self):
        self.assertEqual(run_calculator('12', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+48 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_49(self):
        self.assertEqual(run_calculator('12', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+49 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_plus_50(self):
        self.assertEqual(run_calculator('12', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12+50 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
