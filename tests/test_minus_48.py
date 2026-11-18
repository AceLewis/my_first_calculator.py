# test_minus_48.py
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


class TestMinus48(unittest.TestCase):

    def test_48_minus_0(self):
        self.assertEqual(run_calculator('48', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-0 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_1(self):
        self.assertEqual(run_calculator('48', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-1 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_2(self):
        self.assertEqual(run_calculator('48', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-2 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_3(self):
        self.assertEqual(run_calculator('48', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-3 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_4(self):
        self.assertEqual(run_calculator('48', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-4 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_5(self):
        self.assertEqual(run_calculator('48', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-5 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_6(self):
        self.assertEqual(run_calculator('48', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-6 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_7(self):
        self.assertEqual(run_calculator('48', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-7 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_8(self):
        self.assertEqual(run_calculator('48', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-8 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_9(self):
        self.assertEqual(run_calculator('48', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-9 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_10(self):
        self.assertEqual(run_calculator('48', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-10 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_11(self):
        self.assertEqual(run_calculator('48', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-11 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_12(self):
        self.assertEqual(run_calculator('48', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-12 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_13(self):
        self.assertEqual(run_calculator('48', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-13 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_14(self):
        self.assertEqual(run_calculator('48', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-14 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_15(self):
        self.assertEqual(run_calculator('48', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-15 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_16(self):
        self.assertEqual(run_calculator('48', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-16 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_17(self):
        self.assertEqual(run_calculator('48', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-17 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_18(self):
        self.assertEqual(run_calculator('48', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-18 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_19(self):
        self.assertEqual(run_calculator('48', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-19 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_20(self):
        self.assertEqual(run_calculator('48', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-20 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_21(self):
        self.assertEqual(run_calculator('48', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-21 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_22(self):
        self.assertEqual(run_calculator('48', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-22 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_23(self):
        self.assertEqual(run_calculator('48', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-23 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_24(self):
        self.assertEqual(run_calculator('48', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-24 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_25(self):
        self.assertEqual(run_calculator('48', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-25 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_26(self):
        self.assertEqual(run_calculator('48', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-26 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_27(self):
        self.assertEqual(run_calculator('48', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-27 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_28(self):
        self.assertEqual(run_calculator('48', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-28 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_29(self):
        self.assertEqual(run_calculator('48', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-29 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_30(self):
        self.assertEqual(run_calculator('48', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-30 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_31(self):
        self.assertEqual(run_calculator('48', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-31 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_32(self):
        self.assertEqual(run_calculator('48', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-32 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_33(self):
        self.assertEqual(run_calculator('48', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-33 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_34(self):
        self.assertEqual(run_calculator('48', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-34 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_35(self):
        self.assertEqual(run_calculator('48', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-35 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_36(self):
        self.assertEqual(run_calculator('48', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-36 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_37(self):
        self.assertEqual(run_calculator('48', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-37 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_38(self):
        self.assertEqual(run_calculator('48', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-38 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_39(self):
        self.assertEqual(run_calculator('48', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-39 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_40(self):
        self.assertEqual(run_calculator('48', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-40 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_41(self):
        self.assertEqual(run_calculator('48', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-41 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_42(self):
        self.assertEqual(run_calculator('48', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-42 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_43(self):
        self.assertEqual(run_calculator('48', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-43 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_44(self):
        self.assertEqual(run_calculator('48', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-44 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_45(self):
        self.assertEqual(run_calculator('48', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-45 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_46(self):
        self.assertEqual(run_calculator('48', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-46 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_47(self):
        self.assertEqual(run_calculator('48', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-47 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_48(self):
        self.assertEqual(run_calculator('48', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-48 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_49(self):
        self.assertEqual(run_calculator('48', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-49 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_minus_50(self):
        self.assertEqual(run_calculator('48', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48-50 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
