# test_plus_19.py
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


class TestPlus19(unittest.TestCase):

    def test_19_plus_0(self):
        self.assertEqual(run_calculator('19', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+0 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_1(self):
        self.assertEqual(run_calculator('19', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+1 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_2(self):
        self.assertEqual(run_calculator('19', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+2 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_3(self):
        self.assertEqual(run_calculator('19', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+3 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_4(self):
        self.assertEqual(run_calculator('19', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+4 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_5(self):
        self.assertEqual(run_calculator('19', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+5 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_6(self):
        self.assertEqual(run_calculator('19', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+6 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_7(self):
        self.assertEqual(run_calculator('19', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+7 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_8(self):
        self.assertEqual(run_calculator('19', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+8 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_9(self):
        self.assertEqual(run_calculator('19', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+9 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_10(self):
        self.assertEqual(run_calculator('19', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+10 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_11(self):
        self.assertEqual(run_calculator('19', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+11 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_12(self):
        self.assertEqual(run_calculator('19', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+12 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_13(self):
        self.assertEqual(run_calculator('19', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+13 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_14(self):
        self.assertEqual(run_calculator('19', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+14 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_15(self):
        self.assertEqual(run_calculator('19', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+15 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_16(self):
        self.assertEqual(run_calculator('19', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+16 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_17(self):
        self.assertEqual(run_calculator('19', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+17 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_18(self):
        self.assertEqual(run_calculator('19', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+18 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_19(self):
        self.assertEqual(run_calculator('19', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+19 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_20(self):
        self.assertEqual(run_calculator('19', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+20 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_21(self):
        self.assertEqual(run_calculator('19', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+21 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_22(self):
        self.assertEqual(run_calculator('19', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+22 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_23(self):
        self.assertEqual(run_calculator('19', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+23 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_24(self):
        self.assertEqual(run_calculator('19', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+24 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_25(self):
        self.assertEqual(run_calculator('19', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+25 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_26(self):
        self.assertEqual(run_calculator('19', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+26 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_27(self):
        self.assertEqual(run_calculator('19', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+27 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_28(self):
        self.assertEqual(run_calculator('19', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+28 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_29(self):
        self.assertEqual(run_calculator('19', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+29 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_30(self):
        self.assertEqual(run_calculator('19', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+30 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_31(self):
        self.assertEqual(run_calculator('19', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+31 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_32(self):
        self.assertEqual(run_calculator('19', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+32 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_33(self):
        self.assertEqual(run_calculator('19', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+33 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_34(self):
        self.assertEqual(run_calculator('19', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+34 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_35(self):
        self.assertEqual(run_calculator('19', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+35 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_36(self):
        self.assertEqual(run_calculator('19', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+36 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_37(self):
        self.assertEqual(run_calculator('19', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+37 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_38(self):
        self.assertEqual(run_calculator('19', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+38 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_39(self):
        self.assertEqual(run_calculator('19', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+39 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_40(self):
        self.assertEqual(run_calculator('19', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+40 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_41(self):
        self.assertEqual(run_calculator('19', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+41 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_42(self):
        self.assertEqual(run_calculator('19', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+42 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_43(self):
        self.assertEqual(run_calculator('19', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+43 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_44(self):
        self.assertEqual(run_calculator('19', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+44 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_45(self):
        self.assertEqual(run_calculator('19', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+45 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_46(self):
        self.assertEqual(run_calculator('19', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+46 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_47(self):
        self.assertEqual(run_calculator('19', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+47 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_48(self):
        self.assertEqual(run_calculator('19', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+48 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_49(self):
        self.assertEqual(run_calculator('19', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+49 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_plus_50(self):
        self.assertEqual(run_calculator('19', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19+50 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
