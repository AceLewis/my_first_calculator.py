# test_plus_10.py
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


class TestPlus10(unittest.TestCase):

    def test_10_plus_0(self):
        self.assertEqual(run_calculator('10', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+0 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_1(self):
        self.assertEqual(run_calculator('10', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+1 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_2(self):
        self.assertEqual(run_calculator('10', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+2 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_3(self):
        self.assertEqual(run_calculator('10', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+3 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_4(self):
        self.assertEqual(run_calculator('10', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+4 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_5(self):
        self.assertEqual(run_calculator('10', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+5 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_6(self):
        self.assertEqual(run_calculator('10', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+6 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_7(self):
        self.assertEqual(run_calculator('10', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+7 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_8(self):
        self.assertEqual(run_calculator('10', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+8 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_9(self):
        self.assertEqual(run_calculator('10', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+9 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_10(self):
        self.assertEqual(run_calculator('10', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+10 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_11(self):
        self.assertEqual(run_calculator('10', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+11 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_12(self):
        self.assertEqual(run_calculator('10', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+12 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_13(self):
        self.assertEqual(run_calculator('10', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+13 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_14(self):
        self.assertEqual(run_calculator('10', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+14 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_15(self):
        self.assertEqual(run_calculator('10', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+15 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_16(self):
        self.assertEqual(run_calculator('10', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+16 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_17(self):
        self.assertEqual(run_calculator('10', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+17 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_18(self):
        self.assertEqual(run_calculator('10', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+18 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_19(self):
        self.assertEqual(run_calculator('10', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+19 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_20(self):
        self.assertEqual(run_calculator('10', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+20 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_21(self):
        self.assertEqual(run_calculator('10', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+21 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_22(self):
        self.assertEqual(run_calculator('10', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+22 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_23(self):
        self.assertEqual(run_calculator('10', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+23 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_24(self):
        self.assertEqual(run_calculator('10', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+24 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_25(self):
        self.assertEqual(run_calculator('10', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+25 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_26(self):
        self.assertEqual(run_calculator('10', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+26 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_27(self):
        self.assertEqual(run_calculator('10', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+27 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_28(self):
        self.assertEqual(run_calculator('10', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+28 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_29(self):
        self.assertEqual(run_calculator('10', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+29 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_30(self):
        self.assertEqual(run_calculator('10', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+30 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_31(self):
        self.assertEqual(run_calculator('10', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+31 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_32(self):
        self.assertEqual(run_calculator('10', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+32 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_33(self):
        self.assertEqual(run_calculator('10', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+33 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_34(self):
        self.assertEqual(run_calculator('10', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+34 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_35(self):
        self.assertEqual(run_calculator('10', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+35 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_36(self):
        self.assertEqual(run_calculator('10', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+36 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_37(self):
        self.assertEqual(run_calculator('10', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+37 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_38(self):
        self.assertEqual(run_calculator('10', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+38 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_39(self):
        self.assertEqual(run_calculator('10', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+39 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_40(self):
        self.assertEqual(run_calculator('10', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+40 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_41(self):
        self.assertEqual(run_calculator('10', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+41 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_42(self):
        self.assertEqual(run_calculator('10', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+42 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_43(self):
        self.assertEqual(run_calculator('10', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+43 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_44(self):
        self.assertEqual(run_calculator('10', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+44 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_45(self):
        self.assertEqual(run_calculator('10', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+45 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_46(self):
        self.assertEqual(run_calculator('10', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+46 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_47(self):
        self.assertEqual(run_calculator('10', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+47 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_48(self):
        self.assertEqual(run_calculator('10', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+48 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_49(self):
        self.assertEqual(run_calculator('10', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+49 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_plus_50(self):
        self.assertEqual(run_calculator('10', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10+50 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
