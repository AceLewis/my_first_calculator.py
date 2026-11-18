# test_minus_16.py
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


class TestMinus16(unittest.TestCase):

    def test_16_minus_0(self):
        self.assertEqual(run_calculator('16', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-0 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_1(self):
        self.assertEqual(run_calculator('16', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-1 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_2(self):
        self.assertEqual(run_calculator('16', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-2 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_3(self):
        self.assertEqual(run_calculator('16', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-3 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_4(self):
        self.assertEqual(run_calculator('16', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-4 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_5(self):
        self.assertEqual(run_calculator('16', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-5 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_6(self):
        self.assertEqual(run_calculator('16', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-6 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_7(self):
        self.assertEqual(run_calculator('16', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-7 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_8(self):
        self.assertEqual(run_calculator('16', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-8 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_9(self):
        self.assertEqual(run_calculator('16', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-9 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_10(self):
        self.assertEqual(run_calculator('16', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-10 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_11(self):
        self.assertEqual(run_calculator('16', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-11 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_12(self):
        self.assertEqual(run_calculator('16', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-12 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_13(self):
        self.assertEqual(run_calculator('16', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-13 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_14(self):
        self.assertEqual(run_calculator('16', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-14 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_15(self):
        self.assertEqual(run_calculator('16', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-15 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_16(self):
        self.assertEqual(run_calculator('16', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-16 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_17(self):
        self.assertEqual(run_calculator('16', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-17 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_18(self):
        self.assertEqual(run_calculator('16', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-18 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_19(self):
        self.assertEqual(run_calculator('16', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-19 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_20(self):
        self.assertEqual(run_calculator('16', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-20 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_21(self):
        self.assertEqual(run_calculator('16', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-21 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_22(self):
        self.assertEqual(run_calculator('16', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-22 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_23(self):
        self.assertEqual(run_calculator('16', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-23 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_24(self):
        self.assertEqual(run_calculator('16', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-24 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_25(self):
        self.assertEqual(run_calculator('16', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-25 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_26(self):
        self.assertEqual(run_calculator('16', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-26 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_27(self):
        self.assertEqual(run_calculator('16', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-27 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_28(self):
        self.assertEqual(run_calculator('16', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-28 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_29(self):
        self.assertEqual(run_calculator('16', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-29 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_30(self):
        self.assertEqual(run_calculator('16', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-30 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_31(self):
        self.assertEqual(run_calculator('16', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-31 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_32(self):
        self.assertEqual(run_calculator('16', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-32 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_33(self):
        self.assertEqual(run_calculator('16', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-33 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_34(self):
        self.assertEqual(run_calculator('16', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-34 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_35(self):
        self.assertEqual(run_calculator('16', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-35 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_36(self):
        self.assertEqual(run_calculator('16', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-36 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_37(self):
        self.assertEqual(run_calculator('16', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-37 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_38(self):
        self.assertEqual(run_calculator('16', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-38 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_39(self):
        self.assertEqual(run_calculator('16', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-39 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_40(self):
        self.assertEqual(run_calculator('16', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-40 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_41(self):
        self.assertEqual(run_calculator('16', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-41 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_42(self):
        self.assertEqual(run_calculator('16', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-42 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_43(self):
        self.assertEqual(run_calculator('16', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-43 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_44(self):
        self.assertEqual(run_calculator('16', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-44 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_45(self):
        self.assertEqual(run_calculator('16', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-45 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_46(self):
        self.assertEqual(run_calculator('16', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-46 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_47(self):
        self.assertEqual(run_calculator('16', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-47 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_48(self):
        self.assertEqual(run_calculator('16', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-48 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_49(self):
        self.assertEqual(run_calculator('16', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-49 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_minus_50(self):
        self.assertEqual(run_calculator('16', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16-50 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
