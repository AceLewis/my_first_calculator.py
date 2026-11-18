# test_plus_0.py
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


class TestPlus0(unittest.TestCase):

    def test_0_plus_0(self):
        self.assertEqual(run_calculator('0', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_1(self):
        self.assertEqual(run_calculator('0', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+1 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_2(self):
        self.assertEqual(run_calculator('0', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+2 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_3(self):
        self.assertEqual(run_calculator('0', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+3 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_4(self):
        self.assertEqual(run_calculator('0', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+4 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_5(self):
        self.assertEqual(run_calculator('0', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+5 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_6(self):
        self.assertEqual(run_calculator('0', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+6 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_7(self):
        self.assertEqual(run_calculator('0', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+7 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_8(self):
        self.assertEqual(run_calculator('0', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+8 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_9(self):
        self.assertEqual(run_calculator('0', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+9 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_10(self):
        self.assertEqual(run_calculator('0', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+10 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_11(self):
        self.assertEqual(run_calculator('0', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+11 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_12(self):
        self.assertEqual(run_calculator('0', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+12 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_13(self):
        self.assertEqual(run_calculator('0', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+13 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_14(self):
        self.assertEqual(run_calculator('0', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+14 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_15(self):
        self.assertEqual(run_calculator('0', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+15 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_16(self):
        self.assertEqual(run_calculator('0', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+16 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_17(self):
        self.assertEqual(run_calculator('0', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+17 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_18(self):
        self.assertEqual(run_calculator('0', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+18 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_19(self):
        self.assertEqual(run_calculator('0', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+19 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_20(self):
        self.assertEqual(run_calculator('0', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+20 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_21(self):
        self.assertEqual(run_calculator('0', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+21 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_22(self):
        self.assertEqual(run_calculator('0', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+22 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_23(self):
        self.assertEqual(run_calculator('0', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+23 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_24(self):
        self.assertEqual(run_calculator('0', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+24 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_25(self):
        self.assertEqual(run_calculator('0', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+25 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_26(self):
        self.assertEqual(run_calculator('0', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+26 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_27(self):
        self.assertEqual(run_calculator('0', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+27 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_28(self):
        self.assertEqual(run_calculator('0', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+28 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_29(self):
        self.assertEqual(run_calculator('0', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+29 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_30(self):
        self.assertEqual(run_calculator('0', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+30 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_31(self):
        self.assertEqual(run_calculator('0', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+31 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_32(self):
        self.assertEqual(run_calculator('0', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+32 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_33(self):
        self.assertEqual(run_calculator('0', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+33 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_34(self):
        self.assertEqual(run_calculator('0', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+34 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_35(self):
        self.assertEqual(run_calculator('0', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+35 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_36(self):
        self.assertEqual(run_calculator('0', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+36 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_37(self):
        self.assertEqual(run_calculator('0', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+37 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_38(self):
        self.assertEqual(run_calculator('0', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+38 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_39(self):
        self.assertEqual(run_calculator('0', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+39 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_40(self):
        self.assertEqual(run_calculator('0', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+40 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_41(self):
        self.assertEqual(run_calculator('0', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+41 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_42(self):
        self.assertEqual(run_calculator('0', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+42 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_43(self):
        self.assertEqual(run_calculator('0', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+43 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_44(self):
        self.assertEqual(run_calculator('0', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+44 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_45(self):
        self.assertEqual(run_calculator('0', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+45 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_46(self):
        self.assertEqual(run_calculator('0', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+46 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_47(self):
        self.assertEqual(run_calculator('0', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+47 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_48(self):
        self.assertEqual(run_calculator('0', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+48 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_49(self):
        self.assertEqual(run_calculator('0', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+49 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_plus_50(self):
        self.assertEqual(run_calculator('0', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0+50 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
