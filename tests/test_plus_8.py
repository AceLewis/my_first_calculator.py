# test_plus_8.py
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


class TestPlus8(unittest.TestCase):

    def test_8_plus_0(self):
        self.assertEqual(run_calculator('8', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+0 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_1(self):
        self.assertEqual(run_calculator('8', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+1 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_2(self):
        self.assertEqual(run_calculator('8', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+2 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_3(self):
        self.assertEqual(run_calculator('8', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+3 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_4(self):
        self.assertEqual(run_calculator('8', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+4 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_5(self):
        self.assertEqual(run_calculator('8', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+5 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_6(self):
        self.assertEqual(run_calculator('8', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+6 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_7(self):
        self.assertEqual(run_calculator('8', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+7 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_8(self):
        self.assertEqual(run_calculator('8', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+8 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_9(self):
        self.assertEqual(run_calculator('8', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+9 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_10(self):
        self.assertEqual(run_calculator('8', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+10 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_11(self):
        self.assertEqual(run_calculator('8', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+11 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_12(self):
        self.assertEqual(run_calculator('8', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+12 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_13(self):
        self.assertEqual(run_calculator('8', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+13 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_14(self):
        self.assertEqual(run_calculator('8', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+14 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_15(self):
        self.assertEqual(run_calculator('8', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+15 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_16(self):
        self.assertEqual(run_calculator('8', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+16 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_17(self):
        self.assertEqual(run_calculator('8', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+17 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_18(self):
        self.assertEqual(run_calculator('8', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+18 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_19(self):
        self.assertEqual(run_calculator('8', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+19 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_20(self):
        self.assertEqual(run_calculator('8', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+20 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_21(self):
        self.assertEqual(run_calculator('8', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+21 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_22(self):
        self.assertEqual(run_calculator('8', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+22 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_23(self):
        self.assertEqual(run_calculator('8', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+23 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_24(self):
        self.assertEqual(run_calculator('8', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+24 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_25(self):
        self.assertEqual(run_calculator('8', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+25 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_26(self):
        self.assertEqual(run_calculator('8', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+26 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_27(self):
        self.assertEqual(run_calculator('8', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+27 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_28(self):
        self.assertEqual(run_calculator('8', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+28 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_29(self):
        self.assertEqual(run_calculator('8', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+29 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_30(self):
        self.assertEqual(run_calculator('8', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+30 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_31(self):
        self.assertEqual(run_calculator('8', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+31 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_32(self):
        self.assertEqual(run_calculator('8', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+32 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_33(self):
        self.assertEqual(run_calculator('8', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+33 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_34(self):
        self.assertEqual(run_calculator('8', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+34 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_35(self):
        self.assertEqual(run_calculator('8', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+35 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_36(self):
        self.assertEqual(run_calculator('8', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+36 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_37(self):
        self.assertEqual(run_calculator('8', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+37 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_38(self):
        self.assertEqual(run_calculator('8', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+38 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_39(self):
        self.assertEqual(run_calculator('8', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+39 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_40(self):
        self.assertEqual(run_calculator('8', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+40 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_41(self):
        self.assertEqual(run_calculator('8', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+41 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_42(self):
        self.assertEqual(run_calculator('8', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+42 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_43(self):
        self.assertEqual(run_calculator('8', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+43 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_44(self):
        self.assertEqual(run_calculator('8', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+44 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_45(self):
        self.assertEqual(run_calculator('8', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+45 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_46(self):
        self.assertEqual(run_calculator('8', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+46 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_47(self):
        self.assertEqual(run_calculator('8', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+47 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_48(self):
        self.assertEqual(run_calculator('8', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+48 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_49(self):
        self.assertEqual(run_calculator('8', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+49 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_plus_50(self):
        self.assertEqual(run_calculator('8', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8+50 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
