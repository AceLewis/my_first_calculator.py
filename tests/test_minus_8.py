# test_minus_8.py
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


class TestMinus8(unittest.TestCase):

    def test_8_minus_0(self):
        self.assertEqual(run_calculator('8', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-0 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_1(self):
        self.assertEqual(run_calculator('8', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-1 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_2(self):
        self.assertEqual(run_calculator('8', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-2 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_3(self):
        self.assertEqual(run_calculator('8', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-3 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_4(self):
        self.assertEqual(run_calculator('8', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-4 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_5(self):
        self.assertEqual(run_calculator('8', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-5 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_6(self):
        self.assertEqual(run_calculator('8', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-6 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_7(self):
        self.assertEqual(run_calculator('8', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-7 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_8(self):
        self.assertEqual(run_calculator('8', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-8 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_9(self):
        self.assertEqual(run_calculator('8', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-9 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_10(self):
        self.assertEqual(run_calculator('8', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-10 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_11(self):
        self.assertEqual(run_calculator('8', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-11 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_12(self):
        self.assertEqual(run_calculator('8', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-12 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_13(self):
        self.assertEqual(run_calculator('8', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-13 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_14(self):
        self.assertEqual(run_calculator('8', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-14 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_15(self):
        self.assertEqual(run_calculator('8', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-15 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_16(self):
        self.assertEqual(run_calculator('8', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-16 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_17(self):
        self.assertEqual(run_calculator('8', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-17 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_18(self):
        self.assertEqual(run_calculator('8', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-18 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_19(self):
        self.assertEqual(run_calculator('8', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-19 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_20(self):
        self.assertEqual(run_calculator('8', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-20 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_21(self):
        self.assertEqual(run_calculator('8', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-21 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_22(self):
        self.assertEqual(run_calculator('8', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-22 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_23(self):
        self.assertEqual(run_calculator('8', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-23 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_24(self):
        self.assertEqual(run_calculator('8', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-24 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_25(self):
        self.assertEqual(run_calculator('8', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-25 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_26(self):
        self.assertEqual(run_calculator('8', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-26 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_27(self):
        self.assertEqual(run_calculator('8', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-27 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_28(self):
        self.assertEqual(run_calculator('8', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-28 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_29(self):
        self.assertEqual(run_calculator('8', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-29 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_30(self):
        self.assertEqual(run_calculator('8', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-30 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_31(self):
        self.assertEqual(run_calculator('8', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-31 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_32(self):
        self.assertEqual(run_calculator('8', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-32 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_33(self):
        self.assertEqual(run_calculator('8', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-33 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_34(self):
        self.assertEqual(run_calculator('8', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-34 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_35(self):
        self.assertEqual(run_calculator('8', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-35 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_36(self):
        self.assertEqual(run_calculator('8', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-36 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_37(self):
        self.assertEqual(run_calculator('8', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-37 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_38(self):
        self.assertEqual(run_calculator('8', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-38 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_39(self):
        self.assertEqual(run_calculator('8', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-39 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_40(self):
        self.assertEqual(run_calculator('8', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-40 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_41(self):
        self.assertEqual(run_calculator('8', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-41 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_42(self):
        self.assertEqual(run_calculator('8', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-42 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_43(self):
        self.assertEqual(run_calculator('8', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-43 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_44(self):
        self.assertEqual(run_calculator('8', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-44 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_45(self):
        self.assertEqual(run_calculator('8', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-45 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_46(self):
        self.assertEqual(run_calculator('8', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-46 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_47(self):
        self.assertEqual(run_calculator('8', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-47 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_48(self):
        self.assertEqual(run_calculator('8', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-48 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_49(self):
        self.assertEqual(run_calculator('8', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-49 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_minus_50(self):
        self.assertEqual(run_calculator('8', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8-50 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
