# test_minus_28.py
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


class TestMinus28(unittest.TestCase):

    def test_28_minus_0(self):
        self.assertEqual(run_calculator('28', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-0 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_1(self):
        self.assertEqual(run_calculator('28', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-1 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_2(self):
        self.assertEqual(run_calculator('28', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-2 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_3(self):
        self.assertEqual(run_calculator('28', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-3 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_4(self):
        self.assertEqual(run_calculator('28', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-4 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_5(self):
        self.assertEqual(run_calculator('28', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-5 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_6(self):
        self.assertEqual(run_calculator('28', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-6 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_7(self):
        self.assertEqual(run_calculator('28', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-7 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_8(self):
        self.assertEqual(run_calculator('28', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-8 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_9(self):
        self.assertEqual(run_calculator('28', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-9 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_10(self):
        self.assertEqual(run_calculator('28', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-10 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_11(self):
        self.assertEqual(run_calculator('28', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-11 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_12(self):
        self.assertEqual(run_calculator('28', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-12 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_13(self):
        self.assertEqual(run_calculator('28', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-13 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_14(self):
        self.assertEqual(run_calculator('28', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-14 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_15(self):
        self.assertEqual(run_calculator('28', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-15 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_16(self):
        self.assertEqual(run_calculator('28', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-16 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_17(self):
        self.assertEqual(run_calculator('28', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-17 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_18(self):
        self.assertEqual(run_calculator('28', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-18 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_19(self):
        self.assertEqual(run_calculator('28', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-19 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_20(self):
        self.assertEqual(run_calculator('28', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-20 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_21(self):
        self.assertEqual(run_calculator('28', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-21 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_22(self):
        self.assertEqual(run_calculator('28', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-22 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_23(self):
        self.assertEqual(run_calculator('28', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-23 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_24(self):
        self.assertEqual(run_calculator('28', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-24 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_25(self):
        self.assertEqual(run_calculator('28', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-25 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_26(self):
        self.assertEqual(run_calculator('28', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-26 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_27(self):
        self.assertEqual(run_calculator('28', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-27 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_28(self):
        self.assertEqual(run_calculator('28', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-28 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_29(self):
        self.assertEqual(run_calculator('28', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-29 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_30(self):
        self.assertEqual(run_calculator('28', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-30 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_31(self):
        self.assertEqual(run_calculator('28', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-31 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_32(self):
        self.assertEqual(run_calculator('28', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-32 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_33(self):
        self.assertEqual(run_calculator('28', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-33 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_34(self):
        self.assertEqual(run_calculator('28', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-34 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_35(self):
        self.assertEqual(run_calculator('28', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-35 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_36(self):
        self.assertEqual(run_calculator('28', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-36 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_37(self):
        self.assertEqual(run_calculator('28', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-37 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_38(self):
        self.assertEqual(run_calculator('28', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-38 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_39(self):
        self.assertEqual(run_calculator('28', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-39 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_40(self):
        self.assertEqual(run_calculator('28', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-40 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_41(self):
        self.assertEqual(run_calculator('28', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-41 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_42(self):
        self.assertEqual(run_calculator('28', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-42 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_43(self):
        self.assertEqual(run_calculator('28', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-43 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_44(self):
        self.assertEqual(run_calculator('28', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-44 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_45(self):
        self.assertEqual(run_calculator('28', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-45 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_46(self):
        self.assertEqual(run_calculator('28', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-46 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_47(self):
        self.assertEqual(run_calculator('28', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-47 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_48(self):
        self.assertEqual(run_calculator('28', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-48 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_49(self):
        self.assertEqual(run_calculator('28', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-49 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_minus_50(self):
        self.assertEqual(run_calculator('28', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28-50 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
