# test_minus_45.py
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


class TestMinus45(unittest.TestCase):

    def test_45_minus_0(self):
        self.assertEqual(run_calculator('45', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-0 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_1(self):
        self.assertEqual(run_calculator('45', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-1 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_2(self):
        self.assertEqual(run_calculator('45', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-2 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_3(self):
        self.assertEqual(run_calculator('45', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-3 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_4(self):
        self.assertEqual(run_calculator('45', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-4 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_5(self):
        self.assertEqual(run_calculator('45', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-5 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_6(self):
        self.assertEqual(run_calculator('45', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-6 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_7(self):
        self.assertEqual(run_calculator('45', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-7 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_8(self):
        self.assertEqual(run_calculator('45', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-8 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_9(self):
        self.assertEqual(run_calculator('45', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-9 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_10(self):
        self.assertEqual(run_calculator('45', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-10 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_11(self):
        self.assertEqual(run_calculator('45', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-11 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_12(self):
        self.assertEqual(run_calculator('45', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-12 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_13(self):
        self.assertEqual(run_calculator('45', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-13 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_14(self):
        self.assertEqual(run_calculator('45', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-14 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_15(self):
        self.assertEqual(run_calculator('45', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-15 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_16(self):
        self.assertEqual(run_calculator('45', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-16 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_17(self):
        self.assertEqual(run_calculator('45', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-17 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_18(self):
        self.assertEqual(run_calculator('45', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-18 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_19(self):
        self.assertEqual(run_calculator('45', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-19 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_20(self):
        self.assertEqual(run_calculator('45', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-20 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_21(self):
        self.assertEqual(run_calculator('45', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-21 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_22(self):
        self.assertEqual(run_calculator('45', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-22 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_23(self):
        self.assertEqual(run_calculator('45', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-23 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_24(self):
        self.assertEqual(run_calculator('45', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-24 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_25(self):
        self.assertEqual(run_calculator('45', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-25 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_26(self):
        self.assertEqual(run_calculator('45', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-26 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_27(self):
        self.assertEqual(run_calculator('45', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-27 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_28(self):
        self.assertEqual(run_calculator('45', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-28 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_29(self):
        self.assertEqual(run_calculator('45', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-29 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_30(self):
        self.assertEqual(run_calculator('45', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-30 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_31(self):
        self.assertEqual(run_calculator('45', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-31 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_32(self):
        self.assertEqual(run_calculator('45', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-32 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_33(self):
        self.assertEqual(run_calculator('45', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-33 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_34(self):
        self.assertEqual(run_calculator('45', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-34 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_35(self):
        self.assertEqual(run_calculator('45', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-35 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_36(self):
        self.assertEqual(run_calculator('45', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-36 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_37(self):
        self.assertEqual(run_calculator('45', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-37 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_38(self):
        self.assertEqual(run_calculator('45', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-38 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_39(self):
        self.assertEqual(run_calculator('45', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-39 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_40(self):
        self.assertEqual(run_calculator('45', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-40 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_41(self):
        self.assertEqual(run_calculator('45', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-41 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_42(self):
        self.assertEqual(run_calculator('45', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-42 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_43(self):
        self.assertEqual(run_calculator('45', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-43 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_44(self):
        self.assertEqual(run_calculator('45', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-44 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_45(self):
        self.assertEqual(run_calculator('45', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-45 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_46(self):
        self.assertEqual(run_calculator('45', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-46 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_47(self):
        self.assertEqual(run_calculator('45', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-47 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_48(self):
        self.assertEqual(run_calculator('45', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-48 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_49(self):
        self.assertEqual(run_calculator('45', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-49 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_minus_50(self):
        self.assertEqual(run_calculator('45', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45-50 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
