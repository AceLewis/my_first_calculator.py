# test_minus_50.py
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


class TestMinus50(unittest.TestCase):

    def test_50_minus_0(self):
        self.assertEqual(run_calculator('50', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-0 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_1(self):
        self.assertEqual(run_calculator('50', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-1 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_2(self):
        self.assertEqual(run_calculator('50', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-2 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_3(self):
        self.assertEqual(run_calculator('50', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-3 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_4(self):
        self.assertEqual(run_calculator('50', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-4 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_5(self):
        self.assertEqual(run_calculator('50', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-5 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_6(self):
        self.assertEqual(run_calculator('50', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-6 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_7(self):
        self.assertEqual(run_calculator('50', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-7 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_8(self):
        self.assertEqual(run_calculator('50', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-8 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_9(self):
        self.assertEqual(run_calculator('50', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-9 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_10(self):
        self.assertEqual(run_calculator('50', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-10 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_11(self):
        self.assertEqual(run_calculator('50', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-11 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_12(self):
        self.assertEqual(run_calculator('50', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-12 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_13(self):
        self.assertEqual(run_calculator('50', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-13 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_14(self):
        self.assertEqual(run_calculator('50', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-14 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_15(self):
        self.assertEqual(run_calculator('50', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-15 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_16(self):
        self.assertEqual(run_calculator('50', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-16 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_17(self):
        self.assertEqual(run_calculator('50', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-17 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_18(self):
        self.assertEqual(run_calculator('50', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-18 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_19(self):
        self.assertEqual(run_calculator('50', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-19 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_20(self):
        self.assertEqual(run_calculator('50', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-20 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_21(self):
        self.assertEqual(run_calculator('50', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-21 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_22(self):
        self.assertEqual(run_calculator('50', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-22 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_23(self):
        self.assertEqual(run_calculator('50', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-23 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_24(self):
        self.assertEqual(run_calculator('50', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-24 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_25(self):
        self.assertEqual(run_calculator('50', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-25 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_26(self):
        self.assertEqual(run_calculator('50', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-26 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_27(self):
        self.assertEqual(run_calculator('50', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-27 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_28(self):
        self.assertEqual(run_calculator('50', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-28 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_29(self):
        self.assertEqual(run_calculator('50', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-29 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_30(self):
        self.assertEqual(run_calculator('50', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-30 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_31(self):
        self.assertEqual(run_calculator('50', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-31 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_32(self):
        self.assertEqual(run_calculator('50', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-32 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_33(self):
        self.assertEqual(run_calculator('50', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-33 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_34(self):
        self.assertEqual(run_calculator('50', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-34 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_35(self):
        self.assertEqual(run_calculator('50', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-35 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_36(self):
        self.assertEqual(run_calculator('50', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-36 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_37(self):
        self.assertEqual(run_calculator('50', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-37 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_38(self):
        self.assertEqual(run_calculator('50', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-38 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_39(self):
        self.assertEqual(run_calculator('50', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-39 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_40(self):
        self.assertEqual(run_calculator('50', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-40 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_41(self):
        self.assertEqual(run_calculator('50', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-41 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_42(self):
        self.assertEqual(run_calculator('50', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-42 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_43(self):
        self.assertEqual(run_calculator('50', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-43 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_44(self):
        self.assertEqual(run_calculator('50', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-44 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_45(self):
        self.assertEqual(run_calculator('50', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-45 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_46(self):
        self.assertEqual(run_calculator('50', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-46 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_47(self):
        self.assertEqual(run_calculator('50', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-47 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_48(self):
        self.assertEqual(run_calculator('50', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-48 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_49(self):
        self.assertEqual(run_calculator('50', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-49 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_minus_50(self):
        self.assertEqual(run_calculator('50', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50-50 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
