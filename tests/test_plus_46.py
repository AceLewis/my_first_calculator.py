# test_plus_46.py
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


class TestPlus46(unittest.TestCase):

    def test_46_plus_0(self):
        self.assertEqual(run_calculator('46', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+0 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_1(self):
        self.assertEqual(run_calculator('46', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+1 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_2(self):
        self.assertEqual(run_calculator('46', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+2 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_3(self):
        self.assertEqual(run_calculator('46', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+3 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_4(self):
        self.assertEqual(run_calculator('46', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+4 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_5(self):
        self.assertEqual(run_calculator('46', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+5 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_6(self):
        self.assertEqual(run_calculator('46', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+6 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_7(self):
        self.assertEqual(run_calculator('46', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+7 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_8(self):
        self.assertEqual(run_calculator('46', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+8 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_9(self):
        self.assertEqual(run_calculator('46', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+9 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_10(self):
        self.assertEqual(run_calculator('46', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+10 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_11(self):
        self.assertEqual(run_calculator('46', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+11 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_12(self):
        self.assertEqual(run_calculator('46', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+12 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_13(self):
        self.assertEqual(run_calculator('46', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+13 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_14(self):
        self.assertEqual(run_calculator('46', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+14 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_15(self):
        self.assertEqual(run_calculator('46', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+15 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_16(self):
        self.assertEqual(run_calculator('46', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+16 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_17(self):
        self.assertEqual(run_calculator('46', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+17 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_18(self):
        self.assertEqual(run_calculator('46', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+18 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_19(self):
        self.assertEqual(run_calculator('46', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+19 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_20(self):
        self.assertEqual(run_calculator('46', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+20 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_21(self):
        self.assertEqual(run_calculator('46', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+21 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_22(self):
        self.assertEqual(run_calculator('46', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+22 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_23(self):
        self.assertEqual(run_calculator('46', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+23 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_24(self):
        self.assertEqual(run_calculator('46', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+24 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_25(self):
        self.assertEqual(run_calculator('46', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+25 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_26(self):
        self.assertEqual(run_calculator('46', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+26 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_27(self):
        self.assertEqual(run_calculator('46', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+27 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_28(self):
        self.assertEqual(run_calculator('46', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+28 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_29(self):
        self.assertEqual(run_calculator('46', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+29 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_30(self):
        self.assertEqual(run_calculator('46', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+30 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_31(self):
        self.assertEqual(run_calculator('46', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+31 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_32(self):
        self.assertEqual(run_calculator('46', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+32 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_33(self):
        self.assertEqual(run_calculator('46', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+33 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_34(self):
        self.assertEqual(run_calculator('46', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+34 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_35(self):
        self.assertEqual(run_calculator('46', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+35 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_36(self):
        self.assertEqual(run_calculator('46', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+36 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_37(self):
        self.assertEqual(run_calculator('46', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+37 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_38(self):
        self.assertEqual(run_calculator('46', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+38 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_39(self):
        self.assertEqual(run_calculator('46', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+39 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_40(self):
        self.assertEqual(run_calculator('46', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+40 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_41(self):
        self.assertEqual(run_calculator('46', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+41 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_42(self):
        self.assertEqual(run_calculator('46', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+42 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_43(self):
        self.assertEqual(run_calculator('46', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+43 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_44(self):
        self.assertEqual(run_calculator('46', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+44 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_45(self):
        self.assertEqual(run_calculator('46', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+45 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_46(self):
        self.assertEqual(run_calculator('46', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+46 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_47(self):
        self.assertEqual(run_calculator('46', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+47 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_48(self):
        self.assertEqual(run_calculator('46', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+48 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_49(self):
        self.assertEqual(run_calculator('46', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+49 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_plus_50(self):
        self.assertEqual(run_calculator('46', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46+50 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
