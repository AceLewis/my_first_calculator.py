# test_plus_17.py
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


class TestPlus17(unittest.TestCase):

    def test_17_plus_0(self):
        self.assertEqual(run_calculator('17', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+0 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_1(self):
        self.assertEqual(run_calculator('17', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+1 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_2(self):
        self.assertEqual(run_calculator('17', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+2 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_3(self):
        self.assertEqual(run_calculator('17', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+3 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_4(self):
        self.assertEqual(run_calculator('17', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+4 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_5(self):
        self.assertEqual(run_calculator('17', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+5 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_6(self):
        self.assertEqual(run_calculator('17', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+6 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_7(self):
        self.assertEqual(run_calculator('17', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+7 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_8(self):
        self.assertEqual(run_calculator('17', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+8 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_9(self):
        self.assertEqual(run_calculator('17', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+9 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_10(self):
        self.assertEqual(run_calculator('17', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+10 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_11(self):
        self.assertEqual(run_calculator('17', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+11 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_12(self):
        self.assertEqual(run_calculator('17', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+12 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_13(self):
        self.assertEqual(run_calculator('17', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+13 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_14(self):
        self.assertEqual(run_calculator('17', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+14 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_15(self):
        self.assertEqual(run_calculator('17', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+15 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_16(self):
        self.assertEqual(run_calculator('17', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+16 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_17(self):
        self.assertEqual(run_calculator('17', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+17 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_18(self):
        self.assertEqual(run_calculator('17', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+18 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_19(self):
        self.assertEqual(run_calculator('17', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+19 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_20(self):
        self.assertEqual(run_calculator('17', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+20 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_21(self):
        self.assertEqual(run_calculator('17', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+21 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_22(self):
        self.assertEqual(run_calculator('17', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+22 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_23(self):
        self.assertEqual(run_calculator('17', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+23 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_24(self):
        self.assertEqual(run_calculator('17', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+24 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_25(self):
        self.assertEqual(run_calculator('17', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+25 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_26(self):
        self.assertEqual(run_calculator('17', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+26 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_27(self):
        self.assertEqual(run_calculator('17', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+27 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_28(self):
        self.assertEqual(run_calculator('17', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+28 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_29(self):
        self.assertEqual(run_calculator('17', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+29 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_30(self):
        self.assertEqual(run_calculator('17', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+30 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_31(self):
        self.assertEqual(run_calculator('17', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+31 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_32(self):
        self.assertEqual(run_calculator('17', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+32 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_33(self):
        self.assertEqual(run_calculator('17', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+33 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_34(self):
        self.assertEqual(run_calculator('17', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+34 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_35(self):
        self.assertEqual(run_calculator('17', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+35 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_36(self):
        self.assertEqual(run_calculator('17', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+36 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_37(self):
        self.assertEqual(run_calculator('17', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+37 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_38(self):
        self.assertEqual(run_calculator('17', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+38 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_39(self):
        self.assertEqual(run_calculator('17', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+39 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_40(self):
        self.assertEqual(run_calculator('17', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+40 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_41(self):
        self.assertEqual(run_calculator('17', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+41 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_42(self):
        self.assertEqual(run_calculator('17', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+42 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_43(self):
        self.assertEqual(run_calculator('17', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+43 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_44(self):
        self.assertEqual(run_calculator('17', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+44 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_45(self):
        self.assertEqual(run_calculator('17', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+45 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_46(self):
        self.assertEqual(run_calculator('17', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+46 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_47(self):
        self.assertEqual(run_calculator('17', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+47 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_48(self):
        self.assertEqual(run_calculator('17', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+48 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_49(self):
        self.assertEqual(run_calculator('17', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+49 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_plus_50(self):
        self.assertEqual(run_calculator('17', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17+50 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
