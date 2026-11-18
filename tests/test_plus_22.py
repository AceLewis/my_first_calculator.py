# test_plus_22.py
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


class TestPlus22(unittest.TestCase):

    def test_22_plus_0(self):
        self.assertEqual(run_calculator('22', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+0 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_1(self):
        self.assertEqual(run_calculator('22', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+1 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_2(self):
        self.assertEqual(run_calculator('22', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+2 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_3(self):
        self.assertEqual(run_calculator('22', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+3 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_4(self):
        self.assertEqual(run_calculator('22', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+4 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_5(self):
        self.assertEqual(run_calculator('22', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+5 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_6(self):
        self.assertEqual(run_calculator('22', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+6 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_7(self):
        self.assertEqual(run_calculator('22', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+7 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_8(self):
        self.assertEqual(run_calculator('22', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+8 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_9(self):
        self.assertEqual(run_calculator('22', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+9 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_10(self):
        self.assertEqual(run_calculator('22', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+10 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_11(self):
        self.assertEqual(run_calculator('22', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+11 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_12(self):
        self.assertEqual(run_calculator('22', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+12 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_13(self):
        self.assertEqual(run_calculator('22', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+13 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_14(self):
        self.assertEqual(run_calculator('22', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+14 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_15(self):
        self.assertEqual(run_calculator('22', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+15 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_16(self):
        self.assertEqual(run_calculator('22', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+16 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_17(self):
        self.assertEqual(run_calculator('22', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+17 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_18(self):
        self.assertEqual(run_calculator('22', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+18 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_19(self):
        self.assertEqual(run_calculator('22', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+19 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_20(self):
        self.assertEqual(run_calculator('22', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+20 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_21(self):
        self.assertEqual(run_calculator('22', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+21 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_22(self):
        self.assertEqual(run_calculator('22', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+22 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_23(self):
        self.assertEqual(run_calculator('22', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+23 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_24(self):
        self.assertEqual(run_calculator('22', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+24 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_25(self):
        self.assertEqual(run_calculator('22', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+25 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_26(self):
        self.assertEqual(run_calculator('22', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+26 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_27(self):
        self.assertEqual(run_calculator('22', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+27 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_28(self):
        self.assertEqual(run_calculator('22', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+28 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_29(self):
        self.assertEqual(run_calculator('22', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+29 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_30(self):
        self.assertEqual(run_calculator('22', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+30 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_31(self):
        self.assertEqual(run_calculator('22', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+31 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_32(self):
        self.assertEqual(run_calculator('22', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+32 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_33(self):
        self.assertEqual(run_calculator('22', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+33 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_34(self):
        self.assertEqual(run_calculator('22', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+34 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_35(self):
        self.assertEqual(run_calculator('22', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+35 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_36(self):
        self.assertEqual(run_calculator('22', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+36 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_37(self):
        self.assertEqual(run_calculator('22', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+37 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_38(self):
        self.assertEqual(run_calculator('22', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+38 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_39(self):
        self.assertEqual(run_calculator('22', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+39 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_40(self):
        self.assertEqual(run_calculator('22', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+40 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_41(self):
        self.assertEqual(run_calculator('22', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+41 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_42(self):
        self.assertEqual(run_calculator('22', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+42 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_43(self):
        self.assertEqual(run_calculator('22', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+43 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_44(self):
        self.assertEqual(run_calculator('22', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+44 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_45(self):
        self.assertEqual(run_calculator('22', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+45 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_46(self):
        self.assertEqual(run_calculator('22', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+46 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_47(self):
        self.assertEqual(run_calculator('22', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+47 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_48(self):
        self.assertEqual(run_calculator('22', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+48 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_49(self):
        self.assertEqual(run_calculator('22', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+49 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_plus_50(self):
        self.assertEqual(run_calculator('22', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22+50 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
