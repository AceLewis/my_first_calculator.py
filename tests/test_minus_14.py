# test_minus_14.py
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


class TestMinus14(unittest.TestCase):

    def test_14_minus_0(self):
        self.assertEqual(run_calculator('14', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-0 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_1(self):
        self.assertEqual(run_calculator('14', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-1 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_2(self):
        self.assertEqual(run_calculator('14', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-2 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_3(self):
        self.assertEqual(run_calculator('14', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-3 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_4(self):
        self.assertEqual(run_calculator('14', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-4 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_5(self):
        self.assertEqual(run_calculator('14', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-5 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_6(self):
        self.assertEqual(run_calculator('14', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-6 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_7(self):
        self.assertEqual(run_calculator('14', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-7 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_8(self):
        self.assertEqual(run_calculator('14', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-8 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_9(self):
        self.assertEqual(run_calculator('14', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-9 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_10(self):
        self.assertEqual(run_calculator('14', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-10 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_11(self):
        self.assertEqual(run_calculator('14', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-11 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_12(self):
        self.assertEqual(run_calculator('14', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-12 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_13(self):
        self.assertEqual(run_calculator('14', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-13 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_14(self):
        self.assertEqual(run_calculator('14', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-14 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_15(self):
        self.assertEqual(run_calculator('14', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-15 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_16(self):
        self.assertEqual(run_calculator('14', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-16 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_17(self):
        self.assertEqual(run_calculator('14', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-17 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_18(self):
        self.assertEqual(run_calculator('14', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-18 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_19(self):
        self.assertEqual(run_calculator('14', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-19 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_20(self):
        self.assertEqual(run_calculator('14', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-20 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_21(self):
        self.assertEqual(run_calculator('14', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-21 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_22(self):
        self.assertEqual(run_calculator('14', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-22 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_23(self):
        self.assertEqual(run_calculator('14', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-23 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_24(self):
        self.assertEqual(run_calculator('14', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-24 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_25(self):
        self.assertEqual(run_calculator('14', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-25 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_26(self):
        self.assertEqual(run_calculator('14', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-26 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_27(self):
        self.assertEqual(run_calculator('14', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-27 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_28(self):
        self.assertEqual(run_calculator('14', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-28 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_29(self):
        self.assertEqual(run_calculator('14', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-29 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_30(self):
        self.assertEqual(run_calculator('14', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-30 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_31(self):
        self.assertEqual(run_calculator('14', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-31 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_32(self):
        self.assertEqual(run_calculator('14', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-32 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_33(self):
        self.assertEqual(run_calculator('14', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-33 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_34(self):
        self.assertEqual(run_calculator('14', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-34 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_35(self):
        self.assertEqual(run_calculator('14', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-35 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_36(self):
        self.assertEqual(run_calculator('14', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-36 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_37(self):
        self.assertEqual(run_calculator('14', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-37 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_38(self):
        self.assertEqual(run_calculator('14', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-38 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_39(self):
        self.assertEqual(run_calculator('14', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-39 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_40(self):
        self.assertEqual(run_calculator('14', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-40 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_41(self):
        self.assertEqual(run_calculator('14', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-41 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_42(self):
        self.assertEqual(run_calculator('14', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-42 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_43(self):
        self.assertEqual(run_calculator('14', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-43 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_44(self):
        self.assertEqual(run_calculator('14', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-44 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_45(self):
        self.assertEqual(run_calculator('14', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-45 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_46(self):
        self.assertEqual(run_calculator('14', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-46 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_47(self):
        self.assertEqual(run_calculator('14', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-47 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_48(self):
        self.assertEqual(run_calculator('14', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-48 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_49(self):
        self.assertEqual(run_calculator('14', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-49 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_minus_50(self):
        self.assertEqual(run_calculator('14', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14-50 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
