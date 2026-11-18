# test_minus_38.py
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


class TestMinus38(unittest.TestCase):

    def test_38_minus_0(self):
        self.assertEqual(run_calculator('38', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-0 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_1(self):
        self.assertEqual(run_calculator('38', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-1 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_2(self):
        self.assertEqual(run_calculator('38', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-2 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_3(self):
        self.assertEqual(run_calculator('38', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-3 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_4(self):
        self.assertEqual(run_calculator('38', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-4 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_5(self):
        self.assertEqual(run_calculator('38', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-5 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_6(self):
        self.assertEqual(run_calculator('38', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-6 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_7(self):
        self.assertEqual(run_calculator('38', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-7 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_8(self):
        self.assertEqual(run_calculator('38', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-8 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_9(self):
        self.assertEqual(run_calculator('38', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-9 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_10(self):
        self.assertEqual(run_calculator('38', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-10 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_11(self):
        self.assertEqual(run_calculator('38', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-11 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_12(self):
        self.assertEqual(run_calculator('38', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-12 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_13(self):
        self.assertEqual(run_calculator('38', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-13 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_14(self):
        self.assertEqual(run_calculator('38', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-14 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_15(self):
        self.assertEqual(run_calculator('38', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-15 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_16(self):
        self.assertEqual(run_calculator('38', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-16 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_17(self):
        self.assertEqual(run_calculator('38', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-17 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_18(self):
        self.assertEqual(run_calculator('38', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-18 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_19(self):
        self.assertEqual(run_calculator('38', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-19 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_20(self):
        self.assertEqual(run_calculator('38', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-20 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_21(self):
        self.assertEqual(run_calculator('38', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-21 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_22(self):
        self.assertEqual(run_calculator('38', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-22 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_23(self):
        self.assertEqual(run_calculator('38', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-23 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_24(self):
        self.assertEqual(run_calculator('38', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-24 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_25(self):
        self.assertEqual(run_calculator('38', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-25 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_26(self):
        self.assertEqual(run_calculator('38', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-26 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_27(self):
        self.assertEqual(run_calculator('38', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-27 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_28(self):
        self.assertEqual(run_calculator('38', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-28 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_29(self):
        self.assertEqual(run_calculator('38', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-29 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_30(self):
        self.assertEqual(run_calculator('38', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-30 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_31(self):
        self.assertEqual(run_calculator('38', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-31 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_32(self):
        self.assertEqual(run_calculator('38', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-32 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_33(self):
        self.assertEqual(run_calculator('38', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-33 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_34(self):
        self.assertEqual(run_calculator('38', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-34 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_35(self):
        self.assertEqual(run_calculator('38', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-35 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_36(self):
        self.assertEqual(run_calculator('38', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-36 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_37(self):
        self.assertEqual(run_calculator('38', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-37 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_38(self):
        self.assertEqual(run_calculator('38', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-38 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_39(self):
        self.assertEqual(run_calculator('38', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-39 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_40(self):
        self.assertEqual(run_calculator('38', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-40 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_41(self):
        self.assertEqual(run_calculator('38', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-41 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_42(self):
        self.assertEqual(run_calculator('38', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-42 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_43(self):
        self.assertEqual(run_calculator('38', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-43 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_44(self):
        self.assertEqual(run_calculator('38', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-44 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_45(self):
        self.assertEqual(run_calculator('38', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-45 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_46(self):
        self.assertEqual(run_calculator('38', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-46 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_47(self):
        self.assertEqual(run_calculator('38', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-47 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_48(self):
        self.assertEqual(run_calculator('38', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-48 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_49(self):
        self.assertEqual(run_calculator('38', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-49 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_minus_50(self):
        self.assertEqual(run_calculator('38', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38-50 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
