# test_minus_1.py
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


class TestMinus1(unittest.TestCase):

    def test_1_minus_0(self):
        self.assertEqual(run_calculator('1', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-0 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_1(self):
        self.assertEqual(run_calculator('1', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-1 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_2(self):
        self.assertEqual(run_calculator('1', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-2 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_3(self):
        self.assertEqual(run_calculator('1', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-3 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_4(self):
        self.assertEqual(run_calculator('1', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-4 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_5(self):
        self.assertEqual(run_calculator('1', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-5 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_6(self):
        self.assertEqual(run_calculator('1', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-6 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_7(self):
        self.assertEqual(run_calculator('1', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-7 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_8(self):
        self.assertEqual(run_calculator('1', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-8 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_9(self):
        self.assertEqual(run_calculator('1', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-9 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_10(self):
        self.assertEqual(run_calculator('1', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-10 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_11(self):
        self.assertEqual(run_calculator('1', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-11 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_12(self):
        self.assertEqual(run_calculator('1', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-12 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_13(self):
        self.assertEqual(run_calculator('1', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-13 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_14(self):
        self.assertEqual(run_calculator('1', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-14 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_15(self):
        self.assertEqual(run_calculator('1', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-15 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_16(self):
        self.assertEqual(run_calculator('1', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-16 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_17(self):
        self.assertEqual(run_calculator('1', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-17 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_18(self):
        self.assertEqual(run_calculator('1', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-18 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_19(self):
        self.assertEqual(run_calculator('1', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-19 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_20(self):
        self.assertEqual(run_calculator('1', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-20 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_21(self):
        self.assertEqual(run_calculator('1', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-21 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_22(self):
        self.assertEqual(run_calculator('1', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-22 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_23(self):
        self.assertEqual(run_calculator('1', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-23 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_24(self):
        self.assertEqual(run_calculator('1', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-24 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_25(self):
        self.assertEqual(run_calculator('1', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-25 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_26(self):
        self.assertEqual(run_calculator('1', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-26 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_27(self):
        self.assertEqual(run_calculator('1', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-27 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_28(self):
        self.assertEqual(run_calculator('1', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-28 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_29(self):
        self.assertEqual(run_calculator('1', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-29 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_30(self):
        self.assertEqual(run_calculator('1', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-30 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_31(self):
        self.assertEqual(run_calculator('1', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-31 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_32(self):
        self.assertEqual(run_calculator('1', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-32 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_33(self):
        self.assertEqual(run_calculator('1', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-33 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_34(self):
        self.assertEqual(run_calculator('1', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-34 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_35(self):
        self.assertEqual(run_calculator('1', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-35 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_36(self):
        self.assertEqual(run_calculator('1', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-36 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_37(self):
        self.assertEqual(run_calculator('1', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-37 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_38(self):
        self.assertEqual(run_calculator('1', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-38 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_39(self):
        self.assertEqual(run_calculator('1', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-39 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_40(self):
        self.assertEqual(run_calculator('1', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-40 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_41(self):
        self.assertEqual(run_calculator('1', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-41 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_42(self):
        self.assertEqual(run_calculator('1', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-42 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_43(self):
        self.assertEqual(run_calculator('1', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-43 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_44(self):
        self.assertEqual(run_calculator('1', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-44 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_45(self):
        self.assertEqual(run_calculator('1', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-45 = -44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_46(self):
        self.assertEqual(run_calculator('1', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-46 = -45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_47(self):
        self.assertEqual(run_calculator('1', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-47 = -46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_48(self):
        self.assertEqual(run_calculator('1', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-48 = -47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_49(self):
        self.assertEqual(run_calculator('1', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-49 = -48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_minus_50(self):
        self.assertEqual(run_calculator('1', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1-50 = -49',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
