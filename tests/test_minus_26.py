# test_minus_26.py
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


class TestMinus26(unittest.TestCase):

    def test_26_minus_0(self):
        self.assertEqual(run_calculator('26', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-0 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_1(self):
        self.assertEqual(run_calculator('26', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-1 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_2(self):
        self.assertEqual(run_calculator('26', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-2 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_3(self):
        self.assertEqual(run_calculator('26', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-3 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_4(self):
        self.assertEqual(run_calculator('26', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-4 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_5(self):
        self.assertEqual(run_calculator('26', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-5 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_6(self):
        self.assertEqual(run_calculator('26', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-6 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_7(self):
        self.assertEqual(run_calculator('26', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-7 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_8(self):
        self.assertEqual(run_calculator('26', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-8 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_9(self):
        self.assertEqual(run_calculator('26', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-9 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_10(self):
        self.assertEqual(run_calculator('26', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-10 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_11(self):
        self.assertEqual(run_calculator('26', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-11 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_12(self):
        self.assertEqual(run_calculator('26', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-12 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_13(self):
        self.assertEqual(run_calculator('26', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-13 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_14(self):
        self.assertEqual(run_calculator('26', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-14 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_15(self):
        self.assertEqual(run_calculator('26', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-15 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_16(self):
        self.assertEqual(run_calculator('26', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-16 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_17(self):
        self.assertEqual(run_calculator('26', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-17 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_18(self):
        self.assertEqual(run_calculator('26', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-18 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_19(self):
        self.assertEqual(run_calculator('26', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-19 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_20(self):
        self.assertEqual(run_calculator('26', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-20 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_21(self):
        self.assertEqual(run_calculator('26', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-21 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_22(self):
        self.assertEqual(run_calculator('26', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-22 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_23(self):
        self.assertEqual(run_calculator('26', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-23 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_24(self):
        self.assertEqual(run_calculator('26', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-24 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_25(self):
        self.assertEqual(run_calculator('26', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-25 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_26(self):
        self.assertEqual(run_calculator('26', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-26 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_27(self):
        self.assertEqual(run_calculator('26', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-27 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_28(self):
        self.assertEqual(run_calculator('26', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-28 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_29(self):
        self.assertEqual(run_calculator('26', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-29 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_30(self):
        self.assertEqual(run_calculator('26', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-30 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_31(self):
        self.assertEqual(run_calculator('26', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-31 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_32(self):
        self.assertEqual(run_calculator('26', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-32 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_33(self):
        self.assertEqual(run_calculator('26', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-33 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_34(self):
        self.assertEqual(run_calculator('26', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-34 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_35(self):
        self.assertEqual(run_calculator('26', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-35 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_36(self):
        self.assertEqual(run_calculator('26', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-36 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_37(self):
        self.assertEqual(run_calculator('26', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-37 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_38(self):
        self.assertEqual(run_calculator('26', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-38 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_39(self):
        self.assertEqual(run_calculator('26', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-39 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_40(self):
        self.assertEqual(run_calculator('26', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-40 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_41(self):
        self.assertEqual(run_calculator('26', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-41 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_42(self):
        self.assertEqual(run_calculator('26', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-42 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_43(self):
        self.assertEqual(run_calculator('26', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-43 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_44(self):
        self.assertEqual(run_calculator('26', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-44 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_45(self):
        self.assertEqual(run_calculator('26', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-45 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_46(self):
        self.assertEqual(run_calculator('26', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-46 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_47(self):
        self.assertEqual(run_calculator('26', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-47 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_48(self):
        self.assertEqual(run_calculator('26', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-48 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_49(self):
        self.assertEqual(run_calculator('26', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-49 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_minus_50(self):
        self.assertEqual(run_calculator('26', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26-50 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
