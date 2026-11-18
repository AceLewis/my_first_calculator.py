# test_minus_44.py
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


class TestMinus44(unittest.TestCase):

    def test_44_minus_0(self):
        self.assertEqual(run_calculator('44', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-0 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_1(self):
        self.assertEqual(run_calculator('44', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-1 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_2(self):
        self.assertEqual(run_calculator('44', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-2 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_3(self):
        self.assertEqual(run_calculator('44', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-3 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_4(self):
        self.assertEqual(run_calculator('44', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-4 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_5(self):
        self.assertEqual(run_calculator('44', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-5 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_6(self):
        self.assertEqual(run_calculator('44', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-6 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_7(self):
        self.assertEqual(run_calculator('44', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-7 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_8(self):
        self.assertEqual(run_calculator('44', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-8 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_9(self):
        self.assertEqual(run_calculator('44', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-9 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_10(self):
        self.assertEqual(run_calculator('44', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-10 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_11(self):
        self.assertEqual(run_calculator('44', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-11 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_12(self):
        self.assertEqual(run_calculator('44', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-12 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_13(self):
        self.assertEqual(run_calculator('44', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-13 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_14(self):
        self.assertEqual(run_calculator('44', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-14 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_15(self):
        self.assertEqual(run_calculator('44', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-15 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_16(self):
        self.assertEqual(run_calculator('44', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-16 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_17(self):
        self.assertEqual(run_calculator('44', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-17 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_18(self):
        self.assertEqual(run_calculator('44', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-18 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_19(self):
        self.assertEqual(run_calculator('44', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-19 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_20(self):
        self.assertEqual(run_calculator('44', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-20 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_21(self):
        self.assertEqual(run_calculator('44', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-21 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_22(self):
        self.assertEqual(run_calculator('44', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-22 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_23(self):
        self.assertEqual(run_calculator('44', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-23 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_24(self):
        self.assertEqual(run_calculator('44', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-24 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_25(self):
        self.assertEqual(run_calculator('44', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-25 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_26(self):
        self.assertEqual(run_calculator('44', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-26 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_27(self):
        self.assertEqual(run_calculator('44', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-27 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_28(self):
        self.assertEqual(run_calculator('44', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-28 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_29(self):
        self.assertEqual(run_calculator('44', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-29 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_30(self):
        self.assertEqual(run_calculator('44', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-30 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_31(self):
        self.assertEqual(run_calculator('44', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-31 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_32(self):
        self.assertEqual(run_calculator('44', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-32 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_33(self):
        self.assertEqual(run_calculator('44', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-33 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_34(self):
        self.assertEqual(run_calculator('44', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-34 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_35(self):
        self.assertEqual(run_calculator('44', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-35 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_36(self):
        self.assertEqual(run_calculator('44', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-36 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_37(self):
        self.assertEqual(run_calculator('44', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-37 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_38(self):
        self.assertEqual(run_calculator('44', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-38 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_39(self):
        self.assertEqual(run_calculator('44', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-39 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_40(self):
        self.assertEqual(run_calculator('44', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-40 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_41(self):
        self.assertEqual(run_calculator('44', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-41 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_42(self):
        self.assertEqual(run_calculator('44', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-42 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_43(self):
        self.assertEqual(run_calculator('44', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-43 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_44(self):
        self.assertEqual(run_calculator('44', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-44 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_45(self):
        self.assertEqual(run_calculator('44', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-45 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_46(self):
        self.assertEqual(run_calculator('44', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-46 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_47(self):
        self.assertEqual(run_calculator('44', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-47 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_48(self):
        self.assertEqual(run_calculator('44', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-48 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_49(self):
        self.assertEqual(run_calculator('44', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-49 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_minus_50(self):
        self.assertEqual(run_calculator('44', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44-50 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
