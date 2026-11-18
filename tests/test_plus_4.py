# test_plus_4.py
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


class TestPlus4(unittest.TestCase):

    def test_4_plus_0(self):
        self.assertEqual(run_calculator('4', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+0 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_1(self):
        self.assertEqual(run_calculator('4', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+1 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_2(self):
        self.assertEqual(run_calculator('4', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+2 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_3(self):
        self.assertEqual(run_calculator('4', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+3 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_4(self):
        self.assertEqual(run_calculator('4', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+4 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_5(self):
        self.assertEqual(run_calculator('4', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+5 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_6(self):
        self.assertEqual(run_calculator('4', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+6 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_7(self):
        self.assertEqual(run_calculator('4', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+7 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_8(self):
        self.assertEqual(run_calculator('4', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+8 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_9(self):
        self.assertEqual(run_calculator('4', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+9 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_10(self):
        self.assertEqual(run_calculator('4', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+10 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_11(self):
        self.assertEqual(run_calculator('4', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+11 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_12(self):
        self.assertEqual(run_calculator('4', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+12 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_13(self):
        self.assertEqual(run_calculator('4', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+13 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_14(self):
        self.assertEqual(run_calculator('4', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+14 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_15(self):
        self.assertEqual(run_calculator('4', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+15 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_16(self):
        self.assertEqual(run_calculator('4', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+16 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_17(self):
        self.assertEqual(run_calculator('4', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+17 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_18(self):
        self.assertEqual(run_calculator('4', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+18 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_19(self):
        self.assertEqual(run_calculator('4', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+19 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_20(self):
        self.assertEqual(run_calculator('4', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+20 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_21(self):
        self.assertEqual(run_calculator('4', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+21 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_22(self):
        self.assertEqual(run_calculator('4', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+22 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_23(self):
        self.assertEqual(run_calculator('4', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+23 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_24(self):
        self.assertEqual(run_calculator('4', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+24 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_25(self):
        self.assertEqual(run_calculator('4', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+25 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_26(self):
        self.assertEqual(run_calculator('4', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+26 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_27(self):
        self.assertEqual(run_calculator('4', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+27 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_28(self):
        self.assertEqual(run_calculator('4', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+28 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_29(self):
        self.assertEqual(run_calculator('4', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+29 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_30(self):
        self.assertEqual(run_calculator('4', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+30 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_31(self):
        self.assertEqual(run_calculator('4', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+31 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_32(self):
        self.assertEqual(run_calculator('4', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+32 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_33(self):
        self.assertEqual(run_calculator('4', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+33 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_34(self):
        self.assertEqual(run_calculator('4', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+34 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_35(self):
        self.assertEqual(run_calculator('4', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+35 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_36(self):
        self.assertEqual(run_calculator('4', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+36 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_37(self):
        self.assertEqual(run_calculator('4', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+37 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_38(self):
        self.assertEqual(run_calculator('4', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+38 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_39(self):
        self.assertEqual(run_calculator('4', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+39 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_40(self):
        self.assertEqual(run_calculator('4', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+40 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_41(self):
        self.assertEqual(run_calculator('4', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+41 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_42(self):
        self.assertEqual(run_calculator('4', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+42 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_43(self):
        self.assertEqual(run_calculator('4', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+43 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_44(self):
        self.assertEqual(run_calculator('4', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+44 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_45(self):
        self.assertEqual(run_calculator('4', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+45 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_46(self):
        self.assertEqual(run_calculator('4', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+46 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_47(self):
        self.assertEqual(run_calculator('4', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+47 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_48(self):
        self.assertEqual(run_calculator('4', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+48 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_49(self):
        self.assertEqual(run_calculator('4', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+49 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_plus_50(self):
        self.assertEqual(run_calculator('4', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4+50 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
