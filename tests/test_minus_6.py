# test_minus_6.py
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


class TestMinus6(unittest.TestCase):

    def test_6_minus_0(self):
        self.assertEqual(run_calculator('6', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-0 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_1(self):
        self.assertEqual(run_calculator('6', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-1 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_2(self):
        self.assertEqual(run_calculator('6', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-2 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_3(self):
        self.assertEqual(run_calculator('6', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-3 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_4(self):
        self.assertEqual(run_calculator('6', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-4 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_5(self):
        self.assertEqual(run_calculator('6', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-5 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_6(self):
        self.assertEqual(run_calculator('6', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-6 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_7(self):
        self.assertEqual(run_calculator('6', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-7 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_8(self):
        self.assertEqual(run_calculator('6', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-8 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_9(self):
        self.assertEqual(run_calculator('6', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-9 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_10(self):
        self.assertEqual(run_calculator('6', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-10 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_11(self):
        self.assertEqual(run_calculator('6', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-11 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_12(self):
        self.assertEqual(run_calculator('6', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-12 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_13(self):
        self.assertEqual(run_calculator('6', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-13 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_14(self):
        self.assertEqual(run_calculator('6', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-14 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_15(self):
        self.assertEqual(run_calculator('6', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-15 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_16(self):
        self.assertEqual(run_calculator('6', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-16 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_17(self):
        self.assertEqual(run_calculator('6', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-17 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_18(self):
        self.assertEqual(run_calculator('6', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-18 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_19(self):
        self.assertEqual(run_calculator('6', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-19 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_20(self):
        self.assertEqual(run_calculator('6', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-20 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_21(self):
        self.assertEqual(run_calculator('6', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-21 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_22(self):
        self.assertEqual(run_calculator('6', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-22 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_23(self):
        self.assertEqual(run_calculator('6', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-23 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_24(self):
        self.assertEqual(run_calculator('6', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-24 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_25(self):
        self.assertEqual(run_calculator('6', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-25 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_26(self):
        self.assertEqual(run_calculator('6', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-26 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_27(self):
        self.assertEqual(run_calculator('6', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-27 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_28(self):
        self.assertEqual(run_calculator('6', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-28 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_29(self):
        self.assertEqual(run_calculator('6', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-29 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_30(self):
        self.assertEqual(run_calculator('6', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-30 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_31(self):
        self.assertEqual(run_calculator('6', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-31 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_32(self):
        self.assertEqual(run_calculator('6', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-32 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_33(self):
        self.assertEqual(run_calculator('6', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-33 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_34(self):
        self.assertEqual(run_calculator('6', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-34 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_35(self):
        self.assertEqual(run_calculator('6', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-35 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_36(self):
        self.assertEqual(run_calculator('6', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-36 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_37(self):
        self.assertEqual(run_calculator('6', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-37 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_38(self):
        self.assertEqual(run_calculator('6', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-38 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_39(self):
        self.assertEqual(run_calculator('6', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-39 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_40(self):
        self.assertEqual(run_calculator('6', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-40 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_41(self):
        self.assertEqual(run_calculator('6', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-41 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_42(self):
        self.assertEqual(run_calculator('6', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-42 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_43(self):
        self.assertEqual(run_calculator('6', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-43 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_44(self):
        self.assertEqual(run_calculator('6', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-44 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_45(self):
        self.assertEqual(run_calculator('6', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-45 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_46(self):
        self.assertEqual(run_calculator('6', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-46 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_47(self):
        self.assertEqual(run_calculator('6', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-47 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_48(self):
        self.assertEqual(run_calculator('6', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-48 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_49(self):
        self.assertEqual(run_calculator('6', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-49 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_minus_50(self):
        self.assertEqual(run_calculator('6', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6-50 = -44',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
