# test_plus_49.py
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


class TestPlus49(unittest.TestCase):

    def test_49_plus_0(self):
        self.assertEqual(run_calculator('49', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+0 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_1(self):
        self.assertEqual(run_calculator('49', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+1 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_2(self):
        self.assertEqual(run_calculator('49', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+2 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_3(self):
        self.assertEqual(run_calculator('49', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+3 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_4(self):
        self.assertEqual(run_calculator('49', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+4 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_5(self):
        self.assertEqual(run_calculator('49', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+5 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_6(self):
        self.assertEqual(run_calculator('49', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+6 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_7(self):
        self.assertEqual(run_calculator('49', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+7 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_8(self):
        self.assertEqual(run_calculator('49', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+8 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_9(self):
        self.assertEqual(run_calculator('49', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+9 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_10(self):
        self.assertEqual(run_calculator('49', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+10 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_11(self):
        self.assertEqual(run_calculator('49', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+11 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_12(self):
        self.assertEqual(run_calculator('49', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+12 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_13(self):
        self.assertEqual(run_calculator('49', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+13 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_14(self):
        self.assertEqual(run_calculator('49', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+14 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_15(self):
        self.assertEqual(run_calculator('49', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+15 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_16(self):
        self.assertEqual(run_calculator('49', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+16 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_17(self):
        self.assertEqual(run_calculator('49', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+17 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_18(self):
        self.assertEqual(run_calculator('49', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+18 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_19(self):
        self.assertEqual(run_calculator('49', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+19 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_20(self):
        self.assertEqual(run_calculator('49', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+20 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_21(self):
        self.assertEqual(run_calculator('49', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+21 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_22(self):
        self.assertEqual(run_calculator('49', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+22 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_23(self):
        self.assertEqual(run_calculator('49', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+23 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_24(self):
        self.assertEqual(run_calculator('49', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+24 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_25(self):
        self.assertEqual(run_calculator('49', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+25 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_26(self):
        self.assertEqual(run_calculator('49', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+26 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_27(self):
        self.assertEqual(run_calculator('49', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+27 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_28(self):
        self.assertEqual(run_calculator('49', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+28 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_29(self):
        self.assertEqual(run_calculator('49', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+29 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_30(self):
        self.assertEqual(run_calculator('49', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+30 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_31(self):
        self.assertEqual(run_calculator('49', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+31 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_32(self):
        self.assertEqual(run_calculator('49', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+32 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_33(self):
        self.assertEqual(run_calculator('49', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+33 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_34(self):
        self.assertEqual(run_calculator('49', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+34 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_35(self):
        self.assertEqual(run_calculator('49', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+35 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_36(self):
        self.assertEqual(run_calculator('49', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+36 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_37(self):
        self.assertEqual(run_calculator('49', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+37 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_38(self):
        self.assertEqual(run_calculator('49', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+38 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_39(self):
        self.assertEqual(run_calculator('49', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+39 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_40(self):
        self.assertEqual(run_calculator('49', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+40 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_41(self):
        self.assertEqual(run_calculator('49', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+41 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_42(self):
        self.assertEqual(run_calculator('49', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+42 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_43(self):
        self.assertEqual(run_calculator('49', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+43 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_44(self):
        self.assertEqual(run_calculator('49', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+44 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_45(self):
        self.assertEqual(run_calculator('49', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+45 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_46(self):
        self.assertEqual(run_calculator('49', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+46 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_47(self):
        self.assertEqual(run_calculator('49', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+47 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_48(self):
        self.assertEqual(run_calculator('49', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+48 = 97',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_49(self):
        self.assertEqual(run_calculator('49', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+49 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_plus_50(self):
        self.assertEqual(run_calculator('49', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49+50 = 99',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
