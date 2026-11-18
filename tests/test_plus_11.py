# test_plus_11.py
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


class TestPlus11(unittest.TestCase):

    def test_11_plus_0(self):
        self.assertEqual(run_calculator('11', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+0 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_1(self):
        self.assertEqual(run_calculator('11', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+1 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_2(self):
        self.assertEqual(run_calculator('11', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+2 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_3(self):
        self.assertEqual(run_calculator('11', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+3 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_4(self):
        self.assertEqual(run_calculator('11', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+4 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_5(self):
        self.assertEqual(run_calculator('11', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+5 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_6(self):
        self.assertEqual(run_calculator('11', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+6 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_7(self):
        self.assertEqual(run_calculator('11', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+7 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_8(self):
        self.assertEqual(run_calculator('11', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+8 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_9(self):
        self.assertEqual(run_calculator('11', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+9 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_10(self):
        self.assertEqual(run_calculator('11', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+10 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_11(self):
        self.assertEqual(run_calculator('11', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+11 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_12(self):
        self.assertEqual(run_calculator('11', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+12 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_13(self):
        self.assertEqual(run_calculator('11', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+13 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_14(self):
        self.assertEqual(run_calculator('11', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+14 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_15(self):
        self.assertEqual(run_calculator('11', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+15 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_16(self):
        self.assertEqual(run_calculator('11', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+16 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_17(self):
        self.assertEqual(run_calculator('11', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+17 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_18(self):
        self.assertEqual(run_calculator('11', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+18 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_19(self):
        self.assertEqual(run_calculator('11', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+19 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_20(self):
        self.assertEqual(run_calculator('11', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+20 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_21(self):
        self.assertEqual(run_calculator('11', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+21 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_22(self):
        self.assertEqual(run_calculator('11', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+22 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_23(self):
        self.assertEqual(run_calculator('11', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+23 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_24(self):
        self.assertEqual(run_calculator('11', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+24 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_25(self):
        self.assertEqual(run_calculator('11', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+25 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_26(self):
        self.assertEqual(run_calculator('11', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+26 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_27(self):
        self.assertEqual(run_calculator('11', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+27 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_28(self):
        self.assertEqual(run_calculator('11', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+28 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_29(self):
        self.assertEqual(run_calculator('11', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+29 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_30(self):
        self.assertEqual(run_calculator('11', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+30 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_31(self):
        self.assertEqual(run_calculator('11', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+31 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_32(self):
        self.assertEqual(run_calculator('11', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+32 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_33(self):
        self.assertEqual(run_calculator('11', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+33 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_34(self):
        self.assertEqual(run_calculator('11', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+34 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_35(self):
        self.assertEqual(run_calculator('11', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+35 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_36(self):
        self.assertEqual(run_calculator('11', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+36 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_37(self):
        self.assertEqual(run_calculator('11', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+37 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_38(self):
        self.assertEqual(run_calculator('11', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+38 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_39(self):
        self.assertEqual(run_calculator('11', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+39 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_40(self):
        self.assertEqual(run_calculator('11', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+40 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_41(self):
        self.assertEqual(run_calculator('11', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+41 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_42(self):
        self.assertEqual(run_calculator('11', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+42 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_43(self):
        self.assertEqual(run_calculator('11', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+43 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_44(self):
        self.assertEqual(run_calculator('11', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+44 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_45(self):
        self.assertEqual(run_calculator('11', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+45 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_46(self):
        self.assertEqual(run_calculator('11', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+46 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_47(self):
        self.assertEqual(run_calculator('11', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+47 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_48(self):
        self.assertEqual(run_calculator('11', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+48 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_49(self):
        self.assertEqual(run_calculator('11', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+49 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_plus_50(self):
        self.assertEqual(run_calculator('11', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11+50 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
