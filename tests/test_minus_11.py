# test_minus_11.py
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


class TestMinus11(unittest.TestCase):

    def test_11_minus_0(self):
        self.assertEqual(run_calculator('11', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-0 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_1(self):
        self.assertEqual(run_calculator('11', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-1 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_2(self):
        self.assertEqual(run_calculator('11', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-2 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_3(self):
        self.assertEqual(run_calculator('11', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-3 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_4(self):
        self.assertEqual(run_calculator('11', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-4 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_5(self):
        self.assertEqual(run_calculator('11', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-5 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_6(self):
        self.assertEqual(run_calculator('11', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-6 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_7(self):
        self.assertEqual(run_calculator('11', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-7 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_8(self):
        self.assertEqual(run_calculator('11', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-8 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_9(self):
        self.assertEqual(run_calculator('11', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-9 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_10(self):
        self.assertEqual(run_calculator('11', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-10 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_11(self):
        self.assertEqual(run_calculator('11', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-11 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_12(self):
        self.assertEqual(run_calculator('11', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-12 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_13(self):
        self.assertEqual(run_calculator('11', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-13 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_14(self):
        self.assertEqual(run_calculator('11', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-14 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_15(self):
        self.assertEqual(run_calculator('11', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-15 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_16(self):
        self.assertEqual(run_calculator('11', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-16 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_17(self):
        self.assertEqual(run_calculator('11', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-17 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_18(self):
        self.assertEqual(run_calculator('11', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-18 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_19(self):
        self.assertEqual(run_calculator('11', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-19 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_20(self):
        self.assertEqual(run_calculator('11', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-20 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_21(self):
        self.assertEqual(run_calculator('11', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-21 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_22(self):
        self.assertEqual(run_calculator('11', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-22 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_23(self):
        self.assertEqual(run_calculator('11', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-23 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_24(self):
        self.assertEqual(run_calculator('11', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-24 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_25(self):
        self.assertEqual(run_calculator('11', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-25 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_26(self):
        self.assertEqual(run_calculator('11', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-26 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_27(self):
        self.assertEqual(run_calculator('11', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-27 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_28(self):
        self.assertEqual(run_calculator('11', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-28 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_29(self):
        self.assertEqual(run_calculator('11', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-29 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_30(self):
        self.assertEqual(run_calculator('11', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-30 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_31(self):
        self.assertEqual(run_calculator('11', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-31 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_32(self):
        self.assertEqual(run_calculator('11', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-32 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_33(self):
        self.assertEqual(run_calculator('11', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-33 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_34(self):
        self.assertEqual(run_calculator('11', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-34 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_35(self):
        self.assertEqual(run_calculator('11', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-35 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_36(self):
        self.assertEqual(run_calculator('11', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-36 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_37(self):
        self.assertEqual(run_calculator('11', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-37 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_38(self):
        self.assertEqual(run_calculator('11', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-38 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_39(self):
        self.assertEqual(run_calculator('11', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-39 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_40(self):
        self.assertEqual(run_calculator('11', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-40 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_41(self):
        self.assertEqual(run_calculator('11', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-41 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_42(self):
        self.assertEqual(run_calculator('11', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-42 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_43(self):
        self.assertEqual(run_calculator('11', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-43 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_44(self):
        self.assertEqual(run_calculator('11', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-44 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_45(self):
        self.assertEqual(run_calculator('11', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-45 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_46(self):
        self.assertEqual(run_calculator('11', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-46 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_47(self):
        self.assertEqual(run_calculator('11', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-47 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_48(self):
        self.assertEqual(run_calculator('11', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-48 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_49(self):
        self.assertEqual(run_calculator('11', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-49 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_minus_50(self):
        self.assertEqual(run_calculator('11', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11-50 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
