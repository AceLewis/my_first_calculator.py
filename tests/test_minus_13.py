# test_minus_13.py
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


class TestMinus13(unittest.TestCase):

    def test_13_minus_0(self):
        self.assertEqual(run_calculator('13', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-0 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_1(self):
        self.assertEqual(run_calculator('13', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-1 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_2(self):
        self.assertEqual(run_calculator('13', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-2 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_3(self):
        self.assertEqual(run_calculator('13', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-3 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_4(self):
        self.assertEqual(run_calculator('13', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-4 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_5(self):
        self.assertEqual(run_calculator('13', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-5 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_6(self):
        self.assertEqual(run_calculator('13', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-6 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_7(self):
        self.assertEqual(run_calculator('13', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-7 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_8(self):
        self.assertEqual(run_calculator('13', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-8 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_9(self):
        self.assertEqual(run_calculator('13', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-9 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_10(self):
        self.assertEqual(run_calculator('13', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-10 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_11(self):
        self.assertEqual(run_calculator('13', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-11 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_12(self):
        self.assertEqual(run_calculator('13', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-12 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_13(self):
        self.assertEqual(run_calculator('13', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-13 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_14(self):
        self.assertEqual(run_calculator('13', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-14 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_15(self):
        self.assertEqual(run_calculator('13', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-15 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_16(self):
        self.assertEqual(run_calculator('13', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-16 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_17(self):
        self.assertEqual(run_calculator('13', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-17 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_18(self):
        self.assertEqual(run_calculator('13', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-18 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_19(self):
        self.assertEqual(run_calculator('13', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-19 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_20(self):
        self.assertEqual(run_calculator('13', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-20 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_21(self):
        self.assertEqual(run_calculator('13', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-21 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_22(self):
        self.assertEqual(run_calculator('13', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-22 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_23(self):
        self.assertEqual(run_calculator('13', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-23 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_24(self):
        self.assertEqual(run_calculator('13', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-24 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_25(self):
        self.assertEqual(run_calculator('13', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-25 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_26(self):
        self.assertEqual(run_calculator('13', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-26 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_27(self):
        self.assertEqual(run_calculator('13', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-27 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_28(self):
        self.assertEqual(run_calculator('13', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-28 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_29(self):
        self.assertEqual(run_calculator('13', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-29 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_30(self):
        self.assertEqual(run_calculator('13', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-30 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_31(self):
        self.assertEqual(run_calculator('13', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-31 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_32(self):
        self.assertEqual(run_calculator('13', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-32 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_33(self):
        self.assertEqual(run_calculator('13', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-33 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_34(self):
        self.assertEqual(run_calculator('13', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-34 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_35(self):
        self.assertEqual(run_calculator('13', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-35 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_36(self):
        self.assertEqual(run_calculator('13', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-36 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_37(self):
        self.assertEqual(run_calculator('13', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-37 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_38(self):
        self.assertEqual(run_calculator('13', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-38 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_39(self):
        self.assertEqual(run_calculator('13', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-39 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_40(self):
        self.assertEqual(run_calculator('13', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-40 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_41(self):
        self.assertEqual(run_calculator('13', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-41 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_42(self):
        self.assertEqual(run_calculator('13', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-42 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_43(self):
        self.assertEqual(run_calculator('13', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-43 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_44(self):
        self.assertEqual(run_calculator('13', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-44 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_45(self):
        self.assertEqual(run_calculator('13', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-45 = -32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_46(self):
        self.assertEqual(run_calculator('13', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-46 = -33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_47(self):
        self.assertEqual(run_calculator('13', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-47 = -34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_48(self):
        self.assertEqual(run_calculator('13', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-48 = -35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_49(self):
        self.assertEqual(run_calculator('13', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-49 = -36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_minus_50(self):
        self.assertEqual(run_calculator('13', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13-50 = -37',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
