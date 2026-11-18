# test_plus_13.py
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


class TestPlus13(unittest.TestCase):

    def test_13_plus_0(self):
        self.assertEqual(run_calculator('13', '+', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+0 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_1(self):
        self.assertEqual(run_calculator('13', '+', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+1 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_2(self):
        self.assertEqual(run_calculator('13', '+', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+2 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_3(self):
        self.assertEqual(run_calculator('13', '+', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+3 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_4(self):
        self.assertEqual(run_calculator('13', '+', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+4 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_5(self):
        self.assertEqual(run_calculator('13', '+', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+5 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_6(self):
        self.assertEqual(run_calculator('13', '+', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+6 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_7(self):
        self.assertEqual(run_calculator('13', '+', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+7 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_8(self):
        self.assertEqual(run_calculator('13', '+', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+8 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_9(self):
        self.assertEqual(run_calculator('13', '+', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+9 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_10(self):
        self.assertEqual(run_calculator('13', '+', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+10 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_11(self):
        self.assertEqual(run_calculator('13', '+', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+11 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_12(self):
        self.assertEqual(run_calculator('13', '+', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+12 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_13(self):
        self.assertEqual(run_calculator('13', '+', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+13 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_14(self):
        self.assertEqual(run_calculator('13', '+', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+14 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_15(self):
        self.assertEqual(run_calculator('13', '+', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+15 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_16(self):
        self.assertEqual(run_calculator('13', '+', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+16 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_17(self):
        self.assertEqual(run_calculator('13', '+', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+17 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_18(self):
        self.assertEqual(run_calculator('13', '+', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+18 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_19(self):
        self.assertEqual(run_calculator('13', '+', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+19 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_20(self):
        self.assertEqual(run_calculator('13', '+', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+20 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_21(self):
        self.assertEqual(run_calculator('13', '+', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+21 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_22(self):
        self.assertEqual(run_calculator('13', '+', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+22 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_23(self):
        self.assertEqual(run_calculator('13', '+', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+23 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_24(self):
        self.assertEqual(run_calculator('13', '+', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+24 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_25(self):
        self.assertEqual(run_calculator('13', '+', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+25 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_26(self):
        self.assertEqual(run_calculator('13', '+', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+26 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_27(self):
        self.assertEqual(run_calculator('13', '+', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+27 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_28(self):
        self.assertEqual(run_calculator('13', '+', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+28 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_29(self):
        self.assertEqual(run_calculator('13', '+', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+29 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_30(self):
        self.assertEqual(run_calculator('13', '+', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+30 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_31(self):
        self.assertEqual(run_calculator('13', '+', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+31 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_32(self):
        self.assertEqual(run_calculator('13', '+', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+32 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_33(self):
        self.assertEqual(run_calculator('13', '+', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+33 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_34(self):
        self.assertEqual(run_calculator('13', '+', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+34 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_35(self):
        self.assertEqual(run_calculator('13', '+', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+35 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_36(self):
        self.assertEqual(run_calculator('13', '+', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+36 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_37(self):
        self.assertEqual(run_calculator('13', '+', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+37 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_38(self):
        self.assertEqual(run_calculator('13', '+', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+38 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_39(self):
        self.assertEqual(run_calculator('13', '+', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+39 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_40(self):
        self.assertEqual(run_calculator('13', '+', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+40 = 53',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_41(self):
        self.assertEqual(run_calculator('13', '+', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+41 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_42(self):
        self.assertEqual(run_calculator('13', '+', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+42 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_43(self):
        self.assertEqual(run_calculator('13', '+', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+43 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_44(self):
        self.assertEqual(run_calculator('13', '+', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+44 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_45(self):
        self.assertEqual(run_calculator('13', '+', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+45 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_46(self):
        self.assertEqual(run_calculator('13', '+', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+46 = 59',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_47(self):
        self.assertEqual(run_calculator('13', '+', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+47 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_48(self):
        self.assertEqual(run_calculator('13', '+', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+48 = 61',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_49(self):
        self.assertEqual(run_calculator('13', '+', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+49 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_plus_50(self):
        self.assertEqual(run_calculator('13', '+', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13+50 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
