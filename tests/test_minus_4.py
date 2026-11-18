# test_minus_4.py
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


class TestMinus4(unittest.TestCase):

    def test_4_minus_0(self):
        self.assertEqual(run_calculator('4', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-0 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_1(self):
        self.assertEqual(run_calculator('4', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-1 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_2(self):
        self.assertEqual(run_calculator('4', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-2 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_3(self):
        self.assertEqual(run_calculator('4', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-3 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_4(self):
        self.assertEqual(run_calculator('4', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-4 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_5(self):
        self.assertEqual(run_calculator('4', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-5 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_6(self):
        self.assertEqual(run_calculator('4', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-6 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_7(self):
        self.assertEqual(run_calculator('4', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-7 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_8(self):
        self.assertEqual(run_calculator('4', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-8 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_9(self):
        self.assertEqual(run_calculator('4', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-9 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_10(self):
        self.assertEqual(run_calculator('4', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-10 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_11(self):
        self.assertEqual(run_calculator('4', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-11 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_12(self):
        self.assertEqual(run_calculator('4', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-12 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_13(self):
        self.assertEqual(run_calculator('4', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-13 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_14(self):
        self.assertEqual(run_calculator('4', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-14 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_15(self):
        self.assertEqual(run_calculator('4', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-15 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_16(self):
        self.assertEqual(run_calculator('4', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-16 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_17(self):
        self.assertEqual(run_calculator('4', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-17 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_18(self):
        self.assertEqual(run_calculator('4', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-18 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_19(self):
        self.assertEqual(run_calculator('4', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-19 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_20(self):
        self.assertEqual(run_calculator('4', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-20 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_21(self):
        self.assertEqual(run_calculator('4', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-21 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_22(self):
        self.assertEqual(run_calculator('4', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-22 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_23(self):
        self.assertEqual(run_calculator('4', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-23 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_24(self):
        self.assertEqual(run_calculator('4', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-24 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_25(self):
        self.assertEqual(run_calculator('4', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-25 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_26(self):
        self.assertEqual(run_calculator('4', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-26 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_27(self):
        self.assertEqual(run_calculator('4', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-27 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_28(self):
        self.assertEqual(run_calculator('4', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-28 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_29(self):
        self.assertEqual(run_calculator('4', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-29 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_30(self):
        self.assertEqual(run_calculator('4', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-30 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_31(self):
        self.assertEqual(run_calculator('4', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-31 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_32(self):
        self.assertEqual(run_calculator('4', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-32 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_33(self):
        self.assertEqual(run_calculator('4', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-33 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_34(self):
        self.assertEqual(run_calculator('4', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-34 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_35(self):
        self.assertEqual(run_calculator('4', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-35 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_36(self):
        self.assertEqual(run_calculator('4', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-36 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_37(self):
        self.assertEqual(run_calculator('4', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-37 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_38(self):
        self.assertEqual(run_calculator('4', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-38 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_39(self):
        self.assertEqual(run_calculator('4', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-39 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_40(self):
        self.assertEqual(run_calculator('4', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-40 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_41(self):
        self.assertEqual(run_calculator('4', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-41 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_42(self):
        self.assertEqual(run_calculator('4', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-42 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_43(self):
        self.assertEqual(run_calculator('4', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-43 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_44(self):
        self.assertEqual(run_calculator('4', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-44 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_45(self):
        self.assertEqual(run_calculator('4', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-45 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_46(self):
        self.assertEqual(run_calculator('4', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-46 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_47(self):
        self.assertEqual(run_calculator('4', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-47 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_48(self):
        self.assertEqual(run_calculator('4', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-48 = -44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_49(self):
        self.assertEqual(run_calculator('4', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-49 = -45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_minus_50(self):
        self.assertEqual(run_calculator('4', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4-50 = -46',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
