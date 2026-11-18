# test_minus_3.py
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


class TestMinus3(unittest.TestCase):

    def test_3_minus_0(self):
        self.assertEqual(run_calculator('3', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-0 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_1(self):
        self.assertEqual(run_calculator('3', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-1 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_2(self):
        self.assertEqual(run_calculator('3', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-2 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_3(self):
        self.assertEqual(run_calculator('3', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-3 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_4(self):
        self.assertEqual(run_calculator('3', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-4 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_5(self):
        self.assertEqual(run_calculator('3', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-5 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_6(self):
        self.assertEqual(run_calculator('3', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-6 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_7(self):
        self.assertEqual(run_calculator('3', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-7 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_8(self):
        self.assertEqual(run_calculator('3', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-8 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_9(self):
        self.assertEqual(run_calculator('3', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-9 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_10(self):
        self.assertEqual(run_calculator('3', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-10 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_11(self):
        self.assertEqual(run_calculator('3', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-11 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_12(self):
        self.assertEqual(run_calculator('3', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-12 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_13(self):
        self.assertEqual(run_calculator('3', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-13 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_14(self):
        self.assertEqual(run_calculator('3', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-14 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_15(self):
        self.assertEqual(run_calculator('3', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-15 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_16(self):
        self.assertEqual(run_calculator('3', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-16 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_17(self):
        self.assertEqual(run_calculator('3', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-17 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_18(self):
        self.assertEqual(run_calculator('3', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-18 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_19(self):
        self.assertEqual(run_calculator('3', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-19 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_20(self):
        self.assertEqual(run_calculator('3', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-20 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_21(self):
        self.assertEqual(run_calculator('3', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-21 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_22(self):
        self.assertEqual(run_calculator('3', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-22 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_23(self):
        self.assertEqual(run_calculator('3', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-23 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_24(self):
        self.assertEqual(run_calculator('3', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-24 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_25(self):
        self.assertEqual(run_calculator('3', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-25 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_26(self):
        self.assertEqual(run_calculator('3', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-26 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_27(self):
        self.assertEqual(run_calculator('3', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-27 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_28(self):
        self.assertEqual(run_calculator('3', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-28 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_29(self):
        self.assertEqual(run_calculator('3', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-29 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_30(self):
        self.assertEqual(run_calculator('3', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-30 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_31(self):
        self.assertEqual(run_calculator('3', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-31 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_32(self):
        self.assertEqual(run_calculator('3', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-32 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_33(self):
        self.assertEqual(run_calculator('3', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-33 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_34(self):
        self.assertEqual(run_calculator('3', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-34 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_35(self):
        self.assertEqual(run_calculator('3', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-35 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_36(self):
        self.assertEqual(run_calculator('3', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-36 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_37(self):
        self.assertEqual(run_calculator('3', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-37 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_38(self):
        self.assertEqual(run_calculator('3', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-38 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_39(self):
        self.assertEqual(run_calculator('3', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-39 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_40(self):
        self.assertEqual(run_calculator('3', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-40 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_41(self):
        self.assertEqual(run_calculator('3', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-41 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_42(self):
        self.assertEqual(run_calculator('3', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-42 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_43(self):
        self.assertEqual(run_calculator('3', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-43 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_44(self):
        self.assertEqual(run_calculator('3', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-44 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_45(self):
        self.assertEqual(run_calculator('3', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-45 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_46(self):
        self.assertEqual(run_calculator('3', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-46 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_47(self):
        self.assertEqual(run_calculator('3', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-47 = -44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_48(self):
        self.assertEqual(run_calculator('3', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-48 = -45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_49(self):
        self.assertEqual(run_calculator('3', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-49 = -46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_minus_50(self):
        self.assertEqual(run_calculator('3', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3-50 = -47',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
