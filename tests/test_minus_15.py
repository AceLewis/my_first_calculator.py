# test_minus_15.py
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


class TestMinus15(unittest.TestCase):

    def test_15_minus_0(self):
        self.assertEqual(run_calculator('15', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-0 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_1(self):
        self.assertEqual(run_calculator('15', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-1 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_2(self):
        self.assertEqual(run_calculator('15', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-2 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_3(self):
        self.assertEqual(run_calculator('15', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-3 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_4(self):
        self.assertEqual(run_calculator('15', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-4 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_5(self):
        self.assertEqual(run_calculator('15', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-5 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_6(self):
        self.assertEqual(run_calculator('15', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-6 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_7(self):
        self.assertEqual(run_calculator('15', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-7 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_8(self):
        self.assertEqual(run_calculator('15', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-8 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_9(self):
        self.assertEqual(run_calculator('15', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-9 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_10(self):
        self.assertEqual(run_calculator('15', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-10 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_11(self):
        self.assertEqual(run_calculator('15', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-11 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_12(self):
        self.assertEqual(run_calculator('15', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-12 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_13(self):
        self.assertEqual(run_calculator('15', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-13 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_14(self):
        self.assertEqual(run_calculator('15', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-14 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_15(self):
        self.assertEqual(run_calculator('15', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-15 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_16(self):
        self.assertEqual(run_calculator('15', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-16 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_17(self):
        self.assertEqual(run_calculator('15', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-17 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_18(self):
        self.assertEqual(run_calculator('15', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-18 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_19(self):
        self.assertEqual(run_calculator('15', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-19 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_20(self):
        self.assertEqual(run_calculator('15', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-20 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_21(self):
        self.assertEqual(run_calculator('15', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-21 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_22(self):
        self.assertEqual(run_calculator('15', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-22 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_23(self):
        self.assertEqual(run_calculator('15', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-23 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_24(self):
        self.assertEqual(run_calculator('15', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-24 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_25(self):
        self.assertEqual(run_calculator('15', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-25 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_26(self):
        self.assertEqual(run_calculator('15', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-26 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_27(self):
        self.assertEqual(run_calculator('15', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-27 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_28(self):
        self.assertEqual(run_calculator('15', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-28 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_29(self):
        self.assertEqual(run_calculator('15', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-29 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_30(self):
        self.assertEqual(run_calculator('15', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-30 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_31(self):
        self.assertEqual(run_calculator('15', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-31 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_32(self):
        self.assertEqual(run_calculator('15', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-32 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_33(self):
        self.assertEqual(run_calculator('15', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-33 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_34(self):
        self.assertEqual(run_calculator('15', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-34 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_35(self):
        self.assertEqual(run_calculator('15', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-35 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_36(self):
        self.assertEqual(run_calculator('15', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-36 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_37(self):
        self.assertEqual(run_calculator('15', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-37 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_38(self):
        self.assertEqual(run_calculator('15', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-38 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_39(self):
        self.assertEqual(run_calculator('15', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-39 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_40(self):
        self.assertEqual(run_calculator('15', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-40 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_41(self):
        self.assertEqual(run_calculator('15', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-41 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_42(self):
        self.assertEqual(run_calculator('15', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-42 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_43(self):
        self.assertEqual(run_calculator('15', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-43 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_44(self):
        self.assertEqual(run_calculator('15', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-44 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_45(self):
        self.assertEqual(run_calculator('15', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-45 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_46(self):
        self.assertEqual(run_calculator('15', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-46 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_47(self):
        self.assertEqual(run_calculator('15', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-47 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_48(self):
        self.assertEqual(run_calculator('15', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-48 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_49(self):
        self.assertEqual(run_calculator('15', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-49 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_minus_50(self):
        self.assertEqual(run_calculator('15', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15-50 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
