# test_plus_5.py
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


class TestPlus5(unittest.TestCase):

    def test_5_plus_0(self):
        self.assertEqual(run_calculator('5', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+0 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_1(self):
        self.assertEqual(run_calculator('5', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+1 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_2(self):
        self.assertEqual(run_calculator('5', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+2 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_3(self):
        self.assertEqual(run_calculator('5', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+3 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_4(self):
        self.assertEqual(run_calculator('5', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+4 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_5(self):
        self.assertEqual(run_calculator('5', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+5 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_6(self):
        self.assertEqual(run_calculator('5', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+6 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_7(self):
        self.assertEqual(run_calculator('5', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+7 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_8(self):
        self.assertEqual(run_calculator('5', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+8 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_9(self):
        self.assertEqual(run_calculator('5', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+9 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_10(self):
        self.assertEqual(run_calculator('5', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+10 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_11(self):
        self.assertEqual(run_calculator('5', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+11 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_12(self):
        self.assertEqual(run_calculator('5', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+12 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_13(self):
        self.assertEqual(run_calculator('5', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+13 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_14(self):
        self.assertEqual(run_calculator('5', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+14 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_15(self):
        self.assertEqual(run_calculator('5', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+15 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_16(self):
        self.assertEqual(run_calculator('5', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+16 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_17(self):
        self.assertEqual(run_calculator('5', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+17 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_18(self):
        self.assertEqual(run_calculator('5', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+18 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_19(self):
        self.assertEqual(run_calculator('5', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+19 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_20(self):
        self.assertEqual(run_calculator('5', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+20 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_21(self):
        self.assertEqual(run_calculator('5', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+21 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_22(self):
        self.assertEqual(run_calculator('5', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+22 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_23(self):
        self.assertEqual(run_calculator('5', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+23 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_24(self):
        self.assertEqual(run_calculator('5', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+24 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_25(self):
        self.assertEqual(run_calculator('5', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+25 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_26(self):
        self.assertEqual(run_calculator('5', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+26 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_27(self):
        self.assertEqual(run_calculator('5', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+27 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_28(self):
        self.assertEqual(run_calculator('5', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+28 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_29(self):
        self.assertEqual(run_calculator('5', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+29 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_30(self):
        self.assertEqual(run_calculator('5', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+30 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_31(self):
        self.assertEqual(run_calculator('5', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+31 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_32(self):
        self.assertEqual(run_calculator('5', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+32 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_33(self):
        self.assertEqual(run_calculator('5', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+33 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_34(self):
        self.assertEqual(run_calculator('5', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+34 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_35(self):
        self.assertEqual(run_calculator('5', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+35 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_36(self):
        self.assertEqual(run_calculator('5', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+36 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_37(self):
        self.assertEqual(run_calculator('5', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+37 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_38(self):
        self.assertEqual(run_calculator('5', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+38 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_39(self):
        self.assertEqual(run_calculator('5', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+39 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_40(self):
        self.assertEqual(run_calculator('5', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+40 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_41(self):
        self.assertEqual(run_calculator('5', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+41 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_42(self):
        self.assertEqual(run_calculator('5', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+42 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_43(self):
        self.assertEqual(run_calculator('5', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+43 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_44(self):
        self.assertEqual(run_calculator('5', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+44 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_45(self):
        self.assertEqual(run_calculator('5', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+45 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_46(self):
        self.assertEqual(run_calculator('5', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+46 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_47(self):
        self.assertEqual(run_calculator('5', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+47 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_48(self):
        self.assertEqual(run_calculator('5', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+48 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_49(self):
        self.assertEqual(run_calculator('5', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+49 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_plus_50(self):
        self.assertEqual(run_calculator('5', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5+50 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
