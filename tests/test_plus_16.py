# test_plus_16.py
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


class TestPlus16(unittest.TestCase):

    def test_16_plus_0(self):
        self.assertEqual(run_calculator('16', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+0 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_1(self):
        self.assertEqual(run_calculator('16', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+1 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_2(self):
        self.assertEqual(run_calculator('16', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+2 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_3(self):
        self.assertEqual(run_calculator('16', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+3 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_4(self):
        self.assertEqual(run_calculator('16', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+4 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_5(self):
        self.assertEqual(run_calculator('16', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+5 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_6(self):
        self.assertEqual(run_calculator('16', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+6 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_7(self):
        self.assertEqual(run_calculator('16', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+7 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_8(self):
        self.assertEqual(run_calculator('16', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+8 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_9(self):
        self.assertEqual(run_calculator('16', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+9 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_10(self):
        self.assertEqual(run_calculator('16', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+10 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_11(self):
        self.assertEqual(run_calculator('16', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+11 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_12(self):
        self.assertEqual(run_calculator('16', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+12 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_13(self):
        self.assertEqual(run_calculator('16', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+13 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_14(self):
        self.assertEqual(run_calculator('16', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+14 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_15(self):
        self.assertEqual(run_calculator('16', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+15 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_16(self):
        self.assertEqual(run_calculator('16', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+16 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_17(self):
        self.assertEqual(run_calculator('16', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+17 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_18(self):
        self.assertEqual(run_calculator('16', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+18 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_19(self):
        self.assertEqual(run_calculator('16', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+19 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_20(self):
        self.assertEqual(run_calculator('16', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+20 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_21(self):
        self.assertEqual(run_calculator('16', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+21 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_22(self):
        self.assertEqual(run_calculator('16', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+22 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_23(self):
        self.assertEqual(run_calculator('16', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+23 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_24(self):
        self.assertEqual(run_calculator('16', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+24 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_25(self):
        self.assertEqual(run_calculator('16', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+25 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_26(self):
        self.assertEqual(run_calculator('16', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+26 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_27(self):
        self.assertEqual(run_calculator('16', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+27 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_28(self):
        self.assertEqual(run_calculator('16', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+28 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_29(self):
        self.assertEqual(run_calculator('16', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+29 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_30(self):
        self.assertEqual(run_calculator('16', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+30 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_31(self):
        self.assertEqual(run_calculator('16', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+31 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_32(self):
        self.assertEqual(run_calculator('16', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+32 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_33(self):
        self.assertEqual(run_calculator('16', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+33 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_34(self):
        self.assertEqual(run_calculator('16', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+34 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_35(self):
        self.assertEqual(run_calculator('16', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+35 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_36(self):
        self.assertEqual(run_calculator('16', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+36 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_37(self):
        self.assertEqual(run_calculator('16', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+37 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_38(self):
        self.assertEqual(run_calculator('16', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+38 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_39(self):
        self.assertEqual(run_calculator('16', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+39 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_40(self):
        self.assertEqual(run_calculator('16', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+40 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_41(self):
        self.assertEqual(run_calculator('16', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+41 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_42(self):
        self.assertEqual(run_calculator('16', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+42 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_43(self):
        self.assertEqual(run_calculator('16', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+43 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_44(self):
        self.assertEqual(run_calculator('16', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+44 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_45(self):
        self.assertEqual(run_calculator('16', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+45 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_46(self):
        self.assertEqual(run_calculator('16', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+46 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_47(self):
        self.assertEqual(run_calculator('16', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+47 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_48(self):
        self.assertEqual(run_calculator('16', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+48 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_49(self):
        self.assertEqual(run_calculator('16', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+49 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_plus_50(self):
        self.assertEqual(run_calculator('16', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16+50 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
