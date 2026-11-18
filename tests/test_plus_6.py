# test_plus_6.py
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


class TestPlus6(unittest.TestCase):

    def test_6_plus_0(self):
        self.assertEqual(run_calculator('6', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+0 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_1(self):
        self.assertEqual(run_calculator('6', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+1 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_2(self):
        self.assertEqual(run_calculator('6', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+2 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_3(self):
        self.assertEqual(run_calculator('6', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+3 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_4(self):
        self.assertEqual(run_calculator('6', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+4 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_5(self):
        self.assertEqual(run_calculator('6', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+5 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_6(self):
        self.assertEqual(run_calculator('6', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+6 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_7(self):
        self.assertEqual(run_calculator('6', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+7 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_8(self):
        self.assertEqual(run_calculator('6', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+8 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_9(self):
        self.assertEqual(run_calculator('6', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+9 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_10(self):
        self.assertEqual(run_calculator('6', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+10 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_11(self):
        self.assertEqual(run_calculator('6', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+11 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_12(self):
        self.assertEqual(run_calculator('6', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+12 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_13(self):
        self.assertEqual(run_calculator('6', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+13 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_14(self):
        self.assertEqual(run_calculator('6', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+14 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_15(self):
        self.assertEqual(run_calculator('6', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+15 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_16(self):
        self.assertEqual(run_calculator('6', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+16 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_17(self):
        self.assertEqual(run_calculator('6', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+17 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_18(self):
        self.assertEqual(run_calculator('6', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+18 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_19(self):
        self.assertEqual(run_calculator('6', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+19 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_20(self):
        self.assertEqual(run_calculator('6', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+20 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_21(self):
        self.assertEqual(run_calculator('6', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+21 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_22(self):
        self.assertEqual(run_calculator('6', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+22 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_23(self):
        self.assertEqual(run_calculator('6', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+23 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_24(self):
        self.assertEqual(run_calculator('6', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+24 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_25(self):
        self.assertEqual(run_calculator('6', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+25 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_26(self):
        self.assertEqual(run_calculator('6', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+26 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_27(self):
        self.assertEqual(run_calculator('6', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+27 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_28(self):
        self.assertEqual(run_calculator('6', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+28 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_29(self):
        self.assertEqual(run_calculator('6', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+29 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_30(self):
        self.assertEqual(run_calculator('6', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+30 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_31(self):
        self.assertEqual(run_calculator('6', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+31 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_32(self):
        self.assertEqual(run_calculator('6', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+32 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_33(self):
        self.assertEqual(run_calculator('6', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+33 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_34(self):
        self.assertEqual(run_calculator('6', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+34 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_35(self):
        self.assertEqual(run_calculator('6', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+35 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_36(self):
        self.assertEqual(run_calculator('6', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+36 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_37(self):
        self.assertEqual(run_calculator('6', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+37 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_38(self):
        self.assertEqual(run_calculator('6', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+38 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_39(self):
        self.assertEqual(run_calculator('6', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+39 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_40(self):
        self.assertEqual(run_calculator('6', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+40 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_41(self):
        self.assertEqual(run_calculator('6', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+41 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_42(self):
        self.assertEqual(run_calculator('6', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+42 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_43(self):
        self.assertEqual(run_calculator('6', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+43 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_44(self):
        self.assertEqual(run_calculator('6', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+44 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_45(self):
        self.assertEqual(run_calculator('6', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+45 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_46(self):
        self.assertEqual(run_calculator('6', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+46 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_47(self):
        self.assertEqual(run_calculator('6', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+47 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_48(self):
        self.assertEqual(run_calculator('6', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+48 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_49(self):
        self.assertEqual(run_calculator('6', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+49 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_plus_50(self):
        self.assertEqual(run_calculator('6', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6+50 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
