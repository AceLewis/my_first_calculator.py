# test_minus_22.py
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


class TestMinus22(unittest.TestCase):

    def test_22_minus_0(self):
        self.assertEqual(run_calculator('22', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-0 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_1(self):
        self.assertEqual(run_calculator('22', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-1 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_2(self):
        self.assertEqual(run_calculator('22', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-2 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_3(self):
        self.assertEqual(run_calculator('22', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-3 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_4(self):
        self.assertEqual(run_calculator('22', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-4 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_5(self):
        self.assertEqual(run_calculator('22', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-5 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_6(self):
        self.assertEqual(run_calculator('22', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-6 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_7(self):
        self.assertEqual(run_calculator('22', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-7 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_8(self):
        self.assertEqual(run_calculator('22', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-8 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_9(self):
        self.assertEqual(run_calculator('22', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-9 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_10(self):
        self.assertEqual(run_calculator('22', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-10 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_11(self):
        self.assertEqual(run_calculator('22', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-11 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_12(self):
        self.assertEqual(run_calculator('22', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-12 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_13(self):
        self.assertEqual(run_calculator('22', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-13 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_14(self):
        self.assertEqual(run_calculator('22', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-14 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_15(self):
        self.assertEqual(run_calculator('22', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-15 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_16(self):
        self.assertEqual(run_calculator('22', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-16 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_17(self):
        self.assertEqual(run_calculator('22', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-17 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_18(self):
        self.assertEqual(run_calculator('22', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-18 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_19(self):
        self.assertEqual(run_calculator('22', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-19 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_20(self):
        self.assertEqual(run_calculator('22', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-20 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_21(self):
        self.assertEqual(run_calculator('22', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-21 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_22(self):
        self.assertEqual(run_calculator('22', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-22 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_23(self):
        self.assertEqual(run_calculator('22', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-23 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_24(self):
        self.assertEqual(run_calculator('22', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-24 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_25(self):
        self.assertEqual(run_calculator('22', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-25 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_26(self):
        self.assertEqual(run_calculator('22', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-26 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_27(self):
        self.assertEqual(run_calculator('22', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-27 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_28(self):
        self.assertEqual(run_calculator('22', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-28 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_29(self):
        self.assertEqual(run_calculator('22', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-29 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_30(self):
        self.assertEqual(run_calculator('22', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-30 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_31(self):
        self.assertEqual(run_calculator('22', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-31 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_32(self):
        self.assertEqual(run_calculator('22', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-32 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_33(self):
        self.assertEqual(run_calculator('22', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-33 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_34(self):
        self.assertEqual(run_calculator('22', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-34 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_35(self):
        self.assertEqual(run_calculator('22', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-35 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_36(self):
        self.assertEqual(run_calculator('22', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-36 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_37(self):
        self.assertEqual(run_calculator('22', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-37 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_38(self):
        self.assertEqual(run_calculator('22', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-38 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_39(self):
        self.assertEqual(run_calculator('22', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-39 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_40(self):
        self.assertEqual(run_calculator('22', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-40 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_41(self):
        self.assertEqual(run_calculator('22', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-41 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_42(self):
        self.assertEqual(run_calculator('22', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-42 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_43(self):
        self.assertEqual(run_calculator('22', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-43 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_44(self):
        self.assertEqual(run_calculator('22', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-44 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_45(self):
        self.assertEqual(run_calculator('22', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-45 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_46(self):
        self.assertEqual(run_calculator('22', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-46 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_47(self):
        self.assertEqual(run_calculator('22', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-47 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_48(self):
        self.assertEqual(run_calculator('22', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-48 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_49(self):
        self.assertEqual(run_calculator('22', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-49 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_minus_50(self):
        self.assertEqual(run_calculator('22', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22-50 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
