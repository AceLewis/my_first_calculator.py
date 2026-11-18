# test_minus_42.py
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


class TestMinus42(unittest.TestCase):

    def test_42_minus_0(self):
        self.assertEqual(run_calculator('42', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-0 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_1(self):
        self.assertEqual(run_calculator('42', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-1 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_2(self):
        self.assertEqual(run_calculator('42', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-2 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_3(self):
        self.assertEqual(run_calculator('42', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-3 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_4(self):
        self.assertEqual(run_calculator('42', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-4 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_5(self):
        self.assertEqual(run_calculator('42', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-5 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_6(self):
        self.assertEqual(run_calculator('42', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-6 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_7(self):
        self.assertEqual(run_calculator('42', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-7 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_8(self):
        self.assertEqual(run_calculator('42', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-8 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_9(self):
        self.assertEqual(run_calculator('42', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-9 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_10(self):
        self.assertEqual(run_calculator('42', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-10 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_11(self):
        self.assertEqual(run_calculator('42', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-11 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_12(self):
        self.assertEqual(run_calculator('42', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-12 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_13(self):
        self.assertEqual(run_calculator('42', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-13 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_14(self):
        self.assertEqual(run_calculator('42', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-14 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_15(self):
        self.assertEqual(run_calculator('42', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-15 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_16(self):
        self.assertEqual(run_calculator('42', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-16 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_17(self):
        self.assertEqual(run_calculator('42', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-17 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_18(self):
        self.assertEqual(run_calculator('42', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-18 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_19(self):
        self.assertEqual(run_calculator('42', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-19 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_20(self):
        self.assertEqual(run_calculator('42', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-20 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_21(self):
        self.assertEqual(run_calculator('42', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-21 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_22(self):
        self.assertEqual(run_calculator('42', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-22 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_23(self):
        self.assertEqual(run_calculator('42', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-23 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_24(self):
        self.assertEqual(run_calculator('42', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-24 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_25(self):
        self.assertEqual(run_calculator('42', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-25 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_26(self):
        self.assertEqual(run_calculator('42', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-26 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_27(self):
        self.assertEqual(run_calculator('42', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-27 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_28(self):
        self.assertEqual(run_calculator('42', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-28 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_29(self):
        self.assertEqual(run_calculator('42', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-29 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_30(self):
        self.assertEqual(run_calculator('42', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-30 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_31(self):
        self.assertEqual(run_calculator('42', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-31 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_32(self):
        self.assertEqual(run_calculator('42', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-32 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_33(self):
        self.assertEqual(run_calculator('42', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-33 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_34(self):
        self.assertEqual(run_calculator('42', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-34 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_35(self):
        self.assertEqual(run_calculator('42', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-35 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_36(self):
        self.assertEqual(run_calculator('42', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-36 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_37(self):
        self.assertEqual(run_calculator('42', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-37 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_38(self):
        self.assertEqual(run_calculator('42', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-38 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_39(self):
        self.assertEqual(run_calculator('42', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-39 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_40(self):
        self.assertEqual(run_calculator('42', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-40 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_41(self):
        self.assertEqual(run_calculator('42', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-41 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_42(self):
        self.assertEqual(run_calculator('42', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-42 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_43(self):
        self.assertEqual(run_calculator('42', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-43 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_44(self):
        self.assertEqual(run_calculator('42', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-44 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_45(self):
        self.assertEqual(run_calculator('42', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-45 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_46(self):
        self.assertEqual(run_calculator('42', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-46 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_47(self):
        self.assertEqual(run_calculator('42', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-47 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_48(self):
        self.assertEqual(run_calculator('42', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-48 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_49(self):
        self.assertEqual(run_calculator('42', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-49 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_minus_50(self):
        self.assertEqual(run_calculator('42', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42-50 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
