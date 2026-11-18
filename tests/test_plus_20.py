# test_plus_20.py
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


class TestPlus20(unittest.TestCase):

    def test_20_plus_0(self):
        self.assertEqual(run_calculator('20', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+0 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_1(self):
        self.assertEqual(run_calculator('20', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+1 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_2(self):
        self.assertEqual(run_calculator('20', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+2 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_3(self):
        self.assertEqual(run_calculator('20', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+3 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_4(self):
        self.assertEqual(run_calculator('20', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+4 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_5(self):
        self.assertEqual(run_calculator('20', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+5 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_6(self):
        self.assertEqual(run_calculator('20', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+6 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_7(self):
        self.assertEqual(run_calculator('20', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+7 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_8(self):
        self.assertEqual(run_calculator('20', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+8 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_9(self):
        self.assertEqual(run_calculator('20', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+9 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_10(self):
        self.assertEqual(run_calculator('20', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+10 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_11(self):
        self.assertEqual(run_calculator('20', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+11 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_12(self):
        self.assertEqual(run_calculator('20', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+12 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_13(self):
        self.assertEqual(run_calculator('20', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+13 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_14(self):
        self.assertEqual(run_calculator('20', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+14 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_15(self):
        self.assertEqual(run_calculator('20', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+15 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_16(self):
        self.assertEqual(run_calculator('20', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+16 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_17(self):
        self.assertEqual(run_calculator('20', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+17 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_18(self):
        self.assertEqual(run_calculator('20', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+18 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_19(self):
        self.assertEqual(run_calculator('20', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+19 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_20(self):
        self.assertEqual(run_calculator('20', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+20 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_21(self):
        self.assertEqual(run_calculator('20', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+21 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_22(self):
        self.assertEqual(run_calculator('20', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+22 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_23(self):
        self.assertEqual(run_calculator('20', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+23 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_24(self):
        self.assertEqual(run_calculator('20', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+24 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_25(self):
        self.assertEqual(run_calculator('20', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+25 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_26(self):
        self.assertEqual(run_calculator('20', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+26 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_27(self):
        self.assertEqual(run_calculator('20', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+27 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_28(self):
        self.assertEqual(run_calculator('20', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+28 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_29(self):
        self.assertEqual(run_calculator('20', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+29 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_30(self):
        self.assertEqual(run_calculator('20', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+30 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_31(self):
        self.assertEqual(run_calculator('20', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+31 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_32(self):
        self.assertEqual(run_calculator('20', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+32 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_33(self):
        self.assertEqual(run_calculator('20', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+33 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_34(self):
        self.assertEqual(run_calculator('20', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+34 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_35(self):
        self.assertEqual(run_calculator('20', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+35 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_36(self):
        self.assertEqual(run_calculator('20', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+36 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_37(self):
        self.assertEqual(run_calculator('20', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+37 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_38(self):
        self.assertEqual(run_calculator('20', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+38 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_39(self):
        self.assertEqual(run_calculator('20', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+39 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_40(self):
        self.assertEqual(run_calculator('20', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+40 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_41(self):
        self.assertEqual(run_calculator('20', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+41 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_42(self):
        self.assertEqual(run_calculator('20', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+42 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_43(self):
        self.assertEqual(run_calculator('20', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+43 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_44(self):
        self.assertEqual(run_calculator('20', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+44 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_45(self):
        self.assertEqual(run_calculator('20', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+45 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_46(self):
        self.assertEqual(run_calculator('20', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+46 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_47(self):
        self.assertEqual(run_calculator('20', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+47 = 67',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_48(self):
        self.assertEqual(run_calculator('20', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+48 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_49(self):
        self.assertEqual(run_calculator('20', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+49 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_plus_50(self):
        self.assertEqual(run_calculator('20', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20+50 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
