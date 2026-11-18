# test_minus_18.py
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


class TestMinus18(unittest.TestCase):

    def test_18_minus_0(self):
        self.assertEqual(run_calculator('18', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-0 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_1(self):
        self.assertEqual(run_calculator('18', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-1 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_2(self):
        self.assertEqual(run_calculator('18', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-2 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_3(self):
        self.assertEqual(run_calculator('18', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-3 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_4(self):
        self.assertEqual(run_calculator('18', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-4 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_5(self):
        self.assertEqual(run_calculator('18', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-5 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_6(self):
        self.assertEqual(run_calculator('18', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-6 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_7(self):
        self.assertEqual(run_calculator('18', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-7 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_8(self):
        self.assertEqual(run_calculator('18', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-8 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_9(self):
        self.assertEqual(run_calculator('18', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-9 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_10(self):
        self.assertEqual(run_calculator('18', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-10 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_11(self):
        self.assertEqual(run_calculator('18', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-11 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_12(self):
        self.assertEqual(run_calculator('18', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-12 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_13(self):
        self.assertEqual(run_calculator('18', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-13 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_14(self):
        self.assertEqual(run_calculator('18', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-14 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_15(self):
        self.assertEqual(run_calculator('18', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-15 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_16(self):
        self.assertEqual(run_calculator('18', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-16 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_17(self):
        self.assertEqual(run_calculator('18', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-17 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_18(self):
        self.assertEqual(run_calculator('18', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-18 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_19(self):
        self.assertEqual(run_calculator('18', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-19 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_20(self):
        self.assertEqual(run_calculator('18', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-20 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_21(self):
        self.assertEqual(run_calculator('18', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-21 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_22(self):
        self.assertEqual(run_calculator('18', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-22 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_23(self):
        self.assertEqual(run_calculator('18', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-23 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_24(self):
        self.assertEqual(run_calculator('18', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-24 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_25(self):
        self.assertEqual(run_calculator('18', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-25 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_26(self):
        self.assertEqual(run_calculator('18', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-26 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_27(self):
        self.assertEqual(run_calculator('18', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-27 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_28(self):
        self.assertEqual(run_calculator('18', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-28 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_29(self):
        self.assertEqual(run_calculator('18', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-29 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_30(self):
        self.assertEqual(run_calculator('18', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-30 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_31(self):
        self.assertEqual(run_calculator('18', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-31 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_32(self):
        self.assertEqual(run_calculator('18', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-32 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_33(self):
        self.assertEqual(run_calculator('18', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-33 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_34(self):
        self.assertEqual(run_calculator('18', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-34 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_35(self):
        self.assertEqual(run_calculator('18', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-35 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_36(self):
        self.assertEqual(run_calculator('18', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-36 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_37(self):
        self.assertEqual(run_calculator('18', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-37 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_38(self):
        self.assertEqual(run_calculator('18', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-38 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_39(self):
        self.assertEqual(run_calculator('18', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-39 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_40(self):
        self.assertEqual(run_calculator('18', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-40 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_41(self):
        self.assertEqual(run_calculator('18', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-41 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_42(self):
        self.assertEqual(run_calculator('18', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-42 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_43(self):
        self.assertEqual(run_calculator('18', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-43 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_44(self):
        self.assertEqual(run_calculator('18', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-44 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_45(self):
        self.assertEqual(run_calculator('18', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-45 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_46(self):
        self.assertEqual(run_calculator('18', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-46 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_47(self):
        self.assertEqual(run_calculator('18', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-47 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_48(self):
        self.assertEqual(run_calculator('18', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-48 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_49(self):
        self.assertEqual(run_calculator('18', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-49 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_minus_50(self):
        self.assertEqual(run_calculator('18', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18-50 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
