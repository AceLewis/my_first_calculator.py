# test_minus_17.py
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


class TestMinus17(unittest.TestCase):

    def test_17_minus_0(self):
        self.assertEqual(run_calculator('17', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-0 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_1(self):
        self.assertEqual(run_calculator('17', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-1 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_2(self):
        self.assertEqual(run_calculator('17', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-2 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_3(self):
        self.assertEqual(run_calculator('17', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-3 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_4(self):
        self.assertEqual(run_calculator('17', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-4 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_5(self):
        self.assertEqual(run_calculator('17', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-5 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_6(self):
        self.assertEqual(run_calculator('17', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-6 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_7(self):
        self.assertEqual(run_calculator('17', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-7 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_8(self):
        self.assertEqual(run_calculator('17', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-8 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_9(self):
        self.assertEqual(run_calculator('17', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-9 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_10(self):
        self.assertEqual(run_calculator('17', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-10 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_11(self):
        self.assertEqual(run_calculator('17', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-11 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_12(self):
        self.assertEqual(run_calculator('17', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-12 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_13(self):
        self.assertEqual(run_calculator('17', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-13 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_14(self):
        self.assertEqual(run_calculator('17', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-14 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_15(self):
        self.assertEqual(run_calculator('17', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-15 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_16(self):
        self.assertEqual(run_calculator('17', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-16 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_17(self):
        self.assertEqual(run_calculator('17', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-17 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_18(self):
        self.assertEqual(run_calculator('17', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-18 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_19(self):
        self.assertEqual(run_calculator('17', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-19 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_20(self):
        self.assertEqual(run_calculator('17', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-20 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_21(self):
        self.assertEqual(run_calculator('17', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-21 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_22(self):
        self.assertEqual(run_calculator('17', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-22 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_23(self):
        self.assertEqual(run_calculator('17', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-23 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_24(self):
        self.assertEqual(run_calculator('17', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-24 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_25(self):
        self.assertEqual(run_calculator('17', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-25 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_26(self):
        self.assertEqual(run_calculator('17', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-26 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_27(self):
        self.assertEqual(run_calculator('17', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-27 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_28(self):
        self.assertEqual(run_calculator('17', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-28 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_29(self):
        self.assertEqual(run_calculator('17', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-29 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_30(self):
        self.assertEqual(run_calculator('17', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-30 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_31(self):
        self.assertEqual(run_calculator('17', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-31 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_32(self):
        self.assertEqual(run_calculator('17', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-32 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_33(self):
        self.assertEqual(run_calculator('17', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-33 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_34(self):
        self.assertEqual(run_calculator('17', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-34 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_35(self):
        self.assertEqual(run_calculator('17', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-35 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_36(self):
        self.assertEqual(run_calculator('17', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-36 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_37(self):
        self.assertEqual(run_calculator('17', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-37 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_38(self):
        self.assertEqual(run_calculator('17', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-38 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_39(self):
        self.assertEqual(run_calculator('17', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-39 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_40(self):
        self.assertEqual(run_calculator('17', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-40 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_41(self):
        self.assertEqual(run_calculator('17', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-41 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_42(self):
        self.assertEqual(run_calculator('17', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-42 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_43(self):
        self.assertEqual(run_calculator('17', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-43 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_44(self):
        self.assertEqual(run_calculator('17', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-44 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_45(self):
        self.assertEqual(run_calculator('17', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-45 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_46(self):
        self.assertEqual(run_calculator('17', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-46 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_47(self):
        self.assertEqual(run_calculator('17', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-47 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_48(self):
        self.assertEqual(run_calculator('17', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-48 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_49(self):
        self.assertEqual(run_calculator('17', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-49 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_minus_50(self):
        self.assertEqual(run_calculator('17', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17-50 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
