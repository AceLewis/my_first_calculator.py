# test_minus_2.py
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


class TestMinus2(unittest.TestCase):

    def test_2_minus_0(self):
        self.assertEqual(run_calculator('2', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-0 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_1(self):
        self.assertEqual(run_calculator('2', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-1 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_2(self):
        self.assertEqual(run_calculator('2', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-2 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_3(self):
        self.assertEqual(run_calculator('2', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-3 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_4(self):
        self.assertEqual(run_calculator('2', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-4 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_5(self):
        self.assertEqual(run_calculator('2', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-5 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_6(self):
        self.assertEqual(run_calculator('2', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-6 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_7(self):
        self.assertEqual(run_calculator('2', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-7 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_8(self):
        self.assertEqual(run_calculator('2', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-8 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_9(self):
        self.assertEqual(run_calculator('2', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-9 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_10(self):
        self.assertEqual(run_calculator('2', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-10 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_11(self):
        self.assertEqual(run_calculator('2', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-11 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_12(self):
        self.assertEqual(run_calculator('2', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-12 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_13(self):
        self.assertEqual(run_calculator('2', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-13 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_14(self):
        self.assertEqual(run_calculator('2', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-14 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_15(self):
        self.assertEqual(run_calculator('2', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-15 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_16(self):
        self.assertEqual(run_calculator('2', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-16 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_17(self):
        self.assertEqual(run_calculator('2', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-17 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_18(self):
        self.assertEqual(run_calculator('2', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-18 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_19(self):
        self.assertEqual(run_calculator('2', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-19 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_20(self):
        self.assertEqual(run_calculator('2', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-20 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_21(self):
        self.assertEqual(run_calculator('2', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-21 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_22(self):
        self.assertEqual(run_calculator('2', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-22 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_23(self):
        self.assertEqual(run_calculator('2', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-23 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_24(self):
        self.assertEqual(run_calculator('2', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-24 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_25(self):
        self.assertEqual(run_calculator('2', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-25 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_26(self):
        self.assertEqual(run_calculator('2', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-26 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_27(self):
        self.assertEqual(run_calculator('2', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-27 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_28(self):
        self.assertEqual(run_calculator('2', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-28 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_29(self):
        self.assertEqual(run_calculator('2', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-29 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_30(self):
        self.assertEqual(run_calculator('2', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-30 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_31(self):
        self.assertEqual(run_calculator('2', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-31 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_32(self):
        self.assertEqual(run_calculator('2', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-32 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_33(self):
        self.assertEqual(run_calculator('2', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-33 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_34(self):
        self.assertEqual(run_calculator('2', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-34 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_35(self):
        self.assertEqual(run_calculator('2', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-35 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_36(self):
        self.assertEqual(run_calculator('2', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-36 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_37(self):
        self.assertEqual(run_calculator('2', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-37 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_38(self):
        self.assertEqual(run_calculator('2', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-38 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_39(self):
        self.assertEqual(run_calculator('2', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-39 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_40(self):
        self.assertEqual(run_calculator('2', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-40 = -38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_41(self):
        self.assertEqual(run_calculator('2', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-41 = -39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_42(self):
        self.assertEqual(run_calculator('2', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-42 = -40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_43(self):
        self.assertEqual(run_calculator('2', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-43 = -41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_44(self):
        self.assertEqual(run_calculator('2', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-44 = -42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_45(self):
        self.assertEqual(run_calculator('2', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-45 = -43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_46(self):
        self.assertEqual(run_calculator('2', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-46 = -44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_47(self):
        self.assertEqual(run_calculator('2', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-47 = -45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_48(self):
        self.assertEqual(run_calculator('2', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-48 = -46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_49(self):
        self.assertEqual(run_calculator('2', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-49 = -47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_minus_50(self):
        self.assertEqual(run_calculator('2', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2-50 = -48',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
