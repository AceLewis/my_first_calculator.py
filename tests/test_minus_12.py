# test_minus_12.py
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


class TestMinus12(unittest.TestCase):

    def test_12_minus_0(self):
        self.assertEqual(run_calculator('12', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-0 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_1(self):
        self.assertEqual(run_calculator('12', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-1 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_2(self):
        self.assertEqual(run_calculator('12', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-2 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_3(self):
        self.assertEqual(run_calculator('12', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-3 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_4(self):
        self.assertEqual(run_calculator('12', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-4 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_5(self):
        self.assertEqual(run_calculator('12', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-5 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_6(self):
        self.assertEqual(run_calculator('12', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-6 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_7(self):
        self.assertEqual(run_calculator('12', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-7 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_8(self):
        self.assertEqual(run_calculator('12', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-8 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_9(self):
        self.assertEqual(run_calculator('12', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-9 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_10(self):
        self.assertEqual(run_calculator('12', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-10 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_11(self):
        self.assertEqual(run_calculator('12', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-11 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_12(self):
        self.assertEqual(run_calculator('12', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-12 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_13(self):
        self.assertEqual(run_calculator('12', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-13 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_14(self):
        self.assertEqual(run_calculator('12', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-14 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_15(self):
        self.assertEqual(run_calculator('12', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-15 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_16(self):
        self.assertEqual(run_calculator('12', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-16 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_17(self):
        self.assertEqual(run_calculator('12', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-17 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_18(self):
        self.assertEqual(run_calculator('12', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-18 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_19(self):
        self.assertEqual(run_calculator('12', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-19 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_20(self):
        self.assertEqual(run_calculator('12', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-20 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_21(self):
        self.assertEqual(run_calculator('12', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-21 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_22(self):
        self.assertEqual(run_calculator('12', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-22 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_23(self):
        self.assertEqual(run_calculator('12', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-23 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_24(self):
        self.assertEqual(run_calculator('12', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-24 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_25(self):
        self.assertEqual(run_calculator('12', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-25 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_26(self):
        self.assertEqual(run_calculator('12', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-26 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_27(self):
        self.assertEqual(run_calculator('12', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-27 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_28(self):
        self.assertEqual(run_calculator('12', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-28 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_29(self):
        self.assertEqual(run_calculator('12', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-29 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_30(self):
        self.assertEqual(run_calculator('12', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-30 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_31(self):
        self.assertEqual(run_calculator('12', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-31 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_32(self):
        self.assertEqual(run_calculator('12', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-32 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_33(self):
        self.assertEqual(run_calculator('12', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-33 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_34(self):
        self.assertEqual(run_calculator('12', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-34 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_35(self):
        self.assertEqual(run_calculator('12', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-35 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_36(self):
        self.assertEqual(run_calculator('12', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-36 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_37(self):
        self.assertEqual(run_calculator('12', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-37 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_38(self):
        self.assertEqual(run_calculator('12', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-38 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_39(self):
        self.assertEqual(run_calculator('12', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-39 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_40(self):
        self.assertEqual(run_calculator('12', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-40 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_41(self):
        self.assertEqual(run_calculator('12', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-41 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_42(self):
        self.assertEqual(run_calculator('12', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-42 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_43(self):
        self.assertEqual(run_calculator('12', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-43 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_44(self):
        self.assertEqual(run_calculator('12', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-44 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_45(self):
        self.assertEqual(run_calculator('12', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-45 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_46(self):
        self.assertEqual(run_calculator('12', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-46 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_47(self):
        self.assertEqual(run_calculator('12', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-47 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_48(self):
        self.assertEqual(run_calculator('12', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-48 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_49(self):
        self.assertEqual(run_calculator('12', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-49 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_minus_50(self):
        self.assertEqual(run_calculator('12', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12-50 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
