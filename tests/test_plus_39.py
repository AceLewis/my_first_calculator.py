# test_plus_39.py
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


class TestPlus39(unittest.TestCase):

    def test_39_plus_0(self):
        self.assertEqual(run_calculator('39', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+0 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_1(self):
        self.assertEqual(run_calculator('39', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+1 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_2(self):
        self.assertEqual(run_calculator('39', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+2 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_3(self):
        self.assertEqual(run_calculator('39', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+3 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_4(self):
        self.assertEqual(run_calculator('39', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+4 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_5(self):
        self.assertEqual(run_calculator('39', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+5 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_6(self):
        self.assertEqual(run_calculator('39', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+6 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_7(self):
        self.assertEqual(run_calculator('39', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+7 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_8(self):
        self.assertEqual(run_calculator('39', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+8 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_9(self):
        self.assertEqual(run_calculator('39', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+9 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_10(self):
        self.assertEqual(run_calculator('39', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+10 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_11(self):
        self.assertEqual(run_calculator('39', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+11 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_12(self):
        self.assertEqual(run_calculator('39', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+12 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_13(self):
        self.assertEqual(run_calculator('39', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+13 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_14(self):
        self.assertEqual(run_calculator('39', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+14 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_15(self):
        self.assertEqual(run_calculator('39', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+15 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_16(self):
        self.assertEqual(run_calculator('39', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+16 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_17(self):
        self.assertEqual(run_calculator('39', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+17 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_18(self):
        self.assertEqual(run_calculator('39', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+18 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_19(self):
        self.assertEqual(run_calculator('39', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+19 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_20(self):
        self.assertEqual(run_calculator('39', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+20 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_21(self):
        self.assertEqual(run_calculator('39', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+21 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_22(self):
        self.assertEqual(run_calculator('39', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+22 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_23(self):
        self.assertEqual(run_calculator('39', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+23 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_24(self):
        self.assertEqual(run_calculator('39', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+24 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_25(self):
        self.assertEqual(run_calculator('39', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+25 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_26(self):
        self.assertEqual(run_calculator('39', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+26 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_27(self):
        self.assertEqual(run_calculator('39', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+27 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_28(self):
        self.assertEqual(run_calculator('39', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+28 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_29(self):
        self.assertEqual(run_calculator('39', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+29 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_30(self):
        self.assertEqual(run_calculator('39', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+30 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_31(self):
        self.assertEqual(run_calculator('39', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+31 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_32(self):
        self.assertEqual(run_calculator('39', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+32 = 71',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_33(self):
        self.assertEqual(run_calculator('39', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+33 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_34(self):
        self.assertEqual(run_calculator('39', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+34 = 73',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_35(self):
        self.assertEqual(run_calculator('39', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+35 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_36(self):
        self.assertEqual(run_calculator('39', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+36 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_37(self):
        self.assertEqual(run_calculator('39', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+37 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_38(self):
        self.assertEqual(run_calculator('39', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+38 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_39(self):
        self.assertEqual(run_calculator('39', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+39 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_40(self):
        self.assertEqual(run_calculator('39', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+40 = 79',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_41(self):
        self.assertEqual(run_calculator('39', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+41 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_42(self):
        self.assertEqual(run_calculator('39', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+42 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_43(self):
        self.assertEqual(run_calculator('39', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+43 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_44(self):
        self.assertEqual(run_calculator('39', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+44 = 83',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_45(self):
        self.assertEqual(run_calculator('39', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+45 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_46(self):
        self.assertEqual(run_calculator('39', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+46 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_47(self):
        self.assertEqual(run_calculator('39', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+47 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_48(self):
        self.assertEqual(run_calculator('39', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+48 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_49(self):
        self.assertEqual(run_calculator('39', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+49 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_plus_50(self):
        self.assertEqual(run_calculator('39', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39+50 = 89',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
