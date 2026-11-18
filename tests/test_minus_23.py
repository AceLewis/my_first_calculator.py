# test_minus_23.py
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


class TestMinus23(unittest.TestCase):

    def test_23_minus_0(self):
        self.assertEqual(run_calculator('23', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-0 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_1(self):
        self.assertEqual(run_calculator('23', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-1 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_2(self):
        self.assertEqual(run_calculator('23', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-2 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_3(self):
        self.assertEqual(run_calculator('23', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-3 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_4(self):
        self.assertEqual(run_calculator('23', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-4 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_5(self):
        self.assertEqual(run_calculator('23', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-5 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_6(self):
        self.assertEqual(run_calculator('23', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-6 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_7(self):
        self.assertEqual(run_calculator('23', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-7 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_8(self):
        self.assertEqual(run_calculator('23', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-8 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_9(self):
        self.assertEqual(run_calculator('23', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-9 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_10(self):
        self.assertEqual(run_calculator('23', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-10 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_11(self):
        self.assertEqual(run_calculator('23', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-11 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_12(self):
        self.assertEqual(run_calculator('23', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-12 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_13(self):
        self.assertEqual(run_calculator('23', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-13 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_14(self):
        self.assertEqual(run_calculator('23', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-14 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_15(self):
        self.assertEqual(run_calculator('23', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-15 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_16(self):
        self.assertEqual(run_calculator('23', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-16 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_17(self):
        self.assertEqual(run_calculator('23', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-17 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_18(self):
        self.assertEqual(run_calculator('23', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-18 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_19(self):
        self.assertEqual(run_calculator('23', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-19 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_20(self):
        self.assertEqual(run_calculator('23', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-20 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_21(self):
        self.assertEqual(run_calculator('23', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-21 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_22(self):
        self.assertEqual(run_calculator('23', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-22 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_23(self):
        self.assertEqual(run_calculator('23', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-23 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_24(self):
        self.assertEqual(run_calculator('23', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-24 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_25(self):
        self.assertEqual(run_calculator('23', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-25 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_26(self):
        self.assertEqual(run_calculator('23', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-26 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_27(self):
        self.assertEqual(run_calculator('23', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-27 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_28(self):
        self.assertEqual(run_calculator('23', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-28 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_29(self):
        self.assertEqual(run_calculator('23', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-29 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_30(self):
        self.assertEqual(run_calculator('23', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-30 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_31(self):
        self.assertEqual(run_calculator('23', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-31 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_32(self):
        self.assertEqual(run_calculator('23', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-32 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_33(self):
        self.assertEqual(run_calculator('23', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-33 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_34(self):
        self.assertEqual(run_calculator('23', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-34 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_35(self):
        self.assertEqual(run_calculator('23', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-35 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_36(self):
        self.assertEqual(run_calculator('23', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-36 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_37(self):
        self.assertEqual(run_calculator('23', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-37 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_38(self):
        self.assertEqual(run_calculator('23', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-38 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_39(self):
        self.assertEqual(run_calculator('23', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-39 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_40(self):
        self.assertEqual(run_calculator('23', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-40 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_41(self):
        self.assertEqual(run_calculator('23', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-41 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_42(self):
        self.assertEqual(run_calculator('23', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-42 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_43(self):
        self.assertEqual(run_calculator('23', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-43 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_44(self):
        self.assertEqual(run_calculator('23', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-44 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_45(self):
        self.assertEqual(run_calculator('23', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-45 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_46(self):
        self.assertEqual(run_calculator('23', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-46 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_47(self):
        self.assertEqual(run_calculator('23', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-47 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_48(self):
        self.assertEqual(run_calculator('23', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-48 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_49(self):
        self.assertEqual(run_calculator('23', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-49 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_minus_50(self):
        self.assertEqual(run_calculator('23', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23-50 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
