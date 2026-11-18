# test_plus_14.py
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


class TestPlus14(unittest.TestCase):

    def test_14_plus_0(self):
        self.assertEqual(run_calculator('14', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+0 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_1(self):
        self.assertEqual(run_calculator('14', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+1 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_2(self):
        self.assertEqual(run_calculator('14', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+2 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_3(self):
        self.assertEqual(run_calculator('14', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+3 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_4(self):
        self.assertEqual(run_calculator('14', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+4 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_5(self):
        self.assertEqual(run_calculator('14', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+5 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_6(self):
        self.assertEqual(run_calculator('14', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+6 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_7(self):
        self.assertEqual(run_calculator('14', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+7 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_8(self):
        self.assertEqual(run_calculator('14', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+8 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_9(self):
        self.assertEqual(run_calculator('14', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+9 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_10(self):
        self.assertEqual(run_calculator('14', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+10 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_11(self):
        self.assertEqual(run_calculator('14', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+11 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_12(self):
        self.assertEqual(run_calculator('14', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+12 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_13(self):
        self.assertEqual(run_calculator('14', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+13 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_14(self):
        self.assertEqual(run_calculator('14', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+14 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_15(self):
        self.assertEqual(run_calculator('14', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+15 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_16(self):
        self.assertEqual(run_calculator('14', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+16 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_17(self):
        self.assertEqual(run_calculator('14', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+17 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_18(self):
        self.assertEqual(run_calculator('14', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+18 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_19(self):
        self.assertEqual(run_calculator('14', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+19 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_20(self):
        self.assertEqual(run_calculator('14', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+20 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_21(self):
        self.assertEqual(run_calculator('14', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+21 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_22(self):
        self.assertEqual(run_calculator('14', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+22 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_23(self):
        self.assertEqual(run_calculator('14', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+23 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_24(self):
        self.assertEqual(run_calculator('14', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+24 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_25(self):
        self.assertEqual(run_calculator('14', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+25 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_26(self):
        self.assertEqual(run_calculator('14', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+26 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_27(self):
        self.assertEqual(run_calculator('14', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+27 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_28(self):
        self.assertEqual(run_calculator('14', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+28 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_29(self):
        self.assertEqual(run_calculator('14', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+29 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_30(self):
        self.assertEqual(run_calculator('14', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+30 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_31(self):
        self.assertEqual(run_calculator('14', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+31 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_32(self):
        self.assertEqual(run_calculator('14', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+32 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_33(self):
        self.assertEqual(run_calculator('14', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+33 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_34(self):
        self.assertEqual(run_calculator('14', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+34 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_35(self):
        self.assertEqual(run_calculator('14', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+35 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_36(self):
        self.assertEqual(run_calculator('14', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+36 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_37(self):
        self.assertEqual(run_calculator('14', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+37 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_38(self):
        self.assertEqual(run_calculator('14', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+38 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_39(self):
        self.assertEqual(run_calculator('14', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+39 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_40(self):
        self.assertEqual(run_calculator('14', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+40 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_41(self):
        self.assertEqual(run_calculator('14', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+41 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_42(self):
        self.assertEqual(run_calculator('14', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+42 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_43(self):
        self.assertEqual(run_calculator('14', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+43 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_44(self):
        self.assertEqual(run_calculator('14', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+44 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_45(self):
        self.assertEqual(run_calculator('14', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+45 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_46(self):
        self.assertEqual(run_calculator('14', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+46 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_47(self):
        self.assertEqual(run_calculator('14', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+47 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_48(self):
        self.assertEqual(run_calculator('14', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+48 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_49(self):
        self.assertEqual(run_calculator('14', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+49 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_plus_50(self):
        self.assertEqual(run_calculator('14', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14+50 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
