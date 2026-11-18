# test_minus_47.py
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


class TestMinus47(unittest.TestCase):

    def test_47_minus_0(self):
        self.assertEqual(run_calculator('47', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-0 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_1(self):
        self.assertEqual(run_calculator('47', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-1 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_2(self):
        self.assertEqual(run_calculator('47', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-2 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_3(self):
        self.assertEqual(run_calculator('47', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-3 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_4(self):
        self.assertEqual(run_calculator('47', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-4 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_5(self):
        self.assertEqual(run_calculator('47', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-5 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_6(self):
        self.assertEqual(run_calculator('47', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-6 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_7(self):
        self.assertEqual(run_calculator('47', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-7 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_8(self):
        self.assertEqual(run_calculator('47', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-8 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_9(self):
        self.assertEqual(run_calculator('47', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-9 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_10(self):
        self.assertEqual(run_calculator('47', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-10 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_11(self):
        self.assertEqual(run_calculator('47', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-11 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_12(self):
        self.assertEqual(run_calculator('47', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-12 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_13(self):
        self.assertEqual(run_calculator('47', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-13 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_14(self):
        self.assertEqual(run_calculator('47', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-14 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_15(self):
        self.assertEqual(run_calculator('47', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-15 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_16(self):
        self.assertEqual(run_calculator('47', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-16 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_17(self):
        self.assertEqual(run_calculator('47', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-17 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_18(self):
        self.assertEqual(run_calculator('47', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-18 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_19(self):
        self.assertEqual(run_calculator('47', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-19 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_20(self):
        self.assertEqual(run_calculator('47', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-20 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_21(self):
        self.assertEqual(run_calculator('47', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-21 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_22(self):
        self.assertEqual(run_calculator('47', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-22 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_23(self):
        self.assertEqual(run_calculator('47', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-23 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_24(self):
        self.assertEqual(run_calculator('47', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-24 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_25(self):
        self.assertEqual(run_calculator('47', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-25 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_26(self):
        self.assertEqual(run_calculator('47', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-26 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_27(self):
        self.assertEqual(run_calculator('47', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-27 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_28(self):
        self.assertEqual(run_calculator('47', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-28 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_29(self):
        self.assertEqual(run_calculator('47', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-29 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_30(self):
        self.assertEqual(run_calculator('47', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-30 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_31(self):
        self.assertEqual(run_calculator('47', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-31 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_32(self):
        self.assertEqual(run_calculator('47', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-32 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_33(self):
        self.assertEqual(run_calculator('47', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-33 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_34(self):
        self.assertEqual(run_calculator('47', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-34 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_35(self):
        self.assertEqual(run_calculator('47', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-35 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_36(self):
        self.assertEqual(run_calculator('47', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-36 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_37(self):
        self.assertEqual(run_calculator('47', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-37 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_38(self):
        self.assertEqual(run_calculator('47', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-38 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_39(self):
        self.assertEqual(run_calculator('47', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-39 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_40(self):
        self.assertEqual(run_calculator('47', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-40 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_41(self):
        self.assertEqual(run_calculator('47', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-41 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_42(self):
        self.assertEqual(run_calculator('47', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-42 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_43(self):
        self.assertEqual(run_calculator('47', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-43 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_44(self):
        self.assertEqual(run_calculator('47', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-44 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_45(self):
        self.assertEqual(run_calculator('47', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-45 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_46(self):
        self.assertEqual(run_calculator('47', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-46 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_47(self):
        self.assertEqual(run_calculator('47', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-47 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_48(self):
        self.assertEqual(run_calculator('47', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-48 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_49(self):
        self.assertEqual(run_calculator('47', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-49 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_minus_50(self):
        self.assertEqual(run_calculator('47', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47-50 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
