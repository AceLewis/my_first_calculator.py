# test_plus_1.py
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


class TestPlus1(unittest.TestCase):

    def test_1_plus_0(self):
        self.assertEqual(run_calculator('1', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+0 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_1(self):
        self.assertEqual(run_calculator('1', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+1 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_2(self):
        self.assertEqual(run_calculator('1', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+2 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_3(self):
        self.assertEqual(run_calculator('1', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+3 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_4(self):
        self.assertEqual(run_calculator('1', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+4 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_5(self):
        self.assertEqual(run_calculator('1', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+5 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_6(self):
        self.assertEqual(run_calculator('1', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+6 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_7(self):
        self.assertEqual(run_calculator('1', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+7 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_8(self):
        self.assertEqual(run_calculator('1', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+8 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_9(self):
        self.assertEqual(run_calculator('1', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+9 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_10(self):
        self.assertEqual(run_calculator('1', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+10 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_11(self):
        self.assertEqual(run_calculator('1', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+11 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_12(self):
        self.assertEqual(run_calculator('1', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+12 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_13(self):
        self.assertEqual(run_calculator('1', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+13 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_14(self):
        self.assertEqual(run_calculator('1', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+14 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_15(self):
        self.assertEqual(run_calculator('1', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+15 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_16(self):
        self.assertEqual(run_calculator('1', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+16 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_17(self):
        self.assertEqual(run_calculator('1', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+17 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_18(self):
        self.assertEqual(run_calculator('1', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+18 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_19(self):
        self.assertEqual(run_calculator('1', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+19 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_20(self):
        self.assertEqual(run_calculator('1', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+20 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_21(self):
        self.assertEqual(run_calculator('1', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+21 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_22(self):
        self.assertEqual(run_calculator('1', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+22 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_23(self):
        self.assertEqual(run_calculator('1', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+23 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_24(self):
        self.assertEqual(run_calculator('1', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+24 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_25(self):
        self.assertEqual(run_calculator('1', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+25 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_26(self):
        self.assertEqual(run_calculator('1', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+26 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_27(self):
        self.assertEqual(run_calculator('1', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+27 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_28(self):
        self.assertEqual(run_calculator('1', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+28 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_29(self):
        self.assertEqual(run_calculator('1', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+29 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_30(self):
        self.assertEqual(run_calculator('1', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+30 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_31(self):
        self.assertEqual(run_calculator('1', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+31 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_32(self):
        self.assertEqual(run_calculator('1', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+32 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_33(self):
        self.assertEqual(run_calculator('1', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+33 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_34(self):
        self.assertEqual(run_calculator('1', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+34 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_35(self):
        self.assertEqual(run_calculator('1', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+35 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_36(self):
        self.assertEqual(run_calculator('1', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+36 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_37(self):
        self.assertEqual(run_calculator('1', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+37 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_38(self):
        self.assertEqual(run_calculator('1', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+38 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_39(self):
        self.assertEqual(run_calculator('1', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+39 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_40(self):
        self.assertEqual(run_calculator('1', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+40 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_41(self):
        self.assertEqual(run_calculator('1', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+41 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_42(self):
        self.assertEqual(run_calculator('1', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+42 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_43(self):
        self.assertEqual(run_calculator('1', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+43 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_44(self):
        self.assertEqual(run_calculator('1', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+44 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_45(self):
        self.assertEqual(run_calculator('1', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+45 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_46(self):
        self.assertEqual(run_calculator('1', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+46 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_47(self):
        self.assertEqual(run_calculator('1', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+47 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_48(self):
        self.assertEqual(run_calculator('1', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+48 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_49(self):
        self.assertEqual(run_calculator('1', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+49 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_plus_50(self):
        self.assertEqual(run_calculator('1', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1+50 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
