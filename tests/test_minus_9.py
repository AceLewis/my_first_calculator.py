# test_minus_9.py
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


class TestMinus9(unittest.TestCase):

    def test_9_minus_0(self):
        self.assertEqual(run_calculator('9', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-0 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_1(self):
        self.assertEqual(run_calculator('9', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-1 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_2(self):
        self.assertEqual(run_calculator('9', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-2 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_3(self):
        self.assertEqual(run_calculator('9', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-3 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_4(self):
        self.assertEqual(run_calculator('9', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-4 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_5(self):
        self.assertEqual(run_calculator('9', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-5 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_6(self):
        self.assertEqual(run_calculator('9', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-6 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_7(self):
        self.assertEqual(run_calculator('9', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-7 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_8(self):
        self.assertEqual(run_calculator('9', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-8 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_9(self):
        self.assertEqual(run_calculator('9', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-9 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_10(self):
        self.assertEqual(run_calculator('9', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-10 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_11(self):
        self.assertEqual(run_calculator('9', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-11 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_12(self):
        self.assertEqual(run_calculator('9', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-12 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_13(self):
        self.assertEqual(run_calculator('9', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-13 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_14(self):
        self.assertEqual(run_calculator('9', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-14 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_15(self):
        self.assertEqual(run_calculator('9', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-15 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_16(self):
        self.assertEqual(run_calculator('9', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-16 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_17(self):
        self.assertEqual(run_calculator('9', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-17 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_18(self):
        self.assertEqual(run_calculator('9', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-18 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_19(self):
        self.assertEqual(run_calculator('9', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-19 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_20(self):
        self.assertEqual(run_calculator('9', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-20 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_21(self):
        self.assertEqual(run_calculator('9', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-21 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_22(self):
        self.assertEqual(run_calculator('9', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-22 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_23(self):
        self.assertEqual(run_calculator('9', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-23 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_24(self):
        self.assertEqual(run_calculator('9', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-24 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_25(self):
        self.assertEqual(run_calculator('9', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-25 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_26(self):
        self.assertEqual(run_calculator('9', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-26 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_27(self):
        self.assertEqual(run_calculator('9', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-27 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_28(self):
        self.assertEqual(run_calculator('9', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-28 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_29(self):
        self.assertEqual(run_calculator('9', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-29 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_30(self):
        self.assertEqual(run_calculator('9', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-30 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_31(self):
        self.assertEqual(run_calculator('9', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-31 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_32(self):
        self.assertEqual(run_calculator('9', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-32 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_33(self):
        self.assertEqual(run_calculator('9', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-33 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_34(self):
        self.assertEqual(run_calculator('9', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-34 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_35(self):
        self.assertEqual(run_calculator('9', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-35 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_36(self):
        self.assertEqual(run_calculator('9', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-36 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_37(self):
        self.assertEqual(run_calculator('9', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-37 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_38(self):
        self.assertEqual(run_calculator('9', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-38 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_39(self):
        self.assertEqual(run_calculator('9', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-39 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_40(self):
        self.assertEqual(run_calculator('9', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-40 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_41(self):
        self.assertEqual(run_calculator('9', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-41 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_42(self):
        self.assertEqual(run_calculator('9', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-42 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_43(self):
        self.assertEqual(run_calculator('9', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-43 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_44(self):
        self.assertEqual(run_calculator('9', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-44 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_45(self):
        self.assertEqual(run_calculator('9', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-45 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_46(self):
        self.assertEqual(run_calculator('9', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-46 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_47(self):
        self.assertEqual(run_calculator('9', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-47 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_48(self):
        self.assertEqual(run_calculator('9', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-48 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_49(self):
        self.assertEqual(run_calculator('9', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-49 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_minus_50(self):
        self.assertEqual(run_calculator('9', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9-50 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
