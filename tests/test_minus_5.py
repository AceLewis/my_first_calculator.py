# test_minus_5.py
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


class TestMinus5(unittest.TestCase):

    def test_5_minus_0(self):
        self.assertEqual(run_calculator('5', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-0 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_1(self):
        self.assertEqual(run_calculator('5', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-1 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_2(self):
        self.assertEqual(run_calculator('5', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-2 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_3(self):
        self.assertEqual(run_calculator('5', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-3 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_4(self):
        self.assertEqual(run_calculator('5', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-4 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_5(self):
        self.assertEqual(run_calculator('5', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-5 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_6(self):
        self.assertEqual(run_calculator('5', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-6 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_7(self):
        self.assertEqual(run_calculator('5', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-7 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_8(self):
        self.assertEqual(run_calculator('5', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-8 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_9(self):
        self.assertEqual(run_calculator('5', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-9 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_10(self):
        self.assertEqual(run_calculator('5', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-10 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_11(self):
        self.assertEqual(run_calculator('5', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-11 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_12(self):
        self.assertEqual(run_calculator('5', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-12 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_13(self):
        self.assertEqual(run_calculator('5', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-13 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_14(self):
        self.assertEqual(run_calculator('5', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-14 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_15(self):
        self.assertEqual(run_calculator('5', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-15 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_16(self):
        self.assertEqual(run_calculator('5', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-16 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_17(self):
        self.assertEqual(run_calculator('5', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-17 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_18(self):
        self.assertEqual(run_calculator('5', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-18 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_19(self):
        self.assertEqual(run_calculator('5', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-19 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_20(self):
        self.assertEqual(run_calculator('5', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-20 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_21(self):
        self.assertEqual(run_calculator('5', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-21 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_22(self):
        self.assertEqual(run_calculator('5', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-22 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_23(self):
        self.assertEqual(run_calculator('5', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-23 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_24(self):
        self.assertEqual(run_calculator('5', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-24 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_25(self):
        self.assertEqual(run_calculator('5', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-25 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_26(self):
        self.assertEqual(run_calculator('5', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-26 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_27(self):
        self.assertEqual(run_calculator('5', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-27 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_28(self):
        self.assertEqual(run_calculator('5', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-28 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_29(self):
        self.assertEqual(run_calculator('5', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-29 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_30(self):
        self.assertEqual(run_calculator('5', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-30 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_31(self):
        self.assertEqual(run_calculator('5', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-31 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_32(self):
        self.assertEqual(run_calculator('5', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-32 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_33(self):
        self.assertEqual(run_calculator('5', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-33 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_34(self):
        self.assertEqual(run_calculator('5', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-34 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_35(self):
        self.assertEqual(run_calculator('5', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-35 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_36(self):
        self.assertEqual(run_calculator('5', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-36 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_37(self):
        self.assertEqual(run_calculator('5', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-37 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_38(self):
        self.assertEqual(run_calculator('5', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-38 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_39(self):
        self.assertEqual(run_calculator('5', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-39 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_40(self):
        self.assertEqual(run_calculator('5', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-40 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_41(self):
        self.assertEqual(run_calculator('5', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-41 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_42(self):
        self.assertEqual(run_calculator('5', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-42 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_43(self):
        self.assertEqual(run_calculator('5', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-43 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_44(self):
        self.assertEqual(run_calculator('5', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-44 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_45(self):
        self.assertEqual(run_calculator('5', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-45 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_46(self):
        self.assertEqual(run_calculator('5', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-46 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_47(self):
        self.assertEqual(run_calculator('5', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-47 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_48(self):
        self.assertEqual(run_calculator('5', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-48 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_49(self):
        self.assertEqual(run_calculator('5', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-49 = -44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_minus_50(self):
        self.assertEqual(run_calculator('5', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5-50 = -45',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
