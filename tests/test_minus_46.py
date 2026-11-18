# test_minus_46.py
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


class TestMinus46(unittest.TestCase):

    def test_46_minus_0(self):
        self.assertEqual(run_calculator('46', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-0 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_1(self):
        self.assertEqual(run_calculator('46', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-1 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_2(self):
        self.assertEqual(run_calculator('46', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-2 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_3(self):
        self.assertEqual(run_calculator('46', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-3 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_4(self):
        self.assertEqual(run_calculator('46', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-4 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_5(self):
        self.assertEqual(run_calculator('46', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-5 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_6(self):
        self.assertEqual(run_calculator('46', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-6 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_7(self):
        self.assertEqual(run_calculator('46', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-7 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_8(self):
        self.assertEqual(run_calculator('46', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-8 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_9(self):
        self.assertEqual(run_calculator('46', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-9 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_10(self):
        self.assertEqual(run_calculator('46', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-10 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_11(self):
        self.assertEqual(run_calculator('46', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-11 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_12(self):
        self.assertEqual(run_calculator('46', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-12 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_13(self):
        self.assertEqual(run_calculator('46', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-13 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_14(self):
        self.assertEqual(run_calculator('46', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-14 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_15(self):
        self.assertEqual(run_calculator('46', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-15 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_16(self):
        self.assertEqual(run_calculator('46', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-16 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_17(self):
        self.assertEqual(run_calculator('46', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-17 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_18(self):
        self.assertEqual(run_calculator('46', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-18 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_19(self):
        self.assertEqual(run_calculator('46', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-19 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_20(self):
        self.assertEqual(run_calculator('46', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-20 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_21(self):
        self.assertEqual(run_calculator('46', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-21 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_22(self):
        self.assertEqual(run_calculator('46', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-22 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_23(self):
        self.assertEqual(run_calculator('46', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-23 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_24(self):
        self.assertEqual(run_calculator('46', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-24 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_25(self):
        self.assertEqual(run_calculator('46', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-25 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_26(self):
        self.assertEqual(run_calculator('46', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-26 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_27(self):
        self.assertEqual(run_calculator('46', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-27 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_28(self):
        self.assertEqual(run_calculator('46', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-28 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_29(self):
        self.assertEqual(run_calculator('46', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-29 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_30(self):
        self.assertEqual(run_calculator('46', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-30 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_31(self):
        self.assertEqual(run_calculator('46', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-31 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_32(self):
        self.assertEqual(run_calculator('46', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-32 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_33(self):
        self.assertEqual(run_calculator('46', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-33 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_34(self):
        self.assertEqual(run_calculator('46', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-34 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_35(self):
        self.assertEqual(run_calculator('46', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-35 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_36(self):
        self.assertEqual(run_calculator('46', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-36 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_37(self):
        self.assertEqual(run_calculator('46', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-37 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_38(self):
        self.assertEqual(run_calculator('46', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-38 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_39(self):
        self.assertEqual(run_calculator('46', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-39 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_40(self):
        self.assertEqual(run_calculator('46', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-40 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_41(self):
        self.assertEqual(run_calculator('46', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-41 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_42(self):
        self.assertEqual(run_calculator('46', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-42 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_43(self):
        self.assertEqual(run_calculator('46', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-43 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_44(self):
        self.assertEqual(run_calculator('46', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-44 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_45(self):
        self.assertEqual(run_calculator('46', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-45 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_46(self):
        self.assertEqual(run_calculator('46', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-46 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_47(self):
        self.assertEqual(run_calculator('46', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-47 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_48(self):
        self.assertEqual(run_calculator('46', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-48 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_49(self):
        self.assertEqual(run_calculator('46', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-49 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_minus_50(self):
        self.assertEqual(run_calculator('46', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46-50 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
