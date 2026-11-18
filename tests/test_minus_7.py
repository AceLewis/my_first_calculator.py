# test_minus_7.py
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


class TestMinus7(unittest.TestCase):

    def test_7_minus_0(self):
        self.assertEqual(run_calculator('7', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-0 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_1(self):
        self.assertEqual(run_calculator('7', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-1 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_2(self):
        self.assertEqual(run_calculator('7', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-2 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_3(self):
        self.assertEqual(run_calculator('7', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-3 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_4(self):
        self.assertEqual(run_calculator('7', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-4 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_5(self):
        self.assertEqual(run_calculator('7', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-5 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_6(self):
        self.assertEqual(run_calculator('7', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-6 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_7(self):
        self.assertEqual(run_calculator('7', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-7 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_8(self):
        self.assertEqual(run_calculator('7', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-8 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_9(self):
        self.assertEqual(run_calculator('7', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-9 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_10(self):
        self.assertEqual(run_calculator('7', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-10 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_11(self):
        self.assertEqual(run_calculator('7', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-11 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_12(self):
        self.assertEqual(run_calculator('7', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-12 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_13(self):
        self.assertEqual(run_calculator('7', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-13 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_14(self):
        self.assertEqual(run_calculator('7', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-14 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_15(self):
        self.assertEqual(run_calculator('7', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-15 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_16(self):
        self.assertEqual(run_calculator('7', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-16 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_17(self):
        self.assertEqual(run_calculator('7', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-17 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_18(self):
        self.assertEqual(run_calculator('7', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-18 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_19(self):
        self.assertEqual(run_calculator('7', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-19 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_20(self):
        self.assertEqual(run_calculator('7', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-20 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_21(self):
        self.assertEqual(run_calculator('7', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-21 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_22(self):
        self.assertEqual(run_calculator('7', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-22 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_23(self):
        self.assertEqual(run_calculator('7', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-23 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_24(self):
        self.assertEqual(run_calculator('7', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-24 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_25(self):
        self.assertEqual(run_calculator('7', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-25 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_26(self):
        self.assertEqual(run_calculator('7', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-26 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_27(self):
        self.assertEqual(run_calculator('7', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-27 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_28(self):
        self.assertEqual(run_calculator('7', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-28 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_29(self):
        self.assertEqual(run_calculator('7', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-29 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_30(self):
        self.assertEqual(run_calculator('7', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-30 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_31(self):
        self.assertEqual(run_calculator('7', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-31 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_32(self):
        self.assertEqual(run_calculator('7', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-32 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_33(self):
        self.assertEqual(run_calculator('7', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-33 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_34(self):
        self.assertEqual(run_calculator('7', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-34 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_35(self):
        self.assertEqual(run_calculator('7', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-35 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_36(self):
        self.assertEqual(run_calculator('7', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-36 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_37(self):
        self.assertEqual(run_calculator('7', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-37 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_38(self):
        self.assertEqual(run_calculator('7', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-38 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_39(self):
        self.assertEqual(run_calculator('7', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-39 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_40(self):
        self.assertEqual(run_calculator('7', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-40 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_41(self):
        self.assertEqual(run_calculator('7', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-41 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_42(self):
        self.assertEqual(run_calculator('7', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-42 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_43(self):
        self.assertEqual(run_calculator('7', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-43 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_44(self):
        self.assertEqual(run_calculator('7', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-44 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_45(self):
        self.assertEqual(run_calculator('7', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-45 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_46(self):
        self.assertEqual(run_calculator('7', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-46 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_47(self):
        self.assertEqual(run_calculator('7', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-47 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_48(self):
        self.assertEqual(run_calculator('7', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-48 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_49(self):
        self.assertEqual(run_calculator('7', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-49 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_minus_50(self):
        self.assertEqual(run_calculator('7', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7-50 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
