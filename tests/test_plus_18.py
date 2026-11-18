# test_plus_18.py
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


class TestPlus18(unittest.TestCase):

    def test_18_plus_0(self):
        self.assertEqual(run_calculator('18', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+0 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_1(self):
        self.assertEqual(run_calculator('18', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+1 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_2(self):
        self.assertEqual(run_calculator('18', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+2 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_3(self):
        self.assertEqual(run_calculator('18', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+3 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_4(self):
        self.assertEqual(run_calculator('18', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+4 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_5(self):
        self.assertEqual(run_calculator('18', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+5 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_6(self):
        self.assertEqual(run_calculator('18', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+6 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_7(self):
        self.assertEqual(run_calculator('18', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+7 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_8(self):
        self.assertEqual(run_calculator('18', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+8 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_9(self):
        self.assertEqual(run_calculator('18', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+9 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_10(self):
        self.assertEqual(run_calculator('18', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+10 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_11(self):
        self.assertEqual(run_calculator('18', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+11 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_12(self):
        self.assertEqual(run_calculator('18', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+12 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_13(self):
        self.assertEqual(run_calculator('18', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+13 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_14(self):
        self.assertEqual(run_calculator('18', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+14 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_15(self):
        self.assertEqual(run_calculator('18', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+15 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_16(self):
        self.assertEqual(run_calculator('18', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+16 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_17(self):
        self.assertEqual(run_calculator('18', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+17 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_18(self):
        self.assertEqual(run_calculator('18', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+18 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_19(self):
        self.assertEqual(run_calculator('18', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+19 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_20(self):
        self.assertEqual(run_calculator('18', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+20 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_21(self):
        self.assertEqual(run_calculator('18', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+21 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_22(self):
        self.assertEqual(run_calculator('18', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+22 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_23(self):
        self.assertEqual(run_calculator('18', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+23 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_24(self):
        self.assertEqual(run_calculator('18', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+24 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_25(self):
        self.assertEqual(run_calculator('18', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+25 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_26(self):
        self.assertEqual(run_calculator('18', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+26 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_27(self):
        self.assertEqual(run_calculator('18', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+27 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_28(self):
        self.assertEqual(run_calculator('18', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+28 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_29(self):
        self.assertEqual(run_calculator('18', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+29 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_30(self):
        self.assertEqual(run_calculator('18', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+30 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_31(self):
        self.assertEqual(run_calculator('18', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+31 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_32(self):
        self.assertEqual(run_calculator('18', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+32 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_33(self):
        self.assertEqual(run_calculator('18', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+33 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_34(self):
        self.assertEqual(run_calculator('18', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+34 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_35(self):
        self.assertEqual(run_calculator('18', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+35 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_36(self):
        self.assertEqual(run_calculator('18', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+36 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_37(self):
        self.assertEqual(run_calculator('18', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+37 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_38(self):
        self.assertEqual(run_calculator('18', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+38 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_39(self):
        self.assertEqual(run_calculator('18', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+39 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_40(self):
        self.assertEqual(run_calculator('18', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+40 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_41(self):
        self.assertEqual(run_calculator('18', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+41 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_42(self):
        self.assertEqual(run_calculator('18', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+42 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_43(self):
        self.assertEqual(run_calculator('18', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+43 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_44(self):
        self.assertEqual(run_calculator('18', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+44 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_45(self):
        self.assertEqual(run_calculator('18', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+45 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_46(self):
        self.assertEqual(run_calculator('18', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+46 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_47(self):
        self.assertEqual(run_calculator('18', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+47 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_48(self):
        self.assertEqual(run_calculator('18', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+48 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_49(self):
        self.assertEqual(run_calculator('18', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+49 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_plus_50(self):
        self.assertEqual(run_calculator('18', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18+50 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
