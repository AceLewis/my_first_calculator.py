# test_plus_15.py
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


class TestPlus15(unittest.TestCase):

    def test_15_plus_0(self):
        self.assertEqual(run_calculator('15', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+0 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_1(self):
        self.assertEqual(run_calculator('15', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+1 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_2(self):
        self.assertEqual(run_calculator('15', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+2 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_3(self):
        self.assertEqual(run_calculator('15', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+3 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_4(self):
        self.assertEqual(run_calculator('15', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+4 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_5(self):
        self.assertEqual(run_calculator('15', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+5 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_6(self):
        self.assertEqual(run_calculator('15', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+6 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_7(self):
        self.assertEqual(run_calculator('15', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+7 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_8(self):
        self.assertEqual(run_calculator('15', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+8 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_9(self):
        self.assertEqual(run_calculator('15', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+9 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_10(self):
        self.assertEqual(run_calculator('15', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+10 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_11(self):
        self.assertEqual(run_calculator('15', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+11 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_12(self):
        self.assertEqual(run_calculator('15', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+12 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_13(self):
        self.assertEqual(run_calculator('15', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+13 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_14(self):
        self.assertEqual(run_calculator('15', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+14 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_15(self):
        self.assertEqual(run_calculator('15', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+15 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_16(self):
        self.assertEqual(run_calculator('15', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+16 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_17(self):
        self.assertEqual(run_calculator('15', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+17 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_18(self):
        self.assertEqual(run_calculator('15', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+18 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_19(self):
        self.assertEqual(run_calculator('15', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+19 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_20(self):
        self.assertEqual(run_calculator('15', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+20 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_21(self):
        self.assertEqual(run_calculator('15', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+21 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_22(self):
        self.assertEqual(run_calculator('15', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+22 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_23(self):
        self.assertEqual(run_calculator('15', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+23 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_24(self):
        self.assertEqual(run_calculator('15', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+24 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_25(self):
        self.assertEqual(run_calculator('15', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+25 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_26(self):
        self.assertEqual(run_calculator('15', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+26 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_27(self):
        self.assertEqual(run_calculator('15', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+27 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_28(self):
        self.assertEqual(run_calculator('15', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+28 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_29(self):
        self.assertEqual(run_calculator('15', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+29 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_30(self):
        self.assertEqual(run_calculator('15', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+30 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_31(self):
        self.assertEqual(run_calculator('15', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+31 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_32(self):
        self.assertEqual(run_calculator('15', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+32 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_33(self):
        self.assertEqual(run_calculator('15', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+33 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_34(self):
        self.assertEqual(run_calculator('15', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+34 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_35(self):
        self.assertEqual(run_calculator('15', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+35 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_36(self):
        self.assertEqual(run_calculator('15', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+36 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_37(self):
        self.assertEqual(run_calculator('15', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+37 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_38(self):
        self.assertEqual(run_calculator('15', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+38 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_39(self):
        self.assertEqual(run_calculator('15', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+39 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_40(self):
        self.assertEqual(run_calculator('15', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+40 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_41(self):
        self.assertEqual(run_calculator('15', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+41 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_42(self):
        self.assertEqual(run_calculator('15', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+42 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_43(self):
        self.assertEqual(run_calculator('15', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+43 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_44(self):
        self.assertEqual(run_calculator('15', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+44 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_45(self):
        self.assertEqual(run_calculator('15', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+45 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_46(self):
        self.assertEqual(run_calculator('15', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+46 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_47(self):
        self.assertEqual(run_calculator('15', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+47 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_48(self):
        self.assertEqual(run_calculator('15', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+48 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_49(self):
        self.assertEqual(run_calculator('15', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+49 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_plus_50(self):
        self.assertEqual(run_calculator('15', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15+50 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
