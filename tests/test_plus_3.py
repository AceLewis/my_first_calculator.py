# test_plus_3.py
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


class TestPlus3(unittest.TestCase):

    def test_3_plus_0(self):
        self.assertEqual(run_calculator('3', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+0 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_1(self):
        self.assertEqual(run_calculator('3', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+1 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_2(self):
        self.assertEqual(run_calculator('3', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+2 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_3(self):
        self.assertEqual(run_calculator('3', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+3 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_4(self):
        self.assertEqual(run_calculator('3', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+4 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_5(self):
        self.assertEqual(run_calculator('3', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+5 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_6(self):
        self.assertEqual(run_calculator('3', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+6 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_7(self):
        self.assertEqual(run_calculator('3', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+7 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_8(self):
        self.assertEqual(run_calculator('3', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+8 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_9(self):
        self.assertEqual(run_calculator('3', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+9 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_10(self):
        self.assertEqual(run_calculator('3', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+10 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_11(self):
        self.assertEqual(run_calculator('3', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+11 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_12(self):
        self.assertEqual(run_calculator('3', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+12 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_13(self):
        self.assertEqual(run_calculator('3', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+13 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_14(self):
        self.assertEqual(run_calculator('3', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+14 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_15(self):
        self.assertEqual(run_calculator('3', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+15 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_16(self):
        self.assertEqual(run_calculator('3', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+16 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_17(self):
        self.assertEqual(run_calculator('3', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+17 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_18(self):
        self.assertEqual(run_calculator('3', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+18 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_19(self):
        self.assertEqual(run_calculator('3', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+19 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_20(self):
        self.assertEqual(run_calculator('3', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+20 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_21(self):
        self.assertEqual(run_calculator('3', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+21 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_22(self):
        self.assertEqual(run_calculator('3', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+22 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_23(self):
        self.assertEqual(run_calculator('3', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+23 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_24(self):
        self.assertEqual(run_calculator('3', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+24 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_25(self):
        self.assertEqual(run_calculator('3', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+25 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_26(self):
        self.assertEqual(run_calculator('3', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+26 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_27(self):
        self.assertEqual(run_calculator('3', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+27 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_28(self):
        self.assertEqual(run_calculator('3', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+28 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_29(self):
        self.assertEqual(run_calculator('3', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+29 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_30(self):
        self.assertEqual(run_calculator('3', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+30 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_31(self):
        self.assertEqual(run_calculator('3', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+31 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_32(self):
        self.assertEqual(run_calculator('3', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+32 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_33(self):
        self.assertEqual(run_calculator('3', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+33 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_34(self):
        self.assertEqual(run_calculator('3', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+34 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_35(self):
        self.assertEqual(run_calculator('3', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+35 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_36(self):
        self.assertEqual(run_calculator('3', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+36 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_37(self):
        self.assertEqual(run_calculator('3', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+37 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_38(self):
        self.assertEqual(run_calculator('3', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+38 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_39(self):
        self.assertEqual(run_calculator('3', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+39 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_40(self):
        self.assertEqual(run_calculator('3', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+40 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_41(self):
        self.assertEqual(run_calculator('3', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+41 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_42(self):
        self.assertEqual(run_calculator('3', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+42 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_43(self):
        self.assertEqual(run_calculator('3', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+43 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_44(self):
        self.assertEqual(run_calculator('3', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+44 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_45(self):
        self.assertEqual(run_calculator('3', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+45 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_46(self):
        self.assertEqual(run_calculator('3', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+46 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_47(self):
        self.assertEqual(run_calculator('3', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+47 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_48(self):
        self.assertEqual(run_calculator('3', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+48 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_49(self):
        self.assertEqual(run_calculator('3', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+49 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_plus_50(self):
        self.assertEqual(run_calculator('3', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3+50 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
