# test_minus_41.py
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


class TestMinus41(unittest.TestCase):

    def test_41_minus_0(self):
        self.assertEqual(run_calculator('41', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-0 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_1(self):
        self.assertEqual(run_calculator('41', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-1 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_2(self):
        self.assertEqual(run_calculator('41', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-2 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_3(self):
        self.assertEqual(run_calculator('41', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-3 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_4(self):
        self.assertEqual(run_calculator('41', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-4 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_5(self):
        self.assertEqual(run_calculator('41', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-5 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_6(self):
        self.assertEqual(run_calculator('41', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-6 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_7(self):
        self.assertEqual(run_calculator('41', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-7 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_8(self):
        self.assertEqual(run_calculator('41', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-8 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_9(self):
        self.assertEqual(run_calculator('41', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-9 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_10(self):
        self.assertEqual(run_calculator('41', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-10 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_11(self):
        self.assertEqual(run_calculator('41', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-11 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_12(self):
        self.assertEqual(run_calculator('41', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-12 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_13(self):
        self.assertEqual(run_calculator('41', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-13 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_14(self):
        self.assertEqual(run_calculator('41', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-14 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_15(self):
        self.assertEqual(run_calculator('41', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-15 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_16(self):
        self.assertEqual(run_calculator('41', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-16 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_17(self):
        self.assertEqual(run_calculator('41', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-17 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_18(self):
        self.assertEqual(run_calculator('41', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-18 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_19(self):
        self.assertEqual(run_calculator('41', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-19 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_20(self):
        self.assertEqual(run_calculator('41', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-20 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_21(self):
        self.assertEqual(run_calculator('41', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-21 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_22(self):
        self.assertEqual(run_calculator('41', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-22 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_23(self):
        self.assertEqual(run_calculator('41', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-23 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_24(self):
        self.assertEqual(run_calculator('41', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-24 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_25(self):
        self.assertEqual(run_calculator('41', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-25 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_26(self):
        self.assertEqual(run_calculator('41', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-26 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_27(self):
        self.assertEqual(run_calculator('41', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-27 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_28(self):
        self.assertEqual(run_calculator('41', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-28 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_29(self):
        self.assertEqual(run_calculator('41', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-29 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_30(self):
        self.assertEqual(run_calculator('41', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-30 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_31(self):
        self.assertEqual(run_calculator('41', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-31 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_32(self):
        self.assertEqual(run_calculator('41', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-32 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_33(self):
        self.assertEqual(run_calculator('41', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-33 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_34(self):
        self.assertEqual(run_calculator('41', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-34 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_35(self):
        self.assertEqual(run_calculator('41', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-35 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_36(self):
        self.assertEqual(run_calculator('41', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-36 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_37(self):
        self.assertEqual(run_calculator('41', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-37 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_38(self):
        self.assertEqual(run_calculator('41', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-38 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_39(self):
        self.assertEqual(run_calculator('41', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-39 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_40(self):
        self.assertEqual(run_calculator('41', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-40 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_41(self):
        self.assertEqual(run_calculator('41', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-41 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_42(self):
        self.assertEqual(run_calculator('41', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-42 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_43(self):
        self.assertEqual(run_calculator('41', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-43 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_44(self):
        self.assertEqual(run_calculator('41', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-44 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_45(self):
        self.assertEqual(run_calculator('41', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-45 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_46(self):
        self.assertEqual(run_calculator('41', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-46 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_47(self):
        self.assertEqual(run_calculator('41', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-47 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_48(self):
        self.assertEqual(run_calculator('41', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-48 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_49(self):
        self.assertEqual(run_calculator('41', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-49 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_minus_50(self):
        self.assertEqual(run_calculator('41', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41-50 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
