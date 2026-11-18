# test_plus_2.py
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


class TestPlus2(unittest.TestCase):

    def test_2_plus_0(self):
        self.assertEqual(run_calculator('2', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+0 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_1(self):
        self.assertEqual(run_calculator('2', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+1 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_2(self):
        self.assertEqual(run_calculator('2', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+2 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_3(self):
        self.assertEqual(run_calculator('2', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+3 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_4(self):
        self.assertEqual(run_calculator('2', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+4 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_5(self):
        self.assertEqual(run_calculator('2', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+5 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_6(self):
        self.assertEqual(run_calculator('2', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+6 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_7(self):
        self.assertEqual(run_calculator('2', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+7 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_8(self):
        self.assertEqual(run_calculator('2', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+8 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_9(self):
        self.assertEqual(run_calculator('2', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+9 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_10(self):
        self.assertEqual(run_calculator('2', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+10 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_11(self):
        self.assertEqual(run_calculator('2', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+11 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_12(self):
        self.assertEqual(run_calculator('2', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+12 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_13(self):
        self.assertEqual(run_calculator('2', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+13 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_14(self):
        self.assertEqual(run_calculator('2', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+14 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_15(self):
        self.assertEqual(run_calculator('2', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+15 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_16(self):
        self.assertEqual(run_calculator('2', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+16 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_17(self):
        self.assertEqual(run_calculator('2', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+17 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_18(self):
        self.assertEqual(run_calculator('2', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+18 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_19(self):
        self.assertEqual(run_calculator('2', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+19 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_20(self):
        self.assertEqual(run_calculator('2', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+20 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_21(self):
        self.assertEqual(run_calculator('2', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+21 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_22(self):
        self.assertEqual(run_calculator('2', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+22 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_23(self):
        self.assertEqual(run_calculator('2', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+23 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_24(self):
        self.assertEqual(run_calculator('2', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+24 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_25(self):
        self.assertEqual(run_calculator('2', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+25 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_26(self):
        self.assertEqual(run_calculator('2', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+26 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_27(self):
        self.assertEqual(run_calculator('2', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+27 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_28(self):
        self.assertEqual(run_calculator('2', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+28 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_29(self):
        self.assertEqual(run_calculator('2', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+29 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_30(self):
        self.assertEqual(run_calculator('2', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+30 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_31(self):
        self.assertEqual(run_calculator('2', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+31 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_32(self):
        self.assertEqual(run_calculator('2', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+32 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_33(self):
        self.assertEqual(run_calculator('2', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+33 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_34(self):
        self.assertEqual(run_calculator('2', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+34 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_35(self):
        self.assertEqual(run_calculator('2', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+35 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_36(self):
        self.assertEqual(run_calculator('2', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+36 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_37(self):
        self.assertEqual(run_calculator('2', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+37 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_38(self):
        self.assertEqual(run_calculator('2', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+38 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_39(self):
        self.assertEqual(run_calculator('2', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+39 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_40(self):
        self.assertEqual(run_calculator('2', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+40 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_41(self):
        self.assertEqual(run_calculator('2', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+41 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_42(self):
        self.assertEqual(run_calculator('2', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+42 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_43(self):
        self.assertEqual(run_calculator('2', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+43 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_44(self):
        self.assertEqual(run_calculator('2', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+44 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_45(self):
        self.assertEqual(run_calculator('2', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+45 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_46(self):
        self.assertEqual(run_calculator('2', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+46 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_47(self):
        self.assertEqual(run_calculator('2', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+47 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_48(self):
        self.assertEqual(run_calculator('2', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+48 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_49(self):
        self.assertEqual(run_calculator('2', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+49 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_plus_50(self):
        self.assertEqual(run_calculator('2', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2+50 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
