# test_minus_10.py
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


class TestMinus10(unittest.TestCase):

    def test_10_minus_0(self):
        self.assertEqual(run_calculator('10', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-0 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_1(self):
        self.assertEqual(run_calculator('10', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-1 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_2(self):
        self.assertEqual(run_calculator('10', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-2 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_3(self):
        self.assertEqual(run_calculator('10', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-3 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_4(self):
        self.assertEqual(run_calculator('10', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-4 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_5(self):
        self.assertEqual(run_calculator('10', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-5 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_6(self):
        self.assertEqual(run_calculator('10', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-6 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_7(self):
        self.assertEqual(run_calculator('10', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-7 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_8(self):
        self.assertEqual(run_calculator('10', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-8 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_9(self):
        self.assertEqual(run_calculator('10', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-9 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_10(self):
        self.assertEqual(run_calculator('10', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-10 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_11(self):
        self.assertEqual(run_calculator('10', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-11 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_12(self):
        self.assertEqual(run_calculator('10', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-12 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_13(self):
        self.assertEqual(run_calculator('10', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-13 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_14(self):
        self.assertEqual(run_calculator('10', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-14 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_15(self):
        self.assertEqual(run_calculator('10', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-15 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_16(self):
        self.assertEqual(run_calculator('10', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-16 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_17(self):
        self.assertEqual(run_calculator('10', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-17 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_18(self):
        self.assertEqual(run_calculator('10', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-18 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_19(self):
        self.assertEqual(run_calculator('10', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-19 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_20(self):
        self.assertEqual(run_calculator('10', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-20 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_21(self):
        self.assertEqual(run_calculator('10', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-21 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_22(self):
        self.assertEqual(run_calculator('10', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-22 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_23(self):
        self.assertEqual(run_calculator('10', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-23 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_24(self):
        self.assertEqual(run_calculator('10', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-24 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_25(self):
        self.assertEqual(run_calculator('10', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-25 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_26(self):
        self.assertEqual(run_calculator('10', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-26 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_27(self):
        self.assertEqual(run_calculator('10', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-27 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_28(self):
        self.assertEqual(run_calculator('10', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-28 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_29(self):
        self.assertEqual(run_calculator('10', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-29 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_30(self):
        self.assertEqual(run_calculator('10', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-30 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_31(self):
        self.assertEqual(run_calculator('10', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-31 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_32(self):
        self.assertEqual(run_calculator('10', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-32 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_33(self):
        self.assertEqual(run_calculator('10', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-33 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_34(self):
        self.assertEqual(run_calculator('10', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-34 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_35(self):
        self.assertEqual(run_calculator('10', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-35 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_36(self):
        self.assertEqual(run_calculator('10', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-36 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_37(self):
        self.assertEqual(run_calculator('10', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-37 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_38(self):
        self.assertEqual(run_calculator('10', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-38 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_39(self):
        self.assertEqual(run_calculator('10', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-39 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_40(self):
        self.assertEqual(run_calculator('10', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-40 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_41(self):
        self.assertEqual(run_calculator('10', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-41 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_42(self):
        self.assertEqual(run_calculator('10', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-42 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_43(self):
        self.assertEqual(run_calculator('10', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-43 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_44(self):
        self.assertEqual(run_calculator('10', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-44 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_45(self):
        self.assertEqual(run_calculator('10', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-45 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_46(self):
        self.assertEqual(run_calculator('10', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-46 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_47(self):
        self.assertEqual(run_calculator('10', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-47 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_48(self):
        self.assertEqual(run_calculator('10', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-48 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_49(self):
        self.assertEqual(run_calculator('10', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-49 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_minus_50(self):
        self.assertEqual(run_calculator('10', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10-50 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
